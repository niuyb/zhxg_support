
from django.urls import re_path, path

from user_log import views

urlpatterns = [
    # 操作日志列表页面的url
    re_path(r'^userLogList$', views.userLogList, name="user_log_list"),
    # 获取操作日志的接口：获取操作日志列表数据
    re_path(r'^api/get_user_log$', views.GetUserLog, name="get_user_log"),

]

app_name = "user_log"
