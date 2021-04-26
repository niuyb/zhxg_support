import json
import time
import traceback

import arrow
import pymysql
import pandas as pd
import hashlib
import datetime
import logging
import requests

from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required, login_required
from django.forms import model_to_dict

# from user_center.models import WkTDinguserNew
from django.conf import settings

from customer.forms import CustomerListSelectForm
from customer.service.questionnaireService import encryption
from customer.utils import (
        get_industry_data, get_industry_data_1,
        get_industry_l1_dict, get_industry_l2_dict,
        get_state_dict, get_city_dict, get_district_dict,
        random_password, account_type, version_select
    )
from user_center.models import LocationInfo, UserLog
from public.utils import parse_kwargs_for_pymysql, get_all_data
from customer.models import CrmLocationState, CrmLocationCity, CrmLocationDistrict, Questionaire
from secretary.models import DingGroupMemberMap
from work_platform.models import CrmWechatMapping

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("customer")
import re

# Create your views here.

User = get_user_model()
 
"""客户查询页面"""
@login_required
@permission_required("customer.customer_list.view",login_url=URL_403)
def customer_list(request):
    if request.method == "GET":
        title = "客户查询"
        xtype = request.GET.get("xtype")
        if not xtype:
            xtype = 0

        if xtype in [1, "1"]:
            red = "/customer/government/customer/list?" + request.META["QUERY_STRING"]
            return redirect(red)

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="客户管理-客户列表", action="访问", message=message)
                

        form_dict = json.dumps(dict(request.GET))
        form = CustomerListSelectForm(request.GET)
        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        # init_data["col_names"] = ["客户名称", "一级行业", "二级行业", "客户地域-省", "客户地域-市", "客户地域-县",
        #         "是否覆盖", "客户状态", "调研表状态","操作"]
        init_data["col_names"] = ["客户名称", "一级行业", "二级行业", "客户地域-省", "客户地域-市", "客户地域-县", "客户状态", "操作"]
        init_data["col_model"] = [
            {
                "name": 'customer_name',
                "width": 20
            },
            {
                "name": 'industry1_name',
                "width": 5
            },
            {
                "name": 'industry2_name',
                "width": 5
            },
            {
                "name": 'state',
                "width": 10
            },
            {
                "name": 'city',
                "width": 10
            },
            {
                "name": 'district',
                "width": 10
            },
            # {
            #     "name": 'coverage',
            #     "width": 5
            # },
            {
                "name": 'status',
                "width": 5
            },
            # {
            #     "name": 'have_questionnaire',
            #     "width": 5
            # },
            {
                "name": 'operations',
                "width": 35
            }
        ]

        access = {}
        # 绑定微信群
        if request.user.has_perm("customer.customer_list.bind"):
            access["bind_wechat_group"] = 1

        # 导出客户列表
        if request.user.has_perm("customer.customer_list.export"):
            access["export_customer_list"] = 1

        # 推送微信群消息
        if request.user.has_perm("customer.customer_list.push"):
            access["push_wechat_message"] = 1

        init_data["access"] = access

        init_data["items"] = []
        init_data = json.dumps(init_data)
        
        industry_data = get_industry_data()
        industry_data = json.dumps(industry_data)
        industry_data_1 =[["", "--------"]] + get_industry_data_1()
        industry_data_1 = json.dumps(industry_data_1)
        states = list(CrmLocationState.objects.all().values())
        states = json.dumps(states)
        cities = list(CrmLocationCity.objects.all().values())
        cities = json.dumps(cities)
        districts = list(CrmLocationDistrict.objects.all().values())
        districts = json.dumps(districts)
        return render(request, "customer/customer_list.html", locals())
 
"""公宣客户查询页面"""
@login_required
@permission_required("customer.government_customer_list.view",login_url=URL_403)
def government_customer_list(request):
    if request.method == "GET":

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="客户管理-公宣客户列表", action="访问", message=message)

        title = "公宣客户查询"
        # xtype = request.GET.get("xtype")
        # if not xtype:
        #     xtype = 0
        
        # 强制xtype=1
        xtype = 1

        form_dict = json.dumps(dict(request.GET))
        form = CustomerListSelectForm(request.GET)
        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        init_data["col_names"] = ["客户名称", "一级行业", "二级行业", "客户地域-省", "客户地域-市", "客户地域-县", 
                "是否覆盖", "客户状态"]#, "操作"] 
        init_data["col_model"] = [
            {
                "name": 'customer_name',
                "width": 20
            },
            {
                "name": 'industry1_name',
                "width": 10
            },
            {
                "name": 'industry2_name',
                "width": 10
            },
            {
                "name": 'state',
                "width": 10
            },
            {
                "name": 'city',
                "width": 10
            },
            {
                "name": 'district',
                "width": 10
            },
            {
                "name": 'coverage',
                "width": 10
            },
            {
                "name": 'status',
                "width": 10
            },
            # {
            #     "name": 'operations',
            #     "width": 10
            # }
        ]
        init_data["items"] = []
        init_data = json.dumps(init_data)
        
        industry_data = [
            {"id": 46, "name": "公安局", "pid": 51},
            {"id": 14, "name": "宣传部", "pid": 51}
        ]
        industry_data = json.dumps(industry_data)
        industry_data_1 =[[51, "政府"]]
        industry_data_1 = json.dumps(industry_data_1)
        states = list(CrmLocationState.objects.all().values())

        if (not request.user.is_superuser) and (not request.user.roles.filter(code='leader')):
            dingframes = []
            #dingframes = get_dpts_that_user_can_see(request.user)

            if not dingframes:
                dingframe = request.user.dingframe
                dingframes = dingframe.split(",")

            dpts = DingGroupMemberMap.objects.filter(group_id__in=dingframes)
            dpt_names = []
            for dpt in dpts:
                _dpt_name = dpt.group_name
                _dpt_names = json.loads(dpt.sub_group_names_all)
                if _dpt_names:
                    dpt_names.extend(_dpt_names)
                else:
                    dpt_names.append(_dpt_name)

            _states = states
            states = []
            for state in _states:
                lname = state["lname"]
                for end in ["省", "市", "特别行政区"]:
                    if lname.endswith(end):
                        lname = lname.strip(end)

                if lname.endswith("自治区"):
                    lname = lname[0: 2]

                if lname in dpt_names:
                    states.append(state)

        states = json.dumps(states)
        cities = list(CrmLocationCity.objects.all().values())
        cities = json.dumps(cities)
        districts = list(CrmLocationDistrict.objects.all().values())
        districts = json.dumps(districts)
        return render(request, "customer/customer_list.html", locals())



"""查询客户列表"""
def get_customer_list(request, kws):

    is_first = kws.get("is_first")

    result = {"status": 0, "message": ""}
    form = CustomerListSelectForm(kws)

    # 此参数用来判断查询哪张数据表
    xtype = kws.get("xtype")
    
    if form.is_valid():
        cdata = form.cleaned_data
        customer_name = cdata.get("customer_name")
        coverage = cdata.get("coverage")
        status = cdata.get("status")
        wechat_group = cdata.get("wechat_group")
        industry1_id = cdata.get("industry1")
        industry2_id = cdata.get("industry2")
        state_id = cdata.get("state")
        city_id = cdata.get("city")
        district_id = cdata.get("district")
        industry1_dict = get_industry_l1_dict()
        industry2_dict = get_industry_l2_dict()
        state_dict = get_state_dict()
        city_dict = get_city_dict()
        district_dict = get_district_dict()

        if status == "0" and coverage == "1":
            result["message"] = "不能同时选择“是否覆盖：是”和“客户状态：其他”"
            return result
        if status in ["1", "2"] and coverage == "0":
            result["message"] = "不能同时选择“是否覆盖：否”和“客户状态：正式 或者 试用”"
            return result

        cids = None
        if wechat_group:

            that_time = arrow.now().shift(hours=-25).format("YYYY-MM-DD HH:mm:ss")
            # 未绑定
            if wechat_group in ["0", 0]:
                cids = list(CrmWechatMapping.objects.exclude(status=0).values_list("customer_id", flat=True))

            # 申请中
            elif wechat_group in ["1", 1]:
                cids = list(CrmWechatMapping.objects.filter(status=3).values_list("customer_id", flat=True))

            # 审核中
            elif wechat_group in ["2", 2]:
                cids = list(CrmWechatMapping.objects.filter(status=1, ctime__gte=that_time).values_list("customer_id", flat=True))

            # 已绑定
            elif wechat_group in ["3", 3]:
                cids = list(CrmWechatMapping.objects.filter(status=1, ctime__lt=that_time).values_list("customer_id", flat=True))

            # 绑定失败
            elif wechat_group in ["4", 4]:
                cids = list(CrmWechatMapping.objects.filter(status=2).values_list("customer_id", flat=True))

            else:
                cids = []
                result["status"] = -1
                result["message"] = "参数错误"
                return result

        table1 = "`order`"

        date = datetime.datetime.now() - datetime.timedelta(days=30)
        date = datetime.datetime.strptime(str(date.date()), "%Y-%m-%d")
        timestamp = date.timestamp() * 1000
        dbcDate3 = datetime.datetime.fromtimestamp(timestamp / 1000.0).strftime("%Y-%m-%d %H:%M:%S")

        sql1 = """select dbcrelation1 from {} 
                where  postatus=2 
                    and dbcSelect3=4 
                    and dbcDate3>'{}' 
                    and dbcrelation1 IS NOT NULL 
                group by dbcrelation1""".format(table1, dbcDate3)

        try:
            kws = parse_kwargs_for_pymysql(settings.DATABASES["crminfo_33"])
            conn_33 = pymysql.connect(**kws)
            cursor = conn_33.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql1)
            items = cursor.fetchall()
            cursor.close()
            conn_33.close()
        except Exception as e:
            logger.error(str(e))
            result["message"] = "服务器繁忙，请稍后重试"
            return result

        cid_dict = {}
        for i in items:
            cid = i["dbcrelation1"]
            cid_dict[cid] = 1

        if xtype in [1, "1"]:
            table2 = "police_and_internet_account"
            sql2 = """SELECT id, accountName as customer_name, coverage,
                            industry1_id as industry1_name, industry2_id as industry2_name,
                            fState1 as state, fCity1 as city, fDistrict1 as district, "其他" as status
                    FROM {} 
            """.format(table2)

        else:
            table2 = "account"
            sql2 = """SELECT id, accountName as customer_name, highseastatus as coverage,
                            dbcSelect5 as industry1_name, dbcSelect9 as industry2_name,
                            fState as state, fCity as city, fDistrict as district, "其他" as status
                    FROM {} 
            """.format(table2)

        where = ["id IN {}".format(str(tuple(set(cids))).replace(",)", ")"))] if cids is not None else []

        #判断调研表是否填写
        table3 = "questionaire"
        sql_question = """
            SELECT account_id FROM {} 
        """.format(table3)
        if settings.MODE == 'develops' or settings.MODE == 'beta':
            question_kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
        else:
            question_kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])

        question_conn_33 = pymysql.connect(**question_kws)
        question_cursor = question_conn_33.cursor(pymysql.cursors.DictCursor)
        question_cursor.execute(sql_question)
        question_items = question_cursor.fetchall()
        question_cursor.close()
        question_conn_33.close()
        question_items_ids = [i["account_id"] for i in question_items]


        #判断是否有商机
        sql_opp = "select dbcRelation1 from opportunity "
        kws = parse_kwargs_for_pymysql(settings.DATABASES["crminfo_33"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_opp)
        opp_list = cursor.fetchall()
        cursor.close()
        conn.close()
        opp_account_ids = [i["dbcRelation1"] for i in opp_list]



        """ 以下代码控制数据权限 """
        # group_id = 12，角色是管理层，可以查看全部数据
        # if (not request.user.is_superuser) and (not request.user.roles.filter(code='leader').first()):
        #     dingframes = []
        #     #dingframes = get_dpts_that_user_can_see(request.user)
        #
        #     if not dingframes:
        #         dingframe = request.user.dingframe
        #         dingframes = dingframe.split(",")
        #
        #     dpts = DingGroupMemberMap.objects.filter(group_id__in=dingframes)
        #     dpt_names = []
        #     for dpt in dpts:
        #         _dpt_name = dpt.group_name
        #         _dpt_names = json.loads(dpt.sub_group_names_all)
        #         if _dpt_names:
        #             dpt_names.extend(_dpt_names)
        #         else:
        #             dpt_names.append(_dpt_name)
        #
        #     if not dpt_names:
        #         error = "部门错误"
        #         code = -1
        #         result["message"] = error
        #         result["error"] = error
        #         result["status"] = code
        #         result["code"] = code
        #         return result
        #
        #     w = []
        #     for dpt_name in dpt_names:
        #         item = "state like '%%%s%%'"%dpt_name
        #         if xtype in [1, "1"]:
        #             item = "state1 like '%%%s%%'"%dpt_name
        #         w.append(item)
        #
        #     item = "(" + " OR ".join(w) + ")"
        #     where.append(item)




        if customer_name:
            item = "accountName LIKE '%{}%'".format(customer_name)
            where.append(item)

        if industry1_id:
            if industry1_id == "0":
                item = "((dbcSelect5 IS NULL) OR (dbcSelect5=''))"
                if xtype in [1, "1"]:
                    item = "((industry1_id IS NULL) OR (industry1_id=''))"
            else:
                item = "dbcSelect5={}".format(industry1_id)
                if xtype in [1, "1"]:
                    item = "industry1_id={}".format(industry1_id)

            where.append(item)

        if industry2_id:
            if industry2_id == "0":
                item = "((dbcSelect9 IS NULL) OR (dbcSelect9=''))"
                if xtype in [1, "1"]:
                    item = "((industry2_id IS NULL) OR (industry2_id=''))"
            else:
                item = "dbcSelect9={}".format(industry2_id)
                if xtype in [1, "1"]:
                    item = "industry2_id={}".format(industry2_id)

            where.append(item)

        if state_id:
            if state_id == "0":
                item = "((fstate IS NULL) OR (fstate=''))"
                if xtype in [1, "1"]:
                    item = "((fstate1 IS NULL) OR (fstate1=''))"
            else:
                item = "fstate={}".format(state_id)
                if xtype in [1, "1"]:
                    item = "fstate1={}".format(state_id)

            where.append(item)

        if city_id:
            if city_id == "0":
                item = "((fcity IS NULL) OR (fcity=''))"
                if xtype in [1, "1"]:
                    item = "((fcity1 IS NULL) OR (fcity1=''))"
            else:
                item = "fcity={}".format(city_id)
                if xtype in [1, "1"]:
                    item = "fcity1={}".format(city_id)

            where.append(item)
        if district_id:
            if district_id == "0":
                item = "((fDistrict IS NULL) OR (fDistrict=''))"
                if xtype in [1, "1"]:
                    item = "((fDistrict1 IS NULL) OR (fDistrict1=''))"
            else:
                item = "fDistrict={}".format(district_id)
                if xtype in [1, "1"]:
                    item = "fDistrict1={}".format(district_id)

            where.append(item)

        if coverage:
            if coverage == "1":
                item = "highseastatus IN (1, 3, 4)"

                if xtype in ["1", 1]:
                    item = "coverage={}".format(coverage)

                where.append(item)
            if coverage == "0":
                item = "highseastatus NOT IN (1, 3, 4)"

                if xtype in ["1", 1]:
                    item = "coverage={}".format(coverage)

                where.append(item)

        # status : 0, 其他  1，试用  2，正式
        if status:
            cid_tuple = tuple(cid_dict.keys())
            if status == "2":
                item = "id IN " + str(cid_tuple)

                if xtype in ["1", 1]:
                    item = "status={}".format(status)

                where.append(item)

            if status == "1":
                item = "id NOT IN " + str(cid_tuple)

                if xtype in ["1", 1]:
                    item = "status={}".format(status)

                where.append(item)

            if status == "0":
                if xtype in ["1", 1]:
                    item = "status={}".format(status)
                    where.append(item)

        orderby = ' ORDER BY createdAt DESC '
        if where:
            if is_first:
                sql2 += "WHERE " + " AND ".join(where) + orderby + " limit 0, 500;"
            else:
                sql2 += "WHERE " + " AND ".join(where) + orderby +";"
        else:
            if is_first:
                sql2 += orderby + " limit 0, 500;"




        try:
            kws = parse_kwargs_for_pymysql(settings.DATABASES["crminfo_33"])
            conn_33 = pymysql.connect(**kws)
            cursor = conn_33.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql2)
            items = cursor.fetchall()
            cursor.close()
            conn_33.close()
        except Exception as e:
            logger.error(str(e))
            result["message"] = "服务器繁忙，请稍后重试"
            return result
        for item in items:
            ret = cid_dict.get(item["id"])
            if item["coverage"] in [1, 3, 4]:
                item["coverage"] = "是"
                if ret:
                    item["status"] = "正式"
                else:
                    item["status"] = "试用"
            else:
                item["coverage"] = "否"
            item["industry1_name"] = industry1_dict.get(item["industry1_name"], {}).get("name", "")
            item["industry2_name"] = industry2_dict.get(item["industry2_name"], {}).get("name", "")
            item["state"] = state_dict.get(item["state"], {}).get("lname", "")
            item["city"] = city_dict.get(item["city"], {}).get("lname", "")
            item["district"] = district_dict.get(item["district"], {}).get("lname", "")
            #下面俩是 客户 是否有 调研表 和 商机
            item["has_syc"] = 1 if item["id"] in question_items_ids else 0
            item["has_opp"] = 1 if item["id"] in opp_account_ids else 0

        cwms = list(CrmWechatMapping.objects.filter(status__in=[1, 2, 3], customer_id__gt=0).values("customer_id", "status", "ctime"))
        if cwms and items:
            df = pd.DataFrame(items)
            _df = pd.DataFrame(cwms)
            _df = _df.rename(columns={"status": "wechat_group_status", "ctime": "wechat_group_ctime"})
            df = pd.merge(df, _df, how="left", left_on="id", right_on="customer_id")

            df = df.fillna(0)
            items  = list(df.to_dict(orient="index").values())

        result["status"] = 1
        result["items"] = items
    return result
    

"""客户查询数据接口，返回json格式的数据"""
# @permission_required("customer.customer_list.view",login_url=JSON_403)
def customer_list_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-客户列表api", action="查询", message=message)

    result = get_customer_list(request, kws)
    return JsonResponse(result)

def customer_list_add_api(request):

    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))

    if message:
        crmid = kws.get("account_id")
        sql = "select * from opportunity where dbcRelation1= '{}'".format(crmid)
        kws = parse_kwargs_for_pymysql(settings.DATABASES["crminfo_33"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        oppinfo = cursor.fetchall()
        if oppinfo:
            result = {'code': 0, 'status': 1, 'datas': oppinfo}
            return JsonResponse(result, safe=False)

        else:
            result = {'code': 0, 'status': 0, 'message': '客户下无商机!'}
            return JsonResponse(result, safe=False)

def phone(phone):

    # if re.match(r'1[3,4,5,7,8]\d{9}', phone):
    #     url = 'http://192.168.182.22:8080/yqms/v1/whetherBindPhone?telphone={}'.format(phone)
    #     r = requests.get(url=url)
    #     r = json.loads(r.text)
    #     r = r["result"]["data"]
    #
    #     if r["whetherBindPhone"] is True:
    #         result = {'data': {"data":  r}, 'code': 1, 'message': '已绑定'}
    #     else:
    #         result = {'data': {"data": {}}, 'code': 2, 'message': '未绑定'}
    #     return result
    # else:
    #     result = {'code': 0, 'status': 1, 'message': '手机号格式不正确!'}
    #     return result
    try:
        if re.match(r'1[3,4,5,7,8]\d{9}', phone):

            try:
                url = 'http://192.168.182.22:8080/yqms/v1/whetherBindPhone?telphone={}'.format(phone)
                headers = {'FROM': 'xght'}
                r = requests.get(url=url,headers=headers)
                r = json.loads(r.text)
                try:
                    r = r["result"]["data"]
                    try:
                        if r["whetherBindPhone"] is True:
                            result = {'data': {"data":  r}, 'code': 1, 'message': '已绑定'}
                        else:
                            result = {'data': {"data": {}}, 'code': 2, 'message': '未绑定'}
                    except:
                        result = {'code': 0, 'status': 1, 'message': '获取whetherBindPhone报错!data为：{}'.format(r)}
                except:
                    result = {'code': 0, 'status': 1, 'message': '调秦栓接口获取data报错!r为：{}'.format(r)}
            except:
                result = {'code': 0, 'status': 1, 'message': '调秦栓接口报错!'}
        else:
            result = {'code': 0, 'status': 1, 'message': '手机号格式不正确!'}
    except:
        result = {'code': 0, 'status': 1, 'message': '正则校验报错!'}
    return result






"""
    接口功能：快速创建账号的数据接口(目前支持产品：舆情秘书)；
    参数：
        product_id
        account_id(老客户id)
    返回：json格式的数据。
"""
# @permission_required("customer.customer_list.view",login_url=JSON_403)
def get_account_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-客户列表-创建秘书api", action="查询", message=message)

    # 此参数用来判断要创建的是哪个产品，比如舆情秘书的id为yqms
    product_id = kws.get("product_id")
    if product_id == 'yqms':
        result = create_yqms(kws)
    else:
        # 默认创建舆情秘书账号
        result = create_yqms(kws)

    return JsonResponse(result)


"""获取快速创建舆情秘书账号的信息"""
def create_yqms(kws):
    try:
        account_id = kws.get("account_id")
        # login_name = kws.get("login_name")
        pwd = random_password()

        database = settings.DATABASES["crminfo_33"]
        database_yqht = settings.DATABASES["yqht_199"]
        acc_sql = """ SELECT
                        a.accountName,
                        in1. NAME AS industry1,
                        in2. NAME AS industry2,
                        lo1.lname AS state,
                        lo2.lname AS city,
                        lo3.lname AS district,
                        a.dbcVarchar2 AS phone,
                        a.id,
                        a.dbcSelect5 AS industry1_id,
                        a.dbcSelect9 AS industry2_id,
                        a.fState AS state_id,
                        a.fCity AS city_id,
                        a.fDistrict AS district_id,
                        a.new_account_id,
                        a.update_timestamp
                    FROM
                        account a
                    LEFT JOIN crm_industry_l1 in1 ON a.dbcSelect5 = in1.id
                    LEFT JOIN crm_industry_l2 in2 ON a.dbcSelect9 = in2.id
                    LEFT JOIN crm_location_State lo1 ON a.fState = lo1.lid
                    LEFT JOIN crm_location_City lo2 ON a.fCity = lo2.lid
                    LEFT JOIN crm_location_District lo3 ON a.fDistrict = lo3.lid 
                    WHERE a.id ='{}' """.format(account_id)

        acc_data = get_all_data(database, acc_sql)

        acc_dict = {}
        # acc_data是一个只有一个info的元组
        for info in acc_data:
            state_name = info[3]
            state_id = None
            city_name = info[4]
            city_id = None
            district_name = info[5]
            district_id = None
            if state_name:
                state_id_aql = """ SELECT uuid AS state_id FROM b_locationinfo 
                                WHERE province LIKE '%{}%' AND city = '' AND county = '' LIMIT 1 """.format(state_name)
                state_id = get_all_data(database_yqht, state_id_aql)[0][0]

                if city_name:
                    city_id_aql = """ SELECT uuid AS state_id FROM b_locationinfo 
                                    WHERE province LIKE '%{}%' AND city LIKE '%{}%' 
                                    AND county = '' LIMIT 1 """.format(state_name, city_name)
                    city_id = get_all_data(database_yqht, city_id_aql)[0][0]

                    if district_name:
                        district_id_aql = """ SELECT uuid AS state_id FROM b_locationinfo 
                                            WHERE province LIKE '%{}%' AND city LIKE '%{}%' 
                                            AND county LIKE '%{}%' LIMIT 1 """.format(state_name, city_name, district_name)
                        district_id = get_all_data(database_yqht, district_id_aql)[0][0]


            acc_dict["account_name"] = info[0]  # 客户名称
            acc_dict["account_id"] = info[7]  # 客户id(老)
            acc_dict["new_account_id"] = info[13]  # 客户id(新)
            acc_dict["login_name"] = info[0]    # 账号登录名
            acc_dict["password"] = pwd
            acc_dict["industry1"] = info[1]     # 一级行业
            acc_dict["industry2"] = info[2]     # 二级行业
            acc_dict["industry1_id"] = info[8]  # 一级行业id
            acc_dict["industry2_id"] = info[9]  # 二级行业id
            acc_dict["state"] = info[3]     # 省
            acc_dict["city"] = info[4]      # 市
            acc_dict["district"] = info[5]  # 县区
            acc_dict["state_id"] = state_id  # 省id(老后台的地域id)
            acc_dict["city_id"] = city_id  # 市id(老后台的地域id)
            acc_dict["district_id"] = district_id  # 县区id(老后台的地域id)
            acc_dict["phone"] = info[6]     # 绑定手机号
            if info[14]:
                update_time = datetime.datetime.strptime(info[14], '%Y-%m-%d %H:%M:%S')
                time_format = "{}月{}日 {}点{}分".format(str(update_time.month),str(update_time.day), str(update_time.hour), str(update_time.minute))
            else:
                time_format = ""
            acc_dict["update_timestamp"] = time_format
            # acc_dict["maintainer"] = login_name     # 维护人（默认为新后台的登录名）

        if acc_dict["phone"]:
            try:
                check_phone = phone(acc_dict["phone"])
                if check_phone["code"] == 1:
                    bind_name = check_phone["data"]["data"]["userName"]
                    check_phone_result = '手机号{}已经绑定秘书账号{}，请前往CRM进行修改！'.format(acc_dict["phone"], bind_name)

                elif check_phone["code"] == 0:
                    check_phone_result = check_phone["message"]
                else:
                    check_phone_result = None
                acc_dict["check_phone"] = check_phone_result

                # acc_dict["check_phone"] = check_phone["message"]
            except:
                acc_dict["check_phone"] = '检查手机号接口报错，请联系管理员！'
        else:
            acc_dict["check_phone"] = None


        industry1 = acc_dict["industry1"]
        if industry1:
            acc_type, acc_type_id = account_type(industry1)
        else:
            # 当没有一级行业时，[用户类型]默认为'政府用户'
            acc_type = '政府用户'
            acc_type_id = '1'

        if acc_dict["district"] is None:
            district_level = '市级'
        elif acc_dict["city"] is None:
            district_level = '省级'
        else:
            # 在省为空或者省市县都不为空的情况下，为区县级客户
            district_level = '区县级'
        version, version_id, word_num = version_select(acc_type, district_level)

        acc_dict["account_type"] = acc_type     # 用户类型
        acc_dict["account_type_id"] = acc_type_id  # 用户类型id('1'、'4')
        acc_dict["version"] = version   # 版本选择
        acc_dict["version_id"] = version_id  # 版本选择id('B1'、'B2'、'B3')
        acc_dict["word_num"] = word_num     # 关键词数量、品牌词数量
        acc_dict["zh_type"] = [
            {"zh_type": '用户', "zh_type_id": '0'},
            {"zh_type": '代理商用户', "zh_type_id": '4'}
        ]  # 账号类型：用户、代理商用户（默认：用户）
        acc_dict["agent_name"] = None  # 代理商name（默认为空）
        acc_dict["agent_id"] = None   # 代理商id（默认为空）


        opp_sql = """ SELECT
                        opportunityName,
                        o.id AS opp_id,
                        u.name AS owner
                    FROM
                        opportunity o
                    LEFT JOIN user u ON o.ownerId = u.id 
                    WHERE dbcRelation1 ='{}' """.format(account_id)

        opp_data = get_all_data(database, opp_sql)
        opp_list = []

        # opp_data是一个可能有一个或多个info的元组
        for info in opp_data:
            opp_dict = {}
            opp_dict["opp_name"] = info[0]      # 商机名称
            opp_dict["opp_id"] = info[1]    # 商机id(老)
            opp_dict["opp_owner"] = info[2]     # 商机负责人
            opp_list.append(opp_dict)

        result = {"status": 1, "message": "成功获取创建账号基础数据", "acc_data": acc_dict, "opp_data": opp_list}
    except:
        print(traceback.print_exc())
        result = {"status": 0, "message": "失败", "acc_data": {}, "opp_data": []}
    # print(result)
    return result


