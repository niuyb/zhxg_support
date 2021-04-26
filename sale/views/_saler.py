import os
import re
import time
import json
import arrow
import random
import pandas as pd
import logging

from collections import defaultdict
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mandala.auth import get_user_model
from mandala.auth.decorators import  permission_required, login_required

from customer.models import User as CrmUser, SalerLevel, SalerMonthPromise
from customer.models import Department, Account, Opportunity, SalerKPIMonth, SalerInfoPlus #, SalerInfoFirstOrder
from secretary.utils import get_departments_about_sale, get_group_members, get_can_see, get_can_see_new
from secretary.models import WkTUserservice
from secretary.models import  SalercanseeNew
from user_center.models import UserLog, HrEmployee
from sale.utils import (get_government_sale_center_employees, get_government_sale_center_salers,
        get_government_sale_center_salers_crm, get_crmusers_by_dtalkids, get_date_range_of_month,
        get_last_date_of_month, get_can_see_istarshine_ids)

from .common import get_saler_ids_dingding_crm
from sale.forms import SalerListSelectForm
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

logger = logging.getLogger("sale")
User = get_user_model()

# Create your views here.

"""获取商务列表页面初始数据"""
def get_saler_list_init_data():
    init_data = {"row_list": [10, 20, 50], "row_num": 20}
    init_data["col_names"] = ["商务", "部门", "职位", "入职日期", "客户总数", "新签", "销售额", "状态", "分数"]
    init_data["col_model"] = [
        {
            "name": 'username',
            # "index": 'note',
            "width": 20,
            # "sortable": false
        },
        {
            "name": 'department_name',
            # "index": 'note',
            "width": 15,
            # "sortable": false
        },
        {
            "name": 'position',
            # "index": 'id',
            "width": 10,
            # "sorttype": "int"
        },
        {
            "name": 'ctime',
            # "index": 'tax',
            "width": 12,
            # "align": "right",
            "sorttype": "date",
            # "formatter": "date", "formatoptions":{"srcformat": 'Y-m-d H:i', "newformat": 'Y-m-d'}
        },
        {
            "name": 'customer_count',
            # "index": 'amount',
            "width": 8,
            # "align": "right",
            "sorttype": "int",
            # "formatter": "number"
        },
        {
            "name": 'customer_count_new',
            # "index": 'amount',
            "width": 8,
            # "align": "right",
            # "sorttype": "float",
            # "formatter": "number"
        },
        {
            "name": 'sale_money',
            # "index": 'note',
            "width": 15,
            # "sortable": false
        },
        {
            "name": 'sale_status',
            # "index": 'invdate',
            "width": 8,
            # "sorttype": "date",
        },
        {
            "name": 'sale_score',
            # "index": 'invdate',
            "width": 8,
            # "sorttype": "date",
        },
        # {
        #     "name": 'operations',
        #     # "index": 'note',
        #     "width": 25,
        #     "sortable": False,
        #     # "formatter": "constructOperationCell"
        # },
    ]
    init_data["items"] = []
    return init_data

"""商务人员列表页面"""
@login_required
@permission_required("sale.government_center.saler_tab.view", login_url=URL_403)
def saler_list(request):
    if request.method == "GET":
        title = "商务列表"

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="商务管理-商务列表", action="访问", message=message)

        form = SalerListSelectForm(request.GET)
        init_data = get_saler_list_init_data()
        # if request.user.has_perm("sale.export_saler_list"):
        #     init_data["export_saler_list_access"] = 1

        init_data = json.dumps(init_data)
        # user_log_url = reverse("user_center:user_log")
        # departments_api = reverse("secretary:departments_api")
        # department_data = get_departments_about_sale()
        # department_data = json.dumps(department_data)
        # department_data_1 =[["", "--------"]] + list(settings.SALE_DEPARTMENT_LEVEL_1.items())
        # department_data_1 = json.dumps(department_data_1)
        return render(request, "sale/saler_list.html", locals())
    

"""获取销售人员信息"""
# @permission_required("sale.saler_list.view", login_url=JSON_403)
def saler_list_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务列表api", action="查询", message=message)

    result = {"status": 0, "code": 0, "message": "", "error": "", "data": None, "items": None}

    # 获取政务销售中心的销售
    # QuerySet
    salers = get_government_sale_center_salers()
    if request.user.is_superuser:
        salers = list(salers.values())
    else:
        can_see = get_can_see_new(request.user.istarshine_id)
        if not can_see:
            result["error"] = "无权限"
            result["message"] = "无权限"
            return JsonResponse(result)
            
        salers = list(salers.filter(istarshine_id__in=can_see).values())
    # items = []
    # item = {"username": "丛丛丛", "avatar": "", "position": "商务经理",#/static/img/a7.jpg
    #         "department_name": "政务-一区-北京", "ctime": "2016-05-18",
    #         "customer_count": 220, "customer_count_new": 11, "sale_score": "0.97/1.00",
    #         "sale_money": "1,0000,000", "sale_status": "7,15,10,0,0,12,8"}
    # for _ in range(50):
    #     items.append(item)
    # result["items"] = items
    # result["status"] = 1
    result["items"] = salers
    result["data"] = salers
    result["code"] = 1
    result["status"] = 1
    result["error"] = "查询成功"
    result["message"] = "查询成功"
    return JsonResponse(result)

def get_saler_info_list(saler_ids):
    
    salers = list(CrmUser.objects.filter(id__in=saler_ids).values("id", "name", "departid"))

    sdf = pd.DataFrame(salers)
    sdf = sdf.rename(columns={"departid": "department_id", "name": "saler_name"})

    saler_names = list(sdf["saler_name"])
    
    dpts = list(Department.objects.all().values("id", "departname"))
    ddf = pd.DataFrame(dpts)
    
    ddf["id"] = ddf["id"].apply(lambda x: str(x))
    ddf = ddf.rename(columns={"id": "department_id", "departname": "department_name"})
    
    sdf = pd.merge(sdf, ddf, how="left", on="department_id")
    sdf["id"] = sdf["id"].apply(lambda x: str(x))
    sdf = sdf.rename(columns={"id": "saler_id"})
    
    # aes = Account.objects.filter(ownerid__in=saler_ids, highseastatus__in=[1,3,4]).values("ownerid").annotate(customer_count=Count("ownerid"))
    # adf = pd.DataFrame(aes)
    # adf = adf.rename(columns={"ownerid": "saler_id"})
    # adf["saler_id"] = adf["saler_id"].apply(lambda x: str(x))
    # sdf = pd.merge(sdf, adf, how="left", on="saler_id")

    # mses = WkTUserservice.objects.filter(ku_sale__in=saler_names).values("ku_sale").annotate(account_count=Count("ku_sale"))
    # msdf = pd.DataFrame(mses)
    # msdf = msdf.rename(columns={"ku_sale": "saler_name"})
    # sdf = pd.merge(sdf, msdf, how="left", on="saler_name")

    # oes = Opportunity.objects.filter(ownerid__in=saler_ids).values("ownerid").annotate(opportunity_count=Count("ownerid"))
    # odf = pd.DataFrame(oes)
    # odf = odf.rename(columns={"ownerid": "saler_id"})
    # sdf = pd.merge(sdf, odf, how="left", on="saler_id")

    sfs = list(SalerInfoPlus.objects.all().values())
    sfdf = pd.DataFrame(sfs)
    sfdf = sfdf.rename(columns={"ownerid": "saler_id"})
    
    sdf = pd.merge(sdf, sfdf, how="left", on="saler_id")
    sdf["days_joined"] = sdf["days_joined"].fillna(0)
    sdf = sdf.fillna("")
    # plus = {"customer_count": 0, "account_count": 0, "opportunity_count": 0}
    data = list(sdf.to_dict(orient="index").values())
    return data

@permission_required("sale.government_center.saler_tab.view", login_url=JSON_403)
def saler_info_list_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务信息列表api", action="查询", message=message)

    did = kws.get("did")
    result = {"code": 0, "data": None, "error": ""}
    if not did:
        result["code"] = -1
        result["error"] = "参数错误"        
    saler_ids = get_saler_ids_dingding_crm(did)
    if request.user.is_superuser:
        pass
    else:
        can_see = get_can_see_new(request.user.istarshine_id)
        saler_ids = CrmUser.objects.filter(employeecode__in=can_see).values_list("id", flat=True)
    data = get_saler_info_list(saler_ids)
    result["code"] = 1
    result["data"] = data
    return JsonResponse(result)


"""导出商务人员列表"""
@login_required
@permission_required("sale.saler_list.export", login_url=URL_403)
def export_saler_list(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务列表", action="导出", message=message)

    return JsonResponse({})

"""通过钉钉id获取crm里面的人员"""
def get_crmusers_by_dtalkids(dtalkids):
    """返回一个queryset对象"""
    usernames = list(User.objects.filter(dtalkid__in=dtalkids).values_list("username", flat=True))
    crmusers = CrmUser.objects.filter(name__in=usernames)
    return crmusers

"""
商务月度kpi统计
"""
@login_required
@permission_required("sale.saler_kpi_month.view", login_url=URL_403)
def saler_kpi_month(request):
    title = "商务月度kpi"
    date = request.GET.get("date", "")
    date = date.strip()
    if not date:
        date = arrow.now().format("YYYY-MM")
        url = request.get_full_path()
        us = url.split("?")
        if len(us) == 1:
            query = ""
        else:
            query = us[1]
        _params = query.split("&")
        params = []
        for param in _params:
            if param.startswith("date="):
                pass
            else:
                params.append(param)
        params.append("date={}".format(date))
        query = "&".join(params)
        redirect_url = us[0] + "?" + query
        return redirect(redirect_url)

    api = "/sale/saler/kpi/month/api"
    if request.user.has_perm("sale.saler_kpi_month.export"):
        can_export = 1

    user = request.user
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="商务管理-商务月度kpi统计页面", action="访问", message=message)

    return render(request, "sale/saler-kpi-month.html", locals())

def get_saler_kpi(history=False, date=None, istarshine_id=None):
    result = {"code": 0, "data": None, "error": ""}
    params = {}
    if not date:
        date = ""

    date = date.strip()
    if not date:
        date = arrow.now()

    date_range = get_date_range_of_month(date)
    date_str_range = [d.format("YYYY-MM-DD") for d in date_range]
    if history:
        if not istarshine_id:
            result["error"] = "参数错误"
            return result
        
        params["istarshine_id"] = istarshine_id
        if date:
            params["ctime__in"] = date_str_range
    else:
        if not date:
            result["error"] = "参数错误"
            return result
            
        params["ctime__in"] = date_str_range
        if istarshine_id:
            params["istarshine_id"] = istarshine_id

    items = list(SalerKPIMonth.objects.filter(**params).order_by("-ctime")[: 10000].values())
    if items:
        levels = list(SalerLevel.objects.all().values("istarshine_id", "level"))
        df_levels = pd.DataFrame(levels)

        today = arrow.now()
        df = pd.DataFrame(items)
        df["join_days"] = df["hiredate"].apply(lambda x: (today - arrow.get(x)).days)
        df["day_new_performance"] = df["month_new_performance"]
        df["day_new_performance"].index = df["day_new_performance"].index - 1
        df["day_new_performance"] = df["month_new_performance"] - df["day_new_performance"]

        df["day_renew_performance"] = df["month_renew_performance"]
        df["day_renew_performance"].index = df["day_renew_performance"].index - 1
        df["day_renew_performance"] = df["month_renew_performance"] - df["day_renew_performance"]

        df["day_performance"] = df["month_performance"]
        df["day_performance"].index = df["day_performance"].index - 1
        df["day_performance"] = df["month_performance"] - df["day_performance"]

        df["day_complete_money"] = df["month_complete_money"]
        df["day_complete_money"].index = df["day_complete_money"].index - 1
        df["day_complete_money"] = df["month_complete_money"] - df["day_complete_money"]

        df["day_confirm_money"] = df["month_confirm_money"]
        df["day_confirm_money"].index = df["day_confirm_money"].index - 1
        df["day_confirm_money"] = df["month_confirm_money"] - df["day_confirm_money"]

        df["day_call_num"] = df["month_call_num"]
        df["day_call_num"].index = df["day_call_num"].index - 1
        df["day_call_num"] = df["month_call_num"] - df["day_call_num"]

        df["day_visit_num"] = df["month_visit_num"]
        df["day_visit_num"].index = df["day_visit_num"].index - 1
        df["day_visit_num"] = df["month_visit_num"] - df["day_visit_num"]

        df["ms_day_new_num"] = df["ms_month_new_num"]
        df["ms_day_new_num"].index = df["ms_day_new_num"].index - 1
        df["ms_day_new_num"] = df["ms_month_new_num"] - df["ms_day_new_num"]

        df["ts_day_new_num"] = df["ts_month_new_num"]
        df["ts_day_new_num"].index = df["ts_day_new_num"].index - 1
        df["ts_day_new_num"] = df["ts_month_new_num"] - df["ts_day_new_num"]

        df = df.drop(["level"], axis=1)
        df = pd.merge(df, df_levels, how="left", on="istarshine_id")

        month = date_range[-1].format("YYYY-MM")
        ps = list(SalerMonthPromise.objects.filter(month=month).values("istarshine_id", "promise_money"))
        if not ps:
            ps = [{"istarshine_id": "", "promise_money": 0}]
        pdf = pd.DataFrame(ps)
        pdf = pdf.rename(columns={"promise_money": "month_head_confirm_money"})
        df = pd.merge(df, pdf, how="left", on="istarshine_id")
        # df["month_head_confirm_money"] = 0

        df = df.fillna(0)
        items = list(df.to_dict(orient="index").values())

    result["code"] = 1
    result["error"] = "查询成功"
    result["data"] = items
    return result

def get_saler_kpi_month(date=None, istarshine_ids=None, **kwargs):
    result = {"code": 0, "data": None, "error": ""}
    if date is not None:
        date = date.strip()
    
    if date:
        _date = arrow.get(date)
        if re.search("^\d{4}-\d{2}-\d{2}$", date) or re.search("^\d{4}/\d{2}/\d{2}$", date):
            pass
        else:
            if _date.month >= arrow.now().month:
                _date = None
            else:
                _date = get_last_date_of_month(date)

        date = None
        if _date:
            date = _date.format("YYYY-MM-DD")

    if not date:
        date = SalerKPIMonth.objects.all().last().ctime
        
    params = {"ctime": date}
    if istarshine_ids is not None:
        params["istarshine_id__in"] = istarshine_ids

    items = list(SalerKPIMonth.objects.filter(**params).values())

    def get_rate(row, col1, col2):
        a = row[col1]
        b = row[col2]
        if a and b and (str(a) != 'nan') and (str(b) != 'nan'):
            return round(float(a) / float(b) * 100, 2)
        return 0

    if items:
        levels = list(SalerLevel.objects.all().values("istarshine_id", "level"))
        df_levels = pd.DataFrame(levels)

        today = arrow.now()
        df = pd.DataFrame(items)
        df["confirm_goal_rate"] = df.apply(lambda row: get_rate(row, "month_confirm_money", "month_goal"), axis=1)
        def get_join_days(x):
            if x in [0, "0"]:
                x = "2017-01-01"
            return (today - arrow.get(x)).days

        # df["join_days"] = df["hiredate"].apply(lambda x: (today - arrow.get(x)).days)
        df["join_days"] = df["hiredate"].apply(get_join_days)

        month = arrow.get(date).format("YYYY-MM")
        ps = list(SalerMonthPromise.objects.filter(month=month).values("istarshine_id", "promise_money"))
        if not ps:
            ps = [{"istarshine_id": "", "promise_money": 0}]

        pdf = pd.DataFrame(ps)
        pdf = pdf.rename(columns={"promise_money": "month_head_confirm_money"})
        df = pd.merge(df, pdf, how="left", on="istarshine_id")

        df["month_new_rate"] = df.apply(lambda row: get_rate(row, "month_new_performance", "month_new_goal"), axis=1)
        df["month_renew_rate"] = df.apply(lambda row: get_rate(row, "month_renew_performance", "month_renew_goal"), axis=1)
        df["month_rate"] = df.apply(lambda row: get_rate(row, "month_performance", "month_goal"), axis=1)

        df = df.drop(["level"], axis=1)
        df = pd.merge(df, df_levels, how="left", on="istarshine_id")

        df = df.fillna(0)

        items = list(df.to_dict(orient="index").values())
        
    result["code"] = 1
    result["data"] = items
    result["error"] = "查询成功"
    return result

@permission_required("sale.saler_kpi_month.view", login_url=JSON_403)
def saler_kpi_month_api(request):
    date = request.GET.get("date")

    user = request.user
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="商务管理-商务月度kpi统计api", action="查询", message=message)

    istarshine_ids = get_can_see_istarshine_ids(request)
    if not istarshine_ids:
        result = {"code": 0, "data": [], "error": "无权限"}
        return JsonResponse(result)
        
    result = get_saler_kpi_month(date=date, istarshine_ids=istarshine_ids)
    return JsonResponse(result)

def get_saler_kpi_columns(history=False):
    columns={
        "saler": "商务", 
        "level": "级别",
        "ownerid": "商务销售易ID",
        "istarshine_id": "商务智慧星光唯一ID",
        "hiredate": "入职日期", 
        "join_days": "入职天数",
        "department_name": "四级部门",
        "parent_name": "三级部门",
        "job_name": "职位",

        "month_new_goal": "当月新签任务",
        "month_renew_goal": "当月续签任务",
        "month_goal": "当月任务",

        "month_new_performance": "当月新签业绩",
        "month_renew_performance": "当月续签业绩",
        "month_performance": "当月业绩",

        "month_confirm_money": "当月承诺值",
        "month_fight_money": "当月争取值",
        "month_complete_money": "当月完成值",

        "month_call_num": "当月电话数",
        # "week_call_num": "当周电话数",

        "month_visit_num": "当月出差拜访数",
        # "week_visit_num": "当周出差拜访数",

        "ms_trial_num": "秘书试用账号数",
        "ms_month_active_num": "秘书月活数",
        "ms_month_new_num": "秘书当月新建",
        # "ms_week_new_num": "秘书当周新建",

        "ts_trial_num": "态势试用账号数",
        "ts_month_active_num": "态势月活数",
        "ts_month_new_num": "态势当月新建",
        # "ts_week_new_num": "态势当周新建",

        "ctime": "统计日期"
        }
    if history:
        columns.update({
            "day_new_performance": "当天新签业绩",
            "day_renew_performance": "当天续签业绩",
            "day_performance": "当天业绩",
            "day_complete_money": "当天完成值",
            "day_call_num": "当天电话数",
            "day_visit_num": "当天出差拜访数",
            "ms_day_new_num": "秘书当天新建",
            "ts_day_new_num": "态势当天新建",
        })
    return columns

@login_required
@permission_required("sale.saler_kpi_month.export", login_url=URL_403)
def export_saler_kpi_month(request):
    file_type = request.GET.get("fileType")
    if not file_type:
        file_type = "csv"
    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 0 # 导出全部

    date = request.GET.get("date", None)
    fields = request.GET.get("fields", [])
    if fields:
        fields = fields.split(",")
    col_dict = get_saler_kpi_columns()
    
    filename = str(int(time.time())) + "_" + str(random.randint(10000, 100000)) + ".csv"

    temp_dir = os.path.join(os.path.abspath("."), "download")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    filepath = os.path.join(temp_dir, filename)

    istarshine_ids = get_can_see_istarshine_ids(request)
    result = get_saler_kpi_month(date=date, istarshine_ids=istarshine_ids)

    items = result["data"]
    df = pd.DataFrame(items, columns=list(col_dict.keys()))
    df.rename(columns=col_dict, inplace=True)
    # df = df.drop(["operations"], axis=1)
    df.to_csv(filepath, index=False, encoding="utf_8_sig")

    # 设置HTTPResponse的类型
    # 创建一个sheet对象
    with open(filepath, "rb") as f:
        content = f.read()

    response = HttpResponse(content_type='application/vnd.ms-csv', content=content)
    # 创建一个文件对象
    response['Content-Disposition'] = 'attachment;filename='+filename
    response['Content-Length'] = len(content)
    os.remove(filepath)

    user = request.user
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="商务管理-商务月度kpi统计", action="导出", message=message)

    return response
    

"""
商务历史kpi统计
"""
@login_required
@permission_required("sale.saler_kpi_month.view", login_url=URL_403)
def saler_kpi_history(request):
    istarshine_id = request.GET.get("istarshine_id", "")
    date = request.GET.get("date")
    title = "商务kpi查询"

    api = "/sale/saler/kpi/history/api"

    if request.user.has_perm("sale.saler_kpi_month.export"):
        can_export = 1

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务历史kpi统计页面", action="访问", message=message)

    if istarshine_id:
        if not date:
            date = arrow.now().format("YYYY-MM")
            redirect_url = "/sale/saler/kpi/history?istarshine_id={}&date={}".format(istarshine_id, date)
            return redirect(redirect_url)
        user = User.objects.filter(istarshine_id=istarshine_id).first()
        if user:
            # username = user.username
            # title += " - " + username
            return render(request, "sale/saler-kpi-history.html", locals())
    return render(request, "404.html", locals())

"""
商务历史kpi统计
"""
@permission_required("sale.saler_kpi_month.view", login_url=JSON_403)
def saler_kpi_history_api(request):
    istarshine_id = request.GET.get("istarshine_id")
    date = request.GET.get("date")

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务历史kpi统计页面api", action="查询", message=message)

    result = get_saler_kpi(history=True, date=date, istarshine_id=istarshine_id)
    return JsonResponse(result)

@login_required
@permission_required("sale.saler_kpi_month.export", login_url=URL_403)
def export_saler_kpi_history(request):
    istarshine_id = request.GET.get("istarshine_id")
    date = request.GET.get("date")
    result = get_saler_kpi(istarshine_id=istarshine_id, date=date, history=True)
    if result["code"] != 1:
        error = result["error"]
        return render(request, "404.html", locals())

    items = result["data"]
    file_type = request.GET.get("fileType")
    if not file_type:
        file_type = "csv"
    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 0 # 导出全部

    fields = request.GET.get("fields", [])
    if fields:
        fields = fields.split(",")
    col_dict = get_saler_kpi_columns(history=True)
    
    filename = str(int(time.time())) + "_" + str(random.randint(10000, 100000)) + ".csv"

    temp_dir = os.path.join(os.path.abspath("."), "download")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    filepath = os.path.join(temp_dir, filename)
    
    df = pd.DataFrame(items, columns=list(col_dict.keys()))
    df.rename(columns=col_dict, inplace=True)
    # df = df.drop(["operations"], axis=1)
    df.to_csv(filepath, index=False, encoding="utf_8_sig")

    # 设置HTTPResponse的类型
    # 创建一个sheet对象
    with open(filepath, "rb") as f:
        content = f.read()

    response = HttpResponse(content_type='application/vnd.ms-csv', content=content)
    # 创建一个文件对象
    response['Content-Disposition'] = 'attachment;filename='+filename
    response['Content-Length'] = len(content)
    os.remove(filepath)

    user = request.user
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="商务管理-商务历史kpi统计", action="导出", message=message)

    return response

@login_required
@permission_required("sale.saler_kpi_overview.view", login_url=URL_403)
def saler_kpi_overview(request):
    title = "商务kpi总览"

    api = "/sale/saler/kpi/overview/api"

    kws = request.GET
    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务kpi总览", action="访问", message=message)

    return render(request, "sale/saler-kpi-overview.html", locals())  

def get_kpi_overview_data(date=None, istarshine_ids=None, **kwargs):
    result = {"code": 0, "data": None, "error": ""}
    res = get_saler_kpi_month(date=date, istarshine_ids=istarshine_ids, **kwargs)
    if res["code"] == 1:
        ks = ["month_new_performance", "month_renew_performance", "month_performance",
            "month_head_confirm_money", "confirm_goal_rate", "month_complete_money",
            "month_call_num", "month_visit_num",
            "ms_month_active_num", "ms_month_new_num",
            "ts_month_active_num", "ts_month_new_num"
        ]
        def count(item, to):
            for k in ks:
                if not to.get(k):
                    to[k] = 0
                if item[k] == 0:
                    to[k] += 1
                    
        tableData = []
        tableData1 = defaultdict(int)
        tableData2 = defaultdict(int)
        tableData3 = defaultdict(int)
        tableData1["join_days"] = "三个月以内"
        tableData2["join_days"] = "三到六个月"
        tableData3["join_days"] = "六个月以上"

        items = res["data"]
        for item in items:
            if item["join_days"] <= 90:
                count(item, tableData1)
            elif item["join_days"] <= 180:
                count(item, tableData2)
            elif item["join_days"] > 180:
                count(item, tableData3)
        
        tableData.append(tableData1)
        tableData.append(tableData2)
        tableData.append(tableData3)
        result["data"] = tableData
        result["code"] = 1
        result["error"] = "查询成功"
    else:
        result["code"] = res["code"]
        result["error"] = res["error"]
    return result 

@permission_required("sale.saler_kpi_overview.view", login_url=JSON_403)
def saler_kpi_overview_api(request):
    date = request.GET.get("date", "")
    date = date.strip()

    kws = request.GET
    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务kpi总览api", action="查询", message=message)

    istarshine_ids = get_can_see_istarshine_ids(request)
    result = get_kpi_overview_data(date=date, istarshine_ids=istarshine_ids)
    return JsonResponse(result)