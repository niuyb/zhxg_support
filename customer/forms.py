import datetime

from django import forms
from django.core.exceptions import ValidationError

# from customer.models import (Opportunity)
from customer.utils import get_provinces, get_states, get_industry_data_1
# from customer.utils import get_cities, get_counties as get_districts
from customer.models import CrmIndustryL1, CrmIndustryL2

"""客户活跃度统计筛选表单"""
class ActivitySelectForm(forms.Form):
    product_type = forms.CharField(label='产品类别：', required=True, widget=forms.Select(
        choices=[("1", "舆情秘书"), ("2", "态势感知"), ("3", "智慧网评")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    account_name = forms.CharField(label='账号名称：', max_length=100, required=False, widget=forms.TextInput())
    account_status = forms.CharField(label='账号状态：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("0", "正式"), ("1", "试用"), ("2", "停用"), ("-1", "弃用")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    sale_sure = forms.CharField(label='销售确认：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("1", "承诺"), ("2", "争取"), ("4", "跟进"), ("0", "无")],
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    # 勾选了此筛选项之后，将在活跃日志数据查询时，加入账号状态条件筛选
    account_status_history = forms.CharField(label='是否查询账号历史状态：', required=False, widget=forms.CheckboxInput())

    login_days = forms.IntegerField(label='登录天数：', required=True, widget=forms.TextInput())
    saler = forms.CharField(label='商务：', max_length=100, required=False, widget=forms.TextInput())
    team = forms.CharField(label='是否属于商机团队成员：', required=False, widget=forms.CheckboxInput())
    maint = forms.CharField(label='是否属于账号维护人员：', required=False, widget=forms.CheckboxInput())
    quzong_ok_start = forms.CharField(label='区总确认合同归档日期开始：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    quzong_ok_finish = forms.CharField(label='区总确认合同归档日期结束：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    # 勾选此选项后，区总确认合同归档日期将为空，即筛选区总确认合同归档日期为空的数据
    no_quzong_ok = forms.CharField(label='无区总确认：', required=False, widget=forms.CheckboxInput())

    activity_start = forms.CharField(label='活跃开始日期：', max_length=100, required=False, widget=forms.TextInput())
    activity_finish = forms.CharField(label='活跃结束日期：', max_length=100, required=False, widget=forms.TextInput())
    ctime_start = forms.CharField(label='账号注册日期开始：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}))
    ctime_finish = forms.CharField(label='账号注册日期截止：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}))
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
    industry_l1 = forms.CharField(label='一级行业：', max_length=100, required=False, widget=forms.Select(
        choices=[("", "--------")], 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    industry_l2 = forms.CharField(label='二级行业：', max_length=100, required=False, widget=forms.TextInput())

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product_type"].value = 1
        self.fields['customer_province'].widget.choices = [("", "--------")] + get_provinces()
        self.fields['industry_l1'].widget.choices = [("", "--------")] + get_industry_data_1()
        # self.fields['quzong_ok_start'].value = "----------"
        # self.fields['quzong_ok_finish'].value = "----------"
        self.fields['activity_start'].value = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        self.fields['activity_finish'].value = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # 默认账号状态是试用
        self.fields['account_status'].value = "1"
        # 默认包含商机团队成员
        self.fields['team'].value = "1"
        # 默认包含账号维护人员
        self.fields['maint'].value = "1"
        # self.initial["account_status"] = "1"
        self.fields['login_days'].value = 3
        self.fields['login_days'].min = 0
        self.fields['login_days'].max = 180

"""行业覆盖率筛选表单"""
class IndustryCoverageSelectForm(forms.Form):
    location = forms.CharField(label='客户地域：', required=False, widget=forms.Select(
        choices=[("", "--------")], 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    
    # # 省、市、县三级
    # state = forms.CharField(label='客户省份：', required=False, widget=forms.TextInput())
    # city = forms.CharField(label='客户市：', required=False, widget=forms.TextInput())
    # district = forms.CharField(label='客户区县：', required=False, widget=forms.TextInput())

    industry1 = forms.CharField(label='一级行业：', max_length=100, required=False, widget=forms.TextInput())
    industry2 = forms.CharField(label='二级行业：', max_length=100, required=False, widget=forms.TextInput())

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.choices = [("", "--------")] + get_states()

"""政府行业覆盖率筛选表单"""
class GovernmentIndustryCoverageSelectForm(forms.Form):
    # 获取一级行业（政府）
    def get_industry1_choices():
        industry1_choices = []
        industrys = list(CrmIndustryL1.objects.filter(name="政府").values("id", "name"))
        for industry in industrys:
            industry1_choices.append([industry["id"], industry["name"]])
        return industry1_choices

    # 获取二级行业（公安局、宣传部）
    def get_industry2_choices():
        industry2_choices = [["", "--------"]]
        industrys = list(CrmIndustryL2.objects.filter(name__in=["公安局", "宣传部"]).values("id", "name"))
        for industry in industrys:
            industry2_choices.append([industry["id"], industry["name"]])
        return industry2_choices
    
    # 省、市、县三级
    state = forms.CharField(label='客户省份：', required=False, widget=forms.TextInput())
    city = forms.CharField(label='客户市：', required=False, widget=forms.TextInput())
    district = forms.CharField(label='客户区县：', required=False, widget=forms.TextInput())

    industry1 = forms.CharField(label='一级行业：', max_length=100, required=False, widget=forms.Select(
        choices=get_industry1_choices(), 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            "disabled": "disabled"
            # "onchange": "onProvinceChange()"
            }
    ))
    industry2 = forms.CharField(label='二级行业：', max_length=100, required=False, widget=forms.Select(
        choices=get_industry2_choices(), 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))

"""客户查询筛选表单"""
class CustomerListSelectForm(forms.Form):
    customer_name = forms.CharField(label='客户名称：', max_length=100, required=False, widget=forms.TextInput())
    coverage = forms.CharField(label='是否覆盖：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("1", "是"), ("0", "否")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    status = forms.CharField(label='客户状态：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("2", "正式"), ("1", "试用"), ("0", "其他")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))

    # wechat_group 参数：0、未绑定 1、申请中 2、审核中 3、已绑定 4、绑定失败
    wechat_group = forms.CharField(label='微信群状态：', required=False, widget=forms.Select(
        choices=[("", "--------"), ("0", "未绑定"), ("1", "申请中"), ("2", "审核中"), ("3", "已绑定"), ("4", "绑定失败")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))

    # location 省、市、县三级
    state = forms.CharField(label='客户省份：', required=False, widget=forms.TextInput())
    city = forms.CharField(label='客户市：', required=False, widget=forms.TextInput())
    district = forms.CharField(label='客户区县：', required=False, widget=forms.TextInput())

    industry1 = forms.CharField(label='一级行业：', max_length=100, required=False, widget=forms.TextInput())
    industry2 = forms.CharField(label='二级行业：', max_length=100, required=False, widget=forms.TextInput())

    # # 重写父类的 __init__ 方法
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['state'].widget.choices = [("", "--------")] + get_states()
        # self.fields['city'].widget.choices = [("", "--------")] + get_cities()
        # self.fields['district'].widget.choices = [("", "--------")] + get_districts()

