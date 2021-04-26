from django.urls import re_path, path

from notice import views

urlpatterns = [
    re_path(r'^list$', views.notice_list, name="notice_list"),
    re_path(r'^list/api$', views.notice_list_api, name="notice_list_api"),
    re_path(r'^list/export$', views.export_notice_list, name="export_notice_list"),
    
    re_path(r'^settings$', views.notice_settings, name="notice_settings"),
    re_path(r'^settings/change$', views.change_notice_setting, name="change_notice_setting"),
    re_path(r'^setting/list/api$', views.notice_setting_list_api, name="notice_setting_list_api"),
]

app_name = "notice"
