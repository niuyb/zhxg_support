import json
import logging

from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mandala.auth.decorators import login_required, permission_required

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

from user_center.models import UserLog
from secretary.models import DingGroupMemberMap, WkTDinggroup, UserGroupMap

logger = logging.getLogger("sale")

# # Create your views here.

"""画像模糊匹配，did是大区，就跳转大区画像，did是部门，就跳转部门画像""" 
# @permission_required("sale.view_department_portrait")
def fuzzy_portrait(request):
    did = request.GET.get("did")
    all_groups = {int(dpt.group_id): dpt for dpt in DingGroupMemberMap.objects.all()}
    g_center = all_groups.get(58062185)
    sub_group_ids = json.loads(g_center.sub_group_ids)
    sub_group_ids_all = json.loads(g_center.sub_group_ids_all)
    all_members = json.loads(g_center.member_ids_all)
    if did in all_members:
        return redirect(reverse("sale:saler_portrait") + "?uid=%s"%did)
    try:
        did = int(did)
    except:
        did = None
    if did not in sub_group_ids_all:
        return JsonResponse({"code": -1, "msg": "此部门不属于政务事业部-销售中心"})
    if did in sub_group_ids:
        # 判断，如果此部门是末端部门，即只有组员，没有下级部门，那么，直接跳转到部门画像。
        dpt = all_groups.get(did)
        if dpt:
            sub_ids = json.loads(dpt.sub_group_ids)
            if not sub_ids:
                return redirect(reverse("sale:department_portrait") + "?did=%s"%did)
        return redirect(reverse("sale:region_portrait") + "?did=%s"%did)
    return redirect(reverse("sale:department_portrait") + "?did=%s"%did)

"""政务事业部-销售中心：58062185"""   
@login_required 
@permission_required("sale.region_portrait.view", login_url=URL_403)
def region_portrait(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-大区画像", action="访问", message=message)

    did = request.GET.get("did")
    try:
        did = int(did)
    except:
        return JsonResponse({"code": -1, "msg": "参数错误"})
    _dids = request.user.dingframe.split(",")
    dids = json.loads(json.dumps(_dids))
    jss = DingGroupMemberMap.objects.filter(group_id__in=_dids).values_list("sub_group_ids_all", flat=True)
    for js in jss:
        dids.extend(json.loads(js))
    if not request.user.is_superuser:
        if (did not in dids) and (str(did) not in dids):
            return JsonResponse({"code": -1, "msg": "您无权查看"})
    all_groups = {int(dpt.group_id): dpt for dpt in DingGroupMemberMap.objects.all()}
    g_center = all_groups.get(58062185)
    sub_group_ids = json.loads(g_center.sub_group_ids)
    sub_group_ids_all = json.loads(g_center.sub_group_ids_all)
    try:
        did = int(did)
    except:
        did = None
    if not did:
        uid = request.user.dtalkid
        for group_id in sub_group_ids:
            member_ids_all = json.loads(all_groups.get(group_id).member_ids_all)
            if uid in member_ids_all:
                did = group_id
                break
        if not did:
            did = sub_group_ids[0]
        if did:
            return redirect(reverse("sale:region_portrait") + "?did=%s"%did)
    if did not in sub_group_ids:
        if did in sub_group_ids_all:
            return redirect(reverse("sale:department_portrait") + "?did=%s"%did)
        return JsonResponse({"code": -1, "msg": "此部门不属于政务事业部-销售中心"})
    title = "大区画像"
    return render(request, "sale/region-portrait.html", locals())

"""政务事业部-销售中心：58062185"""    
@login_required
@permission_required("sale.department_portrait.view", login_url=URL_403)
def department_portrait(request):
    title = "部门画像"

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商务管理-商务画像", action="访问", message=message)

    did = request.GET.get("did")
    try:
        did = int(did)
    except:
        return JsonResponse({"code": -1, "msg": "参数错误"})
    _dids = request.user.dingframe.split(",")
    dids = json.loads(json.dumps(_dids))
    jss = DingGroupMemberMap.objects.filter(group_id__in=_dids).values_list("sub_group_ids_all", flat=True)
    for js in jss:
        dids.extend(json.loads(js))
    if not request.user.is_superuser:
        if did not in dids:
            return JsonResponse({"code": -1, "msg": "您无权查看"})
    all_groups = {int(dpt.group_id): dpt for dpt in DingGroupMemberMap.objects.all()}
    g_center = all_groups.get(58062185)
    sub_group_ids = json.loads(g_center.sub_group_ids)
    sub_group_ids_all = json.loads(g_center.sub_group_ids_all)
    member_ids_all = json.loads(g_center.member_ids_all)
    try:
        did = int(did)
    except:
        did = None
    if did in sub_group_ids:
        dpt = all_groups.get(did)
        if dpt:
            sub_ids = json.loads(dpt.sub_group_ids)
            if sub_ids:
                return redirect(reverse("sale:region_portrait") + "?did=%s"%did)
    if not did:
        uid = request.user.dtalkid
        belong = False
        if uid in member_ids_all:
            belong = True

        for group_id in sub_group_ids:
            dpt = all_groups.get(group_id)
            if not dpt:
                continue
            sg_ids = json.loads(dpt.sub_group_ids)
            for sg_id in sg_ids:
                if not belong:
                    did = sg_id
                    break
                sg = all_groups.get(sg_id)
                if sg:
                    member_ids = json.loads(sg.member_ids)
                    if uid in member_ids:
                        did = sg_id
                        break
        if did:
            return redirect(reverse("sale:department_portrait") + "?did=%s"%did)
    if did not in sub_group_ids_all:
        return JsonResponse({"code": -1, "msg": "此部门不属于政务事业部-销售中心"})
    return render(request, "sale/department-portrait.html", locals())

"""政务事业部-销售中心：58062185"""     
@permission_required("sale.department_portrait.view", login_url=JSON_403)
def department_info_api(request):
    result = {"code": 0, "data": {}, "msg": ""}
    did = request.GET.get("did")
    try:
        did = int(did)
    except:
        did = None
    if not did:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    all_groups = {int(department.group_id): department for department in DingGroupMemberMap.objects.all()}
    g_center = all_groups.get(58062185)
    sub_group_ids_all = json.loads(g_center.sub_group_ids_all)
    
    if did not in sub_group_ids_all:
        result["code"] = -1
        result["msg"] = "此部门不属于政务事业部-销售中心"
        return JsonResponse(result)

    sub_group_ids = json.loads(g_center.sub_group_ids)

    department = all_groups.get(did)
    member_ids = json.loads(department.member_ids)
    sub_dpt_ids = json.loads(department.sub_group_ids)
    department = {"name": department.group_name, "did": department.group_id, "level": "", "manager": {}, "children":[]}
    if did in sub_group_ids:
        department["level"] = "1"
        sub_groups = [all_groups.get(group_id) for group_id in sub_dpt_ids]
        children = [{"name": group.group_name, "did": group.group_id, "value": group.group_id} for group in sub_groups]
        department["children"] = children
        manager = UserGroupMap.objects.filter(dgid=did, duposition="区域总经理").first()
        if manager:
            department["manager"]["name"] = manager.duname
            department["manager"]["uid"] = manager.duid
    else:
        department["level"] = "2"
        manager = UserGroupMap.objects.filter(dgid=did, duposition="省域总经理").first()
        if manager:
            department["manager"]["name"] = manager.duname
            department["manager"]["uid"] = manager.duid
        members = UserGroupMap.objects.filter(duid__in=member_ids)
        children = [{"name": member.duname, "uid": member.duid, "value": member.duid} for member in members]
        department["children"] = children
    result["code"] = 1
    result["data"]["department"] = department
    return JsonResponse(result)
