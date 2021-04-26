
from django import forms
from customer.utils import get_states
from competitor.utils import *


class CompetitorSelectForm(forms.Form):
    '''竞品签约客户列表发筛选form表单'''
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

    competitor_name = forms.CharField(label='竞品名称：', max_length=100, required=False,
                                      widget=forms.TextInput(attrs={"class":"form-control","placeholder":"模糊查询"}))
    saler = forms.CharField(label='商务：', max_length=100, required=False, widget=forms.TextInput())
    service_time_start = forms.CharField(label='竞品服务开始日期：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    service_time_finish = forms.CharField(label='竞品服务结束日期：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    no_service_time = forms.CharField(label='无竞品服务日期：', required=False, widget=forms.CheckboxInput())
    department = forms.CharField(label='部门：', max_length=100, required=False, widget=forms.TextInput())

    competitorId = forms.CharField(label='竞品名称：', required=False, widget=forms.Select(
        choices=[("", "--------")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
        }
    ))
    competitorProductId = forms.CharField(label='签单产品：', required=False, widget=forms.Select(
        choices=[("", "--------")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
        }
    ))
    industry_1 = forms.CharField(label='一级行业：', required=False, widget=forms.Select(
        choices=[("", "全部")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            "onchange": "onIndustryChange1()"
        }
    ))
    industry_2 = forms.CharField(label='二级行业：', required=False, widget=forms.Select(
        choices=[("", "全部")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;"
        }
    ))
    # industry1 = forms.CharField(label='一级行业：', max_length=100, required=False, widget=forms.TextInput())
    # industry2 = forms.CharField(label='二级行业：', max_length=100, required=False, widget=forms.TextInput())

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['lang_code'].widget.choices = [("", "--------")] + language_list
        self.fields['customer_province'].widget.choices = [("", "全国")] + get_states()
        self.fields['competitorId'].widget.choices = [("", "全部")] + get_competitor()
        self.fields['competitorProductId'].widget.choices = [("", "全部")] + get_product()

        self.fields['industry_1'].widget.choices = [("", "全部")] + get_industry_l1_list()
        self.fields['industry_2'].widget.choices = [("", "全部")] + get_industry_l2_list()

    def select_province(self,id):
        # 默认省份为河北省
        self.initial["customer_province"] = id

    def input_competitorName(self,name):
        # 根据请求带的条件赋值
        self.initial['competitor_name'] = name

    def select_industry1(self,id):
        # 根据行业id设置行业
        self.initial["industry_1"] = id

    def select_industry2(self,id):
        # 根据行业id设置行业
        self.initial["industry_2"] = id



class CompetitorListSelectForm(forms.Form):
    '''竞品列表页面的form表单'''
    competitor_name = forms.CharField(label='竞品名称：', max_length=100, required=False, widget=forms.TextInput())
    customer_name = forms.CharField(label='客户名称：', max_length=100, required=False, widget=forms.TextInput())
    customer_province = forms.CharField(label='签单地域：', required=False, widget=forms.Select(
        choices=[("", "全国")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    industry_1 = forms.CharField(label='一级行业：', required=False, widget=forms.Select(
        choices=[("", "全部")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            "onchange": "onDepartmentChange1()"
            }
    ))
    industry_2 = forms.CharField(label='二级行业：', required=False, widget=forms.Select(
        choices=[("", "全部")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            # "onchange": "onDepartmentChange1()"
        }
    ))
    # industry1 = forms.CharField(label='一级行业：', max_length=100, required=False, widget=forms.TextInput())
    # industry2 = forms.CharField(label='二级行业：', max_length=100, required=False, widget=forms.TextInput())

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_province'].widget.choices = [("", "全国")] + get_states()
        self.fields['industry_1'].widget.choices = [("", "全部")] + get_industry_l1_list()
        self.fields['industry_2'].widget.choices = [("", "全部")] + get_industry_l2_list()

    def select_province(self,id):
        # 根据id设置省份
        self.initial["customer_province"] = id

    def select_industry1(self,id):
        # 根据行业id设置行业
        self.initial["industry_1"] = id

    def select_industry2(self,id):
        # 根据行业id设置行业
        self.initial["industry_2"] = id

    def input_competitorName(self,name):
        # 根据请求带的条件赋值
        self.initial['competitor_name'] = name


    def input_customerName(self, name):
        # 根据请求带的条件赋值
        self.initial['customer_name'] = name