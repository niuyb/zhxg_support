from django.urls import re_path, path
from work_platform import views
# 工作台接口
urlpatterns = [
    path('login', views.login, name="dingding_login"),
    # 微信群管理
    re_path(r'^wechat$', views.Wechat.as_view(), name="wechat"),
    re_path(r'^wechat/result$', views.WechatResult.as_view(), name="wechat_result"),
    re_path(r'^wechat/test$', views.wechat_test, name="wechat_test"),
    re_path(r'^wechat/result/test$', views.wechat_result_test, name="wechat_result_test"),
    path('wechat/group/message/list/api', views.wechat_group_message_list_api, name="wechat_group_message_list_api"),
    path('wechat/group/list', views.wechat_group_list, name="wechat_group_list"),
    path('wechat/group/members/api', views.wechat_group_members_api, name="wechat_group_members_api"),
    path('wechat/group/message/push', views.push_wechat_group_message, name="push_wechat_group_message"),

    path('index', views.index, name="work_platform_index"),

    ###########################################################
    path('index2', views.index2, name="work_platform_index2"),
    ###########################################################

    path('modules', views.get_modules, name="get_modules"),

    path('upload', views.upload, name="date_index"),

    path('customer/search', views.search_customer, name="work_platform_search_customer"),
    path('customer/list', views.customer_list, name="work_platform_customer_list"),
    path('customer/list/api', views.customer_list_api, name="work_platform_customer_list_api"),
    

    re_path(r'^task$', views.task, name="task"),
    re_path(r'^task/taskapi$', views.task_api, name="task_api"),
    re_path(r'^task/oppapi$', views.task_oppapi, name="task_oppapi"),
    re_path(r'^task/logapi$', views.task_modifyapi, name="task_logapi"),
    re_path(r'^task/addtask$', views.add_task_api, name="addtask"),
    re_path(r'^task/per$', views.person_task, name="team"),
    re_path(r'^team/departapi$', views.team_department_api, name="depart"),
    re_path(r'^team/peiapi$', views.team_pei_api, name="pei"),

    # 工作统计
    re_path(r'^count$', views.work_count, name="count"),
    re_path(r'^count/perapi$', views.work_per_api, name="perapi"),
    re_path(r'^count/departapi$', views.work_depart_api, name="departapi"),
    re_path(r'^count/detailapi$', views.count_detail_api, name="count_detail_api"),

]

app_name = "work_platform"
