import json

from django.shortcuts import render, redirect
from mandala.auth import get_user_model
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import generic
from django.forms import model_to_dict

# Create your views here.
from django.utils.decorators import method_decorator
from mandala.auth.decorators import login_required, permission_required
from mandala.auth.models import Module, Permission
from user_center.models import UserLog
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

User = get_user_model()

def _get_module_dict(request, status=None, show=None):
    """
    status: None, True, False   None means all
    show: None, True, False   None means all
    """
    module_dict = {}

    modules = Module.objects.all()
    for module in modules:
        if status is not None:
            if module.status != status:
                continue

        if show is not None:
            perm = module.code + ".show"
            if request.user.has_perm(perm) != show:
                continue

        module_dict[module.id] = module
    return module_dict


def _get_module_tree(module_dict, parent=None, level=1, with_perms=False):
    tree = []
    for k in list(module_dict.keys()):
        module = module_dict.get(k, None)
        if module and (module.parent == parent):
            # mod = {"id": module.id, "name": module.name, "code": module.code, "icon": module.icon, "url": module.url, "children": [], "status": module.status, "rank": module.rank}
            mod = model_to_dict(module)
            mod["level"] = level
            mod["children"] = []
            if with_perms:
                perms = module.permissions.all()
                for perm in perms:
                    mod["children"].append(model_to_dict(perm))
            module_dict.pop(k)
            if module_dict:
                mod["children"] += _get_module_tree(module_dict, module, level+1, with_perms)
            tree.append(mod)
    return tree

def get_module_tree(request, status=None, show=None):
    module_dict = _get_module_dict(request, status, show)
    return _get_module_tree(module_dict)

# @permission_required('xman.module.view')
def module_tree_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="????????????-????????????-?????????api", action="??????", message=message)

    modules = get_module_tree(request, status=True, show=True)
    result = {"code": 1, "error": "", "data": modules}
    return JsonResponse(result)

@permission_required('xman.module.view', login_url=JSON_403)
def module_tree_all_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="????????????-????????????-?????????api???", action="??????", message=message)

    modules = get_module_tree(request, None, None)
    result = {"code": 1, "error": "", "data": modules}
    return JsonResponse(result)

@login_required
@permission_required('xman.module.view',login_url=URL_403)
def module_tree(request):
    title = "????????????"

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="????????????-????????????-???????????????", action="??????", message=message)

    return render(request, 'xman/module-tree.html', locals())

@permission_required('xman.module.view', login_url=JSON_403)
def module_list_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="????????????-????????????-????????????api", action="??????", message=message)

    result = {"code": 0, "data": None, "error": ""}
    ms = Module.objects.all()
    ml = []
    for m in ms:
        m = model_to_dict(m)
        ml.append(m)
    result["code"] = 1
    result["data"] = ml
    return JsonResponse(result)

def get_module_info(mid):
    result = {"code": 0, "data": None, "error": ""}
    try:
        module = Module.objects.filter(pk=mid).first()
    except Exception as e:
        module = None
        result["error"] = str(e)
    if module:
        permissions = list(module.permissions.all().values())
        data = model_to_dict(module)
        data["permissions"] = permissions
        result["code"] = 1
        result["data"] = data
    return result

@permission_required('xman.module.view', login_url=JSON_403)
def module_info_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="????????????-????????????-????????????api", action="??????", message=message)

    mid = request.GET.get("id")
    module_info = get_module_info(mid)
    return JsonResponse(module_info)

@permission_required('xman.module.view', login_url=JSON_403)
def module_permissions_list_api(request):
    result = {"code": 0, "data": None, "error": ""}
    ms = Module.objects.all()
    ml = []
    for m in ms:
        pl = [model_to_dict(p) for p in m.permissions.all()]
        m = model_to_dict(m)
        m["permissions"] = pl
        ml.append(m)
    result["code"] = 1
    result["data"] = ml
    return JsonResponse(result)

@login_required
@permission_required('xman.module.view',login_url=URL_403)
def module_list(request):
    title="????????????"

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="????????????-????????????-??????????????????", action="??????", message=message)

    return render(request, 'xman/module-list.html', locals())

class ModuleView(generic.View):
    template = "xman/module.html"
    template_404 = "404.html"

    @method_decorator(login_required)
    @method_decorator(permission_required("xman.module.view",login_url=URL_403))
    def get(self, request):
        mid = request.GET.get("id")
        if mid:
            title = "????????????"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="????????????-????????????-??????????????????", action="??????", message=message)

            mc = Module.objects.filter(pk=mid).count()
            if not mc:
                error = ""
                message = "????????????"
                redirect_url = "/xman/module"
                return render(request, self.template_404, 
                        {"error": error, "message": message, "redirect_url": redirect_url})
        else:
            title = "????????????"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="????????????-????????????-??????????????????", action="??????", message=message)

        return render(request, self.template, locals())

    def change_or_create(self, request, kws):
        mid = kws.get("id")
        name = kws.get("name")
        code = kws.get("code")
        status = kws.get("status", 0)
        rank = kws.get("rank")
        icon = kws.get("icon")
        url = kws.get("url")
        parent_id = kws.get("parent")
        ps = kws.get("perms")
        perms = []
        if ps:
            try:
                perms = json.loads(ps)
            except:
                pass
        data = {
            "id": mid, "name": name, "code": code, "status": status, "rank": rank, 
            "icon": icon, "url": url, "parent": parent_id, "perms": ps
        }

        result = {"code": 0, "error": "", "data": data}

        parent = None
        if parent_id and (parent_id != "0"):
            parent = Module.objects.filter(pk=parent_id).first()
            if not parent:
                result["code"] = -1
                result["error"] = "??????????????????"
                return JsonResponse(result)
        if mid:
            ms = Module.objects.filter(pk=mid)
            try:
                ms.update(name=name, code=code, status=status, rank=rank, icon=icon, url=url, parent=parent)
            except Exception as e:
                result["code"] = -1
                result["error"] = "??????????????????????????????" + str(e)
                return JsonResponse(result)
            result["error"] = "??????????????????"
        else:
            try:
                m = Module.objects.create(name=name, code=code, status=status, rank=rank, icon=icon, url=url, parent=parent)
            except Exception as e:
                result["code"] = -1
                result["error"] = "??????????????????????????????" + str(e)
                return JsonResponse(result)
            for perm in perms:
                name = perm.get("name")
                code = perm.get("code")
                if not name or not code:
                    continue

                status = perm.get("status", True)
                rank = perm.get("rank", 0)

                perm = Permission.objects.create(name=name, code=code, status=status, rank=rank, module=m)
            result["data"]["id"] = m.id
            result["error"] = "??????????????????"
        result["code"] = 1
        return JsonResponse(result)

    @method_decorator(permission_required("xman.module.change", login_url=JSON_403))
    def put(self, request):
        kws = QueryDict(request.body)
        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="????????????-????????????-????????????", action="??????", message=message)

        return self.change_or_create(request, kws)

    @method_decorator(permission_required("xman.module.add", login_url=JSON_403))
    def post(self, request):
        kws = request.POST 

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="????????????-????????????-????????????", action="??????", message=message)

        return self.change_or_create(request, kws)

    @method_decorator(permission_required("xman.module.change", login_url=JSON_403))
    def patch(self, request):
        kws = QueryDict(request.body)
        mid = kws.get("id")
        status = kws.get("status")
        data = {"id": mid, "status": status}

        message = json.dumps(dict(data))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="????????????-????????????-????????????", action="??????", message=message)

        result = {"code": 0, "error": "", "data": data}
        if not mid or not status:
            result["error"] = "????????????"
            return JsonResponse(result)
        try:
            modules = Module.objects.filter(pk=mid)
            if len(modules) == 0:
                result["error"] = "?????????????????????"
            else:
                modules.update(status=status)
                result["code"] = 1
                result["error"] = "??????????????????"
        except Exception as e:
            result["code"] = -1
            result["error"] = "????????????????????????%s"%str(e)
        return JsonResponse(result)

    @method_decorator(permission_required("xman.module.delete", login_url=JSON_403))
    def delete(self, request):
        result = {"code": 0, "data": None, "error": ""}
        kws = request.GET 

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="????????????-????????????-????????????", action="??????", message=message)

        mid = kws.get("id")
        if mid:
            try:
                modules = Module.objects.filter(pk=mid)
                if len(modules) == 0:
                    result["error"] = "?????????????????????"
                    return JsonResponse(result)

                modules.delete()
                result["code"] = 1
                result["error"] = "??????????????????"
            except Exception as e:
                result["code"] = -1
                result["error"] = "????????????????????????%s"%str(e)
        else:
            result["error"] = "????????????"
        return JsonResponse(result)