
from django.urls import re_path, path

from customer import views

urlpatterns = [
    re_path(r'^list$', views.customer_list, name="customer_list"),
    re_path(r'^government/customer/list$', views.government_customer_list, name="government_customer_list"),
    re_path(r'^list/api$', views.customer_list_api, name="customer_list_api"),
    re_path(r'^list_opp$', views.customer_list_add_api, name="customer_list_add_api"),
    re_path(r'^phone$', views.phone, name="phone"),
    re_path(r'^activity$', views.activity, name="activity"),
    re_path(r'^activity/api$', views.activity_api, name="activity_api"),
    re_path(r'^industry/coverage$', views.industry_coverage, name="industry_coverage"),
    re_path(r'^industry/coverage/api$', views.industry_coverage_api, name="industry_coverage_api"),
    re_path(r'^cities/api$', views.cities_api, name="cities_api"),
    re_path(r'^counties/api$', views.counties_api, name="counties_api"),
    re_path(r'^activity/export/file$', views.activity_export_file, name="activity_export_file"),
    re_path(r'^get_wp_account_ajax$', views.get_wp_account_ajax, name="get_wp_account_ajax"),
    
    re_path(r'^government/industry/coverage$', views.government_industry_coverage, name="government_industry_coverage"),
    re_path(r'^government/industry/coverage/api$', views.government_industry_coverage_api, name="government_industry_coverage_api"),
    re_path(r'^government/industry/coverage/map$', views.get_coverage_map, name="government_industry_coverage_map"),
    re_path(r'^government/industry/coverage/map2$', views.get_coverage_map2, name="government_industry_coverage_map2"),
    re_path(r'^sync_crm/api$', views.sync_crm_api, name="sync_crm_api"),    # 同步最新的客户、商机实时信息api
    re_path(r'^get_account/api$', views.get_account_api, name="get_account_api"),   # 获取快速建账号的基础数据api
    re_path(r'^agent/api$', views.agent_api, name="agent_api"),     # 模糊搜索代理商api
    re_path(r'^opp_owner/api$', views.opp_owner_api, name="opp_owner_api"),     # 获取某个客户关联的所有商机负责人的api
    re_path(r'^get_environment/api$', views.get_environment, name="get_environment"),     # 获取当前环境(product、beta、develop)
    re_path(r'^add_account_php/api$', views.add_account_php, name="add_account_php"),     # 调php生成账号接口
    re_path(r'^get_finalaccount/api$', views.get_finalaccount, name="get_finalaccount"),    #展示最终客户列表
    re_path(r'^sync_account_data/api$', views.sync_account_data, name="sync_account_data"), #同步
    re_path(r'^save_questionnalre/api$', views.save_questionnalre, name="save_questionnalre"),  #存入调研表
    re_path(r'^get_questionnalre/api', views.get_questionnalre, name="get_questionnalre"), #获取调研表
    re_path(r'^get_uuid/api$', views.get_uuid, name="get_uuid"),  #获取uuid
    re_path(r'^add_account/api$', views.add_account, name="add_account"),  #python实现添加秘书账号
    re_path(r'^get_crm_Id/api$', views.get_crm_Id, name="get_crm_Id"),     #获取crm id
]

app_name = "customer"
