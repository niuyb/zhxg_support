import json
import pandas as pd
import logging
from django.http import HttpResponse, JsonResponse
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required
from django.db.models import F

from secretary.utils import get_departments_about_sale, get_can_see, get_group_members
from secretary.models import DingGroupMemberMap, Crmaccountmapping
from customer.models import User as CrmUser
from customer.models import (Department, Account, Activityrecord, 
        ActivityrecordMapping, Opportunity, Order, SaleStage)
from user_center.models import UserLog
from django.conf import settings

from ._common import (translate_level, make_result)
from ._saler import (get_crmusers_by_dtalkids)

JSON_403 = settings.JSON_403
logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

"""通过指定的商务的id来获取商机列表"""
def get_opportunity_list_by_dtalkids(dtalkids): 
    crmusers = get_crmusers_by_dtalkids(dtalkids)
    salers = crmusers.values(saler_id=F("id"), saler_name=F("name"), department_id=F("departid"))
    sdf = pd.DataFrame(salers)

    departments = Department.objects.all().values(department_id=F("id"), department_name=F("departname"))
    ddf = pd.DataFrame(departments)

    ddf["department_id"] = ddf["department_id"].apply(lambda x: str(x))

    sdf = pd.merge(sdf, ddf, how="left", on="department_id")
    saler_ids = list(sdf["saler_id"])
    oes = Opportunity.objects.filter(ownerid__in=saler_ids).values(
            "createdat", "closedate", opportunity_id=F("id"), 
            opportunity_name=F("opportunityname"), sale_stage_id=F("salestageid"),
            customer_id=F("dbcrelation1"), opportunity_money=F("money"), quzong_ok=F("dbcdate15"), 
            win_rate=F("winrate"), saler_id=F("ownerid"), last_visit=F("recentactivityrecordtime"))
    odf = pd.DataFrame(oes)

    sgs = SaleStage.objects.all().values(sale_stage_id=F("id"), sale_stage_name=F("name"))
    sgdf = pd.DataFrame(sgs)

    odf = pd.merge(odf, sgdf, how="left", on="sale_stage_id")
    sdf["saler_id"] = sdf["saler_id"].astype(str)
    odf = pd.merge(odf, sdf, how="left", on="saler_id")
    odf["quzong_ok"] = odf["quzong_ok"].apply(lambda x: "" if x is None else x.split(" ")[0])
    odf["win_rate"] = odf["win_rate"].apply(lambda x: 0 if x is None or x == "" else x)
    odf["win_rate"] = odf["win_rate"].fillna(0)
    odf["saler_name"] = odf["saler_name"].apply(lambda x: "" if x is None else x)
    odf["last_visit"] = odf["last_visit"].apply(lambda x: "" if x is None else x)
    cids = list(odf["customer_id"])
    
    cs = Account.objects.filter(id__in=cids).values("level", customer_id=F("id"), customer_name=F("accountname"))
    cdf = pd.DataFrame(cs)

    cdf["customer_id"] = cdf["customer_id"].astype(str)
    cdf = pd.merge(odf, cdf, how="left", on="customer_id")
    cdf["customer_id"] = cdf["customer_id"].fillna(0)
    cdf["customer_name"] = cdf["customer_name"].apply(lambda x: "" if x is None else x)
    cdf["customer_name"] = cdf["customer_name"].fillna("")
    cdf["opportunity_money"] = cdf["opportunity_money"].fillna(0)#.apply(lambda x: int(x))
    cdf["level"] = cdf["level"].apply(translate_level)
    cdf = cdf.fillna("----")
    data = list(cdf.to_dict(orient="index").values())
    return make_result(data, 1, "测试")    

"""通过指定的商务的id来获取商机"""
@permission_required("sale.government_center.opportunity_tab.view", login_url=JSON_403)
def opportunity_list_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商机列表api", action="查询", message=message)

    result = {"code": 0, "data": None, "error": ""}
    did = request.GET.get("did")
    uid = request.GET.get("uid")
    page = request.GET.get("page")
    try:
        page = int(page)
    except:
        page = 1
    num = request.GET.get("num")
    try:
        num = int(num)
    except:
        num = 20
    dtalkids = []
    if did:
        dgmm = DingGroupMemberMap.objects.filter(group_id=did).first()
        if dgmm:
            dtalkids = json.loads(dgmm.member_ids_all)
    elif uid:
        dtalkids = [ uid ]

    # 管理员可以查看所有商务的数据
    if request.user.is_superuser:
        pass
    else:
        # 权限控制，可以查看哪些商务的数据？
        can_see = get_can_see(request.user.username)
        salers = set(can_see)
        if not salers:
            result["code"] = 0
            result["error"] = "您无权查看任何数据"
            return result
        dtalkids = User.objects.filter(username__in=list(salers)).values_list("dtalkid", flat=True)

    if not dtalkids:
        result = make_result(None, -1, "找不到任何符合条件的商务人员")
        return JsonResponse(result)
    result = get_opportunity_list_by_dtalkids(dtalkids)
    if result["code"] < 1:
        return JsonResponse(result)
    items = result["data"]
    total = len(items)
    if num == 0:
        page = 1
    if total >= page * num:
        start = (page - 1) * num
        end = page * num - 1
        items = items[start: end]
    else:
        x = total % num
        page = (total - total % num) / num
        if x:
            page += 1
    data = {"data": items, "page": page, "num": total, "total": total}
    result["data"] = data
    return JsonResponse(result)

def get_opportunity_info(oid):
    result = {"code": 0, "data": None, "error": ""}
    opps = list(Opportunity.objects.filter(pk=oid).values(opportunity_id=F("id"), opportunity_name=F("opportunityname"), 
            saler_id=F("ownerid"), createdby_id=F("createdby"), updatedby_id=F("updatedby"), account_id=F("accountid"),
            customer_id=F("dbcrelation1"), opportunity_money=F("money"), sale_stage_id=F("salestageid")))
    if not opps:
        result["code"] = -1
        result["error"] = "参数错误"
        return result
    opp = opps[0]
    sale_stage_id = opp["sale_stage_id"]
    ss = SaleStage.objects.filter(pk=sale_stage_id).first()

    saler_ids = []
    saler_id = opp["saler_id"]
    createdby_id = opp["createdby_id"]
    updatedby_id = opp["updatedby_id"]
    if saler_id:
        saler_ids.append(saler_id)
    if createdby_id:
        saler_ids.append(createdby_id)
    if updatedby_id:
        saler_ids.append(updatedby_id)
    salers = list(CrmUser.objects.filter(pk__in=saler_ids).values().extra(select={"saler_id": "id", 
            "saler_name": "name"}))
    saler_dict = {str(saler["saler_id"]): saler for saler in salers}
    customer_ids = []
    account_id = opp["account_id"]
    customer_id = opp["customer_id"]
    if account_id:
        customer_ids.append(account_id)
    if customer_id:
        customer_ids.append(customer_id)
    customers = list(Account.objects.filter(pk__in=customer_ids).values().extra(select={"customer_id": "id", "customer_name": "accountname"}))
    customer_dict = {str(customer["customer_id"]): customer for customer in customers}
    saler = saler_dict.get(str(saler_id))
    if saler:
        opp["saler_name"] = saler["saler_name"]
    saler = saler_dict.get(str(createdby_id))
    if saler:
        opp["createdby"] = saler["saler_name"]
    saler = saler_dict.get(str(updatedby_id))
    if saler:
        opp["updatedby"] = saler["saler_name"]
    customer = customer_dict.get(str(account_id))
    if customer:
        opp["account"] = customer["customer_name"]
    customer = customer_dict.get(str(customer_id))
    if customer:
        opp["customer_name"] = customer["customer_name"]
    if ss:
        opp["sale_stage"] = ss.name
    result["code"] = 1
    result["data"] = opp   
    return result

@permission_required("sale.government_center.opportunity_tab.view", login_url=JSON_403)
def opportunity_info_api(request):
    oid = request.GET.get("id")
    result = get_opportunity_info(oid)

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商机详情api", action="查询", message=message)

    return JsonResponse(result)
