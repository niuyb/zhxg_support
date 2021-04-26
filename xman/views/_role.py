import json
import logging
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import generic
from django.shortcuts import render
from mandala.auth import get_user_model
from django.utils.decorators import method_decorator
from mandala.auth.decorators import login_required, permission_required
from django.forms import model_to_dict

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

from mandala.auth.models import Role, Permission
from user_center.models import UserLog

logger = logging.getLogger("xman")
User = get_user_model()

def get_role_list():
    result = {"code": 0, "data": None, "error": ""}
    data = list(Role.objects.all().values())
    result["code"] = 1
    result["data"] = data
    return result

class RoleListView(generic.View):
    @method_decorator(permission_required("xman.role.view", login_url=URL_403))
    def get(self, request):
        rand = request.GET.get("rand")
        if not rand:
            title = "角色管理"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-角色管理-角色列表", action="访问", message=message)

            return render(request, "xman/role-list.html", locals())
        else:

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-角色管理-角色列表api", action="查询", message=message)

            return JsonResponse(get_role_list())

    @method_decorator(permission_required("xman.role.change", login_url=JSON_403))
    def patch(self, request):
        result = {"code": 0, "data": None, "error": ""}
        kws = QueryDict(request.body)

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-角色管理-角色列表", action="批量配权", message=message)

        rids = kws.get("rids")
        if rids:
            rids = rids.replace(" ", "").split(",")
        pids = kws.get("pids")
        if pids:
            pids = pids.replace(" ", "").split(",")

        if not rids or not pids:
            result["error"] = "参数错误"
            return JsonResponse(result)

        roles = Role.objects.filter(pk__in=rids)
        perms = list(Permission.objects.filter(pk__in=pids))
        rl = len(roles)
        pl = len(perms)
        if not rl or not pl:
            result["error"] = "没有查到相关角色或者权限"
            return JsonResponse(result)
        for role in roles:
            role.permissions.add(*perms)
        result["error"] = "操作成功"
        result["code"] = 1
        return JsonResponse(result)

    @method_decorator(permission_required("xman.role.delete", login_url=JSON_403))
    def delete(self, request):
        kws = request.GET
        result = {"code": 0, "data": None, "error": ""}

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-角色管理-角色列表", action="批量删除", message=message)

        rids = kws.get("rids")
        if rids:
            rids = rids.strip().replace(" ", "").split(",")
        if not rids:
            result["error"] = "参数错误"
            return JsonResponse(result)
        try:
            Role.objects.filter(pk__in=rids).delete()
            result["code"] = 1
            result["error"] = "操作成功"
        except Exception as e:
            result["error"] = "操作失败，原因：%s"%str(e)
        return JsonResponse(result)


def get_role_info(rid):
    user_fields = ["id", "username"]
    result = {"code": 0, "data": None, "error": ""}
    try:
        role = Role.objects.filter(pk=rid).first()
    except Exception as e:
        logger.error("get_role_info error: %s"%e)
        result["code"] = -1
        result["error"] = "服务器繁忙，请稍后重试"
        return result
    if role:
        role_info = model_to_dict(role)

        result["data"] = role_info
        users = list(role.users.all().values(*user_fields))
        uids = [user["id"] for user in users]
        result["data"]["uids"] = uids
        result["data"]["users"] = users

        permissions = list(role.permissions.all().values())
        pids = [p["id"] for p in permissions]
        result["data"]["pids"] = pids
        result["data"]["permissions"] = permissions
        result["code"] = 1
        result["error"] = "角色信息获取成功"
    else:
        result["error"] = "此角色不存在"
    return result

@permission_required("auth.view_role",login_url=URL_403)
def role_detail(request):
    rid = request.GET.get("id")
    role = None
    if rid:
        role = Role.objects.filter(pk=rid).first()
    if role:
        title = "修改角色"
        mode = "change"

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-角色管理-角色详情", action="访问", message=message)

        return render(request, "xman/role.html", locals())
    title = "新建角色"
    mode = "add"
    return render(request, "xman/role.html", locals())

class RoleView(generic.View):

    @method_decorator(permission_required("xman.role.view",login_url=URL_403))
    def get(self, request):
        kws = request.GET
        rid = kws.get("id")
        if not rid:
            title = "新建角色"
            mode = "add"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-角色管理-角色详情", action="访问", message=message)

            return render(request, "xman/role.html", locals())
        else:

            message = json.dumps(dict(kws))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-角色管理-角色详情api", action="查询", message=message)
            result = get_role_info(rid)
            return JsonResponse(result)

    @method_decorator(permission_required("xman.role.add", login_url=JSON_403))
    def post(self, request):
        result = {"code": 0, "data": None, "error": ""}
        name = request.POST.get("name")
        code = request.POST.get("code")
        rank = request.POST.get("rank", 0)
        status = request.POST.get("status", 0)

        pids = request.POST.get("pids", "")
        if not pids:
            pids = []
        else:
            pids = pids.split(",")

        result["data"] = {"name": name, "code": code, "rank": rank, "status": status, "pids": pids}
        
        gc = Role.objects.filter(name=name).count()
        if not name:
            result["code"] = -1
            result["error"] = "名称不能为空"
            return JsonResponse(result)
        if gc > 0:
            result["error"] = "名称为'%s'的角色已经存在，请更换名称"%name
            return JsonResponse(result)
        ps = None
        if pids:
            ps = list(Permission.objects.filter(pk__in=pids))
            if not ps:
                result["error"] = "权限不存在"
                return JsonResponse(result)
        try:
            role = Role(name=name, code=code, rank=rank, status=status)
            role.save()
        except Exception as e:
            logger.error("add_role: %s"%e)
            result["code"] = -1
            result["error"] = str(e)
            return JsonResponse(result)
        result["data"] = model_to_dict(role)
        result["code"] = 1
        result["error"] = "成功创建'%s'角色"%name

        message = json.dumps(dict(request.POST))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-角色管理", action="添加", message=message)

        if ps:
            try:
                role.permissions.set(ps)
            except Exception as e:
                logger.error("add_role: %s"%e)
                result["code"] = -1
                result["error"] = str(e)
                try:
                    role.delete()
                except Exception as e:
                    logger.error("add_role: %s"%e)
        return JsonResponse(result)

    @method_decorator(permission_required("xman.role.change", login_url=JSON_403))
    def put(self, request):
        kws = QueryDict(request.body)
        result = {"code": 0, "data": None, "error": ""}
        rid = kws.get("id")
        name = kws.get("name")
        code = kws.get("code")
        rank = kws.get("rank")
        status = kws.get("status")

        pids = kws.get("pids")
        if pids:
            pids = pids.split(",")
        else:
            pids = []
        result["data"] = {"id": rid, "name": name, "code": code, "rank": rank, "status": status, "pids": pids}
        if not rid or not name:
            result["error"] = "参数错误"
            result["code"] = -1
            return JsonResponse(result)
        r1 = Role.objects.filter(pk=rid).first()
        if not r1:
            result["error"] = "找不到此角色"
            return JsonResponse(result)
        r2 = Role.objects.filter(name=name).exclude(pk=rid).first()
        if r2:
            result["error"] = '名称为"%s"的角色已经存在，请更换角色名称'%name
            return JsonResponse(result)
        r3 = Role.objects.filter(code=code).exclude(pk=rid).first()
        if r3:
            result["error"] = '代码为"%s"的角色已经存在，请更换角色名称'%code
            return JsonResponse(result)

        ps = None
        if pids:
            ps = list(Permission.objects.filter(pk__in=pids))
            if not ps:
                result["error"] = "所选权限不存在"
                return JsonResponse(result)
        try:
            if ps:
                r1.permissions.set(ps)
            else:
                r1.permissions.clear()
            r1.name = name
            r1.code = code
            r1.rank = rank
            r1.status = status

            r1.save()
            result["code"] = 1
            result["error"] = "角色信息修改成功"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-角色管理", action="修改", message=message)

        except Exception as e:
            logger.error("change_role: %s"%e)
            result["code"] = -1
            result["error"] = "角色信息修改失败"
        return JsonResponse(result)

    @method_decorator(permission_required("xman.role.change", login_url=JSON_403))
    def patch(self, request):
        result = {"code": 0, "data": None, "error": ""}
        kws = QueryDict(request.body)
        rid = kws.get("id")
        status = kws.get("status")
        if (rid is None) or (status is None):
            result["error"] = "参数错误"
            return JsonResponse(result)
        roles = Role.objects.filter(pk=rid)
        if len(roles) == 0:
            result["error"] = "找不到相应角色"
            return JsonResponse(result)
        try:
            roles.update(status=status)
            result["code"] = 1
            result["error"] = "操作成功"
        except Exception as e:
            result["code"] = -1
            result["error"] = "操作失败，原因：%s"%str(e)
        return JsonResponse(result)

    @method_decorator(permission_required("xman.role.delete", login_url=JSON_403))
    def delete(self, request):

        result = {"code": 0, "data": None, "error": ""}
        rid = request.GET.get("id")
        if not rid:
            result["code"] = -1
            result["error"] = "参数错误"
            return JsonResponse(result)
        role = Role.objects.filter(pk=rid).first()
        if not role:
            result["error"] = "此角色不存在"
            return JsonResponse(result)
        result["data"] = model_to_dict(role)
        result["data"].pop("permissions")
        try:
            role.permissions.clear()
            role.delete()
            result["code"] = 1
            result["error"] = "成功删除此角色"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-角色管理", action="删除", message=message)

        except Exception as e:
            logger.error("delete_role: %s"%e)
            result["code"] = -1
            result["error"] = "删除失败：%s"%e
        return JsonResponse(result)
        