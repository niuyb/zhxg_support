import json
import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect
from mandala.auth import get_user_model
from mandala.auth.decorators import permission_required,login_required
from notice.models import NoticeType, NoticeSetting
from notice.forms import  NoticeSettingForm
from user_center.models import UserLog

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
# Create your views here.

logger = logging.getLogger("notice")
User = get_user_model()
@login_required()
@permission_required("notice.notice_setting.change",login_url=JSON_403)
def change_notice_setting(request):
    result = {"code": 0, "error": ""}
    if request.user.is_anonymous:
        result["error"] = "会话已过期，请重新登录"
        return JsonResponse(result)
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    ding_user_id = kws.get("ding_user_id")
    if not ding_user_id:
        ding_user_id = request.user.dtalkid
    if not request.user.is_superuser:
        if ding_user_id != request.user.dtalkid:
            result["error"] = "您没有权限"
            return JsonResponse(result)
    form = NoticeSettingForm(kws)
    if not form.is_valid():
        result["code"] = -1
        result["error"] = "参数错误"
        return JsonResponse(result)
    params = {"ding_user__dtalkid": ding_user_id, "notice_type_id": kws.get("notice_type_id")}
    ns = NoticeSetting.objects.filter(**params)
    if len(ns) > 0:
        ns.update(status=kws.get("status"))
    else:
        params = {"ding_user_id": ding_user_id, "notice_type_id": kws.get("notice_type_id"), "status": kws.get("status")}
        NoticeSetting.objects.create(**params)

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="通知管理-通知设置", action="修改", message=message)

    result["code"] = 1
    result["error"] = "设置成功"
    return JsonResponse(result)

def get_notice_setting_list(ding_user_id):
    notice_type_list = list(NoticeType.objects.all().values())
    nsl = list(NoticeSetting.objects.filter(ding_user__dtalkid=ding_user_id).values())
    notice_setting_dict = {ns["notice_type_id"]: ns for ns in nsl}
    notice_setting_list = []
    # fields = NoticeSetting._meta.fields
    for notice_type in notice_type_list:
        notice_type_id = notice_type["id"]
        ns = notice_setting_dict.get(notice_type_id)
        if not ns:
            ns = {"notice_type_id": notice_type_id, "status": 1, "ding_user_id": ding_user_id}
        for k, v in notice_type.items():
            if k != "id":
                ns[k] = v
        notice_setting_list.append(ns)
    result = {"code": 1, "data": notice_setting_list, "error": ""}
    return result

@login_required()
@permission_required("notice.notice_setting.view",login_url=JSON_403)
def notice_setting_list_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="通知管理-通知设置api", action="查询", message=message)

    result = {"code": 0, "data": None, "error": ""}
    if request.method != "GET":
        result["code"] = -1
        result["error"] = "错误的方法"
        return JsonResponse(result)
    ding_user_id = request.GET.get("ding_user_id")
    if ding_user_id:
        if not request.user.is_superuser:
            return redirect(request.path)
    if not ding_user_id:
        ding_user_id = request.user.dtalkid
    result = get_notice_setting_list(ding_user_id)
    return JsonResponse(result)

@login_required()
@permission_required("notice.notice_setting.view",login_url=URL_403)
def notice_settings(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="通知管理-通知设置", action="访问", message=message)

    title = "修改钉钉通知设置"
    return render(request, "notice/notice_settings.html", locals())

                