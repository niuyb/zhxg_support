import json
import time
import arrow
import random
import pymysql
import pandas as pd
import hashlib
import datetime
import logging

from math import ceil
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required
from django.forms import model_to_dict

from user_center.models import UserLog
from public.utils import get_all_data, gen_date_list, gen_month_list, parse_kwargs_for_pymysql
from secretary.utils import get_departments_about_sale, get_sub_departments, get_all_sub_departments
from sale.forms import PaymentPlanListSelectForm

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

# Create your views here.

logger = logging.getLogger("sale")

"""获取回款计划列表页面初始数据"""
def get_payment_plan_list_init_data():
    init_data = {"row_list": [10, 20, 50], "row_num": 20}
    init_data["col_names"] = ["编号", "计划回款金额", "计划回款日期", "客户名称", "实际回款金额", "合同编号",
            "订单所有人", "订单实际负责人", "本期逾期状态",  "客户所属事业部", "销售所属大区"]#"回款已逾期天数",
    init_data["col_model"] = [
        {
            "name": 'code',
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'amount',
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'planTime',
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'customer_name',#accountId
            # "index": 'note',
            "width": 10,
            # "sortable": false
        },
        {
            "name": 'actualAmount',
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'customItem124__c',#合同编号
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'customItem141__c',#订单所有人
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'customItem142__c',#订单实际负责人
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'overdueStatus',#本期逾期状态
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        # {
        #     "name": 'customItem150__c',#回款已逾期天数
        #     # "index": 'note',
        #     "width": 5,
        #     # "sortable": false
        # },
        {
            "name": 'customItem158__c',#客户所属事业部
            # "index": 'note',
            "width": 5,
            # "sortable": false
        },
        {
            "name": 'customItem159__c',#销售所属大区
            # "index": 'note',
            "width": 5,
            # "sortable": false
        }
    ]
    init_data["items"] = []
    return init_data

"""回款计划列表数据api"""
@permission_required("sale.payment_plan_list.view", login_url=JSON_403)
def payment_plan_list_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-回款计划列表api", action="查询", message=message)

    result = {"code": 0, "msg": "", "data": []}
    form = PaymentPlanListSelectForm(request.GET)
    if not form.is_valid():
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    cdata = form.cleaned_data
    ses = ['code', 'amount', 'planTime', 'accountId', 'actualAmount', 'customItem124__c', 'customItem141__c', 'customItem142__c', 'overdueStatus', 'customItem150__c', 'customItem158__c', 'customItem159__c']
    where = ["status=0"]
    start = cdata.get("plantime_start")
    end = cdata.get("plantime_end")
    overdue = cdata.get("overdue")
    if start:
        start = datetime.datetime.strptime(start, "%Y-%m-%d").timestamp() * 1000
        where.append("planTime >= " + str(start))
    if end:
        end = datetime.datetime.strptime(end, "%Y-%m-%d").timestamp() * 1000 + 24 * 3600 * 1000
        where.append("planTime <= " + str(end))
    if overdue not in ["", None]:
        where.append("overdueStatus = " + str(overdue))
    if where:
        where = "Where {}".format(" AND ".join(where))
    else:
        where = ""
    # sql = "select * from `paymentplan`;"
    sql = "select {} from `paymentplan` {};".format(", ".join(ses), where)
    sql2 = "select id as customer_id, accountName as customer_name from account;"
    kws = parse_kwargs_for_pymysql(settings.DATABASES["contract_33"])
    conn = pymysql.connect(**kws)
    pps = pd.read_sql(sql, conn)
    cs = pd.read_sql(sql2, conn)
    conn.close()
    pps = pd.merge(pps, cs, how='inner', left_on='accountId', right_on="customer_id")
    items = list(pps.to_dict(orient="index").values())
    result["code"] = 1
    result["data"] = items
    return JsonResponse(result)

"""回款计划青青页"""
@login_required
@permission_required("sale.payment_plan_list.view", login_url=URL_403)
def payment_plan_list(request):
    if request.method == "GET":
        title = "回款计划列表"

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="商务管理-回款计划列表", action="访问", message=message)

        form = PaymentPlanListSelectForm(request.GET)
        init_data = get_payment_plan_list_init_data()
        # if request.user.has_perm("sale.export_payment_plan_list"):
        #     init_data["export_payment_plan_list_access"] = 1

        init_data = json.dumps(init_data)
        user_log_url = reverse("user_center:user_log")
        departments_api = reverse("secretary:departments_api")
        department_data = get_departments_about_sale()
        department_data = json.dumps(department_data)
        department_data_1 =[["", "--------"]] + list(settings.SALE_DEPARTMENT_LEVEL_1.items())
        department_data_1 = json.dumps(department_data_1)
        return render(request, "sale/payment_plan_list.html", locals())