import json


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.forms import model_to_dict


from secretary.models import DingGroupMemberMap
from customer.models import Department, Account

# logger = logging.getLogger("sale")

# # Create your views here.

region_name_map = dict([(2, "一大区"), (3, "二大区"), (4, "三大区"), (5, "四大区"), (6, "五大区"), (30, "六大区"), 
            (31, "七大区"), (32, "八大区"), (23, "九大区"), (33, "上海特区"), (39, "行业扩展二部"), (22, "政务客户成功部"), (7, "办公室")])

# """钉钉跟account表里面某事业部销售中心的对应关系"""
# dingding_account_sale_center_map = {"58062185": "1", "58034238": "2"}

# """钉钉跟account表里面大区的对应关系"""
# dingding_account_region_map = {
#     "58084244": "2", "58127361": "3", "58068265": "4", "155650269": "5", "58111257": "6",
#     "98192107": "30", "98019131": "31", "98006134": "32", "98266229": "23", 
#     "98187117": "33", "111457167": "39", "61147353": "22", "58040397": "7",
# }

"""销售易跟account表里面某事业部销售中心的对应关系"""
crm_account_sale_center_map = {"432566": "1", "432567": "2"}

"""销售易跟account表里面大区的对应关系"""
crm_account_region_map = {
    "435509": "2", "435342": "3", "435343": "4", "435634": "5", "435445": "6",
    "876279": "30", "875683": "31", "876483": "32", "876486": "23", 
    "876487": "33", "665498088571089": "39", "435633": "22", #"58040397": "7", 在销售易中未找到办公室  这个部门 的对应关系
}

# """钉钉 - 政务事业部 - 销售中心"""
# # @permission_required("sale.view_department_portrait")
# def dingding_government_center(request):
#     title = "政务事业部 - 销售中心"
#     g_center_did = "58062185"
#     did = request.GET.get("did")
#     if did != g_center_did:
#         path = request.path + "?did=" + g_center_did
#         return redirect(path)
#     return render(request, "sale/g-center.html", locals())

"""销售易 - 政务事业部 - 销售中心"""
# @permission_required("sale.view_department_portrait")
def crm_government_center(request):
    title = "政务事业部 - 销售中心"
    g_center_did = "432566"
    did = request.GET.get("did")
    if did != g_center_did:
        path = request.path + "?did=" + g_center_did
        return redirect(path)
    return render(request, "sale/g-center.html", locals())

"""此函数针对ding_group_member这张表里面的数据结构"""
def dingding_get_children(did, all, deep=False):
    children = []
    root = all.get(did)
    if not root:
        return children
    sub_js = json.loads(root.get("sub_group_ids"))
    if not sub_js:
        return children
    for group_id in sub_js:
        group_id = str(group_id)
        child = {}
        item = all.get(group_id)
        
        if item:
            child["did"] = group_id
            child["name"] = item["group_name"]
            if deep == True:
                child["children"] = dingding_get_children(group_id, all, deep=deep)
            children.append(child)
    return children

# def test():
#     all = DingGroupMemberMap.objects.all()
#     all_dict = {}
#     for a in all:
#         a = model_to_dict(a)
#         all_dict[a["group_id"]] = a
#     did = "58062185"
#     c = get_children(did, all_dict)
#     print(c)

# def test2():
#     all = DingGroupMemberMap.objects.all()
#     all_dict = {}
#     for a in all:
#         a = model_to_dict(a)
#         all_dict[a["group_id"]] = a
#     did = "58062185"
#     c = get_children(did, all_dict, deep=True)
#     print(c)

"""钉钉部门架构"""    
def dingding_department_frame_api(request):
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
    tree["children"] = dingding_get_children(did, all_dict, deep=True)
    result["code"] = 1
    result["data"] = tree
    return JsonResponse(result)

"""销售易部门架构"""
def crm_get_children(did, all, deep=False):
    children = []
    for k, v in all.items():
        if v["parentdepartid"] == did:
            child = {}
            child["did"] = k
            child["name"] = v["departname"]
            if deep == True:
                child["children"] = crm_get_children(k, all, deep=deep)
            children.append(child)
    return children

"""销售易部门架构"""    
def crm_department_frame_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    all = Department.objects.all()
    all_dict = {}
    for i in all:
        i = model_to_dict(i)
        all_dict[i["id"]] = i
    did = int(did)
    head = all_dict.get(did)
    if not head:
        result["msg"] = "此部门不存在"
        return JsonResponse(result)
    # tree = {"did": did, "name": head["group_name"]}
    tree = {"did": did, "name": head["departname"]}
    tree["children"] = crm_get_children(did, all_dict, deep=True)
    result["code"] = 1
    result["data"] = tree
    return JsonResponse(result)

"""某销售中心-客户数量"""
def count_customer_sale_center(cid):
    # cid: 1 政务, 2 企业
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week_once": 0, "month_once": 0, "three_month_once": 0, 
            "trial_three_months_高活跃":0, "dead": 0, "highsea_activity": 0}
    total = Account.objects.filter(dbcselect6=cid).count()
    formal = Account.objects.filter(dbcselect6=cid, level=5).count()
    important = Account.objects.filter(dbcselect6=cid, level=1).count()
    develop = Account.objects.filter(dbcselect6=cid, level=4).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return data

"""某大区-客户数量"""
def count_customer_region(rid):
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week_once": 0, "month_once": 0, "three_month_once": 0, 
            "trial_three_months_高活跃":0, "dead": 0, "highsea_activity": 0}
    total = Account.objects.filter(dbcselect7=rid).count()
    formal = Account.objects.filter(dbcselect7=rid, level=5).count()
    important = Account.objects.filter(dbcselect7=rid, level=1).count()
    develop = Account.objects.filter(dbcselect7=rid, level=4).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return data

"""某部门-客户数量"""
def count_customer_department(did):
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week_once": 0, "month_once": 0, "three_month_once": 0, 
            "trial_three_months_高活跃":0, "dead": 0, "highsea_activity": 0}
    total = Account.objects.filter(dbcvarchar8=did).count()
    formal = Account.objects.filter(dbcvarchar8=did, level=5).count()
    important = Account.objects.filter(dbcvarchar8=did, level=1).count()
    develop = Account.objects.filter(dbcvarchar8=did, level=4).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return data

"""政务中心-销售中心-某大区-某部门-某商务-客户数量"""
def count_customer_saler(sid):
    data = {"total": 0, "formal": 0, "important": 0, "develop": 0, 
            "week_twice": 0, "week_once": 0, "month_once": 0, "three_month_once": 0, 
            "trial_three_months_高活跃":0, "dead": 0, "highsea_activity": 0}
    total = Account.objects.filter(dbcselect6=sid).count()
    formal = Account.objects.filter(dbcselect6=sid, level=5).count()
    important = Account.objects.filter(dbcselect6=sid, level=1).count()
    develop = Account.objects.filter(dbcselect6=sid, level=4).count()
    data["total"] = total
    data["formal"] = formal
    data["important"] = important
    data["develop"] = develop
    return data

def customer_count_sale_center_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    cid = request.GET.get("cid")
    cid = crm_account_sale_center_map.get(cid)
    if not cid:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_sale_center(cid)
    result["data"] = data
    return JsonResponse(result)

def customer_count_region_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    rid = request.GET.get("rid")
    rid = crm_account_region_map.get(rid)
    if not rid:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_region(rid)
    result["data"] = data
    return JsonResponse(result)

def customer_count_department_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    # did = ding_account_department_map.get(did)
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_department(did)
    result["data"] = data
    return JsonResponse(result)

def customer_count_saler_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    sid = request.GET.get("sid")
    # sid = dingding_account_region_map.get(sid)
    if not sid:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    data = count_customer_saler(sid)
    result["data"] = data
    return JsonResponse(result)

    