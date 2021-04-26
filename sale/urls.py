
from django.urls import re_path, path

from sale import views

urlpatterns = [
    re_path(r'^index$', views.sale_index, name="sale_index"),
    re_path(r'^data/customer/all$', views.get_data_customer_all, name="data_customer_all"),
    re_path(r'^data/customer/day$', views.get_data_customer_day, name="data_customer_day"),
    re_path(r'^data/money/all$', views.get_data_money_all, name="data_money_all"),
    re_path(r'^data/money/day$', views.get_data_money_day, name="data_money_day"),

    # re_path(r'^goal/regionals/year/api$', views.goal_regionals_year_api, name="goal_regionals_year_api"),
    re_path(r'^goal/regionals/month/api$', views.goal_regionals_month_api, name="goal_regionals_month_api"),

    re_path(r'^payment/company/months/api$', views.payment_company_months_api, name="payment_company_months_api"),
    re_path(r'^payment/company/days/api$', views.payment_company_days_api, name="payment_company_days_api"),

    re_path(r'^saler/list$', views.saler_list, name="saler_list"),
    re_path(r'^saler/list/api$', views.saler_list_api, name="saler_list_api"),
    re_path(r'^saler/info/list/api$', views.saler_info_list_api, name="saler_info_list_api"),
    
    re_path(r'^saler/list/export$', views.export_saler_list, name="export_saler_list"),

    re_path(r'^payment/plan/list$', views.payment_plan_list, name="payment_plan_list"),
    re_path(r'^payment/plan/list/api$', views.payment_plan_list_api, name="payment_plan_list_api"),
    # re_path(r'^payment/plan/list/export$', views.export_payment_plan_list, name="export_payment_plan_list"),

    re_path(r'^portrait/saler$', views.saler_portrait, name="saler_portrait"),
    re_path(r'^portrait/saler/1$', views.saler_portrait1, name="saler_portrait1"),
    re_path(r'^portrait/saler/2$', views.saler_portrait2, name="saler_portrait2"),
    re_path(r'^portrait/saler/3$', views.saler_portrait3, name="saler_portrait3"),
    re_path(r'^data/work/daily$', views.get_data_work_daily, name="data_work_daily"),

    re_path(r'^portrait/fuzzy$', views.fuzzy_portrait, name="fuzzy_portrait"),
    re_path(r'^portrait/region$', views.region_portrait, name="region_portrait"),
    re_path(r'^portrait/department$', views.department_portrait, name="department_portrait"),

    re_path(r'^analysis$', views.opp_analysis, name="opp_analysis"),
    re_path(r'^analysis/tableapi$', views.get_opptable_info, name="opp_tableapi"),
    re_path(r'^analysis/allapi$', views.get_opp_info, name="opp_allapi"),
    re_path(r'^analysis/api$', views.get_oppt_info_single, name="opp_api"),

    re_path(r'^dingding/government/center$', views.dingding_government_center, name="dingding_government_center"),
    re_path(r'^dingding/government/center/tab$', views.dingding_government_center_tab, name="dingding_government_center_tab"),
    re_path(r'^dingding/government/center/table$', views.dingding_government_center_table, name="dingding_government_center_table"),

    re_path(r'^dingding/department/frame/api$', views.dingding_department_frame_api, name="dingding_department_frame_api"),
    re_path(r'^dingding/region/frame/members/api$', views.dingding_region_frame_members_api, name="dingding_region_frame_members_api"),
    re_path(r'^dingding/department/frame/members/api$', views.dingding_department_frame_members_api, name="dingding_department_frame_members_api"),

    re_path(r'^customer/count/sale/center/api$', views.customer_count_sale_center_api, name="customer_count_sale_center_api"),
    re_path(r'^customer/count/region/api$', views.customer_count_region_api, name="customer_count_region_api"),
    re_path(r'^customer/count/department/api$', views.customer_count_department_api, name="customer_count_department_api"),
    re_path(r'^customer/count/saler/api$', views.customer_count_saler_api, name="customer_count_saler_api"),
    re_path(r'^work/daily/department/api$', views.work_daily_department_api, name="work_daily_department_api"),
    re_path(r'^work/daily/department/salers/api$', views.work_daily_department_salers_api, name="work_daily_department_salers_api"),
    re_path(r'^payment/department/days/api$', views.payment_department_days_api, name="payment_department_days_api"),
    re_path(r'^goal/regions/month/api$', views.goal_regions_month_api, name="goal_regions_month_api"),
    re_path(r'^goal/departments/month/api$', views.goal_departments_month_api, name="goal_departments_month_api"),
    re_path(r'^goal/salers/month/api$', views.goal_salers_month_api, name="goal_salers_month_api"),
    re_path(r'^account/count/api$', views.account_count_api, name="account_count_api"),
    re_path(r'^products/account/count/api$', views.products_account_count_api, name="products_account_count_api"),
    re_path(r'^opportunity/count/api$', views.opportunity_count_api, name="opportunity_count_api"),

    re_path(r'^department/info/api$', views.department_info_api, name="department_info_api"),
    re_path(r'^saler/info/api$', views.saler_info_api, name="saler_info_api"),
    re_path(r'^work/daily/saler/api$', views.work_daily_saler_api, name="work_daily_saler_api"),
    re_path(r'^goal/saler/month/api$', views.goal_saler_month_api, name="goal_saler_month_api"),

    re_path(r'^customer/list/api$', views.customer_list_api, name="sale_customer_list_api"),
    re_path(r'^opportunity/list/api$', views.opportunity_list_api, name="sale_opportunity_list_api"),
    re_path(r'^opportunity$', views.opportunity_info_api, name="sale_opportunity_api"),
    re_path(r'^opportunity/info/api$', views.opportunity_info_api, name="sale_opportunity_info_api"),

    re_path(r'^test$', views.test, name="test"),
    re_path(r'^department/info/api$', views.department_info_api, name="department_info_api"),
    re_path(r'^tenders/info/api$', views.Tenders.as_view(), name="tenders_info_api"),

    re_path(r'^saler/kpi/overview$', views.saler_kpi_overview, name="saler_kpi_overview"),
    re_path(r'^saler/kpi/overview/api$', views.saler_kpi_overview_api, name="saler_kpi_overview_api"),
    re_path(r'^saler/kpi/month$', views.saler_kpi_month, name="saler_kpi_month"),
    re_path(r'^saler/kpi/month/api$', views.saler_kpi_month_api, name="saler_kpi_month_api"),
    re_path(r'^saler/kpi/month/export$', views.export_saler_kpi_month, name="export_saler_kpi_month"),
    re_path(r'^saler/kpi/history$', views.saler_kpi_history, name="saler_kpi_history"),
    re_path(r'^saler/kpi/history/api$', views.saler_kpi_history_api, name="saler_kpi_history_api"),
    re_path(r'^saler/kpi/history/export$', views.export_saler_kpi_history, name="export_saler_kpi_history"),
]

app_name = "sale"
