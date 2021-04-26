import json
import copy
import logging

from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render
from mandala.auth import get_user_model
from django.utils.decorators import method_decorator
from mandala.auth.decorators import  permission_required
from django.forms import model_to_dict
from django.views import generic

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

from mandala.auth.models import Permission, Module
from user_center.models import UserLog
from xman.views._module import _get_module_dict

logger = logging.getLogger("xman")
User = get_user_model()

def get_groups_permissions(self):
    perms = set()
    for group in self.groups.all():
        _perms = group.permissions.all()
        for perm in _perms:
            perms.add(perm)
    return list(perms)

User.get_groups_perms = get_groups_permissions

def _get_perm_tree(module_dict, parent=None, level=1, pure=True):
    tree = []
    for k in list(module_dict.keys()):
        module = module_dict.get(k, None)
        if module and (module.parent == parent):
            # mod = {"id": module.id, "name": module.name, "code": module.code, "icon": module.icon, "url": module.url, "children": [], "status": module.status, "rank": module.rank}
            mod = model_to_dict(module)
            mod["type"] = "module"
            if pure:
                # pop掉模块的id，防止出现叶节点模块被当成权限这种情况
                mod.pop("id")
            mod["level"] = level
            mod["children"] = []
            perms = module.permissions.all()
            for perm in perms:
                perm = model_to_dict(perm)
                perm["type"] = "permission"
                mod["children"].append(perm)
            module_dict.pop(k)
            if module_dict:
                mod["children"] += _get_perm_tree(module_dict, module, level+1, pure)
            tree.append(mod)
    return tree

def get_pure_perm_tree(request, status=None, show=None):
    module_dict = _get_module_dict(request, status, show)
    return _get_perm_tree(module_dict)


@permission_required('xman.perm.view', login_url=JSON_403)
def pure_perm_tree_api(request):
    perms = get_pure_perm_tree(request)
    result = {"code": 1, "error": "", "data": perms}
    return JsonResponse(result)

def get_perm_tree(request, status=None, show=None):
    module_dict = _get_module_dict(request, status, show)
    return _get_perm_tree(module_dict, pure=False)


@permission_required('xman.perm.view', login_url=JSON_403)
def perm_tree_api(request):
    perms = get_perm_tree(request)
    result = {"code": 1, "error": "", "data": perms}
    return JsonResponse(result)

@permission_required('xman.perm.view',login_url=URL_403)
def perm_tree(request):
    title = "权限管理"
    return render(request, "xman/perm-tree.html", locals())

def parse_perm_tree_to_list(perm_tree, module=None):
    perm_list = []
    if module is None:
        full_name = ""
    else:
        full_name = module["full_name"] + " | "
    for perm in perm_tree:
        if perm["type"] == "module":
            module_full_name = full_name + perm["name"]
            perm["full_name"] = module_full_name
            children = perm.pop("children")
            _perm_list = parse_perm_tree_to_list(children, perm)
            perm_list.extend(_perm_list)
        else:
            perm["module"] = module
            perm_list.append(perm)
    return perm_list

def get_perm_list(request, status=None, show=None):
    result = {"code": 0, "data": None, "error": ""}
    perm_tree = get_perm_tree(request)
    perm_list = parse_perm_tree_to_list(perm_tree)
    result["code"] = 1
    result["data"] = perm_list
    return result

@permission_required("xman.perm.view", login_url=JSON_403)
def perm_list_api(request):
    # result = get_perm_list()
    result = get_perm_list(request)

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="系统管理-权限管理-权限列表api", action="查询", message=message)

    return JsonResponse(result)

def get_perm_info(pid):
    user_fields = ["id", "username"]

    result = {"code": 0, "data": None, "error": ""}
    perm = Permission.objects.filter(pk=pid).first()
    if not perm:
        result["code"] = -1
        result["error"] = "权限不存在"
        return result

    module = model_to_dict(perm.module)
    perm_info = model_to_dict(perm)
    users = list(perm.users.all().values(*user_fields))
    roles = list(perm.roles.all().values())
    perm_info["users"] = users
    perm_info["roles"] = roles
    perm_info["module"] = module
    result["code"] = 1
    result["data"] = perm_info
    return result

@permission_required("xman.perm.view", login_url=JSON_403)
def perm_info_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="系统管理-权限管理-权限详情api", action="查询", message=message)

    pid = request.GET.get("id")
    result = get_perm_info(pid)
    return JsonResponse(result)

class PermListView(generic.View):

    @method_decorator(permission_required("xman.perm.view",login_url=URL_403))
    def get(self, request):
        rand = request.GET.get("rand")
        if rand:

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-权限管理-权限列表api", action="查询", message=message)

            result = get_perm_list(request)
            return JsonResponse(result)
        else:
            title = "权限管理"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-权限管理-权限列表", action="访问", message=message)

            return render(request, "xman/perm-list.html", locals())


    @method_decorator(permission_required("xman.perm.delete", login_url=JSON_403))
    def delete(self, request):
        result = {"code": 0, "data": None, "error": ""}
        pids = request.GET.get("pids")

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-权限管理-权限列表", action="删除", message=message)

        if pids:
            pids = pids.strip().split(",")
        if pids:
            try:
                Permission.objects.filter(pk__in=pids).delete()
                result["code"] = 1
                result["error"] = "删除成功"
            except Exception as e:
                result["code"] = -1
                result["error"] = "删除失败，原因：%s"%str(e)
        else:
            result["error"] = "参数错误"
        return JsonResponse(result)


class PermView(generic.View):

    template_name = "xman/perm.html"
    template_404 = "404.html"

    fields = {'id': None, 'name': "", 'code': "", 'rank': 0, 'status': 1, 'module': 0}

    def _parse(self, kws):
        params = {k: kws.get(k, v) for k, v in self.fields.items()}
        return params

    @method_decorator(permission_required("xman.perm.view",login_url=URL_403))
    def get(self, request):
        pid = request.GET.get("id")
        if pid:
            title = "修改权限"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-权限管理-修改权限页面", action="访问", message=message)

            perm = Permission.objects.filter(pk=pid).first()
            if not perm:
                error = ""
                message = "新建权限"
                redirect_url = "/xman/perm"
                return render(request, self.template_404, 
                        {"error": error, "message": message, "redirect_url": redirect_url})
        else:
            title = "新建权限"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-权限管理-新建权限页面", action="访问", message=message)

        return render(request, self.template_name, {"title": title})

    @method_decorator(permission_required("xman.perm.add", login_url=JSON_403))
    def post(self, request):  

        message = json.dumps(dict(request.POST))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-权限管理-新建权限", action="添加", message=message)
  
        _params = self._parse(request.POST)
        result = {"code": 0, "data": _params, "error": ""}
        params = copy.deepcopy(_params)
        Id = params.pop("id")
        if Id:
            result["code"] = -1
            result["error"] = "参数错误"
            return JsonResponse(result)
        module = None
        module_id = params.pop("module")
        if module_id:
            module = Module.objects.filter(pk=module_id).first()
        if not module:
            result["error"] = "无法找到模块"
            return JsonResponse(result)
        try:
            perm = Permission.objects.create(module=module, **params)
            result["code"] = 1
            result["data"] = model_to_dict(perm)
            result["error"] = "权限创建成功"
        except Exception as e:
            result["code"] = -1
            result["error"] = "权限创建失败，原因：" + str(e)
        return JsonResponse(result)

    @method_decorator(permission_required("xman.perm.change", login_url=JSON_403))
    def put(self, request): 
        kws = QueryDict(request.body)   

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-权限管理-修改权限", action="修改", message=message)

        _params = self._parse(kws)
        result = {"code": 0, "data": _params, "error": ""}
        params = copy.deepcopy(_params)
        Id = params.pop("id")
        if not Id:
            result["error"] = "参数错误"
            return JsonResponse(result)
        params.pop("module")
        perms = Permission.objects.filter(pk=Id)
        try:
            perms.update(**params)
            result["code"] = 1
            result["error"] = "权限更新成功"
        except Exception as e:
            result["code"] = -1
            result["error"] = "权限更新失败，原因：" + str(e)
        return JsonResponse(result)

    # 主要是修改status时用
    @method_decorator(permission_required("xman.perm.change", login_url=JSON_403))
    def patch(self, request):

        kws = QueryDict(request.body)   
        result = {"code": 0, "data": None, "error": ""}

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-权限管理-修改权限状态", action="修改", message=message)
        
        pid = kws.get("id");
        status = kws.get("status")
        if not pid or not status:
            result["error"] = "修改失败，原因：参数错误"
            return JsonResponse(result)
        try:
            perms = Permission.objects.filter(pk=pid)
            if len(perms) > 0:
                perms.update(status=status)
                result["code"] = 1
                result["error"] = "状态修改成功"
            else:
                result["error"] = "状态修改失败，原因：未找到相应权限"
        except Exception as e:
            result["code"] = -1
            result["error"] = "状态修改失败，原因：%s"%str(e)

        return JsonResponse(result) 

    @method_decorator(permission_required("xman.perm.delete", login_url=JSON_403))
    def delete(self, request): 
        kws = request.GET   

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-权限管理-删除权限", action="删除", message=message)

        _params = self._parse(kws)
        result = {"code": 0, "data": _params, "error": ""}
        params = copy.deepcopy(_params)
        Id = params.pop("id")
        if not Id:
            result["error"] = "参数错误"
            return JsonResponse(result)
        try:
            Permission.objects.filter(pk=Id).delete()
            result["code"] = 1
            result["error"] = "权限成功删除"
        except Exception as e:
            result["code"] = -1
            result["error"] = "权限删除失败，原因：" + str(e)
        return JsonResponse(result)
