import re
import os
import time
import uuid
import json
import copy
import arrow
import base64
import random
import hashlib
import requests
import pandas as pd

from urllib.parse import urlencode

from django.urls import reverse
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse, QueryDict, StreamingHttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from mandala.auth import authenticate, login, logout, get_user_model
from mandala.auth.decorators import login_required, permission_required

from user_center.models import UserLog, Material
from public.utils import Result
from secretary.utils import get_can_see_new

from django.conf import settings
import logging

URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

logger = logging.getLogger("default")

# Create your views here.

User = get_user_model()

# /index
@login_required
def index(request):
    title = "首页"
    print("hello")
    return render(request, 'index-2.html', locals())
    # if not request.user.has_perm("sale.view_saleappaccess"):
    #     return render(request, 'index-2.html', locals())
    # customer_count = Account.objects.filter(highseastatus__in=[1, 3, 4]).count()
    # opp_count = Opportunity.objects.all().count()
    # msuser_count = WkTUserservice.objects.filter(ku_userstatus__in=[0, 1, 2]).count()
    # order_count = Order.objects.filter(postatus=2).count()
    # top_bar_data = {"customer": customer_count, "account": msuser_count, "order": order_count, "opportunity": opp_count}
    # return render(request,'index.html', locals())

"""获取用户列表"""
@login_required
def get_user_list(request):
    user_list = User.objects.all()    
    return render(request,'user_center/user_list.html',{'user_list':user_list})

@login_required
def base(request):
    return render(request, 'base.html')

"""从老后台跳到新后台"""
def login_from_old_backend(request):
    next_url = settings.NEW_SUPPORT_HOST + reverse("user_center:index")
    username = request.GET.get("username")
    token = request.GET.get("token")
    jump = request.GET.get("jump")
    if not jump:
        jump = next_url
    # 校验数据
    if not username:
        errmsg = '用户名'
        return render(request, "login.html", locals())
    if not token:
        errmsg = 'token不能为空'
        return render(request, "login.html", locals())
    try:
        username = base64.b64decode(username).decode("utf8")
    except Exception as e:
        logger.error(str(e))
        errmsg = '用户名非法'
        return render(request, "login.html", locals())
    salt = settings.LOGIN_SALT
    _token = hashlib.md5((salt + username).encode("utf8")).hexdigest()
    if _token != token:
        errmsg = "token错误"
        return render(request, "login.html", locals())
    user = User.objects.filter(mobile=username).first()
    if not user:
        user = User.objects.filter(username=username).first()
    if not user:
        errmsg = '用户不存在'
        return render(request, "login.html", locals())
    if not user.is_superuser:
        # status: 0, 未激活   1，激活   2，离职
        if (not user.is_active) or (user.status != 1):
            errmsg = '用户未激活'
            return render(request, "login.html", locals())
    login(request, user)

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="用户中心-老后台跳转新后台", action="跳转", message=message)

    return redirect(jump)


"""从新后台跳到老后台"""
@login_required
def jump_to_old_backend(request):
    next_url = request.GET.get("next_url", settings.OLD_SUPPORT_HOST)
    # 老后台用户表存的是用户的昵称，新后台用户表存的是用户的名称
    # 所以相互跳转时，需要用手机号或者dingid这种字段来验证
    # 本函数中用的是手机号
    # username = request.user.username
    username = request.user.mobile
    salt = settings.LOGIN_SALT
    token = hashlib.md5((salt + username).encode("utf8")).hexdigest()
    params = {}
    params["username"] = base64.b64encode(username.encode("utf8"))
    params["token"] = token
    params["jump"] = next_url
    url = settings.LOGIN_URL_OLD_BACKEND + "?" + urlencode(params)

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="用户中心-新后台跳转老后台", action="跳转", message=message)
    return redirect(url)

"""退出登录"""
def log_out(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="用户中心", action="登出", message=message)

    logout(request)
    login_url = settings.LOGIN_URL
    # return redirect(login_url)
    if not settings.DEBUG:
        # 暂时先跳到老后台
        login_url = settings.LOGIN_URL_OLD
    return redirect(login_url)

"""登录"""
"""20200708修改，禁用用户名登录，只能用手机号登录"""
class LoginView(View):
    def get(self, request):
        if not settings.DEBUG:
            if settings.MODE == 'product':
                # 暂时先跳到老后台
                login_url = settings.LOGIN_URL_OLD
                return redirect(login_url)

        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            if username:
                try:
                    username = base64.b64decode(username.encode("utf8")).decode("utf8")
                except Exception as e:
                    logger.error(e)
                    username = ""
            checked = 'checked'
        else:
            username = ''
            checked = ''

        p = "^\d+$"
        errmsg = ''
        if username and not re.match(p, username):
            username = ""
            errmsg = '请输入手机号登录'
            
        # 使用模板
        return render(request, 'login.html', {'username':username, 'checked':checked, 'errmsg': errmsg})

    def post(self, request):
        '''登录校验'''
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        
        # 校验数据
        if not username:
            errmsg = '手机号不能为空'
            return render(request, 'login.html', locals())


        if not password:
            errmsg = '密码不能为空'
            return render(request, 'login.html', locals())

        # 校验是否是正确的手机号
        if not re.match("^1\d{10}$", username):
            errmsg = '请输入正确的手机号'
            return render(request, 'login.html', locals())
            
        # user = User.objects.filter(username=username).first()
        user = User.objects.filter(mobile=username).first()
        if not user:
            errmsg = '用户不存在'
            return render(request, 'login.html', locals())

        if not user.is_superuser:
            if (not user.is_active) or (user.status != 1):
                errmsg = '用户未激活'
                return render(request, 'login.html', locals())

        # 业务处理:登录校验
        md5_password = hashlib.md5((password.encode(encoding='UTF-8'))).hexdigest().upper()

        print(md5_password)
        print(user.password_md5.upper())

        if md5_password == user.password_md5.upper():
            # 用户名密码正确
            # 获取登录后所要跳转到的地址
            # 默认跳转到首页
            login(request, user)

            message = json.dumps(dict(request.POST))
            UserLog.objects.create(username=user.username, user_id=user.id,
                    model="用户中心-用户登录", action="登录", message=message)

            next_url = request.GET.get('next', '/index')

            # 跳转到next_url
            response = redirect(next_url) # HttpResponseRedirect

            # # 判断是否需要记住用户名
            # if remember == 'on':
            #     # 记住用户名

            #     response.set_cookie('username', username, max_age=7*24*3600)
            # else:
            #     response.delete_cookie('username')

            # 用户名基本都是汉字，所以需要base64加密一下，变成英文字母
            u = base64.b64encode(username.encode("utf8")).decode("utf8")
            response.set_cookie('username', u, max_age=7*24*3600)

            # 返回response
            return response
        else:
            # 用户名或密码错误
            errmsg = '用户名或密码错误'
            return render(request, 'login.html', locals())


# /set_code
def set_code(request):
    phone = request.GET.get('username')
    code = ''.join(str(random.randint(0,9)) for i in range(6) )
    cache.set(phone,code,2*60)
    return HttpResponse(code)


# /read_code
def read_code(request):
    phone = request.GET.get('username')
    code = cache.get(phone)
    return HttpResponse(code)

"""免密登录"""
def quick_login(request):
    username = request.GET.get("username")
    if not username:
        errmsg = '用户名不能为空'
        return render(request, 'login.html', locals())

    user = User.objects.filter(username=username).first()
    if not user:
        user = User.objects.filter(mobile=username).first()

    if not user:
        errmsg = '用户不存在'
        return render(request, 'login.html', locals())

    if not user.is_active:
        errmsg = '用户未激活'
        return render(request, 'login.html', locals())

    login(request, user)

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="用户中心-快速登录", action="登录", message=message)

    next_url = request.GET.get('next', '/index')

    # 跳转到next_url
    response = redirect(next_url) # HttpResponseRedirect
    return response

@login_required
def user_log(request):
    action = request.GET.get("action", "")
    message = request.GET.get("message", "")
    model = request.GET.get("model", "")
    user = request.user
    result = {"status": 0, "message": "保存操作记录失败，原因：参数不正确"}
    if action or message or model:
        try:
            UserLog.objects.create(action=action, message=message, 
                    object_repr=model, username=user.username, user_id=user.id)
            result["status"] = 1
            result["message"] = "用户操作记录保存成功"
        except Exception as e:
            logger.error(str(e))
            result["status"] = -1
            result["message"] = "保存操作记录失败，原因：%s"%e
    return JsonResponse(result)

@csrf_exempt
def mirror(request):
    if request.method == "GET":
        kwargs = request.GET 
    elif request.method == "POST":
        kwargs = request.POST 
    else:
        kwargs = QueryDict(request.body)

    return JsonResponse(kwargs) 

# 对接钉钉免登录
def get_ding_talk_user(code):
    if not code:
        return {}

    AppKey = settings.APP_KEY
    AppSecret = settings.APP_SECRET
    url = "https://oapi.dingtalk.com/gettoken?appkey={0}&appsecret={1}".format(AppKey, AppSecret)
    logger.info("url: %s"%url)
    resp = requests.get(url)
    resp = resp.json()
    logger.info("resp: %s"%str(resp))
    if resp.get("errcode") != 0:
        return {}

    access_token = resp["access_token"]
    # 获取userId 
    url1 = "https://oapi.dingtalk.com/user/getuserinfo?access_token={0}&code={1}".format(access_token, code)
    resp1 = requests.get(url1)
    logger.info("url1: %s"%url1)
    resp1 = resp1.json()
    logger.info("resp1: %s"%str(resp1))
    if resp1.get("errcode") != 0:
        return {}
        
    else:
        user = {"username": resp1["name"], "ding_talk_id": resp1["userid"]}
        return user
    # # 获取userInfo   
    # url2 = "https://oapi.dingtalk.com/user/get?access_token={0}&userid={1}".format(access_token, resp1["userid"])
    # resp2 = requests.get(url2)
    # resp2 = resp2.json()
    # return resp2

# 对接钉钉企业内部H5应用免登录
def ding_talk_login(request):
    info = request.GET 
    code = info.get("code", None)
    ding_talk_user = get_ding_talk_user(code)
    logger.info("ding_talk_user: %s"%str(ding_talk_user))
    ding_talk_id = ding_talk_user.get("ding_talk_id", "")
    logger.info("ding_talk_id: %s"%ding_talk_id)
    user = None
    if ding_talk_id:
        user = User.objects.filter(dtalkid=ding_talk_id).first()
        if user:
            login(request, user)
            session_id = request.session.session_key
            request.session_id = session_id
            data = {"session_id": session_id}
            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=user.username, user_id=user.id,
                    model="用户中心-钉钉企业H5应用登录新后台", action="登录", message=message)

            return JsonResponse({"code": 1, "data": data, "error": "登录成功"})
    return JsonResponse({"code": 0, "data": {}, "error": "登录失败"})

@login_required(login_url=settings.JSON_403)
def is_logined(request):
    return JsonResponse({"code": 1, "data": None, "error": "已登录"})
    

# 资料相关，资料列表html页面
def material_list(request):
    title = "星光资料"
    return render(request, "user_center/material-list.html", locals())

def get_material_list(request):
    params = {}
    if not request.user.is_superuser:
        can_see = get_can_see_new(request.user.istarshine_id)
        params["istarshine_id__in"] = can_see

    res = {"code": 0, "data": None, "error": ""}
    material_list = list(Material.objects.filter(**params).order_by("-ctime").values())

    res["code"] = 1
    res["data"] = material_list
    res["error"] = "查询成功"
    if material_list:
        df = pd.DataFrame(material_list)
        user_list = list(User.objects.filter(**params).values("username", "istarshine_id"))
        if user_list:
            df = pd.merge(pd.DataFrame(material_list), pd.DataFrame(user_list), how="left", on="istarshine_id")
            df["created_at"] = df["ctime"].apply(lambda x: arrow.get(x).format("YYYY-MM-DD HH:mm:ss"))
            
        df["url"] = df["code"].apply(lambda x: "/user_center/video?code=" + x)
        res["data"] = list(df.to_dict(orient="index").values())

    return res

# 资料页面中相关的数据接口
class MaterialListView(View):
    @method_decorator(permission_required("user_center.material_list.view", login_url=URL_403))
    def get(self, request):

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料列表api", action="查询", message=message)

        return JsonResponse(get_material_list(request))

    @method_decorator(permission_required("user_center.material.change", login_url=JSON_403))
    def patch(self, request):

        res = Result()
        kws = QueryDict(request.body)

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料列表", action="批量修改", message=message)

        pks = kws.get("ids")
        if pks:
            pks = pks.replace(" ", "").split(",")

        if not pks:
            res.error = "参数错误"
            return JsonResponse(res.dict())

        materials = Material.objects.filter(pk__in=pks)
        """

        """
        res.error = "操作成功"
        res.code = 1
        return JsonResponse(res.dict())

    @method_decorator(permission_required("user_center.material.delete", login_url=JSON_403))
    def delete(self, request):

        kws = request.GET
        res = Result()

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料列表", action="批量删除", message=message)

        pks = kws.get("ids")
        if pks:
            pks = pks.strip().replace(" ", "").split(",")
        if not pks:
            res.error = "参数错误"
            return JsonResponse(res.dict())

        try:
            materials = Material.objects.filter(pk__in=pks)
            if len(materials) < 1:
                res.error = "未查找到相关数据"
                
            else:
                materials.delete()
                res.code = 1
                res.error = "操作成功"

        except Exception as e:
            res.error = "操作失败，原因：%s"%str(e)

        return JsonResponse(res.dict())

def material_detail(request):
    title = "星光资料"

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="用户中心-星光资料-资料详情", action="访问", message=message)

    return render(request, "user_center/material-detail.html", locals())

class MaterialView(View):
    def get_cann_see(self, request):
        can_see = None
        if not request.user.is_superuser:
            can_see = get_can_see_new(request.user.istarshine_id)
            
        return can_see

    @method_decorator(permission_required("user_center.material_list.view", login_url=URL_403))
    def get(self, request):

        res = Result()

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料详情api", action="查询", message=message)

        code = request.GET.get("code", "")
        if not code:
            res.code = -1
            res.error = "参数错误"
            return JsonResponse(res.dict())
            
        material = Material.objects.filter(code=code).first()
        if not material:
            res.error = "未查询到相关信息"
            return JsonResponse(res.dict())

        can_see = self.get_cann_see(request)
        if can_see is not None:
            if material.istarshine_id not in can_see:
                res.error = "您无权查看此条数据"
                return JsonResponse(res.dict())

        res.code = 1
        res.error = "查询成功"
        res.data = model_to_dict(material)
        return JsonResponse(res.dict())

    @method_decorator(permission_required("user_center.material.add", login_url=JSON_403))
    def post(self, request):

        res = Result()

        title = request.POST.get("title", "")
        comment = request.POST.get("comment", "")
        typ = request.POST.get("typ", "0")
        if typ not in ["1", "2", "3", "4"]:
            res.code = -1
            res.error = "错误的类型"
            return JsonResponse(res.dict())

        file = request.FILES.get("file", None)

        message = json.dumps(dict(request.POST))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料详情", action="添加", message=message)

        if not file:
            res.code = -1
            res.error = "您未上传任何文件"
            return JsonResponse(res.dict())

        name = file.name
        _, suffix = os.path.splitext(name)
        code = str(uuid.uuid1())
        path = os.path.join(settings.MEDIA_ROOT, code + suffix)

        with open(path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        istarshine_id = request.user.istarshine_id
        ctime = int(time.time())
        Material.objects.create(name=name, code=code, path=path, typ=typ, ctime=ctime,
                title=title, comment=comment, istarshine_id=istarshine_id)
        res.code = 1
        res.data = {"name": name, "code": code, "path": path, "comment": comment}
        res.error = "文件上传成功"
        return JsonResponse(res.dict())

    # @method_decorator(permission_required("user_center.material.change", login_url=JSON_403))
    # def put(self, request):
    #     res = Result()
    #     kws = QueryDict(request.body)

    #     message = json.dumps(dict(kws))
    #     UserLog.objects.create(username=request.user.username, user_id=request.user.id,
    #             model="用户中心-星光资料-资料详情", action="修改", message=message)

    #     code = kws.get("code")
    #     pass


    @method_decorator(permission_required("user_center.material.change", login_url=JSON_403))
    def patch(self, request):
        res = Result()
        kws = QueryDict(request.body)

        message = json.dumps(dict(kws))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料详情", action="修改", message=message)

        code = kws.get("code", "")
        typ = kws.get("typ", "0")
        title = kws.get("title", "")
        comment = kws.get("comment", "")

        if not code:
            res.code = -1
            res.error = "参数错误"
            return JsonResponse(res.dict())

        materials = Material.objects.filter(code=code)
        if len(materials) < 1:
            res.error = "没有找到需要更新的数据"
            return JsonResponse(res.dict())

        materials.update(typ=typ, title=title, comment=comment)
        res.code = 1
        res.data = {"code": code, "typ": typ, "title": title, "comment": comment}
        res.error = "更新成功"
        return JsonResponse(res.dict())

    @method_decorator(permission_required("user_center.material.delete", login_url=JSON_403))
    def delete(self, request):
        
        res = Result()

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="用户中心-星光资料-资料详情", action="删除", message=message)

        code = request.GET.get("code")
    
        if not code:
            res.code = -1
            res.error = "参数错误"
            return JsonResponse(res.dict())

        try:
            materials = Material.objects.filter(code=code)
            if len(materials) < 1:
                res.error = "未找到需要删除的数据"

            else:
                materials.delete()
                res.code = 1
                res.error = "数据成功删除"

        except Exception as e:
            res.code = -1
            res.error = "操作失败，原因：%s"%str(e)

        return JsonResponse(res.dict())

# 视频播放页面
def video(request):
    code = request.GET.get("code")
    title = "视频播放"
    if code:
        video = Material.objects.filter(code=code, typ=1).first()
        if video:
            video.url = os.path.join("/user_center/video/" + video.code)

    if request.user.is_anonymous:
        return render(request, "user_center/video_anonymous.html", locals())
        
    return render(request, "user_center/video.html", locals())


#视频流
def video_stream_handler(request, code):
	#创建一个生成器用于播放视频
	#filepath视频名称
	#length 长度
	#offset偏移量即视频字节需要跳过的值
    def read_video(filepath, length, offset):
        with open(filepath,'rb') as f:
            # 跳过offset个字节
            f.seek(offset)
            while True:
                # 读取指定长度的数据
                data = f.read(length)
                # 如果有数据-->生成数据
                if data:
                    yield data
                # 如果没有数据-->跳出循环
                else:
                    break
                
    try:
		#找到资料
        material = Material.objects.get(code=code)

        #读取视频的大小
        size = os.path.getsize(material.path)

        #请求头文件中的range
        request_range = request.headers.get('range')
        #得到客户端想得到数据的起始位置
        start_bytes = re.findall('=(\d+)-',request_range)
        start_bytes = int(start_bytes[0]) if start_bytes else 0
        #定义数据终止位置
        last_bytes = start_bytes +1024*1024
        last_bytes = min(last_bytes,size-1)
        #数据长度
        length = last_bytes-start_bytes+1
        #构造response对象
        response = StreamingHttpResponse(
            read_video(
                material.path,
                length=length,
                offset=start_bytes,
            ),
            status=206,
        )
        # 设置响应字节流的长度
        response['Content-Length'] = str(length)
        # Content-Range：bytes 起始字节位-终止字节位/总字节位
        response['Content-Range'] = 'bytes %s-%s/%s' % (start_bytes,last_bytes,size)
        return response
            
    except:
        return HttpResponse(status=404)