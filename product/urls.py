
from django.urls import re_path, path

from product import views

urlpatterns = [
    # 账号管理默认页面的url
    re_path(r'^accounts_list$', views.accounts_list, name="accounts_list"),
    re_path(r'^yqms_accounts/list/api$', views.yqms_accounts_list_api, name="product_yqms_accounts_list_api"),
    re_path(r'^yqms_accounts/reset_access_frequencylock$', views.reset_access_frequencylock, name="reset_access_frequencylock"),
    re_path(r'^yqms_accounts/clear_phone$', views.clear_phone, name="clear_phone"),

    # 舆情秘书操作日志页面url
    re_path(r'^yqms_accounts/yqms_log_overview$', views.yqms_log_overview, name="yqms_log_overview"),  #秘书日志-总览入口
    re_path(r'^yqms_accounts/yqms_log_detail$', views.yqms_log_detail, name="yqms_log_detail"),  #秘书日志-详情入口
    re_path(r'^yqms_accounts/yqms_log_calendar_api$', views.yqms_log_calendar_api, name="yqms_log_calendar_api"),
    re_path(r'^yqms_accounts/yqms_log_overview_api$', views.yqms_log_overview_api, name="yqms_log_overview_api"),
    re_path(r'^yqms_accounts/yqms4_log_detail_api$', views.yqms4_log_detail_api, name="yqms4_log_detail_api"),
    re_path(r'^yqms_accounts/yqms3_log_detail_api$', views.yqms3_log_detail_api, name="yqms3_log_detail_api"),
    re_path(r'^yqms_accounts/export_log$', views.yqms_log_data.export_log, name='yqms_export_log'),
	# 网评url
    re_path(r'^zhwp_accounts_list_api$', views.zhwp_accounts_list_api, name="product_zhwp_accounts_list_api"),
    re_path(r'^zhwp_accounts_list_count$', views.zhwp_accounts_list_count, name="product_zhwp_accounts_list_count"),
    re_path(r'^getLoginBase$', views.getLoginBase, name="product_getLoginBase"),


    # 态势感知
    re_path(r'^tsgz/list', views.tsgz_list, name="tsgz_list"),
    re_path(r'tsgz/list/api', views.tsgz_list_api, name="tsgz_list_api"),

]

app_name = "product"
