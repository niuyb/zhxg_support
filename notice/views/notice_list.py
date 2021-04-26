import json
import arrow
import logging

from django.http import  JsonResponse
from django.shortcuts import render
from mandala.auth import get_user_model
from mandala.auth.decorators import  permission_required,login_required
from notice.forms import NoticeListSelectForm
from notice.models import NoticeList
from notice.apps import NoticeConfig
from user_center.models import UserLog
from secretary.models import SalercanseeNew

from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
# Create your views here.
app_name = "notice"
logger = logging.getLogger(app_name)

User = get_user_model()

"""获取钉钉通知消息列表页面初始数据"""
def get_notice_list_init_data():
    init_data = {"row_list": [10, 20, 50], "row_num": 20}
    init_data["col_names"] = ["用户", "消息内容", "消息类型", "发送时间", "发送状态"]
    init_data["col_model"] = [
        {
            "name": 'ding_user__username',
            # "index": 'note',
            "width": 6,
            # "sortable": false
        },
        {
            "name": 'content',
            # "index": 'note',
            "width": 60,
            # "sortable": false
        },
        {
            "name": 'notice_type__name',
            # "index": 'id',
            "width": 12,
            # "sorttype": "int"
        },
        {
            "name": 'ctime',
            # "index": 'tax',
            "width": 10,
            # "sortable": false
        },
        {
            "name": 'status',
            # "index": 'tax',
            "width": 6,
            # "sortable": false
        }
    ]
    init_data["items"] = []
    return init_data

"""通知消息列表页面"""
@login_required()
@permission_required("notice.notice_list.view",login_url=URL_403)
def notice_list(request):
    if request.method == "GET":

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="通知管理-通知列表", action="访问", message=message)

        title = "钉钉通知消息列表"
        form = NoticeListSelectForm(request.GET)
        init_data = get_notice_list_init_data()
        # if request.user.has_perm("notice.export_notice_list"):
        #     init_data["export_notice_list_access"] = 1

        init_data = json.dumps(init_data)
        # user_log_url = reverse("user_center:user_log")
        # departments_api = reverse("secretary:departments_api")
        # department_data = get_departments_about_sale()
        # department_data = json.dumps(department_data)
        # department_data_1 =[["", "--------"]] + list(settings.SALE_DEPARTMENT_LEVEL_1.items())
        # department_data_1 = json.dumps(department_data_1)
        return render(request, "notice/notice_list.html", locals())

"""接口：获取钉钉消息通知信息列表"""
@login_required()
@permission_required("notice.notice_list.view",login_url=JSON_403)
def notice_list_api(request):
    result = {"code": 0, "msg": ""}
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    message = json.dumps(dict(kws))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="通知管理-通知列表api", action="查询", message=message)

    form = NoticeListSelectForm(kws)
    if not form.is_valid():
        result["code"] = -1
        result["msg"] = "参数错误"
    # 根据输入的商务名查询数据
    cdata = form.cleaned_data
    ding_user = cdata.get("ding_user")
    params = {}

    # 查询数据权限
    cansee_users = json.loads(
        SalercanseeNew.objects.filter(saleid=request.user.istarshine_id).values_list('cansee', flat=True).first())
    # print(cansee_users)

    cansee_users_obj = list(User.objects.filter(istarshine_id__in=cansee_users))
    if ding_user:
        # 如果有筛选条件，模糊查询
        ding_users = list(User.objects.filter(username__icontains=ding_user))
        # print(ding_users)
        if not ding_users:
            result["msg"] = "查无此人"
            return JsonResponse(result)
        else:
            # 如果是超管，按照模糊查询结果查
            if request.user.is_superuser:
                ding_users = ding_users
            else:
                # 非超管，需要和cansee表结果取交集
                ding_users_obj = list(set(ding_users)&set(cansee_users_obj))
                if not ding_users_obj:
                    result["msg"] = "您没有权限"
                    return JsonResponse(result)
                else:
                    ding_users = ding_users_obj
    else:
        # 如果是超管
        if request.user.is_superuser:
            ding_users = None
        else:
            ding_users = cansee_users_obj


    if ding_users:
        params["ding_user__in"] = ding_users

    # 根据消息内容查询数据
    content = cdata.get("content")
    if content:
        params["content__icontains"] = content

    # 根据发送状态查询数据
    status = cdata.get("status")
    if status:
        params["status"] = status

    # 根据消息类型查询数据
    notice_type = cdata.get("notice_type")
    if notice_type:
        params["notice_type"] = notice_type

    fields = ["ding_user__username", 'notice_type__name']
    for field in NoticeList._meta.fields:
        fields.append(field.name)

    _items = NoticeList.objects.filter(**params).values(*fields).order_by("-id")
    items = []
    status_map = dict(NoticeConfig.notice_sending_status_choices)
    for item in _items:
        ctime = item.get("ctime")
        if ctime:
            ctime = arrow.get(ctime).datetime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            ctime = "--------"
        item["ctime"] = ctime
        item["status"] = status_map.get(item["status"], "--------")
        items.append(item)
    result["data"] = items
    result["code"] = 1
    return JsonResponse(result)

"""导出钉钉消息通知列表"""
@login_required()
@permission_required("notice.notice_list.export",login_url=JSON_403)
def export_notice_list(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="通知管理-通知列表", action="导出", message=message)

    return JsonResponse({})
