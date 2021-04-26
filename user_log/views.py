from django.shortcuts import render

# Create your views here.
import json
import logging

from mandala.auth.decorators import login_required,permission_required
from django.http import JsonResponse, HttpResponse,QueryDict
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

from user_log.forms import userLogListSelectForm
from user_log.models import *
from customer.utils import get_industry_data, get_industry_data_1
from public.utils import *
import pandas as pd
import numpy as np
from user_center.models import UserLog
from django.utils.decorators import method_decorator
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("user_log")


'''获取操作日志列表数据的接口'''
@login_required()
@permission_required("user_log.view",login_url=JSON_403)    #配置角色、权限
def GetUserLog(request):
    #获取操作日志列表数据
    result = {"status": 0, "message": "", "items": []}
    form = userLogListSelectForm(request.GET)
    if form.is_valid():
        cdata = form.cleaned_data
        operator = cdata.get("operator")
        operation_type = cdata.get("operation_type")
        operator_model = cdata.get("operator_model")
        operation_time_start = cdata.get("operation_time_start")
        operation_time_finish = cdata.get("operation_time_finish")

        user_log_condition = {}
        # 处理筛选条件
        # 操作人
        # print("操作人参数："+operator)
        if operator:
            user_log_condition = {"username__contains": operator}

        # 操作日期
        # print("操作日期参数：开始时间" + operation_time_start)
        # print("操作日期参数：结束时间" + operation_time_finish)
        if operation_time_start:
            if operation_time_finish:
                operation_time_finish = operation_time_finish + " 23:59:59"
                user_log_condition["ctime__gte"] = operation_time_start
                user_log_condition["ctime__lte"] = operation_time_finish

        # 操作类型
        # print("操作类型参数：" + operation_type)
        if operation_type:
            user_log_condition["action__exact"] = operation_type

        # 操作模块
        # print("操作模块参数："+operator_model)
        if operator_model:
            user_log_condition["model__contains"] = operator_model


        # user_log_list = get_value_list(NewUserLog, user_log_condition,
        #                                ["username", "user_id", "action", "message", "ctime", "model", "object_repr"])
        user_log_list = list(NewUserLog.objects.filter(**user_log_condition).order_by("-ctime").values(
                "username", "user_id", "action", "model", "message", "ctime"))


        user_log_df = pd.DataFrame(data=user_log_list,
                                   columns=["username", "user_id", "action", "model", "message", "ctime"])
        user_log_df["ctime"] = user_log_df["ctime"].apply(lambda x: arrow.get(x).format("YYYY-MM-DD HH:mm:ss"))

        items_df = user_log_df
        # items_df["province_name"] = customer_province

        user_log_info = items_df.fillna('--')
        # print(crm_info.columns)
        items = list(user_log_info.to_dict(orient="index").values())

        result["status"] = 1
        result["items"] = items
    return JsonResponse(result)



"""操作日志列表页面"""
@login_required()
@permission_required("user_log.view", login_url=URL_403)
def userLogList(request):
    if request.method == "GET":
        title = "操作日志列表"
        form = userLogListSelectForm()
        # 带条件请求页面时，设置默认的条件
        operator = request.GET.get("operator")
        operation_type = request.GET.get("operation_type")
        operation_time = request.GET.get("operation_time")
        if operator:
            form.input_operator_Name(operator)
        if operation_type:
            form.select_operation_type(operation_type)
        if operation_time:
            form.select_operation_time(operation_time)

        init_data = {"row_list": [10, 20, 50], "row_num": 20}
        init_data["col_names"] = ["操作人", "操作人id", "操作类型", "操作模块", "操作条件", "操作日期"]
        init_data["col_model"] = [
            {
                "name": 'username',
                "width": 6
            },
            {
                "name": 'user_id',
                "width": 6
                # "sorttype": "int"
            },
            {
                "name": 'action',
                "width": 10
            },
            {
                "name": 'model',
                "width": 22,
            },
            {
                "name": 'message',
                "width": 40
            },
            {
                "name": 'ctime',
                "width": 15
            }
        ]
        init_data["items"] = []
        init_data = json.dumps(init_data)


        # 记日志
        # user = request.user
        # if user.username not in ["武翠霞", "丛大侠", "王寅", "张太锋", "黄远", "朱铭鑫", "袁战梅"]:
        #     message = json.dumps(dict(request.GET))
        #     UserLog.objects.create(username=user.username, user_id=user.id,
        #                            model="操作日志列表", action="进入操作日志列表", message=message)
        return render(request, "user_log/user_log_list.html", locals())



