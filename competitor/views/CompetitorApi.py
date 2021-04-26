

"""添加竞品接口"""
import json
import logging

from mandala.auth.decorators import login_required,permission_required
from django.http import JsonResponse, HttpResponse,QueryDict
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

from competitor.forms import CompetitorListSelectForm
from competitor.models import *
from customer.utils import get_industry_data, get_industry_data_1
from public.utils import *
import pandas as pd
import numpy as np
from user_center.models import UserLog
from django.utils.decorators import method_decorator
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("competitor")



@method_decorator(csrf_exempt,name='dispatch')
class OperateCompetitor(View):
    '''操作竞品的接口'''
    @method_decorator(permission_required("competitor.competitor_list.view",login_url=JSON_403))
    def get(self,request):
        # 获取竞品列表数据
        result = {"status": 0, "message": "", "items": []}
        form = CompetitorListSelectForm(request.GET)
        if form.is_valid():
            cdata = form.cleaned_data
            competitor_name = cdata.get("competitor_name")
            customer_name = cdata.get("customer_name")
            customer_province_id = cdata.get("customer_province")
            industry1 = cdata.get("industry_1")
            industry2 = cdata.get("industry_2")

            crm_condition = {}
            # 处理筛选条件
            # 竞品名称
            if competitor_name:
                competitor_condition = {"competitorname__contains": competitor_name}
                competitor_id = get_value_list(Competitor, competitor_condition, ["competitorid", "competitorname","remark"])
            else:
                # 查询所有竞品
                competitor_id = get_value_list(Competitor, {}, ["competitorid", "competitorname","remark"])

            l = len(competitor_id)
            if l > 0:
                # 竞品
                competitor_df = pd.DataFrame(data=competitor_id, columns=["competitor_id", "competitor_name","remark"])
                v = ["competitorid", "accountid", "competitormoney"]
                if l == 1:
                    crm_competitor_list = get_value_list(CrmCompetitorMap, {"competitorid": competitor_id[0][0]}, v)
                else:
                    competitor_id = [comid[0] for comid in competitor_id]
                    crm_competitor_list = get_value_list(CrmCompetitorMap, {"competitorid__in": competitor_id}, v)
                # 竞品客户关联表
                crm_competitor_df = pd.DataFrame(data=crm_competitor_list,
                                                 columns=["competitor_id", "accountid", "money"])
                if len(crm_competitor_df) > 0:
                    select_crm1 = list(crm_competitor_df["accountid"])
                    if len(select_crm1) > 1:
                        crm_condition["id__in"] = select_crm1
                    else:
                        crm_condition["id"] = select_crm1[0]
                else:
                    crm_condition["id"] = '0000000000000'
                    # result["message"] = "该竞品没有关联的客户信息"
                    # return JsonResponse(result)
            else:
                result["message"] = "没有该竞品信息"
                return JsonResponse(result)
            # 客户名称
            if customer_name:
                crm_condition["accountname__contains"] = customer_name

            # 客户地域
            if customer_province_id:
                if customer_province_id != '0':
                    crm_condition["fstate"] = customer_province_id
                    customer_province = CrmLocationState.objects.get(lid=customer_province_id).lname
                else:
                    crm_condition["fstate__isnull"] = True
                    customer_province = '未知'
            else:
                customer_province = '全国'

            # 一级行业
            if industry1:
                if industry1 != '0':
                    crm_condition["dbcselect5"] = industry1
                    industry1_name = CrmIndustryL1.objects.get(id=industry1).name
                else:
                    crm_condition["dbcselect5__isnull"] = True
                    industry1_name = "未知"
            else:
                industry1_name = "全部"

            # 二级行业
            if industry2:
                if industry2 != '0':
                    crm_condition["dbcselect9"] = industry2
                    industry2_name = CrmIndustryL2.objects.get(id=industry2).name
                else:
                    crm_condition["dbcselect9__isnull"] = True
                    industry2_name = "未知"
            else:
                industry2_name = "全部"

            customer_list = get_value_list(Account, crm_condition,
                                           ["id", "accountname", "fstate", "dbcselect5", "dbcselect9"])
            customer_df = pd.DataFrame(data=customer_list,
                                       columns=["accountid", "accountname", "fstate", "industry1", "industry2"])
            # 过滤掉特定客户
            passname = ["智慧星光", "测试", "销售易"]
            customer_df = customer_df.loc[~customer_df.accountname.apply(lambda x: isInString(str(x), passname))]

            items_df = competitor_df
            items_df["province_name"] = customer_province
            items_df["industry1_name"] = industry1_name
            items_df["industry2_name"] = industry2_name
            # if request.user.is_superuser:
            #     items_df["cansee"] = 'True'
            # else:
            #     items_df["cansee"] = 'False'

            crm_competitor_df = crm_competitor_df.loc[crm_competitor_df.accountid.isin(customer_df["accountid"])]
            # 继续拼接数据
            for i, competitor_id in items_df["competitor_id"].items():
                mid_df = crm_competitor_df.loc[crm_competitor_df.competitor_id == competitor_id]
                items_df.loc[i, "customer_num"] = len(mid_df)
                items_df.loc[i, "money"] = format(mid_df["money"].sum(), ',')

            crm_info = items_df.fillna('--')
            # print(crm_info.columns)
            items = list(crm_info.to_dict(orient="index").values())

            result["status"] = 1
            result["items"] = items
        return JsonResponse(result)

    @method_decorator(permission_required("competitor.competitor_list.add",login_url=JSON_403))
    def post(self,request):
        # 添加竞品
        result = {"status": 0, "message": ""}
        form = dict(k.split('=') for k in request.POST.get("form_data").split('&'))
        # print(form)
        name = form.get("competitor_name")
        remark = form.get("competitor_remark")
        source_type = form.get("source_type") #数据来源，招投标模块创建1，人为录入2，项目部数据录入3

        nameobj = Competitor.objects.filter(competitorname=name)
        if nameobj:
            result["status"] = 2
            result["message"] = '竞品已存在'
            return JsonResponse(result)
        com = Competitor.objects.all().aggregate(Max('competitorid'))
        if com:
            id = com.get('competitorid__max') + 1
        else:
            id = 1
        try:
            Competitor.objects.create(competitorid=id, competitorname=name,remark=remark,source_type=source_type)
            result["status"] = 200
            result["message"] = '添加竞品成功'
        except Exception as e:
            logger.error(str(e))
            result["message"] = '添加竞品失败'

        user = request.user
        message = json.dumps(dict(request.POST))
        UserLog.objects.create(username=user.username, user_id=user.id,
                               model="竞品签约客户", action="添加竞品", message=message)
        return JsonResponse(result)

    @method_decorator(permission_required("competitor.competitor_list.delete",login_url=JSON_403))
    def delete(self,request):
        # 删除竞品
        result = {"status": 0, "message": ""}
        id = request.GET.get('id')
        nameobj = Competitor.objects.filter(competitorid=id)
        if nameobj:
            try:
                nameobj.delete()
                # 开始删除竞品和客户的关联关系
                con = CrmCompetitorMap.objects.filter(competitorid=id)
                if con:
                    con.delete()

                result["status"] = 200
                result["message"] = '删除竞品成功'

            except Exception as e:
                logger.error(str(e))
                result["message"] = '删除竞品失败'
        else:
            result["status"] = 2
            result["message"] = '竞品不存在'
            return JsonResponse(result)
        # 记日志
        user = request.user
        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=user.username, user_id=user.id,
                               model="竞品列表", action="删除竞品", message=message)
        return JsonResponse(result)

    @method_decorator(permission_required("competitor.competitor_list.put",login_url=JSON_403))
    def put(self,request):
        # 修改竞品
        result = {"status": 200, "message": ""}
        id = request.GET.get("id")
        name = request.GET.get("name")
        remark = request.GET.get("remark")
        # print(remark)
        # print(id,type(id))
        if id and name:
            # 查询竞品id不同，但是名称相同的，说明竞品已存在
            nameobj = Competitor.objects.exclude(competitorid=id).filter(competitorname=name)
            # print(nameobj)
            if len(nameobj) > 0:
                result["status"] = 2
                result["message"] = '竞品已存在'
                return JsonResponse(result)
            try:
                competitor_obj = Competitor.objects.get(competitorid=id)
                before_name = competitor_obj.competitorname #获取修改前的名字

                competitor_obj.competitorname = name
                competitor_obj.remark = remark
                competitor_obj.save()
                result["status"] = 200
                result["message"] = '修改竞品成功'
            except Exception as e:
                logger.error(str(e))
                result["status"] = -1
                result["message"] = '修改竞品失败'
                return JsonResponse(result)

            # 记日志
            user = request.user
            data = dict(request.GET)
            data["before_name"] = before_name
            message = json.dumps(data)
            UserLog.objects.create(username=user.username, user_id=user.id,
                                   model="竞品列表", action="修改竞品", message=message)
        return JsonResponse(result)


"""竞品列表页面"""
@login_required()
@permission_required("competitor.competitor_list.view",login_url=URL_403)
def competitorList(request):
    if request.method == "GET":
        title = "竞品列表"
        form = CompetitorListSelectForm()
        # 带条件请求页面时，设置默认的条件
        customer_province = request.GET.get("customer_province")
        industry1 = request.GET.get("industry_1")
        industry2 = request.GET.get("industry_2")
        competitor_name = request.GET.get("competitor_name")
        customer_name = request.GET.get("customer_name")
        # print(customer_province,industry1,industry2)
        if customer_province:
            form.select_province(customer_province)
        if industry1:
            form.select_industry1(industry1)
        if industry2:
            form.select_industry2(industry2)
        if competitor_name:
            form.input_competitorName(competitor_name)
        if customer_name:
            form.input_customerName(customer_name)

        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        init_data["col_names"] = ["竞品名称", "签单地域","一级行业", "二级行业","客户数","总金额", "操作"]
        init_data["col_model"] = [
            {
                "name": 'competitor_name',
                "width": 25
            },
            {
                "name": 'province_name',
                "width": 13
            },
            {
                "name": 'industry1_name',
                "width": 13
            },
            {
                "name": 'industry2_name',
                "width": 13
            },
            {
                "name": 'customer_num',
                "width": 13,
                "sorttype": "int"
            },
            {
                "name": 'money',
                "width": 15,
                "sorttype": "int"
            },
            {
                "name": 'operations',
                "width": 15
            }
        ]
        init_data["items"] = []
        init_data = json.dumps(init_data)

        # 二级行业
        industry_data = get_industry_data()
        industry_data = json.dumps(industry_data)
        # # 一级行业
        # industry_data_1 = [["", "全部"]] + get_industry_data_1()
        # industry_data_1 = json.dumps(industry_data_1)

        canChange = 0
        canDelete = 0
        if request.user.has_perm("competitor.competitor_list.change"):
            canChange = 1
        if request.user.has_perm("competitor.competitor_list.delete"):
            canDelete = 1
        
        # 记日志
        user = request.user
        if user.username not in ["武翠霞", "丛大侠", "王寅", "张太锋", "黄远", "朱铭鑫", "袁战梅"]:
            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=user.username, user_id=user.id,
                                   model="竞品列表", action="进入竞品列表", message=message)
        return render(request, "competitor/competitor_list.html", locals())

