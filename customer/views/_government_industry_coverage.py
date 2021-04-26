"""
政务行业覆盖率
20200619：只统计公安、宣传两个行业
"""


import json
import pymysql
import datetime
import logging

from django.http import JsonResponse
from django.shortcuts import render
from mandala.auth import get_user_model
from mandala.auth.decorators import  permission_required, login_required

from django.conf import settings

from customer.forms import GovernmentIndustryCoverageSelectForm

from secretary.models import  DingGroupMemberMap

from customer.utils import (
        get_industry_data, get_industry_data_1,
        get_industry_l1_dict, get_industry_l2_dict,
        get_state_dict, get_city_dict, get_district_dict,
        get_state_list, get_city_list, get_district_list
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
@permission_required("customer.government_industry_coverage.view",login_url=URL_403)
def government_industry_coverage(request):
    if request.method == "GET":

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="客户管理-公宣覆盖率", action="访问", message=message)

        title = "公宣地域覆盖率"
        form = GovernmentIndustryCoverageSelectForm()
        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        init_data["col_names"] = ["客户地域-省", "客户地域-市", "客户地域-县", "一级行业", "二级行业", "基数", "覆盖(正式+试用)", "覆盖率", 
                "正式", "占有率", "试用"] 
        init_data["col_model"] = [
            {
                "name": 'state_name',
                "width": 10
            },
            {
                "name": 'city_name',
                "width": 10
            },
            {
                "name": 'district_name',
                "width": 10
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
            }
        ]
        init_data["items"] = []
        init_data = json.dumps(init_data)
        states = get_state_list()

        if (not request.user.is_superuser) and (not request.user.roles.filter(code="region")):
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
        cities = json.dumps(get_city_list())
        districts = json.dumps(get_district_list())
        return render(request, "customer/government_industry_coverage.html", locals())


"""客户行业覆盖率统计查询数据接口，返回json格式的数据"""
@permission_required("customer.government_industry_coverage.view",login_url=JSON_403)
def government_industry_coverage_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    result = {"status": 0, "message": ""}

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-公宣覆盖率api", action="查询", message=message)

    form = GovernmentIndustryCoverageSelectForm(kws)
    if form.is_valid():
        cdata = form.cleaned_data
        industry1_id = cdata.get("industry1")
        industry2_id = cdata.get("industry2")
        state_id = cdata.get("state")
        city_id = cdata.get("city")
        district_id = cdata.get("district")
        now = datetime.datetime.now()
        
        table = "police_and_internet_coverage"
        sql = """SELECT *
                FROM {}  """.format(table) 

        where = []

        if (not request.user.is_superuser) and (not request.user.roles.filter(code="region")):
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
                    
            if not dpt_names:
                error = "部门错误"
                code = -1
                result["message"] = error
                result["error"] = error
                result["status"] = code
                result["code"] = code
                return JsonResponse(result)

            w = []
            for dpt_name in dpt_names:
                item = "state_name like '%%%s%%'"%dpt_name
                w.append(item)

            item = "(" + " OR ".join(w) + ")"
            where.append(item)

        # if industry1_id:
        #     item = "industry1_id={}".format(industry1_id)
        #     where.append(item)
        ######### industry1_id 需要等于 51， 即政府
        item = "industry1_id=51"
        where.append(item)
        if industry2_id:
            item = "industry2_id={}".format(industry2_id)
            where.append(item)
        else:
            item = "industry2_id IN (46, 14)"
            where.append(item)

        if state_id:
            item = "province_id={}".format(state_id)
            where.append(item)

            if city_id:
                item = "city_id={}".format(city_id)
                where.append(item)
        
                if district_id:
                    item = "district_id={}".format(district_id)
                    where.append(item)
                else:
                    item = "district_id<>0"
                    where.append(item)
            else:
                item = "city_id<>0"
                where.append(item)
                item = "district_id=0"
                where.append(item)
        else:
            item = "province_id<>0"
            where.append(item)
            item = "city_id=0"
            where.append(item)
            item = "district_id=0"
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
        state_dict = get_state_dict()
        city_dict = get_city_dict()
        district_dict = get_district_dict()
        if not items:
            items = [{}]
            # industry1_name = ""
            # industry2_name = ""
            # state_name = ""
            # city_name = ""
            # district_name = ""
            # if industry1_id:
            #     industry_l1_dict = get_industry_l1_dict()
            #     industry_l1 = industry_l1_dict.get(int(industry1_id))
            #     if industry_l1:
            #         industry1_name = industry_l1.get("name")
            # if not industry1_name:
            #     industry1_name = "----"
            # if industry2_id:
            #     industry_l2_dict = get_industry_l2_dict()
            #     industry_l2 = industry_l2_dict.get(int(industry2_id))
            #     if industry_l2:
            #         industry2_name = industry_l2.get("name")
            # if not industry2_name:
            #     industry2_name = "----"
            # if state_id:
            #     state = state_dict.get(int(state_id))
            #     if state:
            #         state_name = state.get("lname")
            # if city_id:
            #     city = city_dict.get(int(city_id))
            #     if city:
            #         city_name = city.get("lname")
            # if district_id:
            #     district = district_dict.get(int(district_id))
            #     if district:
            #         district_name = district.get("lname")
            # if not state_name:
            #     state_name = "----"
            # if not city_name:
            #     city_name = "----"
            # if not district_name:
            #     district_name = "----"
            # item = {"industry1_name": industry1_name, "industry2_name": industry2_name, 
            #         "state_name": state_name, "city_name": city_name, "district_name": district_name}
            # items = [item]
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
            state_name = "----"
            city_name = "----"
            district_name = "----"
            if state_id:
                _state_id = state_id
            else:
                # _state_id = item.get("state_id")
                _state_id = item.get("province_id")
            if _state_id:
                _state_name = state_dict.get(int(_state_id), {}).get("lname")
                if _state_name:
                    state_name = _state_name
            if city_id:
                _city_id = city_id
            else:
                _city_id = item.get("city_id")
            if _city_id:
                _city_name = city_dict.get(int(_city_id), {}).get("lname")
                if _city_name:
                    city_name = _city_name
            if district_id:
                _district_id = district_id
            else:
                _district_id = item.get("district_id")
            if _district_id:
                _district_name = district_dict.get(int(_district_id), {}).get("lname")
                if _district_name:
                    district_name = _district_name
            item["state_name"] = state_name
            item["city_name"] = city_name
            item["district_name"] = district_name
            if not item.get("industry2_name"):
                item["industry2_name"] = "----"
        result["status"] = 1
        result["items"] = items
    return JsonResponse(result)

@login_required
@permission_required("customer.government_industry_coverage_map.view",login_url=URL_403)
def get_coverage_map(request):
    title = "公宣覆盖率地图"

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-公宣覆盖率地图", action="访问", message=message)

    return render(request, "customer/coverage-map.html", locals()) 

@login_required
@permission_required("customer.government_industry_coverage_map.view",login_url=URL_403)
def get_coverage_map2(request):
    title = "公宣覆盖率地图"

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-公宣覆盖率地图", action="访问", message=message)

    return render(request, "customer/coverage-map2.html", locals()) 