from urllib.parse import quote
import datetime
import logging
from django.http import JsonResponse
from django.shortcuts import render
from mandala.auth.decorators import login_required,permission_required
import json

from django.urls import reverse

from competitor.forms import CompetitorSelectForm, get_product
from secretary.utils import get_departments_about_sale, get_group_members
from support import settings
from user_center.utils import make_jump_url, get_user_group_map
import redis
from competitor.models import *
from customer.models import Opportunity
from customer.utils import get_industry_data, get_industry_data_1
from django.views.decorators.csrf import csrf_exempt
from public.utils import *
from customer.utils import get_states
import pandas
import numpy
from user_center.models import UserLog
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

logger = logging.getLogger("competitor")



"""竞品签约客户页面配置"""
@login_required()
@permission_required("competitor.competitor_crm.view",login_url=URL_403)
@csrf_exempt
def competitorCrm(request):
    if request.method == "GET":
        title = "竞品签约客户"
        form = CompetitorSelectForm()
        competitor_name = request.GET.get("competitor_name")
        customer_province = request.GET.get("customer_province")
        industry1 = request.GET.get("industry_1")
        industry2 = request.GET.get("industry_2")
        if competitor_name:
            form.input_competitorName(competitor_name)
            # form = CompetitorSelectForm(initial={"competitor_name":competitor_name})
        if industry1:
            form.select_industry1(industry1)
        if industry2:
            form.select_industry2(industry2)
        if customer_province:
            form.select_province(customer_province)
        if not competitor_name and not industry1 and not industry2 and not customer_province:
            # 如果是超管 "郭燕双","骆飞","李青龙"，默认选择河北省
            if request.user.is_superuser or request.user.dtalkid in ["340511313646","luofei","01040827261237"]:
                form.select_province("4")
        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        init_data["col_names"] = ["客户名称", "商机名称","竞品名称", "签单产品","签单金额", "开始日期",
                                   "结束日期", "商务","部门","地域","一级行业","二级行业",  "操作"]
        init_data["col_model"] = [
            {
                "name": 'customer_name',
                "width": 20,
            },
            {
                "name": 'opportunity_name',
                "width": 13,
            },
            {
                "name": 'competitor_name',
                "width": 15,
            },
            {
                "name": 'competitor_product_name',
                "width": 10,
            },
            {
                "name": 'competitor_money',
                "width": 12,
                "sorttype": "int"
            },
            {
                "name": 'service_time_start',
                "width": 10,
            },
            {
                "name": 'service_time_finish',
                "width": 10,
            },
            {
                "name": 'saler',
                "width": 10,
            },
            {
                "name": 'department_name',
                "width": 10,
            },
            {
                "name": 'customer_province',
                "width": 10,
            },
            {
                "name": 'industry1_name',
                "width": 12,
            },
            {
                "name": 'industry2_name',
                "width": 12,
            },
            {
                "name": 'operations',
                "width": 20,
                "sortable": False,
            },
        ]
        init_data["items"] = []
        ########## 跳转CRM客户名称首页 #############
        crm_customer_jump_url = settings.CRM_CUSTOMER_JUMP_URL
        ########## 跳转查看客户画像 ################
        crmuser_next_url = settings.CRMUSER_NEXT_URL
        crmuser_jump_url = make_jump_url(request.user.mobile, crmuser_next_url)

        init_data = json.dumps(init_data)
        departments_api = reverse("secretary:departments_api")
        department_data = get_departments_about_sale()
        department_data = json.dumps(department_data)
        department_data_1 = [["", "全部"]] + list(settings.SALE_DEPARTMENT_LEVEL_1.items())
        department_data_1 = json.dumps(department_data_1)

        industry_data = get_industry_data()
        industry_data = json.dumps(industry_data)
        # industry_data_1 = [["", "全部"]] + get_industry_data_1()
        # industry_data_1 = json.dumps(industry_data_1)
        # 记日志
        user = request.user
        if user.username not in ["武翠霞", "丛大侠", "王寅", "张太锋", "黄远", "朱铭鑫", "袁战梅"]:
            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=user.username, user_id=user.id,
                                   model="竞品签约客户", action="进入页面", message=message)
        return render(request, "competitor/crm_competitor.html", locals())



"""竞品签约客户查询数据接口，返回json格式的数据"""
@permission_required("competitor.competitor_crm.view",login_url=JSON_403)
def competitorCrmListApi(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    result = {"status": 0, "message": "","items":[]}
    form = CompetitorSelectForm(kws)
    if form.is_valid():
        cdata = form.cleaned_data
        customer_name = cdata.get("customer_name")
        customer_province_id = cdata.get("customer_province")
        competitor_name = cdata.get("competitor_name")
        # no_service_time = cdata.get("no_service_time")
        # service_time_start = cdata.get("service_time_start")
        # service_time_finish = cdata.get("service_time_finish")
        saler = cdata.get("saler")
        department_id = cdata.get("department")
        industry1 = cdata.get("industry1")
        industry2 = cdata.get("industry2")

        flag1 = 0  # 代表无筛选条件
        flag2 = 0  # 代表无筛选条件
        # 根据竞品查找
        if competitor_name:
            flag1 = 1
            competitor_id = get_value_list(Competitor,{"competitorname__contains":competitor_name},["competitorid"])
            l = len(competitor_id)
            if l > 0:
                if l == 1:
                    select_crm1 = get_value_list(CrmCompetitorMap,{"competitorid":competitor_id[0][0]},["accountid"])
                else:
                    competitor_id = [comid[0] for comid in competitor_id]
                    select_crm1 = get_value_list(CrmCompetitorMap,{"competitorid__in":competitor_id},["accountid"])
                if len(select_crm1):
                    select_crm1 = [crmid[0] for crmid in select_crm1]
                else:
                    result["message"] = "该竞品没有关联的客户信息"
                    return JsonResponse(result)
            else:
                result["message"] = "没有该竞品信息"
                return JsonResponse(result)
        else:
            select_crm1 = []

        select_condition = {}
        # 根据商务和部门查找
        ownerlist=[]
        if saler:
            ownerlist = get_value_list(User,{"name__contains":saler},["id"])
            if len(ownerlist) > 0:
                ownerlist = [owner[0] for owner in ownerlist]
            else:
                result["message"] = "未查到该商务信息"
                return JsonResponse(result)

        # 按部门条件筛选
        if department_id:
            group_members = get_group_members(department_id)
            if not group_members:
                result["message"] = "部门成员为空，请检查部门是否存在"
                return JsonResponse(result)
            else:
                group_members_owner = get_value_list(User,{"name__in":group_members},["id"])
                group_members_owner = [owner[0] for owner in group_members_owner]
                if group_members_owner:
                    if ownerlist:
                        ownerlist = list(set(ownerlist) & set(group_members_owner))
                        if not ownerlist:
                            result["message"] = "搜索的商务不在该部门下，请修改部门查询"
                            return JsonResponse(result)
                    else:
                        ownerlist += group_members_owner
                else:
                    result["message"] = "部门成员下无客户信息，请修改部门查询"
                    return JsonResponse(result)

        if ownerlist:
            select_condition["ownerid__in"] = ownerlist
        # 按照客户名称搜索
        if customer_name:
            select_condition["accountname__contains"] = customer_name
        # 按照客户省份搜索
        if customer_province_id:
            if customer_province_id != '0':
                select_condition["fstate"] = customer_province_id
            else:
                select_condition["fstate__isnull"] = True

        # 一级行业
        if industry1:
            if industry1 != '0':
                select_condition["dbcselect5"] = industry1
            else:
                select_condition["dbcselect5__isnull"] = True

        # 二级行业
        if industry2:
            if industry2 != '0':
                select_condition["dbcselect9"] = industry2
            else:
                select_condition["dbcselect9__isnull"] = True


        if select_condition != {}:
            select_crm2 = get_value_list(Account,select_condition,["id"])
            select_crm2 = [crmid[0] for crmid in select_crm2]
            # 筛选结果取交集,flag = 1代表有筛选条件
            flag2 = 1
        else:
            select_crm2 = []

        if flag1:
            if flag2:
                select_crm = set(select_crm1) & set(select_crm2)
            else:
                select_crm = set(select_crm1)
        elif flag2:
            select_crm = set(select_crm2)
        else:
            select_crm = set()
        # 管理员可以查看所有商务的数据
        # conn33 = pymysql.connect(host='192.168.185.33', user='root', password='1CzoOCywfJ*h', db='contract',
        #                          charset='utf8')
        if request.user.is_superuser:
            # 如果有筛选条件，取过交集后，select_crm不为空
            if (flag1 or flag2 ):
                crm_list = list(select_crm)
            else:
                # 如果没筛选条件,查询库中所有的客户id
                crminfo_list = Account.objects.values_list("id", "accountname")
                crminfo_list = pandas.DataFrame(data=crminfo_list,
                                                columns=["customer_id", "customer_name"])
                crm_list = list(crminfo_list['customer_id'])

            if not crm_list:
                # 取过交集，但是筛选结果为空，说明没有满足筛选条件中的客户信息，直接返回
                result["message"] = "没有符合条件的信息"
                return JsonResponse(result)
        else:
            # 从redis取出可看到的客户id，作为基数
            r = redis.Redis(host='192.168.187.55', db=5)
            crm_list = r.hget(name='DingId',key=request.user.dtalkid)
            crm_list = json.loads(crm_list)
            # 如果有筛选条件，取过交集后，select_crm不为空
            if (flag1 or flag2 ):
                crm_list = list(set(select_crm) & set(crm_list))

            if not crm_list:
                # 取过交集，但是筛选结果为空，说明没有满足筛选条件中的客户信息，直接返回
                result["message"] = "没有符合条件的信息"
                return JsonResponse(result)

        l = len(crm_list)
        if l == 0:
            result["message"] = "无可看的客户信息"
            return JsonResponse(result)
        elif len(crm_list) == 1:
            crm_condition = {"id":crm_list[0]}
            opp_condition = {"dbcrelation1":crm_list[0]}
            # competitor_condition = {"accountid":crm_list[0]}
        else:
            crm_condition = {"id__in": crm_list}
            opp_condition = {"dbcrelation1__in": crm_list}
            # competitor_condition = {"accountid__in": crm_list}

        crminfo_list = get_value_list(Account, crm_condition, ["id", "accountname","ownerid","fstate",
                                                               "dbcselect5","dbcselect9"])
        crminfo_list = pandas.DataFrame(data=crminfo_list,
                                        columns=["customer_id", "customer_name", "ownerId", "fState",
                                                 "industry1_id","industry2_id"])
        crm_info = crminfo_list.copy()
        crm_info[["fState","industry1_id","industry2_id"]] = crm_info[["fState","industry1_id","industry2_id"]].fillna(0)
        # 修改字段类型，设置商务的筛选条件
        crm_info["ownerId"] = crm_info.loc[:,"ownerId"].values.astype(numpy.int64)

        # 获取商机信息
        opp_list = get_value_list(Opportunity, opp_condition, ["dbcrelation1", "opportunityname"])
        opp_info = pandas.DataFrame(data=opp_list, columns=["customer_id", "opportunity_name"])
        opp_info["customer_id"] = opp_info["customer_id"].values.astype(numpy.int64)

        crm_info = pandas.merge(crm_info, opp_info, how="left", on="customer_id")  # 拼接数据
        crm_info = crm_info.loc[crm_info["customer_id"].drop_duplicates().index, :]  # 如果有多个商机只取一个

        # 获取商务名
        owner_list = list(set(crm_info["ownerId"]))
        if len(owner_list) == 1:
            owner_condition = {"id": owner_list[0]}
        elif len(owner_list) > 1:
            owner_condition = {"id__in": owner_list}
        else:
            owner_condition = ''
        if owner_condition:
            saler_list = get_value_list(User,owner_condition,["id","name"])
            saler_df = pandas.DataFrame(data=saler_list,columns=["ownerId","saler"])
            crm_info = pandas.merge(crm_info, saler_df, how="left", on="ownerId")
        else:
            # 增加一列为空值的商务列
            crm_info = pandas.concat([crm_info, pandas.DataFrame(columns=["ownerId", "saler"])])

        # 获取商务 - 部门对应关系
        try:
            user_group_map = get_user_group_map()
        except Exception as e:
            logger.error(e)
            result["message"] = "服务器繁忙，请稍后重试"
            return result
        crm_info["department_name"] = crm_info["saler"].apply(lambda x: user_group_map.get(x, ""))

        # 获取省份名称
        province_list = get_states()
        province_info = pandas.DataFrame(data=province_list,columns=["fState","customer_province"])
        province_info["fState"] = province_info["fState"].astype(numpy.int64)
        crm_info = pandas.merge(crm_info, province_info, how="left", on="fState")


        # 拼接行业数据
        industry1_data = get_industry_data_1()
        industry1_df = pandas.DataFrame(industry1_data,columns=["industry1_id","industry1_name"])
        # industry1_df = industry1_df.rename({"id":"industry1_id","name":"industry1_name"})

        industry2_data = get_industry_data() +[{'id': 0, 'name': '未知', 'pid': 0}]
        industry2_df = pandas.DataFrame(data=industry2_data)
        industry2_df = industry2_df.rename(columns={"id": "industry2_id", "name": "industry2_name"})
        industry2_df = industry2_df.drop(['pid'],axis=1)
        crm_info = pandas.merge(crm_info, industry1_df,how='left',on='industry1_id')
        crm_info = pandas.merge(crm_info, industry2_df,how='left',on='industry2_id')

        # 获取竞品相关信息
        competitor_condition = {}
        if competitor_name:
            if len(competitor_id)>1:
                competitor_condition["competitorid__in"] = competitor_id
            else:
                competitor_condition["competitorid"] = competitor_id[0][0]

        v1 = ["record_id","customer_id","competitorId","competitorProductId","competitor_money","service_time_start","service_time_finish","status"]
        crm_competitor_list = get_value_list(CrmCompetitorMap,competitor_condition,[])
        competitor_df = pandas.DataFrame(data=crm_competitor_list,columns=v1)
        competitor_df["competitor_money"] = competitor_df["competitor_money"].apply(lambda x:format(x,','))

        # 获取竞品名称
        competitor_list = get_value_list(Competitor, {}, ["competitorid", "competitorname"])
        competitor_info = pandas.DataFrame(data=competitor_list,columns=["competitorId", "competitor_name"])
        competitor_df = pandas.merge(competitor_df, competitor_info, how="left", on="competitorId")

        # 获取产品名称
        product_list = get_product()
        product_info = pandas.DataFrame(data=product_list,columns=["competitorProductId", "competitor_product_name"])
        # # 追加一行
        # product_info = product_info.append({"competitorProductId":0,"competitor_product_name":"其他"},ignore_index=True)
        # competitor_df1 = competitor_df.loc[competitor_df.competitorProductId.notnull()]
        # competitor_df2 = competitor_df.loc[competitor_df.competitorProductId.isnull()]
        # competitor_df1 = pandas.merge(competitor_df1, product_info, how="left", on="competitorProductId")
        # competitor_df2 = pandas.concat([competitor_df2, pandas.DataFrame(columns=["competitor_product_name"])],sort=False)
        # # 按行拼接数据
        # competitor_df = pandas.concat([competitor_df1,competitor_df2],axis=0,sort=False)

        competitor_df = pandas.merge(competitor_df, product_info, how="left", on="competitorProductId")
        # 客户信息拼接竞品信息
        crm_info = pandas.merge(crm_info, competitor_df, how="left", on="customer_id")

        crm_info = crm_info.drop(["ownerId","fState"], axis=1)
        crm_info["competitor_money"] = crm_info["competitor_money"].fillna(0)
        crm_info = crm_info.fillna('--')
        # print(crm_info.columns)
        items = list(crm_info.to_dict(orient="index").values())
        result["status"] = 1
        result["items"] = items

    return JsonResponse(result)



"""关联竞品接口"""
@permission_required("competitor.competitor_crm.connect",login_url=JSON_403)
@csrf_exempt
def connect_competitor_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    result = {"status": 0, "message": ""}
    form = dict(k.split('=') for k in kws.get("form_data").split('&'))
    if form:
        conditions = {}
        customer_id = form.get("customer_id")
        if customer_id:
            customer_id = int(customer_id)
            conditions["accountid"] = customer_id

        competitor_id = form.get("competitorId")
        if competitor_id:
            competitor_id = int(competitor_id)
            conditions["competitorid"] = competitor_id

        competitor_product_id = form.get("competitorProductId")
        if competitor_product_id:
            competitor_product_id = int(competitor_product_id)
            conditions["competitorproductid"] = competitor_product_id

        competitor_money = form.get("competitor_money")
        if competitor_money:
            conditions["competitormoney"] = competitor_money

        service_time_start = form.get("service_time_start")
        if '---' not in service_time_start:
            conditions["competitorstartdate"] = service_time_start

        service_time_finish = form.get("service_time_finish")
        if '---' not in service_time_finish:
            conditions["competitorfindate"] = service_time_finish
        # print(form)
        record = get_value_list(CrmCompetitorMap,conditions,["id","accountid"])
        # print(record)
        if len(record) >= 1:
            result["status"] = 2
            result["message"] = '竞品已关联过'
            return JsonResponse(result)
        try:
            CrmCompetitorMap.objects.create(**conditions)
            result["status"] = 200
            result["message"] = '关联竞品成功'
            user = request.user
            message = json.dumps(dict(kws))
            UserLog.objects.create(username=user.username, user_id=user.id,
                                   model="竞品签约客户", action="关联竞品", message=message)
        except Exception as e:
            logger.error(str(e))
            result["message"] = '关联竞品失败'

        return JsonResponse(result)

"""加载页面下拉框的选项值"""
@permission_required("competitor.competitor_crm.connect",login_url=JSON_403)
def updateSelectForm(request):
    if request.method == "GET":
        form = CompetitorSelectForm()
        result = {"status": 200, "message": form.fields['competitorId'].widget.choices}
        return JsonResponse(result)