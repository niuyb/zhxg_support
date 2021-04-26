
from django.urls import re_path, path

from interface import views

urlpatterns = [
    # 增量更新account表的接口url
    re_path(r'^update_account$', views.update_account_table, name="update_account"),
    # 增量更新opportunity表的接口url
    re_path(r'^update_opportunity$', views.update_opp_table, name="update_opportunity"),

]

app_name = "interface"