import json
import logging

import pymysql
from django.http import JsonResponse
from django.shortcuts import render, redirect
from mandala.auth.decorators import login_required, permission_required

from user_center.models import UserLog
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("sale")

# # Create your views here.

"""钉钉 - 政务事业部 - 销售中心"""
@login_required
@permission_required("sale.government_center.view", login_url=URL_403)
def dingding_government_center(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-政务中心", action="访问", message=message)

    title = "政务事业部 - 销售中心"
    g_center_did = "58062185"
    did = request.GET.get("did")
    if did != g_center_did:
        path = request.path + "?did=" + g_center_did
        return redirect(path)
    # return render(request, "sale/g-center-table.html", locals())
    return render(request, "sale/g-center.html", locals())


"""钉钉 - 政务事业部 - 销售中心"""
@login_required
@permission_required("sale.government_center.view",login_url=URL_403)
def dingding_government_center_table(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-政务事业部-销售中心table", action="访问", message=message)

    title = "政务事业部 - 销售中心"
    g_center_did = "58062185"
    did = request.GET.get("did")
    if did != g_center_did:
        path = request.path + "?did=" + g_center_did
        return redirect(path)
    return render(request, "sale/g-center-table.html", locals())


"""钉钉 - 政务事业部 - 销售中心"""
@login_required
@permission_required("sale-government_center.view",login_url=URL_403)
def dingding_government_center_tab(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-政务事业部-销售中心tab", action="访问", message=message)

    title = "政务事业部 - 销售中心"
    g_center_did = "58062185"
    did = request.GET.get("did")
    if did != g_center_did:
        path = request.path + "?did=" + g_center_did
        return redirect(path)
    return render(request, "sale/g-center-tab.html", locals())


