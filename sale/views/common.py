import json
import arrow
import urllib
import pymysql
import pandas as pd
import datetime
import logging

from math import ceil
from django.http import HttpResponse, JsonResponse
from mandala.auth import get_user_model
from django.forms import model_to_dict

from django.conf import settings

from public.utils import get_all_data, gen_date_list, gen_month_list, parse_kwargs_for_pymysql
from secretary.models import DingGroupMemberMap
from customer.models import User as CrmUser
from customer.models import Department, Account, Activityrecord, ActivityrecordMapping, Opportunity
from customer.views.activity import select_x_yqms, select_x_tsgz, select_x_zhwp, get_activity_data_yqms

logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

region_name_map = dict([(2, "一大区"), (3, "二大区"), (4, "三大区"), (5, "四大区"), (6, "五大区"), (30, "六大区"), 
            (31, "七大区"), (32, "八大区"), (23, "九大区"), (33, "上海特区"), (39, "行业扩展二部"), (22, "政务客户成功部"), (7, "办公室")])

"""钉钉跟account表里面某事业部销售中心的对应关系"""
dingding_account_sale_center_map = {"58062185": "1", "58034238": "2"}

"""钉钉跟account表里面大区的对应关系"""
dingding_account_region_map = {
    "58084244": "2", "58127361": "3", "58068265": "4", "155650269": "5", "58111257": "6",
    "98192107": "30", "98019131": "31", "98006134": "32", "98266229": "23", 
    "98187117": "33", "111457167": "39", "61147353": "22", "58040397": "7",
}

def make_result(code, data, msg):
    return {"code": code, "data": data, "msg": msg}

"""钉钉，获取某部门下的所有人员名字"""
def dingding_get_all_member_names(did):
    ding = DingGroupMemberMap.objects.filter(group_id=did)
    if not ding:
        return []
    ding = ding[0]
    all_member_names = json.loads(ding.member_names_all)
    return all_member_names

"""通过dingding的部门获取商务人员的名字，然后再到销售易，通过这些商务人员的名字，来获取这些人员的ID"""
def get_saler_ids_dingding_crm(did):
    # 根据部门ID，从钉钉里面获取此部门下面所有人员的名字
    salers = dingding_get_all_member_names(did)
    # 从销售易里面的部门人员架构里面获取商务人员的ID
    saler_ids = list(CrmUser.objects.filter(name__in=salers).values_list("id", flat=True))
    return saler_ids


"""此函数针对ding_group_member_map这张表里面的数据结构"""
def dingding_get_children(did, all, deep=False):
    children = []
    root = all.get(did)
    if not root:
        return children
    sub_js = json.loads(root.get("sub_group_ids"))
    if not sub_js:
        return children
    for group_id in sub_js:
        if group_id in [58040397, "58040397"]:
            continue
        group_id = str(group_id)
        child = {}
        item = all.get(group_id)
        
        if item:
            child["did"] = group_id
            child["value"] = group_id
            child["name"] = item["group_name"]
            if deep == True:
                child["children"] = dingding_get_children(group_id, all, deep=deep)
            children.append(child)
    return children

"""获取部门成员，此函数主要是为了渲染部门信息用"""
def dingding_get_members(did):
    # return [{'name': '', 'value': '', 'type': 'user'}]
    if did is None:
        return []
    params = {}
    params["dingframe__contains"] = str(did)
    users = User.objects.filter(**params)
    members = []
    for user in users:
        member = {"type": "user"}
        member["name"] = user.username
        member["value"] = user.dtalkid
        members.append(member)
    return members

def dingding_department_frame(did):
    if not did:
        return None, -1, "参数错误"
    all = DingGroupMemberMap.objects.all()
    all_dict = {}
    for i in all:
        i = model_to_dict(i)
        all_dict[i["group_id"]] = i
    head = all_dict.get(did)
    if not head:
        return None, 0, "此部门不存在"
    # tree = {"did": did, "name": head["group_name"]}
    tree = {"name": head["group_name"]}
    tree["children"] = dingding_get_children(did, all_dict, deep=True)
    return tree, 1, None

"""钉钉部门架构"""    
def dingding_department_frame_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    tree, code, error = dingding_department_frame(did)
    result["code"] = code
    result["message"] = error
    result["data"] = tree
    return JsonResponse(result)

"""当没有下级部门时，获取此部门的所有人员"""
def dingding_region_frame_members_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    all = DingGroupMemberMap.objects.all()
    all_dict = {}
    for i in all:
        i = model_to_dict(i)
        all_dict[i["group_id"]] = i
    head = all_dict.get(did)
    if not head:
        result["msg"] = "此部门不存在"
        return JsonResponse(result)
    # tree = {"did": did, "name": head["group_name"]}
    tree = {"name": head["group_name"]}
    # 获取大区下面的部门
    tree["children"] = dingding_get_children(did, all_dict, deep=False)
    # 每个部门获取里面的人员
    for child in tree["children"]:
        child["children"] = dingding_get_members(child["value"])
    result["code"] = 1
    result["data"] = tree
    return JsonResponse(result)

"""当没有下级部门时，获取此部门的所有人员"""
def dingding_department_frame_members_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    all = DingGroupMemberMap.objects.all()
    all_dict = {}
    for i in all:
        i = model_to_dict(i)
        all_dict[i["group_id"]] = i
    head = all_dict.get(did)
    if not head:
        result["msg"] = "此部门不存在"
        return JsonResponse(result)
    # tree = {"did": did, "name": head["group_name"]}
    tree = {"name": head["group_name"]}
    # 每个部门获取里面的人员
    tree["children"] = dingding_get_members(did)
    result["code"] = 1
    result["data"] = tree
    return JsonResponse(result)

def make_customer_count_chart_data(data):
    # keys = ["total", "formal", "important", "develop", "week_twice", "week", "month", 
    #         "three_months", "trial_three_months_high", "highsea_activity", "dead"]
    keys = ["total", "formal", "important", "develop"]#, "highsea_activity"]
    List = []
    for k in keys:
        List.append(data.get(k, 0))
    return List

def make_account_count_chart_data(data):
    keys = ["total", "formal", "trial", "stop", "drop", "week_twice", "week", 
            "month", "three_months", "dead", "trial_three_months_high"]
    List = []
    for k in keys:
        List.append(data.get(k, 0))
    return List

"""某销售中心-客户数量"""
def count_customer_sale_center(cid):
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week": 0, "month": 0, "three_months": 0, 
            "trial_three_months_high":0, "dead": 0, "highsea_activity": 0}
    keys = ["total", "formal", "important", "develop", "week_twice", "week", "month", 
            "three_months", "trial_three_months_high", "highsea_activity", "dead"]
    saler_ids = get_saler_ids_dingding_crm(cid)
    total = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1, 3, 4]).count()
    formal = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1, 3, 4], level=5).count()
    important = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1, 3, 4], level=1).count()
    develop = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1, 3, 4], level=4).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return make_customer_count_chart_data(data)

"""某大区-客户数量"""
def count_customer_region(rid):
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week": 0, "month": 0, "three_months": 0, 
            "trial_three_months_high":0, "dead": 0, "highsea_activity": 0}
    keys = ["total", "formal", "important", "develop", "week_twice", "week", "month", 
            "three_months", "trial_three_months_high", "highsea_activity", "dead"]
    saler_ids = get_saler_ids_dingding_crm(rid)
    total = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1, 3, 4]).count()
    formal = Account.objects.filter(ownerid__in=saler_ids, level=5, highseastatus__in=[1, 3, 4]).count()
    important = Account.objects.filter(ownerid__in=saler_ids, level=1, highseastatus__in=[1, 3, 4]).count()
    develop = Account.objects.filter(ownerid__in=saler_ids, level=4, highseastatus__in=[1, 3, 4]).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return make_customer_count_chart_data(data)

"""某部门-客户数量"""
def count_customer_department(did):
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week": 0, "month": 0, "three_months": 0, 
            "trial_three_months_high":0, "dead": 0, "highsea_activity": 0}
    keys = ["total", "formal", "important", "develop", "week_twice", "week", "month", 
            "three_months", "trial_three_months_high", "highsea_activity", "dead"]
    saler_ids = get_saler_ids_dingding_crm(did)
    total = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1, 3, 4]).count()
    formal = Account.objects.filter(ownerid__in=saler_ids, level=5, highseastatus__in=[1, 3, 4]).count()
    important = Account.objects.filter(ownerid__in=saler_ids, level=1, highseastatus__in=[1, 3, 4]).count()
    develop = Account.objects.filter(ownerid__in=saler_ids, level=4, highseastatus__in=[1, 3, 4]).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return make_customer_count_chart_data(data)

"""政务中心-销售中心-某大区-某部门-某商务-客户数量"""
def count_customer_saler(dtalkid):
    user = User.objects.filter(dtalkid=dtalkid).first()
    saler = CrmUser.objects.filter(name=user.username).first()
    sid = saler.id
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week": 0, "month": 0, "three_months": 0, 
            "trial_three_months_high":0, "dead": 0, "highsea_activity": 0}
    keys = ["total", "formal", "important", "develop", "week_twice", "week", "month", 
            "three_months", "trial_three_months_high", "highsea_activity", "dead"]
    # total = Account.objects.filter(dbcselect6=sid).count()
    # formal = Account.objects.filter(dbcselect6=sid, level=5).count()
    # important = Account.objects.filter(dbcselect6=sid, level=1).count()
    # develop = Account.objects.filter(dbcselect6=sid, level=4).count()
    total = Account.objects.filter(ownerid=sid, highseastatus__in=[1, 3, 4]).count()
    formal = Account.objects.filter(ownerid=sid, level=5, highseastatus__in=[1, 3, 4]).count()
    important = Account.objects.filter(ownerid=sid, level=1, highseastatus__in=[1, 3, 4]).count()
    develop = Account.objects.filter(ownerid=sid, level=4, highseastatus__in=[1, 3, 4]).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return make_customer_count_chart_data(data)

def customer_count_sale_center_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    cid = request.GET.get("cid")
    if not cid:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_sale_center(cid)
    result["data"]["name"] = ""
    result["data"]["type"] = "bar"
    result["data"]["data"] = data
    result["code"] = 1
    return JsonResponse(result)

def customer_count_region_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    rid = request.GET.get("rid")
    if not rid:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_region(rid)
    result["data"]["name"] = ""
    result["data"]["type"] = "bar"
    result["data"]["data"] = data
    result["code"] = 1
    return JsonResponse(result)

def customer_count_department_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_department(did)
    result["data"]["name"] = ""
    result["data"]["type"] = "bar"
    result["data"]["data"] = data
    result["code"] = 1
    return JsonResponse(result)

def customer_count_saler_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    uid = request.GET.get("uid")
    if not uid:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_saler(uid)
    result["data"]["name"] = ""
    result["data"]["type"] = "bar"
    result["data"]["data"] = data
    result["code"] = 1
    return JsonResponse(result)

def work_daily_department(did, date_str=None):
    if not date_str:
        date = arrow.now()
    else:
        date = arrow.get(date_str, "YYYY/M")
    date_str = date.strftime("%Y-%m")
    saler_ids = get_saler_ids_dingding_crm(did)
    date_list = arrow.Arrow.range("day", date.floor("month"), date.floor("month").shift(months=1).shift(days=-1))
    date_str_list = [date.strftime("%Y-%m-%d") for date in date_list]
    acts = Activityrecord.objects.filter(createdat__contains=date_str, ownerid__in=saler_ids)
    # 电话拜访：4173078，签到拜访：4173079，快速记录：-11
    a_list = []
    b_list = []
    c_list = []
    for d in date_str_list:
        a = b = c = 0
        for act in acts:
            if d in act.createdat:
                if act.entitytype == "4173078":
                    a += 1
                elif act.entitytype == "4173079":
                    b += 1
                elif act.entitytype == "-11":
                    c += 1
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
    data = {"title": {"text": date_str}, "series": {"a": a_list, "b": b_list, "c": c_list}, "date_str_list": date_str_list}
    return data

def work_daily_department_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    date_str = request.GET.get("date_str")
    dpt = DingGroupMemberMap.objects.filter(group_id=did)
    if dpt.count() < 1:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = work_daily_department(did, date_str)
    result["code"] = 1
    result["data"] = data
    return JsonResponse(result)  

def work_daily_department_salers(did):
    date = arrow.now()
    date_str = date.strftime("%Y-%m")
    saler_ids = get_saler_ids_dingding_crm(did)
    salers = CrmUser.objects.filter(id__in=saler_ids)
    saler_dict = {str(saler.id): saler for saler in salers}
    date_list = arrow.Arrow.range("day", date.floor("month"), date.floor("month").shift(months=1).shift(days=-1))
    date_str_list = [date.strftime("%Y-%m-%d") for date in date_list]
    acts = Activityrecord.objects.filter(createdat__contains=date_str, ownerid__in=saler_ids)
    # 电话拜访：4173079，签到拜访：4173078，快速记录：-11
    items = []
    dpts = Department.objects.all()
    dpt_dict = {str(dpt.id): dpt for dpt in dpts}
    for ownerid in saler_ids:
        saler = saler_dict.get(str(ownerid))
        if not saler:
            continue
        name = ""
        depart = ""
        name = saler.name
        dpt = dpt_dict.get(saler.departid)
        if dpt:
            depart = dpt.departname
        item = {"ownerid": ownerid, "saler": name, "depart": depart, "departId": saler.departid}
        a = b = c = d = 0
        for act in acts:
            if act.ownerid == ownerid:
                if act.entitytype == "4173079":
                    a += 1
                elif act.entitytype == "4173078":
                    b += 1
                elif act.entitytype == "-11":
                    c += 1
        d = a + b + c
        item["call"] = a
        item["visit"] = b
        item["record"] = c
        item["total"] = d
        items.append(item)
    data = items
    return data

def work_daily_department_salers_api(request):
    result = {"code": 0, "data": {}, "error": ""}
    did = request.GET.get("did")
    items = work_daily_department_salers(did)
    # data = []
    # columns = ["saler", "call", "visit", "record"]
    # for item in items:
    #     i = []
    #     for c in columns:
    #         i.append(item.get(c))
    #     data.append(i)
    result["code"] = 1
    result["data"] = items
    return JsonResponse(result)

# def work_daily_saler(dtalkid):
#     result = {"code": 0, "data": None, "error": ""}
#     date = arrow.now()
#     date_str = date.strftime("%Y-%m")
#     user = User.objects.filter(dtalkid=dtalkid).first()
#     if not user:
#         result["code"] = -1
#         result["error"] = "查无此人"
#         return result
#     saler = CrmUser.objects.filter(name=user.username).first()
#     if not saler:
#         result["code"] = -1
#         result["error"] = "此人不是商务人员"
#         return result
#     sid = saler.id
#     date_list = arrow.Arrow.range("day", date.floor("month"), date.floor("month").shift(months=1).shift(days=-1))
#     date_str_list = [date.strftime("%Y-%m-%d") for date in date_list]
#     acts = Activityrecord.objects.filter(createdat__contains=date_str, ownerid=sid)
#     # 电话拜访：4173079，签到拜访：4173078，快速记录：-11
#     dpt = Department.objects.filter(id=saler.departid).first()
#     item = {"ownerid": sid, "saler": saler.name, "depart": dpt.departname, "departId": saler.departid}
#     a = b = c = d = 0
#     for act in acts:
#         if act.entitytype == "4173079":
#             a += 1
#         elif act.entitytype == "4173078":
#             b += 1
#         elif act.entitytype == "-11":
#             c += 1
#     d = a + b + c
#     item["call"] = a
#     item["visit"] = b
#     item["record"] = c
#     item["total"] = d
#     result["code"] = 1
#     result["data"] = item
#     return result

def work_daily_saler(dtalkid):
    result = {"code": 0, "data": None, "error": ""}
    date = arrow.now()
    date_str = date.strftime("%Y-%m")
    date_str2 = str(date.year) + "年" + str(date.month) + "月"
    user = User.objects.filter(dtalkid=dtalkid).first()
    if not user:
        result["code"] = -1
        result["error"] = "查无此人"
        return result
    saler = CrmUser.objects.filter(name=user.username).first()
    if not saler:
        result["code"] = -1
        result["error"] = "此人不是商务人员"
        return result
    date_list = arrow.Arrow.range("day", date.floor("month"), date.floor("month").shift(months=1).shift(days=-1))
    date_str_list = [date.strftime("%Y-%m-%d") for date in date_list]
    sid = saler.id
    acts = Activityrecord.objects.filter(createdat__contains=date_str, ownerid=sid)
    # 电话拜访：4173079，签到拜访：4173078，快速记录：-11
    a_list = []
    b_list = []
    c_list = []
    for d in date_str_list:
        a = b = c = 0
        for act in acts:
            if d in act.createdat:
                if act.entitytype == "4173079":
                    a += 1
                elif act.entitytype == "4173078":
                    b += 1
                elif act.entitytype == "-11":
                    c += 1
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
    data = {"title": {"text": date_str2}, "series": {"a": a_list, "b": b_list, "c": c_list}, "date_str_list": date_str_list}
    result["code"] = 1
    result["data"] = data
    return result

# @login_required
def work_daily_saler_api(request):
    uid = request.GET.get("uid")
    if not id:
        uid = request.user.dtalkid
    result = work_daily_saler(uid)
    return JsonResponse(result)
    

'''指定时间段内，公司每天回款情况'''
def payment_department_days_api(request):
    result = {"code": 0, "msg": "", "data": None}
    did = request.GET.get("did")
    dpt = DingGroupMemberMap.objects.filter(group_id=did).first()
    if not dpt:
        result["code"] = -1
        result["msg"] = "部门ID不能为空"
        return JsonResponse(result)
    start = request.GET.get("start")
    if not start:
        start = None
    start = arrow.get(start).floor("month")
    end = request.GET.get("end")
    if not end:
        end = start.shift(months=1).shift(days=-1)
    end = arrow.get(end)
    date_list = gen_date_list(start, end)
    if not date_list:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    date_fmt = "%Y-%m-%d"
    date_fmt_short = "%m-%d"
    date_tuple = tuple([date.strftime(date_fmt) for date in date_list])
    date_tuple_str = str(date_tuple) if len(date_tuple) > 1 else str(date_tuple).replace(",", "")
    _date_list = [date.strftime(date_fmt) for date in date_list]
    date_list = [date.strftime(date_fmt_short) for date in date_list]
    saler_ids = get_saler_ids_dingding_crm(did)
    if not saler_ids:
        result["msg"] = "请确认此部门是否属于销售部门"
        return JsonResponse(result)
    scount = len(saler_ids)
    saler_ids = str(tuple(saler_ids))
    if scount == 1:
        saler_ids = saler_ids.replace(",", "")
    # 计划回款
    sql1 = "SELECT FROM_UNIXTIME(planTime/1000, '{}') as ptime, SUM(amount) FROM `paymentplan` WHERE FROM_UNIXTIME(planTime/1000, '{}') in {} AND ownerId in {} GROUP BY ptime;".format(date_fmt, date_fmt, date_tuple_str, saler_ids)
    # 实际回款
    sql2 = "SELECT FROM_UNIXTIME(planTime/1000, '{}') as ptime, SUM(actualAmount) FROM `paymentplan` WHERE FROM_UNIXTIME(planTime/1000, '{}') in {} AND ownerId in {} GROUP BY ptime;".format(date_fmt, date_fmt, date_tuple_str, saler_ids)
    plan_data = []
    actual_data = []
    try:
        plan_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
        actual_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    except Exception as e:
        logger.error(e)
        result["code"] = -1
        result["msg"] = "服务器繁忙，请稍后重试！"
        return JsonResponse(result)
    for date in date_tuple:
        plan_data.append(plan_data_dict.get(date, 0))
        actual_data.append(actual_data_dict.get(date, 0))
    count = {
        "计划回款": {
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "data": [int(i) for i in plan_data],
            "type": "bar",
            # "color": "#fb9678",
            "barCategoryGap": '80%'
        },
        "实际回款": {
            "label": {
                "normal": {
                    "show": True,
                    "position": "right",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "data": [int(i) for i in actual_data],
            "type": "bar",
            # "color": "#00c292",
            "barCategoryGap": '80%'
        }
    }
    legend_data = ["计划回款", "实际回款"]
    series = []
    for legend in legend_data:
        _sery = count[legend]
        sery = {
            "name": legend,
            "type": 'bar',
            "stack": legend,
            "data": []
        }
        sery.update(_sery)
        series.append(sery)
    plan_all = ceil(sum(plan_data))
    actual_all = int(sum(actual_data))
    params = {
        "plantime_start": start.strftime("%Y-%m-%d") if start else "",
        "plantime_end": end.strftime("%Y-%m-%d") if end else "",
        "overdue": 1
    }
    query = urllib.parse.urlencode(params)
    option = {
        "title": {
            "text": '{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '计划回款：%s元，实际回款：%s元'%(format(plan_all, ","), format(actual_all, ",")),
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "x" : 'right',
            "y" : 'top',
            "itemWidth": 8,
            "itemHeight": 8,
            "textStyle":{
                "fontSize":12
            },
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        # "toolbox": {
        #     "feature": {
        #         # "saveAsImage": {},
        #         "myDataView": {
        #             "show": True,
        #             "title": "查看详情",
        #             "icon": "image://static/img/detail.png",
        #             "url": reverse("sale:payment_plan_list") + "?" + query,
        #             "onclick": None
        #         }
        #     }
        # },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": _date_list,
            "axisLabel": {
                "interval":0, # 坐标刻度之间的显示间隔，默认就可以了（默认是不重叠）
                "rotate":38   # 调整数值改变倾斜的幅度（范围-90到90）
            }
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["data"] = option
    return JsonResponse(result)

'''政务中心各大区目标完成情况(某月)'''
def goal_regions_month_api(request):
    result = {"code": 0, "msg": "", "data": {}}
    date_list = ["一大区", "二大区", "三大区", "四大区", "五大区", "六大区", "七大区", "八大区", "九大区", "上海特区"]
    legend_data = ["大区目标", "确认归档", "实际完成"]
    start = request.GET.get("start")
    if start:
        start = arrow.get(start, "YYYY/M")
    else:
        start = arrow.now()
    start = start.floor("month")
    sql1 = "Select goalName, month{} from goalDepart;".format(start.month)
    goal_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
    goal_data_list = []
    for d in date_list:
        g = goal_data_dict.get(d + "汇总目标", 0)
        goal_data_list.append(g)
    company_month_goal = float(goal_data_dict.get("公司总目标", 0))
    goverment_month_goal = float(goal_data_dict.get("政务事业部汇总目标", 0))
    regional_name_map = dict([(2, "一大区"), (3, "二大区"), (4, "三大区"), (5, "四大区"), (6, "五大区"), (30, "六大区"), 
            (31, "七大区"), (32, "八大区"), (23, "九大区"), (33, "上海特区"), (39, "行业扩展二部"), (22, "政务客户成功部"), (7, "办公室")])
    # regional_id_list = [1, 2, 3, 4, 5, 6, 23, 28, 30, 31]#, 32, 33, 39]
    regional_id_list = [2, 3, 4, 5, 6, 30, 31, 32, 23, 33]#39, 22
    # 从商机表中根据政务事业部、区总确认合同归档日期等条件查询商机金额
    sql2 = """Select dbcSelect4, sum(money) as sum_money from `opportunity` WHERE dbcSelect3=1 
            AND dbcDate15 LIKE '%{}%' GROUP BY dbcSelect4;""".format(start.strftime("%Y-%m"))
    regional_datas = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    ok_data_list = [regional_datas.get(k, 0) for k in regional_id_list]

    #从订单中根据订单状态，按照大区查询政务事业部实际收款情况
    sql3 = """SELECT dbcSelect11, sum(amount), sum(dbcReal2) FROM `order` WHERE poStatus=2 AND dbcDate14 IS TRUE AND dbcSelect10=1 
            AND FROM_UNIXTIME(dbcDate14/1000, '%Y-%m')='{}' GROUP BY dbcSelect11;""".format(start.strftime("%Y-%m")) 
    datas = get_all_data(settings.DATABASES["contract_33"], sql3)
    regional_name_map = dict([(1, "一大区"), (2, "二大区"), (3, "三大区"), (4, "四大区"), (5, "五大区"), (33, "六大区"), (34, "七大区"), 
            (35, "八大区"), (26, "九大区"), (36, "上海特区"), (42, "行业扩展二部"), (7, "办公室"), (25, "政务客户成功部"), (None, "其他")])
    regional_id_list = [1, 2, 3, 4, 5, 33, 34, 35, 26, 36]
    # ok_data_list = []
    actual_data_list = []
    for i in regional_id_list:
        for x, y, z in datas:
            if x == i:
                # if not y:
                #     y = 0
                # ok_data_list.append(y)
                if not z:
                    z = 0
                actual_data_list.append(z)
    plan_all = int(sum(ok_data_list))
    actual_all = int(sum(actual_data_list))
    series = [
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "大区目标",  
            "stack": "目标",
            "data": [ceil(float(i)) for i in goal_data_list],
            "type": "line",
            # "color": "#fb9678"
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "确认归档",  
            "stack": "归档",
            "data": [int(i) for i in ok_data_list],
            "type": "bar",
            # "color": "#00c292",
            "barCategoryGap": '80%'
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "实际完成",  
            "stack": "实际",
            "data": [int(i) for i in actual_data_list],
            "type": "bar",
            # "color": "#ab8ce4",
            "barCategoryGap": '80%'
        }
    ]
    
    option = {
        "title": {
            "text": "",#'{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '目标：%s元，区总确认归档：%s元，实际：%s元'%(format(ceil(goverment_month_goal), ","), format(plan_all, ","), format(actual_all, ","))
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "x" : 'right',
            "y" : 'top',
            "itemWidth": 8,
            "itemHeight": 8,
            "textStyle":{
                "fontSize":12
            },
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        # "toolbox": {
        #     "feature": {
        #         "saveAsImage": {},
        #         "restore": {},
        #         "dataView": {},
        #         # "dataZoom": {},
        #         # "magicType": {},
        #         # "brush": {}
        #     }
        # },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list,
            "axisLabel": {
                "interval":0, # 坐标刻度之间的显示间隔，默认就可以了（默认是不重叠）
                "rotate":38   # 调整数值改变倾斜的幅度（范围-90到90）
            }
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["msg"] = "数据获取成功"
    result["data"] = option
    return JsonResponse(result)

'''大区中各部门目标完成情况(某月)'''
def goal_departments_month_api(request):
    result = {"code": 0, "error": "", "data": {}}
    # 获取大区ID
    did = request.GET.get("did")
    if did in [None, ""]:
        result["code"] = -1
        result["error"] = "参数错误"
        return JsonResponse(result)
    tree, code, error = dingding_department_frame(did)
    if code < 1:
        result["code"] = code
        result["error"] = error
        return JsonResponse(result)
    region_name = tree["name"]
    date_list = []
    for child in tree["children"]:
        date_list.append(child["name"])
    legend_data = ["部门目标", "确认归档", "实际完成"]
    now = arrow.now()
    start = request.GET.get("start")
    if not start:
        start = arrow.now().floor("month")
    sql1 = "Select goalName, month{} from goalDepart;".format(now.month)
    goal_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
    goal_data_list = []
    for d in date_list:
        key = region_name.replace("大", "") + d
        if "上海" in d:
            key = "上海"
        g = goal_data_dict.get(key, 0)
        goal_data_list.append(g)
    region_month_goal = float(goal_data_dict.get(region_name + "汇总目标", 0))
    ok_data_list = []
    actual_data_list = []
    for child in tree["children"]:
        saler_ids = get_saler_ids_dingding_crm(child["value"])
        saler_id_tuple_str = str(tuple(saler_ids)).replace(",)", ")")
        # 从商机表中ownerId、区总确认合同归档日期等条件查询商机金额
        sql2 = """Select sum(money) as sum_money from `opportunity` WHERE ownerId IN {} 
                AND dbcDate15 LIKE '%{}%';""".format(saler_id_tuple_str, now.strftime("%Y-%m"))
        saler_datas = get_all_data(settings.DATABASES["contract_33"], sql2)
        ok_data_list.append(saler_datas[0][0] or 0)

        #从订单中根据订单状态，按照大区查询政务事业部实际收款情况
        sql3 = """SELECT sum(amount), sum(dbcReal2) FROM `order` WHERE poStatus=2 
                AND dbcDate14 IS TRUE AND dbcSelect10=1 AND ownerId IN {} 
                AND FROM_UNIXTIME(dbcDate14/1000, '%Y-%m')='{}';""".format(saler_id_tuple_str, now.strftime("%Y-%m")) 
        datas = get_all_data(settings.DATABASES["contract_33"], sql3)
        actual_data_list.append(datas[0][1] or 0)
    plan_all = int(sum(ok_data_list))
    actual_all = int(sum(actual_data_list))
    series = [
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "部门目标",  
            "stack": "目标",
            "data": [ceil(float(i)) for i in goal_data_list],
            "type": "line" if len(date_list) > 1 else "bar",
            # "color": "#fb9678"
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "确认归档",  
            "stack": "归档",
            "data": [int(i) for i in ok_data_list],
            "type": "bar",
            # "color": "#00c292",
            "barCategoryGap": '80%'
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "实际完成",  
            "stack": "实际",
            "data": [int(i) for i in actual_data_list],
            "type": "bar",
            # "color": "#ab8ce4",
            "barCategoryGap": '80%'
        }
    ]
    
    option = {
        "title": {
            "text": '{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '目标：%s元，区总确认归档：%s元，实际：%s元'%(format(ceil(region_month_goal), ","), format(plan_all, ","), format(actual_all, ","))
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "x" : 'right',
            "y" : 'top',
            "itemWidth": 8,
            "itemHeight": 8,
            "textStyle":{
                "fontSize":12
            },
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        # "toolbox": {
        #     "feature": {
        #         "saveAsImage": {},
        #         "restore": {},
        #         "dataView": {},
        #         # "dataZoom": {},
        #         # "magicType": {},
        #         # "brush": {}
        #     }
        # },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list,
            "axisLabel": {
                "interval":0, # 坐标刻度之间的显示间隔，默认就可以了（默认是不重叠）
                "rotate":38   # 调整数值改变倾斜的幅度（范围-90到90）
            }
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["msg"] = "数据获取成功"
    result["data"] = option
    return JsonResponse(result)

'''部门中各商务目标完成情况(某月)'''
def goal_salers_month_api(request):
    result = {"code": 0, "msg": "", "data": {}}
    # 获取部门ID
    did = request.GET.get("did")
    if did in [None, ""]:
        result["code"] = -1
        result["error"] = "参数错误"
        return JsonResponse(result)
    tree, code, error = dingding_department_frame(did)
    members = dingding_get_members(did)
    if code < 1:
        result["code"] = code
        result["error"] = error
        return JsonResponse(result)
    department_name = tree["name"]
    date_list = []
    for child in members:
        date_list.append(child["name"])
    # legend_data = ["个人目标", "确认归档", "实际完成"]
    legend_data = ["确认归档", "实际完成"]
    now = arrow.now()
    start = request.GET.get("start")
    if not start:
        start = arrow.now().floor("month")
    sql1 = "Select goalName, month{} from goalDepart;".format(now.month)
    goal_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
    goal_data_list = []
    department_month_goal = float(goal_data_dict.get(department_name, 0))
    ok_data_list = []
    actual_data_list = []
    saler_ids = get_saler_ids_dingding_crm(did)
    salers = CrmUser.objects.filter(id__in=saler_ids)
    saler_dict = {saler.id: saler.name for saler in salers}
    saler_id_tuple_str = str(tuple(saler_ids)).replace(",)", ")")
    # 从商机表中ownerId、区总确认合同归档日期等条件查询商机金额
    sql2 = """Select ownerId, sum(money) as sum_money from `opportunity` WHERE ownerId IN {} 
            AND dbcDate15 LIKE '%{}%' GROUP BY ownerId;""".format(saler_id_tuple_str, now.strftime("%Y-%m"))
    saler_datas = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    for ownerId in saler_ids:
        ok_data_list.append(saler_datas.get(str(ownerId), 0))
    
    #从订单中根据订单状态，按照大区查询政务事业部实际收款情况
    sql3 = """SELECT ownerId, sum(amount), sum(dbcReal2) FROM `order` WHERE poStatus=2 
            AND dbcDate14 IS TRUE AND dbcSelect10=1 AND ownerId IN {} 
            AND FROM_UNIXTIME(dbcDate14/1000, '%Y-%m')='{}' GROUP BY ownerId;""".format(saler_id_tuple_str, now.strftime("%Y-%m")) 
    datas = get_all_data(settings.DATABASES["contract_33"], sql3)
    
    for i in saler_ids:
        _z = 0
        for x, y, z in datas:
            if x == i:
                if z:
                    _z = z
        actual_data_list.append(_z)

    date_list = []
    for i in saler_ids:
        date_list.append(saler_dict.get(i, ""))
        
    plan_all = int(sum(ok_data_list))
    actual_all = int(sum(actual_data_list))
    series = [
        # {   
        #     "label": {
        #         "normal": {
        #             "show": True,
        #             "position": "top",
        #             # "textStyle": {
        #             #     "color": 'black',
        #             #     # "fontSize": 10
        #             # }
        #         }
        #     },
        #     "name": "个人目标",  
        #     "stack": "目标",
        #     "data": [ceil(float(i)) for i in goal_data_list],
        #     "type": "line" if len(date_list) > 1 else "bar",
        #     # "color": "#fb9678"
        # },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "确认归档",  
            "stack": "归档",
            "data": [int(i) for i in ok_data_list],
            "type": "bar",
            # "color": "#00c292",
            "barCategoryGap": '80%'
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "实际完成",  
            "stack": "实际",
            "data": [int(i) for i in actual_data_list],
            "type": "bar",
            # "color": "#ab8ce4",
            "barCategoryGap": '80%'
        }
    ]
    
    option = {
        "title": {
            "text": '{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '目标：%s元，区总确认归档：%s元，实际：%s元'%(format(ceil(department_month_goal), ","), format(plan_all, ","), format(actual_all, ","))
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "x" : 'right',
            "y" : 'top',
            "itemWidth": 8,
            "itemHeight": 8,
            "textStyle":{
                "fontSize":12
            },
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        # "toolbox": {
        #     "feature": {
        #         "saveAsImage": {},
        #         "restore": {},
        #         "dataView": {},
        #         # "dataZoom": {},
        #         # "magicType": {},
        #         # "brush": {}
        #     }
        # },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list,
            "axisLabel": {
                "interval":0, # 坐标刻度之间的显示间隔，默认就可以了（默认是不重叠）
                "rotate":38   # 调整数值改变倾斜的幅度（范围-90到90）
            }
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["msg"] = "数据获取成功"
    result["data"] = option
    return JsonResponse(result)

def account_count_yqms(did):
    salers = dingding_get_all_member_names(did)
    res = select_x_yqms(salers=salers)
    items = res["items"]
    mcrms = res["mcrms"]
    msuser_ids = list(mcrms.keys())
    # 总数
    # 正式
    # 试用
    # 停用
    # 弃用
    total = len(items)
    formal = trial = stop = drop = 0
    trial_list = []
    for item in items:
        status = item["account_status"]
        if status == "0":
            formal += 1
        elif status == "1":
            trial_list.append(item["id"])
            trial += 1
        elif status == "2":
            stop += 1
        else:
            drop += 1
    now = arrow.now()
    fmt = "%Y-%m-%d"
    # 周双活
    activity_start = now.shift(days=-7).strftime(fmt)
    activity_finish = now.shift(days=-1).strftime(fmt)
    login_days = 2
    acts, b, c = get_activity_data_yqms(msuser_ids, activity_start, activity_finish, login_days)
    week_twice = len(acts)
    # 周活跃
    activity_start = now.shift(days=-7).strftime(fmt)
    activity_finish = now.shift(days=-1).strftime(fmt)
    login_days = 3
    acts, b, c = get_activity_data_yqms(msuser_ids, activity_start, activity_finish, login_days)
    week = len(acts)
    # 月活跃
    activity_start = now.shift(months=-1).strftime(fmt)
    activity_finish = now.shift(days=-1).strftime(fmt)
    login_days = 12
    acts, b, c = get_activity_data_yqms(msuser_ids, activity_start, activity_finish, login_days)
    month = len(acts)
    # 三月活跃
    activity_start = now.shift(months=-3).strftime(fmt)
    activity_finish = now.shift(days=-1).strftime(fmt)
    login_days = 36
    acts, b, c = get_activity_data_yqms(msuser_ids, activity_start, activity_finish, login_days)
    three_months = len(acts)
    # 零活跃
    activity_start = now.shift(months=-3).strftime(fmt)
    activity_finish = now.shift(days=-1).strftime(fmt)
    login_days = 0
    acts, b, c = get_activity_data_yqms(msuser_ids, activity_start, activity_finish, login_days)
    dead = len(acts)
    # 试用高活三个月
    activity_start = now.shift(months=-3).strftime(fmt)
    activity_finish = now.shift(days=-1).strftime(fmt)
    login_days = 36
    acts, b, c = get_activity_data_yqms(trial_list, activity_start, activity_finish, login_days)
    trial_three_months_high = len(acts)
    data = {"total": total, "formal": formal, "trial": trial, "stop": stop, "drop": drop,
            "week_twice": week_twice, "week": week, "month": month, 
            "three_months": three_months, "dead": dead, "trial_three_months_high": trial_three_months_high}
    return data

def count_account(did=None, uid=None):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    where = ["created_at LIKE '{}%' ".format(today)]
    if uid:
        where.append("ding_id=" + str(uid))
    else:
        if did:
            saler_ids = get_saler_ids_dingding_crm(did)
            saler_ids = str(tuple(saler_ids)).replace(",)", ")")
            where.append("user_id IN " + saler_ids)
    where = " AND ".join(where)
    column_map = {"account_sum": "total", "account_formal_num": "formal", "account_trial_num": "trial",
            "account_stop_num": "stop", "account_aband_num": "drop", "week_two_days": "week_twice",
            "week_three_days": "week", "month_one": "month", "month_three": "three_months", 
            "never_use": "dead", "month_three_trial": "trial_three_months_high"}
    sql = """
        SELECT sum(account_sum) as total, sum(account_formal_num) as formal, sum(account_trial_num) as trial, 
            sum(account_stop_num) as stop, sum(account_aband_num) as `drop`, sum(week_two_days) as week_twice,
            sum(week_three_days) as week, sum(month_one) as month, sum(month_three) as three_months, 
            sum(never_use) as dead, sum(month_three_trial) as trial_three_months_high, account_type as product
        FROM sale_account_data 
        WHERE {} 
        GROUP BY account_type;
        """.format(where)
    product_map = {"yqms": "舆情秘书", "tsgz": "态势感知", "zhwp": "智慧网评"}
    try:
        database = settings.DATABASES["default"]
        kws = parse_kwargs_for_pymysql(database)
        conn = pymysql.connect(**kws)
        df = pd.read_sql(sql, conn)
        for k, v in column_map.items():
            df[v] = df[v].astype(int)
        accounts = list(df.to_dict(orient="index").values())
        order = ['yqms', 'tsgz', 'zhwp']
        account_num = []
        for o in order:
            for account in accounts:
                if account["product"] == o:
                    account["product"] = product_map.get(o, o)
                    account_num.append(account)
        return (account_num, 1, "")
    except Exception as e:
        logger.error(str(e))
        return ([], -1, "服务器繁忙，请稍后再查")

def products_account_count_api(request):
    did = request.GET.get("did")
    if not did:
        result = make_result(-1, None, "参数错误")
        return JsonResponse(result)
    account_data, code, error = count_account(did)
    data = {}
    data["data"] = account_data
    result = make_result(code, data, error)
    return JsonResponse(result)

def account_count_api(request):
    did = request.GET.get("did")
    pro = request.GET.get("pro")
    if not did or not pro:
        result = make_result(-1, None, "参数错误")
        return JsonResponse(result)
    if pro == "yqms":
        account_count_func = account_count_yqms
    else:
        result = make_result(-1, None, "参数错误")
        return JsonResponse(result)
    account_data = account_count_func(did)
    account_data = make_account_count_chart_data(account_data)
    data = {}
    data["data"] = account_data
    result = make_result(1, data, "")
    return JsonResponse(result)

def opportunity_count(did):
    saler_ids = get_saler_ids_dingding_crm(did)
    sale_stage_map = {
        '1172739': '产品新单-潜在商机(新)', '1172741': '产品新单-商机确认(新)', 
        '1186830': '产品新单-商务谈判（新）', '1172743': '产品新单-合同确认（新）', 
        '1209860': '产品新单-赢单（新）', '1172744': '产品新单-输单(新)', 
        '1186615': '产品续单-商机确认（续）', '1197988': '产品续单-商务谈判（续）', 
        '1186616': '产品续单-合同确认（续）', '1595051': '产品续单-赢单（续）', 
        '1186617': '产品续单-输单（续）', '1723501': '项目型业务-初步沟通（项目）', 
        '1723502': '项目型业务-意向客户（项目）', '1723701': '项目型业务-商机确认（项目）', 
        '1723503': '项目型业务-需求确认（项目）', '1723504': '项目型业务-商务谈判（项目）', 
        '1723003': '项目型业务-合同确认（项目）', '1723505': '项目型业务-赢单（项目）', 
        '1723506': '项目型业务-输单（项目）', '1850762': '星光数据-初步沟通（数据）', 
        '1850763': '星光数据-需求确认（数据）', '1850764': '星光数据-商务谈判（数据）', 
        '1850765': '星光数据-合同确认（数据）', '1850766': '星光数据-赢单（数据）', 
        '1850767': '星光数据-输单（数据）', '1135781124718941': '代理商商机-初步接洽', 
        '1135781124718942': '代理商商机-需求确定', '1135781124718943': '代理商商机-方案/报价', 
        '1135781124718944': '代理商商机-谈判审核', '1135781124718945': '代理商商机-赢单', 
        '1135781124718946': '代理商商机-输单'
    }
    now = arrow.now()
    today = now.strftime("%Y-%m-%d")
    three_months_before = now.floor("day").shift(months=-3).shift(days=1).strftime("%Y-%m-%d %H:%M")
    total = Opportunity.objects.filter(ownerid__in=saler_ids).count()
    new = Opportunity.objects.filter(ownerid__in=saler_ids, createdat__contains=today).count()
    no_account = Opportunity.objects.filter(ownerid__in=saler_ids, winrate__lt=100, dbcjoin13=None).count()
    stop_three_months = Opportunity.objects.filter(ownerid__in=saler_ids, winrate__lt=100, recentactivityrecordtime__lt=three_months_before).count()
    return [total, new, no_account, stop_three_months]

def opportunity_count_api(request):
    did = request.GET.get("did")
    if not did:
        result = make_result(-1, None, "参数错误")
        return JsonResponse(result)
    count_data = opportunity_count(did)
    data = {"data": count_data}
    result = make_result(1, data, "")
    return JsonResponse(result)


'''某商务目标完成情况(某月)'''
def goal_saler_month_api(request):
    result = {"code": 0, "msg": "", "data": {}}
    # 获取部门ID
    uid = request.GET.get("uid")
    if not uid:
        uid = request.user.dtalkid
    if uid in [None, ""]:
        result["code"] = -1
        result["error"] = "参数错误"
        return JsonResponse(result)
    legend_data = ["确认归档", "实际完成"]
    now = arrow.now()
    start = request.GET.get("start")
    if not start:
        start = arrow.now().floor("month")
    ok_data_list = []
    actual_data_list = []
    user = User.objects.filter(dtalkid=uid).first()
    name = user.username
    saler = CrmUser.objects.filter(name=name).first()
    if not saler:
        result["code"] = -1
        result["error"] = "查无此人"
        return JsonResponse(result)
    # 从商机表中ownerId、区总确认合同归档日期等条件查询商机金额
    sql2 = """Select ownerId, sum(money) as sum_money from `opportunity` WHERE ownerId={} 
            AND dbcDate15 LIKE '%{}%' GROUP BY ownerId;""".format(saler.id, now.strftime("%Y-%m"))
    saler_datas = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    ok_data_list.append(saler_datas.get(str(saler.id), 0))
    
    #从订单中根据订单状态，按照大区查询政务事业部实际收款情况
    sql3 = """SELECT ownerId, sum(amount), sum(dbcReal2) FROM `order` WHERE poStatus=2 
            AND dbcDate14 IS TRUE AND dbcSelect10=1 AND ownerId={} 
            AND FROM_UNIXTIME(dbcDate14/1000, '%Y-%m')='{}' GROUP BY ownerId;""".format(saler.id, now.strftime("%Y-%m")) 
    datas = get_all_data(settings.DATABASES["contract_33"], sql3)
    if not datas:
        datas = ((0, 0, 0),)
    actual_data_list.append(datas[0][2])

    date_list = []
    date_list.append(name)
        
    plan_all = int(sum(ok_data_list))
    actual_all = int(sum(actual_data_list))
    series = [
        # {   
        #     "label": {
        #         "normal": {
        #             "show": True,
        #             "position": "top",
        #             # "textStyle": {
        #             #     "color": 'black',
        #             #     # "fontSize": 10
        #             # }
        #         }
        #     },
        #     "name": "个人目标",  
        #     "stack": "目标",
        #     "data": [ceil(float(i)) for i in goal_data_list],
        #     "type": "line" if len(date_list) > 1 else "bar",
        #     # "color": "#fb9678"
        # },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "确认归档",  
            "stack": "归档",
            "data": [int(i) for i in ok_data_list],
            "type": "bar",
            # "color": "#00c292",
            "barCategoryGap": '80%'
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "实际完成",  
            "stack": "实际",
            "data": [int(i) for i in actual_data_list],
            "type": "bar",
            # "color": "#ab8ce4",
            "barCategoryGap": '80%'
        }
    ]
    
    option = {
        "title": {
            "text": '{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '区总确认归档：%s元，实际：%s元'%(format(plan_all, ","), format(actual_all, ","))
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "x" : 'right',
            "y" : 'top',
            "itemWidth": 8,
            "itemHeight": 8,
            "textStyle":{
                "fontSize":12
            },
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        # "toolbox": {
        #     "feature": {
        #         "saveAsImage": {},
        #         "restore": {},
        #         "dataView": {},
        #         # "dataZoom": {},
        #         # "magicType": {},
        #         # "brush": {}
        #     }
        # },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list,
            "axisLabel": {
                "interval":0, # 坐标刻度之间的显示间隔，默认就可以了（默认是不重叠）
                "rotate":38   # 调整数值改变倾斜的幅度（范围-90到90）
            }
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["error"] = "数据获取成功"
    result["data"] = option
    return JsonResponse(result)
    