from django.http import JsonResponse
from  secretary.models import Crmaccountmapping
from recorder.models import WkTUseractivity
import pandas as pd
from public.utils import get_value_list
from datetime import datetime,timedelta
from mandala.auth.decorators import login_required


# @login_required
def crm_activity_info(request):
    '''根据客户id，查询近n天活跃情况，以秘书账号为主
    :param
        id 客户id，可传单个值,可传多个值（字符串类型，多个值逗号分隔）
        date 需要查询账号的近n天活跃，字符串类型，不传值默认为30
    :return
            "msuid": date时间内最活跃的秘书账号,
            "msname":date时间内最活跃的秘书账号,
            "crmuid": ,
            "opportunityid": ,
            "act_days":最活跃的账号在date内的活跃天数,
            "last_act_date":最近一次活跃日期,
            "ms_count":客户的秘书账号数,
            "act_ms_count":在date时间内客户活跃账号数
    '''
    # 获取请求参数
    result = {"status": 0, "message": "", "items": []}
    # pd.set_option('display.max_rows', None)
    customer = request.GET.get("id")
    try:
        # 查询多长时间的活跃
        act_date = int(request.GET.get("date"))
    except:
        act_date = 30

    # 1 根据客户id查所有的秘书账号
    if customer:
        customer = customer.split(',')
        customer = [int(x) for x in customer]
        if len(customer) == 1:
            condition1 = {"crmuid":customer[0]}
        else:
            condition1 = {"crmuid__in":customer if len(customer)>1 else "crmUid"}
    else:
        result["message"] = "请传入参数，客户信息"
        return JsonResponse(result)
    values1 = ["msuid","msname","crmuid","opportunityid"]

    msuid = get_value_list(Crmaccountmapping,condition1,values1)
    msuid_df = pd.DataFrame(data=msuid,columns=values1)
    if len(msuid_df) == 0:
        result["status"] = -1
        result["message"] = "该客户没有关联的秘书账号"
        return JsonResponse(result)


    # 2 根据需要查的近几天活跃和上一步的秘书账号，查秘书账号的活跃情况
    act_date_ago = (datetime.now() - timedelta(days=act_date)).strftime("%Y%m%d")
    if len(msuid_df)==1:
        condition2 = {"uid":list(msuid_df["msuid"])[0],"date__gte":act_date_ago}
    else:
        condition2 = {"uid__in":list(msuid_df["msuid"]),"date__gte":act_date_ago}

    act = get_value_list(WkTUseractivity, condition2,
                         ["uid", "uname", "date", "activity_self", "self", "phone", "wechat"])
    act_df = pd.DataFrame(data=act, columns=["msuid", "msname", "date", "activity_self", "self", "phone", "wechat"])

    act_df["date"] = act_df["date"].apply(lambda x: datetime.strptime(x,"%Y%m%d").strftime("%Y-%m-%d"))
    # 以秘书账号分类
    msuid_df['act_days'] = 0
    msuid_df['last_act_date'] = ''
    act_grouped = act_df.groupby(["msuid"])
    for name, group in act_grouped:
        act_days = len(group.loc[group.activity_self>0])
        if act_days>0:
            group = group.sort_values(by="date", ascending=False).reset_index(drop=True)
            last_act_date = list(group["date"])[0]
        else:
            last_act_date = ''
        msuid_df.loc[msuid_df.msuid==name,"act_days"] = act_days
        msuid_df.loc[msuid_df.msuid==name,"last_act_date"] = last_act_date

    # print(msuid_df)
    msuid_df['act_days'] = msuid_df["act_days"].fillna(0)
    msuid_df['last_act_date'] = msuid_df["last_act_date"].fillna('')
    msuid_df['act_days'] = msuid_df["act_days"].astype(int)

    items = []
    # 以客户id分类
    crm_grouped = msuid_df.groupby(["crmuid"])
    for crmid,crm_group in crm_grouped:
        crm_group["ms_count"] = len(msuid_df.loc[msuid_df.crmuid==crmid])
        crm_group.loc[:,"act_ms_count"] = int(len(crm_group.loc[crm_group.act_days>0]))
        crm_group = crm_group.sort_values(by="act_days", ascending=False).reset_index(drop=True)

        # 将结果放入items
        item = list(crm_group.to_dict(orient="index").values())[0]
        item["act_detail"] = list(
            act_df.loc[act_df.msuid == item['msuid']].sort_values(by="date", ascending=False).reset_index(
                drop=True).to_dict(orient="index").values())
        items.append(item)
    for id in (set(customer)-set(msuid_df["crmuid"])):
        items.append({"crmuid":id})
    # print(items)
    result["status"] = 1
    result["message"] = "ok"
    result["items"] = items
    return JsonResponse(result)


# @login_required
def opp_activity_info(request):
    '''根据商机id，查询近n天活跃情况，以秘书账号为主
    :param
        id 商机id，可传单个值,可传多个值（字符串类型，多个值逗号分隔）
        date 需要查询账号的近n天活跃，字符串类型，不传值默认为30
    :return
            "msuid": date时间内最活跃的秘书账号,
            "msname":date时间内最活跃的秘书账号,
            "crmuid":808874708074793,
            "opportunityid":855520865009920,
            "act_days":最活跃的账号在date内的活跃天数,
            "last_act_date":最近一次活跃日期,
            "ms_count":商机的秘书账号数,
            "act_ms_count":在date时间内商机活跃账号数
    '''
    # 获取请求参数
    result = {"status": 0, "message": "", "items": []}
    # pd.set_option('display.max_rows', None)
    opportunity = request.GET.get("id")
    try:
        act_date = int(request.GET.get("date"))
    except:
        act_date = 30

    # 1 根据商机id查所有的秘书账号
    if opportunity:
        opportunity = opportunity.split(',')
        opportunity = [int(x) for x in opportunity]
        if len(opportunity) == 1:
            condition1 = {"opportunityid":opportunity[0]}
        else:
            condition1 = {"opportunityid__in":opportunity if len(opportunity)>1 else "opportunityid"}
    else:
        result["message"] = "请传入参数，商机信息"
        return JsonResponse(result)
    values1 = ["msuid","msname","crmuid","opportunityid"]

    msuid = get_value_list(Crmaccountmapping,condition1,values1)
    msuid_df = pd.DataFrame(data=msuid,columns=values1)
    if len(msuid_df) == 0:
        result["status"] = -1
        result["message"] = "该商机没有关联的秘书账号"
        return JsonResponse(result)


    # 2 根据需要查的近几天活跃和上一步的秘书账号，查秘书账号的活跃情况
    act_date_ago = (datetime.now() - timedelta(days=act_date)).strftime("%Y%m%d")
    if len(msuid_df)==1:
        condition2 = {"uid":list(msuid_df["msuid"])[0],"date__gte":act_date_ago}
    else:
        condition2 = {"uid__in":list(msuid_df["msuid"]),"date__gte":act_date_ago}

    act = get_value_list(WkTUseractivity,condition2,["uid","uname","date","activity_self","self","phone","wechat"])
    act_df = pd.DataFrame(data=act,columns=["msuid","msname","date","activity_self","self","phone","wechat"])
    act_df["date"] = act_df["date"].apply(lambda x: datetime.strptime(x,"%Y%m%d").strftime("%Y-%m-%d"))
    # 以秘书账号分类
    msuid_df['act_days'] = 0
    msuid_df['last_act_date'] = ''
    act_grouped = act_df.groupby(["msuid"])

    for name, group in act_grouped:
        act_days = len(group.loc[group.activity_self>0])
        if act_days>0:
            group = group.sort_values(by="date", ascending=False).reset_index(drop=True)
            last_act_date = list(group["date"])[0]
        else:
            last_act_date = ''
        msuid_df.loc[msuid_df.msuid==name,"act_days"] = act_days
        msuid_df.loc[msuid_df.msuid==name,"last_act_date"] = last_act_date

    msuid_df['act_days'] = msuid_df["act_days"].fillna(0)
    msuid_df['last_act_date'] = msuid_df["last_act_date"].fillna('')
    msuid_df['act_days'] = msuid_df["act_days"].astype(int)

    items = []
    # 以商机id分类
    crm_grouped = msuid_df.groupby(["opportunityid"])
    for crmid, crm_group in crm_grouped:
        crm_group["ms_count"] = len(msuid_df.loc[msuid_df.opportunityid==crmid])
        crm_group.loc[:,"act_ms_count"] = len(crm_group.loc[crm_group.act_days>0])
        crm_group = crm_group.sort_values(by="act_days", ascending=False).reset_index(drop=True)

        # 将结果放入items
        item = list(crm_group.to_dict(orient="index").values())[0]
        item["act_detail"] = list(
            act_df.loc[act_df.msuid == item['msuid']].sort_values(by="date", ascending=False).reset_index(
                drop=True).to_dict(orient="index").values())
        items.append(item)
    for id in (set(opportunity)-set(msuid_df["opportunityid"])):
        # item = {
        #     "msuid":
        # }
        items.append({"opportunityid":id})
    # print(items)
    result["status"] = 1
    result["message"] = "ok"
    result["items"] = items
    return JsonResponse(result)


def crm_activity_info1(request):
    '''根据客户id，以end_date往前推date天，查询账号活跃情况，以秘书账号为主
    :param
        id 客户id，可传单个值,可传多个值（字符串类型，多个值逗号分隔）
        days 需要查询账号的n天活跃，字符串类型，不传值默认为30
        end_date 查询活跃的结束日期，不传默认为当天
    :return
            "msuid": date时间内最活跃的秘书账号,
            "msname":date时间内最活跃的秘书账号,
            "crmuid": ,
            "opportunityid": ,
            "act_days":最活跃的账号在date内的活跃天数,
            "last_act_date":最近一次活跃日期,
            "ms_count":客户的秘书账号数,
            "act_ms_count":在date时间内客户活跃账号数
    '''
    # 获取请求参数
    result = {"status": 0, "message": "", "items": []}
    # pd.set_option('display.max_rows', None)
    customer = request.GET.get("id")
    try:
        # 查询多长时间的活跃
        act_date = int(request.GET.get("days"))
    except:
        act_date = 30

    try:
        # 查询多长时间的活跃
        end_act_date = request.GET.get("end_date")
    except:
        end_act_date = datetime.now().strftime("%Y%m%d")

    # 1 根据客户id查所有的秘书账号
    if customer:
        customer = customer.split(',')
        customer = [int(x) for x in customer]
        if len(customer) == 1:
            condition1 = {"crmuid":customer[0]}
        else:
            condition1 = {"crmuid__in":customer if len(customer)>1 else "crmUid"}
    else:
        result["message"] = "请传入参数，客户信息"
        return JsonResponse(result)
    values1 = ["msuid","msname","crmuid","opportunityid"]

    msuid = get_value_list(Crmaccountmapping,condition1,values1)
    msuid_df = pd.DataFrame(data=msuid,columns=values1)
    if len(msuid_df) == 0:
        result["status"] = -1
        result["message"] = "该客户没有关联的秘书账号"
        return JsonResponse(result)


    # 2 根据需要查的近几天活跃和上一步的秘书账号，查秘书账号的活跃情况
    act_date_ago = (datetime.strptime(end_act_date,"%Y%m%d") - timedelta(days=act_date)).strftime("%Y%m%d")
    if len(msuid_df)==1:
        condition2 = {"uid":list(msuid_df["msuid"])[0],"date__gte":act_date_ago,"date__lte":end_act_date}
    else:
        condition2 = {"uid__in":list(msuid_df["msuid"]),"date__gte":act_date_ago,"date__lte":end_act_date}

    act = get_value_list(WkTUseractivity, condition2,
                         ["uid", "uname", "date", "activity_self", "self", "phone", "wechat"])
    act_df = pd.DataFrame(data=act, columns=["msuid", "msname", "date", "activity_self", "self", "phone", "wechat"])

    act_df["date"] = act_df["date"].apply(lambda x: datetime.strptime(x,"%Y%m%d").strftime("%Y-%m-%d"))
    # 以秘书账号分类
    msuid_df['act_days'] = 0
    msuid_df['last_act_date'] = ''
    act_grouped = act_df.groupby(["msuid"])
    for name, group in act_grouped:
        act_days = len(group.loc[group.activity_self>0])
        if act_days>0:
            group = group.sort_values(by="date", ascending=False).reset_index(drop=True)
            last_act_date = list(group["date"])[0]
        else:
            last_act_date = ''
        msuid_df.loc[msuid_df.msuid==name,"act_days"] = act_days
        msuid_df.loc[msuid_df.msuid==name,"last_act_date"] = last_act_date

    # print(msuid_df)
    msuid_df['act_days'] = msuid_df["act_days"].fillna(0)
    msuid_df['last_act_date'] = msuid_df["last_act_date"].fillna('')
    msuid_df['act_days'] = msuid_df["act_days"].astype(int)

    items = []
    # 以客户id分类
    crm_grouped = msuid_df.groupby(["crmuid"])
    for crmid,crm_group in crm_grouped:
        crm_group["ms_count"] = len(msuid_df.loc[msuid_df.crmuid==crmid])
        crm_group.loc[:,"act_ms_count"] = int(len(crm_group.loc[crm_group.act_days>0]))
        crm_group = crm_group.sort_values(by="act_days", ascending=False).reset_index(drop=True)

        # 将结果放入items
        item = list(crm_group.to_dict(orient="index").values())[0]
        item["act_detail"] = list(
            act_df.loc[act_df.msuid == item['msuid']].sort_values(by="date", ascending=False).reset_index(
                drop=True).to_dict(orient="index").values())
        items.append(item)
    for id in (set(customer)-set(msuid_df["crmuid"])):
        items.append({"crmuid":id})
    # print(items)
    result["status"] = 1
    result["message"] = "ok"
    result["items"] = items
    return JsonResponse(result)