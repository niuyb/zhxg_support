import json
import arrow
import pandas as pd
import logging
from django.http import JsonResponse
from django.shortcuts import render
from mandala.auth import get_user_model
from mandala.auth.decorators import permission_required

from secretary.utils import get_can_see
from secretary.models import DingGroupMemberMap, Crmaccountmapping
from customer.models import (Department, Account, Activityrecord, 
        ActivityrecordMapping, Opportunity, Order, SaleStage)
from user_center.models import UserLog
from django.db.models import Sum, Count, Max
from django.conf import settings

from ._common import (get_left_days, get_left_days_by_utimestamp, translate_level, make_result)
from ._saler import (get_crmusers_by_dtalkids)

JSON_403 = settings.JSON_403
logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

"""通过指定的商务的id来获取客户列表"""
def get_customer_list_by_dtalkids(dtalkids): 
    crmusers = get_crmusers_by_dtalkids(dtalkids)
    salers = list(crmusers.values("id", "name", "departid"))
    sdf = pd.DataFrame(salers)
    sdf = sdf.rename(columns={"id": "saler_id", "name": "saler_name", "departid": "department_id"})
    departments = list(Department.objects.all().values("id", "departname"))
    ddf = pd.DataFrame(departments)
    ddf["id"] = ddf["id"].apply(lambda x: str(x))
    ddf = ddf.rename(columns={"id": "department_id", "departname": "department_name"})
    sdf = pd.merge(sdf, ddf, how="left", on="department_id")
    saler_ids = list(sdf["saler_id"])
    # 默认展示非公海池的客户
    cs = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1,3,4]).values("id", "accountname", "level", "ownerid", "recentactivityrecordtime")
    cdf = pd.DataFrame(cs)
    cids = list(cdf["id"])
    cdf = cdf.rename(columns={"id": "customer_id", "accountname": "customer_name", 
            "level": "customer_level", "ownerid": "saler_id", 
            "recentactivityrecordtime": "last_activity"})
    cdf = pd.merge(cdf, sdf, how="left", on="saler_id")
    cdf["customer_name"] = cdf["customer_name"].apply(lambda x: "" if x is None else x)
    cdf["customer_name"] = cdf["customer_name"].fillna("")
    cdf["saler_name"] = cdf["saler_name"].apply(lambda x: "" if x is None else x)
    cdf["saler_name"] = cdf["saler_name"].fillna("")
    cdf["last_activity"] = cdf["last_activity"].apply(lambda x: "" if x is None else x)
    cdf["last_activity"] = cdf["last_activity"].fillna("")
    crmams = Crmaccountmapping.objects.filter(crmuid__in=cids).values("crmuid").annotate(account_num=Count('msuid'))
    crmdf = pd.DataFrame(crmams)
    crmdf = crmdf.rename(columns={"crmuid": "customer_id"})
    # today = arrow.now()
    cdf = pd.merge(cdf, crmdf, how="left", on="customer_id")

    # # 从Activityrecord_mapping表里面通过客户ID查询活动记录ID
    # # 为什么要这么查询呢？因为商务有可能把拜访记录写在客户下，也有可能写在商机下，比较扯。。。
    # arids = ActivityrecordMapping.objects.filter(accountid__in=cids).values("activityid", "accountid")
    # adf = pd.DataFrame(arids)
    # adf = adf.rename(columns={"accountid": "customer_id"})

    # # 最近签到拜访日期
    # ares = Activityrecord.objects.filter(entitytype=4173079).values("id").annotate(last_visit=Max("createdat"))
    # ardf = pd.DataFrame(ares)
    # ardf = ardf.rename(columns={"id": "activityid"})
    # ardf = pd.merge(ardf, adf, how="left", on="activityid")
    # ardf = ardf.drop(["activityid"], axis=1)
    
    # cdf = pd.merge(cdf, ardf, how="left", on="customer_id")
    # cdf["last_visit"] = cdf["last_visit"].apply(lambda x: "" if x is None else x)
    # cdf["last_visit"] = cdf["last_visit"].fillna("")
    
    # # 最近电话拜访日期
    # ares = Activityrecord.objects.filter(entitytype=4173078).values("id").annotate(last_call=Max("createdat"))
    # ardf = pd.DataFrame(ares)
    # ardf = ardf.rename(columns={"id": "activityid"})
    # ardf = pd.merge(ardf, adf, how="left", on="activityid")
    # ardf = ardf.drop(["activityid"], axis=1)
    
    # cdf = pd.merge(cdf, ardf, how="left", on="customer_id")
    # cdf["last_call"] = cdf["last_call"].apply(lambda x: "" if x is None else x)
    # cdf["last_call"] = cdf["last_call"].fillna("")

    oes = Order.objects.filter(accountid__in=cids).values("accountid").annotate(days_left=Max("dbcdate7"))
    odf = pd.DataFrame(oes)
    odf = odf.rename(columns={"accountid": "customer_id"})
    cdf = pd.merge(cdf, odf, how="left", on="customer_id")
    cdf["customer_level"] = cdf["customer_level"].apply(translate_level)
    cdf["account_num"] = cdf["account_num"].fillna(0).apply(lambda x: int(x))
    now = arrow.now()
    cdf["days_left"] = cdf["days_left"].fillna(0).apply(lambda x: get_left_days_by_utimestamp(x, now))
    cdf = cdf.fillna("----")
    data = list(cdf.to_dict(orient="index").values())
    return make_result(data, 1, "测试")

"""api, 获取客户列表，用于政务中心页面客户tab页"""
@permission_required("sale.government_center.customer_tab.view", login_url=JSON_403)
def customer_list_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务列表api", action="查询", message=message)

    result = {"data": None, "code": 0, "error": ""}
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
    result = get_customer_list_by_dtalkids(dtalkids)
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

def test(request):
    print(request.META["REMOTE_ADDR"])
    return render(request, "sale/test.html")