import datetime

from django import forms
from django.core.exceptions import ValidationError

from customer.utils import get_provinces, get_states

"""商务人员列表筛选表单"""
class SalerListSelectForm(forms.Form):
    username = forms.CharField(label='姓名：', max_length=100, required=False, widget=forms.TextInput())
    department = forms.CharField(label='部门：', max_length=100, required=False, widget=forms.TextInput())

"""客户活跃度统计筛选表单"""
class PaymentPlanListSelectForm(forms.Form):
    account_name = forms.CharField(label='账号名称：', max_length=100, required=False, widget=forms.TextInput())
    account_status = forms.CharField(label='账号状态：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("0", "正式"), ("1", "试用"), ("2", "停用"), ("-1", "弃用")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    overdue = forms.CharField(label='逾期状态：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("1", "已逾期"), ("0", "未逾期")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    overdue_days = forms.IntegerField(label='逾期天数：', required=False, widget=forms.TextInput())
    saler = forms.CharField(label='商务：', max_length=100, required=False, widget=forms.TextInput())
    plantime_start = forms.CharField(label='计划回款日期-从：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    plantime_end = forms.CharField(label='计划回款日期-止：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    no_plantime = forms.CharField(label='无计划回款日期：', required=False, widget=forms.CheckboxInput())
    activity_start = forms.CharField(label='活跃开始日期：', max_length=100, required=False, widget=forms.TextInput())
    activity_finish = forms.CharField(label='活跃结束日期：', max_length=100, required=False, widget=forms.TextInput())
    customer_name = forms.CharField(label='客户名称：', max_length=100, required=False, widget=forms.TextInput())
    customer_province = forms.CharField(label='客户地域-省：', required=False, widget=forms.Select(
        choices=[("", "--------")], 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    # customer_city = forms.CharField(label='客户地域-市：', required=False, widget=forms.Select(
    #     choices=[("", "--------")], 
    #     attrs={
    #         "type": "text", 
    #         "class": "form-control", 
    #         "style": "padding-top: 2px;",
    #         "onchange": "onCityChange()"
    #     }
    # ))
    # customer_county = forms.CharField(label='客户地域-县：', required=False, widget=forms.Select(
    #     choices=[("", "--------")], 
    #     attrs={
    #         "type": "text", 
    #         "class": "form-control", 
    #         "style": "padding-top: 2px;",
    #     }
    # ))
    department = forms.CharField(label='部门：', max_length=100, required=False, widget=forms.TextInput())

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["product_type"].value = 1
        self.fields['customer_province'].widget.choices = [("", "--------")] + get_provinces()
        # self.fields['quzong_ok_start'].value = "----------"
        # self.fields['quzong_ok_finish'].value = "----------"
        self.fields['activity_start'].value = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        self.fields['activity_finish'].value = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # 默认账号状态是试用
        self.fields['account_status'].value = "1"
        # self.initial["account_status"] = "1"
        # self.fields['login_days'].value = 3
        # self.fields['login_days'].min = 0
        # self.fields['login_days'].max = 180
