import json
import logging
import datetime

from mandala.auth.decorators import login_required,permission_required
from django.http import JsonResponse, HttpResponse,QueryDict
from django.shortcuts import render, redirect

from user_center.models import UserLog
from django.conf import settings
from support.settings import domain_support

URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("user_log")


"""产品管理-账号列表"""
@login_required()
@permission_required("product.accounts_manage.view", login_url=URL_403)
def accounts_list(request):
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="产品管理-账号列表", action="访问", message=message)
    title = "产品管理 - 账号列表"

    # 新建账号跳转链接，根据环境不同，设置不同的域名
    domain = domain_support
    href = "http://" + domain + ".istarshine.com/Newcustomer/adduserz"

    print(message)
    print("===========locals()", locals())

    return render(request, "product/accounts_list.html", locals())



"""舆情秘书-操作日志-总览"""
@login_required()
@permission_required("product.accounts_manage.view", login_url=URL_403)
def yqms_log_overview(request):
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="舆情秘书-操作日志-总览", action="访问", message=message)
    uid = request.GET.get("uid")
    account_name = str(request.GET.get("account_name"))

    title = "舆情秘书-操作日志：" + account_name

    return render(request, "product/yqms_log_overview.html", locals())


"""舆情秘书-操作日志-详情"""
@login_required()
@permission_required("product.accounts_manage.view", login_url=URL_403)
def yqms_log_detail(request):
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="舆情秘书-操作日志-详情", action="访问", message=message)
    uid = request.GET.get("uid")
    account_name = str(request.GET.get("account_name"))

    title = "舆情秘书-操作日志：" + account_name

    return render(request, "product/yqms_log_detail.html", locals())