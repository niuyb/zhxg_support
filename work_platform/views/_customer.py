import json
import time
import arrow
import logging

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from mandala.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from customer.models import Account
from work_platform.models import CrmWechatMapping, WechatGroupMessage
from secretary.utils import get_can_see_new
from sale.utils import get_can_see_owner_ids_new
from customer.models import User as CrmUser
from user_center.models import UserLog
from mandala.auth.models import Module

from public.utils import Result

import pandas as pd

logger = logging.getLogger('default')

# strict : 当value_list中有None的时候，当成两种情况处理: None 和 ""
def parse_common_field(name, value_list, strict=False):
    qs = None
    if value_list is not None:
        if not isinstance(value_list, list):
            value_list = [str(value_list)]
        
        if value_list:
            for value in value_list:
                q = None
                if value is None:
                    q = Q(**{name + "__isnull" : True})
                    if strict:
                        q |= Q(**{name: ""})
                else:
                    q = Q(**{name: value})
                
                if qs is None:
                    qs = q
                else:
                    qs |= q
    return qs


@login_required(login_url="/work_platform/login")
def customer_list(request):
    title = "全部客户"
    data_api = "/work_platform/customer/list/api"

    user = request.user
    if not user.roles.filter(code="developer").count():
        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=user.username, user_id=user.id,
                            model="商务工作台-客户列表", action="访问", message=message)

    return render(request, "work_platform/customer-list.html", locals())

def customer_list_api(request):
    result = Result()
    power = request.GET.get("power", "0")
    try:
        orderBy = json.loads(request.GET.get("sortBy"))
    except Exception as e:
        logger.warn(e)
        orderBy = {}

    try:
        filterBy = json.loads(request.GET.get("filterBy"))
    except Exception as e:
        logger.warn(e)
        filterBy = {}

    filter_by_qs = None
    filter_by = {}
    customer_name = filterBy.get("accountname")
    if customer_name:
        filter_by["accountname__icontains"] = customer_name

    page = request.GET.get("page")

    # power  0，默认查看 1，查看自己 2，查看团队
    owner_ids = get_can_see_owner_ids_new(request.user, see_type=power)
    if not owner_ids:
        result.code = 0
        result.error = "没有找到符合条件的客户"
        return JsonResponse(result.dict())

    try:
        page = int(page)
    except:
        page = 1

    if page < 1:
        page = 1

    page_size = request.GET.get("page_size")
    try:
        page_size = int(page_size)
    except:
        page_size = 20

    if page_size < 1 or page_size > 100:
        page_size = 20

    params = {"highseastatus__in": [1,3,4]}
    params["ownerid__in"] = owner_ids

    filter_by.update(params)
    
    # customers = Account.objects.filter(**params)
    is_read = filterBy.get("is_read")
    if is_read:
        if not isinstance(is_read, list):
            is_read = [str(is_read)]

    # wechat_group 参数：0、未绑定 1、申请中 2、审核中 3、已绑定 4、绑定失败
    wechat_group = filterBy.get("wechat_group")
    if wechat_group is not None:
        if not isinstance(wechat_group, list):
            wechat_group = [str(wechat_group)]
        
    if wechat_group:
        that_time = arrow.now().shift(hours=-25).format("YYYY-MM-DD HH:mm:ss")
        logger.info("that_time: %s"%that_time)
        for i in wechat_group:
            temp = None
            # 未绑定
            if i in ["0", 0]:
                cids = list(CrmWechatMapping.objects.exclude(status=0).values_list("customer_id", flat=True))
                temp = ~Q(id__in=cids)
            # 申请中
            elif i in ["1", 1]:
                cids = list(CrmWechatMapping.objects.filter(status=3).values_list("customer_id", flat=True))
            # 审核中
            elif i in ["2", 2]:
                cids = list(CrmWechatMapping.objects.filter(status=1, ctime__gte=that_time).values_list("customer_id", flat=True))
            # 已绑定
            elif i in ["3", 3]:
                cids = list(CrmWechatMapping.objects.filter(status=1, ctime__lt=that_time).values_list("customer_id", flat=True))
            # 绑定失败
            elif i in ["4", 4]:
                cids = list(CrmWechatMapping.objects.filter(status=2).values_list("customer_id", flat=True))
            else:
                cids = []

            if temp is None:
                temp = Q(id__in=cids)

            if filter_by_qs is None:
                filter_by_qs = temp
            else:
                filter_by_qs |= temp
    
    level = filterBy.get("level") 
    level_qs = parse_common_field("level", level)
    if level_qs is not None:
        if filter_by_qs is not None:
            filter_by_qs &= level_qs
        else:
            filter_by_qs = level_qs
            
    customers = Account.objects.filter(**filter_by)
    if filter_by_qs is not None:
        customers = customers.filter(filter_by_qs)
        
    customers = list(customers.values(
            "id", "accountname", "createdat", "ownerid", "level", "recentactivityrecordtime"))

    if not customers:
        result.code = 1
        result.error = "没有检索到符合要求的客户"
        return JsonResponse(result.dict())

    df = pd.DataFrame(customers)
    salers = list(CrmUser.objects.all().values("id", "name"))
    _df = pd.DataFrame(salers)
    _df = _df.rename(columns={"id": "ownerid", "name": "owner_name"})
    df = pd.merge(df, _df, how="left")

    crm_wechats = list(CrmWechatMapping.objects.filter(status__in=[1, 2, 3]).values("customer_id", "wechat_group_id", "status", "ctime"))
    if not crm_wechats:
        data = list(df.to_dict(orient="index").values())
        result.code = 1
        result.data = data
        return JsonResponse(result.dict())

    _df = pd.DataFrame(crm_wechats)
    df = pd.merge(df, _df, how="left", left_on="id", right_on="customer_id")

    where = ""
    if is_read:
        where = "AND a.is_read IN %s "%(str(tuple(is_read)).replace(",)", ")"))

    sql = """
        SELECT * 
        FROM `wechat_group_message` AS a 
        INNER JOIN(
            SELECT customer_id, MAX(ctime) AS ctime 
            FROM `wechat_group_message` 
            GROUP BY customer_id) AS b 
        ON a.customer_id=b.customer_id AND a.ctime=b.ctime AND a.customer_id <> 0 AND b.customer_id <> 0 {};
        """.format(where)
        
    wgms = WechatGroupMessage.objects.raw(sql)
    wgm_list = []
    for wgm in wgms:
        w = {}
        w["customer_id"] = wgm.customer_id
        w["message_ctime"] = wgm.ctime
        w["is_read"] = wgm.is_read
        wgm_list.append(w)
        
    _df = pd.DataFrame(wgm_list)
    if wgm_list: 
        if is_read:
            df = pd.merge(_df, df, how="inner", on="customer_id")
        else:
            df = pd.merge(df, _df, how="left", on="customer_id")

    else:
        if is_read:
            df = _df

    df["createdat"] = df["createdat"].fillna("")
    df["recentactivityrecordtime"] = df["recentactivityrecordtime"].fillna("")
    
    df = df.fillna(0)
    data = list(df.to_dict(orient="index").values())

    key = None
    value = None

    for key, value in orderBy.items():
        if value:
            break
        
    if key:
        def func(item):
            return item.get(key)

        if value in ["-", "desc"]:
            data.sort(key=func, reverse=True)

        elif value in ["+", "asc"]:
            data.sort(key=func)
            
    data = data[20 * (page - 1) : 20 * page]
    result.code = 1
    result.data = data
    return JsonResponse(result.dict())

@login_required(login_url="/work_platform/login")
def search_customer(request):
    title = "所有客户"
    data_api = "/work_platform/customer/list/api"

    user = request.user
    if not user.roles.filter(code="developer").count():
        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=user.username, user_id=user.id,
                            model="商务工作台-客户搜索", action="访问", message=message)

    return render(request, "work_platform/customer-search.html", locals())

    