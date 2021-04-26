
from django.urls import re_path, path

from salerVisit import views

urlpatterns = [
    # 签到详情接口
    # re_path(r'^api/visitDetail$', views.visitDetailApi, name="api_visitDetail"),

    # 进入全国签到页面
    re_path(r'^visitDetail$',views.visitHtml,name="visit_detail"),

    # 进入签到选择页面
    re_path(r'^selectVisit$',views.selectVisitHtml,name="select_visit"),

    # 签到选择页面的数据接口
    re_path(r'^selectVisitApi$',views.selectVisitApi,name="api_select_visit"),

    # 签到详情列表页面
    re_path(r'^visitTable$',views.VisitTableHtml,name="visit_table"),

    # 签到详情列表数据导出
    re_path(r'^exportVisitTable$',views.export_excel,name="export_visit_table")



]

app_name = "salerVisit"
