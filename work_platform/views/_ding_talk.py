import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from mandala.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt

from mandala.auth.models import Module

from public.utils import Result

@login_required(login_url="/work_platform/login")
def index(request):
    title = "首页"
    return render(request, "work_platform/index.html", locals())


#为了测试某些手机cookie丢失问题而添加些函数
def index2(request):
    title = "首页"
    print(request.user)
    print(request.COOKIES)
    print(request.session)
    return render(request, "work_platform/index.html", locals())

def get_modules(request):
    ro = Result()
    # modules = list(Module.objects.filter(parent__code="work_platform").values())
    modules = [
        {"name": "首页", "code": "work_platform-index", "url": "/work_platform/index", "status": True, "dot": False, "icon": "weapp-nav"},
        {"name": "客户", "code": "work_platform-customer_list", "url": "/work_platform/customer/list", "status": True, "dot": False, "icon": "friends"},
        {"name": "任务", "code": "work_platform-task", "url": "/work_platform/task", "status": True, "dot": False, "icon": "todo-list"},
        {"name": "统计", "code": "work_platform-task", "url": "/work_platform/count", "status": True, "dot": False,
         "icon": "todo-list"},

        {
            "name": "消息", 
            "code": "work_platform-wechat_group_list", 
            "url": "/work_platform/customer/list?sortBy=%7B%22createdat%22:%22desc%22%7D&filterBy=%7B%22level%22:[],%22wechat_group%22:[2,3],%22is_read%22:[0]%7D&page=1&pageSize=20", 
            "status": True, 
            "icon": "chat-o", 
            "badge": "99+"
        },
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        # {"name": "首页", "code": "work_platform_index", "url": "/work_platform/index", "status": True, "icon": "weapp-nav"},
        # {"name": "客户", "code": "work_platform_customer_list", "url": "/work_platform/customer/list", "status": True, "icon": "friends"},
        # {"name": "任务", "code": "work_platform_task", "url": "/work_platform/task", "status": True, "icon": "todo-list"},
        ]
    ro.code = 1
    ro.data = modules
    ro.error = "查询成功" 
    return JsonResponse(ro.dict())

def login(request):
    title = "登录"
    return render(request, "work_platform/login.html", locals())
