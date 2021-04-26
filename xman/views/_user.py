import json
import arrow
import logging
import pandas as pd

from django.http import  JsonResponse, QueryDict
from django.views import generic
from django.shortcuts import render
from mandala.auth import get_user_model
from mandala.auth.models import Role, Permission
from django.utils.decorators import method_decorator
from mandala.auth.decorators import  permission_required
from django.forms import model_to_dict
from public.utils import engine
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

from xman.forms import UserNewForm, UserChangeForm
from xman.models import UserRoleMapping, UserPermissionMapping
from user_center.models import UserLog
from salerVisit.utils import get_department

logger = logging.getLogger("xman")
User = get_user_model()

def get_user_list(**kwargs):
    result = {"code": 0, "data": None, "error": ""}
    data = list(User.objects.filter(**kwargs).values('id', 'dtalkid', 'last_login', 'is_superuser', 'username', 
            'email', 'is_staff', 'is_active', 'date_joined', 'mobile', 
            'status', 'dingframe', 'position', 'istarshine_id'))#'avatar', 'id', 
    dt = []
    for user in data:
        dj = user['date_joined']
        ll = user['last_login']
        if dj:
            try:
                dj = arrow.get(dj)
                dj = dj.strftime("%Y-%m-%d %H:%M:%S")
            except:
                dj = str(dj)
        else:
            dj = ""
        if ll:
            try:
                ll = arrow.get(ll)
                ll = ll.strftime("%Y-%m-%d %H:%M:%S")
            except Exception as e:
                logger.error(e)
                ll = str(ll)
        else:
            ll = ""
        user['date_joined'] = dj
        user['last_login'] = ll
        dt.append(user)

    result["data"] = dt
    if len(dt) > 0:
        result["code"] = 1
        result["error"] = "成功获取数据"
    else:
        result["error"] = "未获取到符合条件的数据"
    return result

def get_all_departments():
    # dpt_list = Department.objects.all().values_list("did", "name")
    # dpt_dict = {str(k): v for k, v in dpt_list}
    # return dpt_dict
    return {}

def get_department_names(did_str, dpt_dict):
    dids = did_str.strip().split(",")
    dpts = []
    for did in dids:
        name = dpt_dict.get(did)
        if name:
            dpts.append(name)
    return ",".join(dpts)

def get_user_info_list(**kwargs):
    # 默认排除掉离职人员, status=2是离职人员
    result = get_user_list(**kwargs)
    if result["code"] != 1:
        return result
    user_list = result["data"]
    df = pd.DataFrame(user_list)

    urm = list(UserRoleMapping.objects.all().values())
    role_list = list(Role.objects.all().values_list("id", "name"))
    # rdf = pd.DataFrame(role_list)
    role_dict = dict(role_list)
    ur_dict = {}
    for ur in urm:
        user_id = ur["user_id"]
        role_id = ur["role_id"]
        name = role_dict.get(role_id, "")
        if not ur_dict.get(user_id):
            ur_dict[user_id] = {"user_id": user_id, "role_names": []}
        if name:
            ur_dict[user_id]["role_names"].append(name)

    ur_list = [{"user_id": item["user_id"], "role_names": ",".join(item["role_names"])} for item in ur_dict.values()]
    if not ur_list:
        ur_list = [{"user_id": 0, "role_names": ""}]

    urdf = pd.DataFrame(ur_list)

    upm = list(UserPermissionMapping.objects.all().values())
    perm_list = list(Permission.objects.all().values_list("id", "name"))
    perm_dict = dict(perm_list)
    up_dict = {}
    for up in upm:
        user_id = up["user_id"]
        perm_id = up["permission_id"]
        name = perm_dict.get(perm_id, "")
        if not up_dict.get(user_id):
            up_dict[user_id] = {"user_id": user_id, "permission_names": []}
        if name:
            up_dict[user_id]["permission_names"].append(name)

    up_list = [{"user_id": item["user_id"], "permission_names": ",".join(item["permission_names"])} for item in up_dict.values()]
    if not up_list:
        up_list = [{"user_id": 0, "permission_names": ""}]

    updf = pd.DataFrame(up_list)

    dpt_df = get_department([])
    df = pd.merge(df,dpt_df,how='left',on='dingframe')

    df = pd.merge(df, urdf, how="left", left_on="id", right_on="user_id")
    df = df.drop(["user_id"], axis=1)

    df = pd.merge(df, updf, how="left", left_on="id", right_on="user_id")
    df = df.drop(["user_id"], axis=1)
    df = df.fillna("")
    user_list = list(df.to_dict(orient="index").values())
    result["data"] = user_list
    return result


class UserListView(generic.View):
    # def get_user_info_list(self, **kwargs):
    #     result = {"code": 0, "data": None, "error": ""}
    #     user_list = get_user_list(**kwargs)
    #     for user in user_list:
    #         user_info["roles"] = ",".join(user.roles.values_list("name", flat=True))
    #         user_info["perms"] = ",".join(user.user_permissions.values_list("name", flat=True))
    #     result["data"] = user_list
    #     result["error"] = "查询成功"
    #     return result

    @method_decorator(permission_required("xman.user.view", login_url=URL_403))
    def get(self, request):
        rand = request.GET.get("rand")
        status = request.GET.get("status")
        params = {}
        if status:
            params["status__in"] = status.strip().split(",")
        if rand:

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-用户管理-用户列表api", action="查询", message=message)

            # result = self.get_user_info_list()
            # result = get_user_list()
            result = get_user_info_list(**params)
            return JsonResponse(result)

        title = "用户列表"

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-用户管理-用户列表", action="访问", message=message)

        return render(request, "xman/user-list.html", locals())


    @method_decorator(permission_required("xman.user.change", login_url=JSON_403))
    def patch(self, request):
        result = {"code": 0, "data": None, "error": "操作失败，原因："}
        kws = QueryDict(request.body)

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-用户管理-用户列表", action="修改", message=message)

        uids = kws.get("uids")
        if uids:
            uids = uids.replace(" ", "").split(",")
        rids = kws.get("rids")
        if rids:
            rids = rids.replace(" ", "").split(",")
        pids = kws.get("pids")
        if pids:
            pids = pids.replace(" ", "").split(",")

        role_type = kws.get("role_type")

        if not (uids and (rids or pids)):
            result["error"] = "操作失败，原因：参数错误"
            return JsonResponse(result)

        users = User.objects.filter(pk__in=uids)
        roles = []
        perms = []
        if len(users) > 0:
            if rids:
                roles = list(Role.objects.filter(pk__in=rids))
            if pids:
                perms = list(Permission.objects.filter(pk__in=pids))
            rl = len(roles)
            pl = len(perms)

            if rl or pl:
                # 加权限
                if role_type == "1":
                    for user in users:
                        if rl:
                            user.roles.add(*list(roles))
                        if pl:
                            user.user_permissions.add(*list(perms))
                # 减权限
                elif role_type == "2":
                    for user in users:
                        if rl:
                            user.roles.filter(pk__in=rids).delete()
                        if pl:
                            user.user_permissions.filter(pk__in=pids).delete()
                # 替换权限
                elif role_type == "3":
                    for user in users:
                        if rl:
                            user.roles.set(list(roles))
                        if pl:
                            user.user_permissions.set(list(perms))
                result["code"] = 1
                result["error"] = "操作成功"
            else:
                result["error"] = "操作失败，原因：找不到符合条件的角色或者权限"
        else:
            result["error"] += "请选择您要操作的用户"
        return JsonResponse(result)


    @method_decorator(permission_required("xman.user.delete", login_url=JSON_403))
    def delete(self, request):
        result = {"code": 0, "data": None, "error": ""}

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-用户管理-用户列表", action="批量删除", message=message)

        uids = request.GET.get("uids")
        if uids:
            uids = uids.strip().split(",")
        if not uids:
            result["error"] = "参数错误"
            return JsonResponse(result)

        try:
            users = User.objects.filter(pk__in=uids)
            if len(users) == 0:
                result["error"] = "没有符合条件的用户"
            else:
                users.delete()
                result["code"] = 1
                result["error"] = "成功删除符合条件的用户"
        except Exception as e:
            result["code"] = -1
            result["error"] = "删除失败，原因：%s"%str(e)
        return JsonResponse(result)


def get_user_info(uid=None, dtalkid=None):
    result = {"code": 0, "data": None, "error": ""}
    user = None
    try:
        if uid is not None:
            user = User.objects.filter(pk=uid).first()
        if not user:
            if dtalkid is not None:
                user = User.objects.filter(dtalkid=dtalkid).first()
    except Exception as e:
        logger.error("get_user_info error: %s"%e)
        result["code"] = -1
        result["error"] = "服务器繁忙，请稍后重试。"
        return result
    if user:
        user_info = model_to_dict(user)
        roles = list(user.roles.values())
        user_permissions = list(user.user_permissions.values())
        rids = [role["id"] for role in roles]
        pids = [permission["id"] for permission in user_permissions]
        user_info["rids"] = rids
        user_info["pids"] = pids
        user_info["roles"] = roles
        user_info["user_permissions"] = user_permissions
        result["code"] = 1
        result["data"] = user_info
    else:
        result["error"] = "用户不存在"
    return result

@permission_required("xman.user.view", login_url=URL_403)
def user_detail(request):
    uid = request.GET.get("id")
    if uid:
        title = "修改用户"
        mode = "change"

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-用户管理-用户详情", action="访问", message=message)

        return render(request, "xman/user.html", locals())
    else:
        title = "新建用户"
        mode = "edit"
        return render(request, "xman/user.html", locals())


@method_decorator(csrf_exempt, name='dispatch')
def data_node(request):
    engine_yqms = engine(settings.DATABASES['yqms2_199'])
    if request.POST:
        kws = request.POST
        for key, value in dict(kws).items():
            update_sql = ("update SALERCANSEESETTING set member_list='{}' where node_id='{}'".format(",".join(value), key[5:]))
            engine_yqms.execute(update_sql)
    # 获取所有权限节点设置
    sql = ("select * from SALERCANSEESETTING")
    setting_df = pd.read_sql_query(sql, engine_yqms)
    setting_result = setting_df.to_dict(orient='records')
    # print(setting_result)
    # return JsonResponse({'status': 1})
    return render(request, "xman/data_node.html", locals())


class UserView(generic.View):


    @method_decorator(permission_required("xman.user.view", login_url=URL_403))
    def get(self, request):
        uid = request.GET.get("id")
        message = json.dumps(dict(request.GET))
        if not uid:
            title = "新建用户"
            mode = "add"
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-用户管理-新建用户", action="访问", message=message)

            return render(request, "xman/user.html", locals())

        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="系统管理-用户管理-用户信息", action="查询", message=message)

        result = get_user_info(uid=uid)
        return JsonResponse(result)


    @method_decorator(permission_required("xman.user.add", login_url=JSON_403))
    def post(self, request):
        result = {"code": 0, "data": None, "error": ""}
        rids = request.POST.get("rids", "")
        pids = request.POST.get("pids", "")
        if rids:
            rids = rids.split(",")
        else:
            rids = []
        if pids:
            pids = pids.split(",")
        else:
            pids = []
        result["data"] = dict(request.POST)
        form = UserNewForm(request.POST)
        if not form.is_valid():
            result["error"] = "参数错误"
            return JsonResponse(result)
        cdata = form.cleaned_data
        rs = None
        if rids:
            rs = list(Role.objects.filter(pk__in=rids))
        ps = None
        if pids:
            ps = list(Permission.objects.filter(pk__in=pids))
        try:
            user = User(**cdata)
            user.save()
        except Exception as e:
            logger.error("add_user: %s"%e)
            result["code"] = -1
            result["error"] = str(e)    
            return JsonResponse(result)
        try:
            if rs:
                user.roles.set(rs)
            if ps:
                user.user_permissions.set(ps)
            result["data"]["id"] = user.id
            result["code"] = 1
            result["error"] = "用户创建成功"

            message = json.dumps(dict(request.POST))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-用户管理", action="添加", message=message)

        except Exception as e:
            logger.error("add_user: %s"%e)
            try:
                user.delete()
            except Exception as e:
                logger.error("add_user - delete_user: %s"%e)
                pass
            result["error"] = str(e)
            result["code"] = -1
        return JsonResponse(result)


    @method_decorator(permission_required("xman.user.change",login_url=JSON_403))
    def put(self, request):
        kws = QueryDict(request.body)
        uid = kws.get("id")
        if not uid:
            title = "修改用户"
            mode = "change"
            return render(request, "xman/user.html", locals())
        result = {"code": 0, "data": None, "error": ""}
        rids = kws.get("rids", "")
        pids = kws.get("pids", "")
        if rids:
            rids = rids.split(",")
        else:
            rids = []
        if pids:
            pids = pids.split(",")
        else:
            pids = []
        result["data"] = dict(kws)
        form = UserChangeForm(kws)
        if not form.is_valid():
            result["error"] = "参数错误"
            return JsonResponse(result)
        cdata = form.cleaned_data
        uid = cdata.get("id", "")
        user = User.objects.filter(pk=uid).first()
        if not user:
            result["error"] = "查无此人"
            return JsonResponse(result)
        rs = None
        if rids:
            rs = list(Role.objects.filter(pk__in=rids))
        ps = None
        if pids:
            ps = list(Permission.objects.filter(pk__in=pids))
        
        try:
            cdata.pop("id")
            User.objects.filter(pk=uid).update(**cdata)
            if rs:
                user.roles.set(rs)
            else:
                user.roles.clear()
            if ps:
                user.user_permissions.set(ps)
            else:
                user.user_permissions.clear()
            result["code"] = 1
            result["error"] = "用户修改成功"

            message = json.dumps(dict(kws))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-用户管理", action="修改", message=message)

        except Exception as e:
            logger.error("change_user: %s"%e)
            result["error"] = str(e)
            result["code"] = -1
        return JsonResponse(result)


    @method_decorator(permission_required("xman.user.delete", login_url=JSON_403))
    def delete(self, request):
        result = {"code": 0, "data": None, "error": ""}
        uid = request.GET.get("id")
        if not uid:
            result["code"] = -1
            result["error"] = "参数错误"
            return JsonResponse(result)
        user = User.objects.filter(pk=uid).first()
        if not user:
            result["error"] = "查无此人"
            return JsonResponse(result)
        user_info = model_to_dict(user)
        user_info.pop("roles")
        user_info.pop("user_permissions")
        result["data"] = user_info
        try:
            user.delete()
            result["code"] = 1
            result["error"] = "删除成功"

            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                    model="系统管理-用户管理", action="删除", message=message)

        except Exception as e:
            logger.error("delete_user: %s"%e)
            result["error"] = str(e)
            result["code"] = -1
        return JsonResponse(result)



