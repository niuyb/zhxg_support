from django.urls import re_path, path

from statistical import views

urlpatterns = [
    re_path(r'^api/saler_info$', views.saler_info, name="saler_info_api"),
    # 计算客户账号活跃情况
    re_path(r'^api/crm_act_info$', views.crm_activity_info, name="crm_act_info"),
    # 计算客户账号活跃情况，增加结束日期的参数
    re_path(r'^api/crm_act_info1$', views.crm_activity_info1, name="crm_act_info1"),
    # 计算商机账号活跃情况
    re_path(r'^api/opp_act_info$', views.opp_activity_info, name="opp_act_info"),
    # 计算客户拜访记录情况
    re_path(r'^api/crm_record_info$', views.crm_record_info, name="crm_record_info"),
    # 计算商机拜访记录情况
    re_path(r'^api/opp_record_info$', views.opp_record_info, name="opp_record_info"),
    # 计算商机拜访记录详细列表
    re_path(r'^api/opp_record_list$', views.opp_record_list, name="opp_record_list"),
    # 计算客户拜访记录详细列表
    re_path(r'^api/crm_record_list$', views.crm_record_list, name="crm_record_list"),
    # 计算经纬度距离
    re_path(r'^api/cal_distance$', views.cal_distance, name="cal_distance"),
]

app_name = "statistical"
