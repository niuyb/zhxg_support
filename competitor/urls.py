
from django.urls import re_path, path

from competitor import views

urlpatterns = [
    # 竞品列表页面的url,侧边栏调用
    re_path(r'^competitorList$', views.competitorList, name="competitor_list"),

    # 设置竞品签约客户页面的url,侧边栏调用
    re_path(r'^competitorCrm$', views.competitorCrm, name="competitor_crm"),

    # 竞品签约客户的列表加载数据接口
    re_path(r'^api/competitorCrm$', views.competitorCrmListApi, name="competitor_api"),

    # 操作竞品的接口,获取竞品列表数据、添加竞品、删除竞品、修改竞品
    re_path(r'^api/operate_competitor$', views.OperateCompetitor.as_view(), name="operate_competitor"),

    # 关联竞品的接口，关联、删除关联关系、修改关联的信息
    re_path(r'^api/connect_competitor$', views.connect_competitor_api, name="connect_competitor_api"),

    # 更新关联竞品页面的下拉框选项值
    re_path(r'^api/updateSelectForm$', views.updateSelectForm, name="updateSelectForm_api"),

    # 竞品分析页面
    re_path(r'^analysis$', views.analysis, name="competitor_analysis"),
    # 客户占有分析
    re_path(r'^occupiedAnalysis$', views.occupiedAnalysis, name="occupied"),
    # 签单金额分析
    re_path(r'^moneyAnalysis$', views.moneyAnalysis, name="money"),
    # 签单地域分析
    re_path(r'^localAnalysis$', views.localAnalysis, name="local"),
    # 签单行业分析
    re_path(r'^industryAnalysis$', views.industryAnalysis, name="industry"),
    re_path(r'^industry2Analysis$', views.industry2Analysis, name="industry2money"),
    # 计算签单客户的状态
    re_path(r'^customerStatus$', views.UpdateStatus.as_view(), name="customerStatus"),


    re_path(r'^getIP$', views.getIP, name="getIP$"),

]

app_name = "competitor"
