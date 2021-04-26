
import json
import pymysql
import datetime
import logging
from django.http import JsonResponse
from django.shortcuts import render
from mandala.auth import get_user_model
from mandala.auth.decorators import  permission_required, login_required

from django.conf import settings

from customer.forms import IndustryCoverageSelectForm

from customer.utils import (
        get_industry_data, get_industry_data_1,
        get_industry_l1_dict, get_industry_l2_dict,
        get_state_dict
    )
from user_center.models import LocationInfo, UserLog
from public.utils import parse_kwargs_for_pymysql
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("customer")

# Create your views here.

User = get_user_model()

"""客户行业覆盖率统计页面"""
@login_required
@permission_required("customer.industry_coverage.view",login_url=URL_403)
def industry_coverage(request):
    if request.method == "GET":

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="客户管理-行业覆盖率", action="访问", message=message)

        title = "客户行业覆盖率"
        form = IndustryCoverageSelectForm()
        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        init_data["col_names"] = ["一级行业", "二级行业", "地域", "基数", "覆盖(正式+试用)", "覆盖率", 
                "正式", "占有率", "试用", "竞品"] 
        init_data["col_model"] = [
            {
                "name": 'industry1_name',
                "width": 10
            },
            {
                "name": 'industry2_name',
                "width": 10
            },
            {
                "name": 'province_name',
                "width": 10
            },
            {
                "name": 'base_count',
                "width": 10,
                "sorttype": "number"
            },
            {
                "name": 'have_count',
                "width": 10,
                "sorttype": "number"
            },
            {
                "name": 'have_rate',
                "width": 10,
                "sorttype": "number"
            },
            {
                "name": 'formal_count',
                "width": 10,
                "sorttype": "number"
            },
            {
                "name": 'formal_rate',
                "width": 10,
                "sorttype": "number"
            },
            {
                "name": 'trial_count',
                "width": 10,
                "sorttype": "number"
            },
            {
                "name": 'competitor_count',
                "width": 10,
                "sorttype": "number"
            }
        ]
        init_data["items"] = []
        init_data = json.dumps(init_data)
        
        industry_data = get_industry_data()
        industry_data = json.dumps(industry_data)
        industry_data_1 =[["", "--------"]] + get_industry_data_1()
        industry_data_1 = json.dumps(industry_data_1)
        return render(request, "customer/industry_coverage.html", locals())


"""客户行业覆盖率统计查询数据接口，返回json格式的数据"""
@permission_required("customer.industry_coverage.view", login_url=JSON_403)
def industry_coverage_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-行业覆盖率api", action="查询", message=message)

    result = {"status": 0, "message": ""}
    form = IndustryCoverageSelectForm(kws)
    if form.is_valid():
        cdata = form.cleaned_data
        industry1_id = cdata.get("industry1")
        industry2_id = cdata.get("industry2")
        location_id = cdata.get("location")
        
        now = datetime.datetime.now()

        table = "INDUSTRYAREACOVERAGE"
        sql = """SELECT *
                FROM {}  """.format(table) 
        where = []
        if industry1_id:
            item = "industry1_id={}".format(industry1_id)
            where.append(item)
        if industry2_id:
            item = "industry2_id={}".format(industry2_id)
            where.append(item)
        if location_id:
            item = "province_id={}".format(location_id)
            where.append(item)
        if where:
            sql += "WHERE " + " AND ".join(where)
        sql += ";"
        try:
            kws = parse_kwargs_for_pymysql(settings.DATABASES["contract_33"])
            conn_33 = pymysql.connect(**kws)
            cursor = conn_33.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            items = cursor.fetchall()
            cursor.close()
            conn_33.close()
        except Exception as e:
            logger.error(str(e))
            result["message"] = "服务器繁忙，请稍后重试"
            return JsonResponse(result)
        if not items:
            industry1_name = ""
            industry2_name = ""
            province_name = ""
            if industry1_id:
                industry_l1_dict = get_industry_l1_dict()
                industry_l1 = industry_l1_dict.get(int(industry1_id))
                if industry_l1:
                    industry1_name = industry_l1.get("name")
            if not industry1_name:
                industry1_name = "----"
            if industry2_id:
                industry_l2_dict = get_industry_l2_dict()
                industry_l2 = industry_l2_dict.get(int(industry2_id))
                if industry_l2:
                    industry2_name = industry_l2.get("name")
            if not industry2_name:
                industry2_name = "----"
            if location_id:
                province_dict = get_state_dict()
                province = province_dict.get(int(location_id))
                if province:
                    province_name = province.get("lname")
            if not province_name:
                province_name = "----"
            item = {"industry1_name": industry1_name, "industry2_name": industry2_name, "province_name": province_name}
            items = [item]
        for item in items:
            # item["competitor"] = "----"
            base_count = item.get("base_count")
            have_count = item.get("have_count")
            formal_count = item.get("formal_count")
            trial_count = item.get("trial_count")
            competitor_count = item.get("competitor_count")
            if not base_count:
                item["base_count"] = 0
            if not have_count:
                item["have_count"] = 0
            if not formal_count:
                item["formal_count"] = 0
            if not trial_count:
                item["trial_count"] = 0
            if not competitor_count:
                item["competitor_count"] = 0
            if base_count and have_count:
                rate = have_count / base_count * 100
            else:
                rate = 0
            if rate:
                item["have_rate"] = "{}%".format("%.2f"%rate)
            else:
                item["have_rate"] = "0"
            if base_count and formal_count:
                rate = formal_count / base_count * 100
            else:
                rate = 0
            if rate:
                item["formal_rate"] = "{}%".format("%.2f"%rate)
            else:
                item["formal_rate"] = "0"
            if not item.get("province_name"):
                item["province_name"] = "未知"
            if not item.get("industry2_name"):
                item["industry2_name"] = "未知"
        result["status"] = 1
        result["items"] = items
    return JsonResponse(result)
 