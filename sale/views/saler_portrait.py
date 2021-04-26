import json
import logging

from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required
from django.forms import model_to_dict

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

from .index import get_data_customer
from customer.models import Department, User as CrmUser
from user_center.models import UserLog
# from public.utils import parse_kwargs_for_pymysql

logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

def get_data_work_daily(request):
    data = get_data_customer(request)
    date_list = data["day"]["date_list"]
    count = data["day"]["count"]
    legend_data = ["拜访总数", "签到拜访", "电话拜访"]
    option = {
        "title": {
            "text": ''
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [
            {
                "name": legend_data[0],
                "type": 'line',
                "stack": '总数',
                "data": count["all"]
            },
            {
                "name": legend_data[1],
                "type": 'bar',
                "stack": '电话拜访',
                "data": count["trial"]
            },
            {
                "name": legend_data[2],
                "type": 'bar',
                "stack": '签到拜访',
                "data": count["formal"]
            }
        ]
    }
    return JsonResponse(option)

@login_required
@permission_required("sale.saler_portrait.view", login_url=URL_403)
def saler_portrait(request):
    title = "商务画像"
    if request.method == "GET":

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="商务管理-商务画像", action="访问", message=message)

        uid = request.GET.get("uid")
        if not uid:
            uid = request.GET.get("sid")
            if uid:
                return redirect(reverse("sale:saler_portrait") + "?uid=%s"%uid)
        if not uid:
            uid = request.user.dtalkid
            return redirect(reverse("sale:saler_portrait") + "?uid=%s"%uid)
        return render(request, "sale/saler-portrait.html", locals())

@login_required
@permission_required("sale.saler_portrait.view", login_url=URL_403)
def saler_portrait1(request):
    title = "商务画像"
    return render(request, "sale/saler-portrait-1.html", locals())

@login_required
@permission_required("sale.saler_portrait.view", login_url=URL_403)
def saler_portrait2(request):
    title = '商务画像'
    return render(request, "sale/saler-portrait-2.html", locals())

@login_required
@permission_required("sale.saler_portrait.view", login_url=URL_403)
def saler_portrait3(request):
    title = '商务画像'
    return render(request, "sale/saler-portrait-3.html", locals())

def get_saler_info_by_dtalkid(dtalkid):
    info = {"code": 0, "data": None, "error": ""}
    user = User.objects.filter(dtalkid=dtalkid).first()
    if not user:
        info["code"] = -1
        info["error"] = "查无此人"
        return info
    saler = CrmUser.objects.filter(name=user.username).first()
    if not saler:
        info["code"] = -1
        info["error"] = "此人不是商务人员"
        return info
    depart = Department.objects.filter(id=saler.departid).first()
    user = model_to_dict(user)
    user["roles"] = []
    user["user_permissions"] = []
    # roles = user["roles"]
    # user["roles"] = []
    # for role in roles:
    #     role = model_to_dict(role)
    #     perms = role["permissions"]
    #     role["permissions"] = []
    #     for perm in perms:
    #         perm = model_to_dict(perm)
    #         role["permissions"].append(perm)
    #     user["roles"].append(role)
    saler = model_to_dict(saler)
    data = {}
    data["user"] = user
    data["saler"] = saler
    if depart:
        data["depart"] = model_to_dict(depart)
    info["code"] = 1
    info["data"] = data
    return info

def get_saler_info_by_dtalkid_or_istarshine_id(dtalkid=None, istarshine_id=None):
    info = {"code": 0, "data": None, "error": ""}
    if (not dtalkid) and (not istarshine_id):
        info["error"] = "参数错误"
        return info
    if dtalkid:
        user = User.objects.filter(dtalkid=dtalkid).first()
    else:
        user = User.objects.filter(istarshine_id=istarshine_id).first()
    if not user:
        info["code"] = -1
        info["error"] = "查无此人"
        return info
    saler = CrmUser.objects.filter(name=user.username).first()
    if not saler:
        info["code"] = -1
        info["error"] = "此人不是商务人员"
        return info
    depart = Department.objects.filter(id=saler.departid).first()
    user = model_to_dict(user)
    user["roles"] = []
    user["user_permissions"] = []
    # roles = user["roles"]
    # user["roles"] = []
    # for role in roles:
    #     role = model_to_dict(role)
    #     perms = role["permissions"]
    #     role["permissions"] = []
    #     for perm in perms:
    #         perm = model_to_dict(perm)
    #         role["permissions"].append(perm)
    #     user["roles"].append(role)
    saler = model_to_dict(saler)
    data = {}
    data["user"] = user
    data["saler"] = saler
    if depart:
        data["depart"] = model_to_dict(depart)
    info["code"] = 1
    info["data"] = data
    return info

@permission_required("sale.saler_portrait.view", login_url=JSON_403)
def saler_info_api(request):
    uid = request.GET.get("uid")
    istarshine_id = request.GET.get("istarshine_id")
    if (not uid) and (not istarshine_id):
        uid = request.user.dtalkid
    result = get_saler_info_by_dtalkid_or_istarshine_id(uid, istarshine_id)
    return JsonResponse(result)

