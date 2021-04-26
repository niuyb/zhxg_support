import datetime
from django import forms
from customer.utils import get_states
from user_log.utils import *



class userLogListSelectForm(forms.Form):
    '''操作日志列表页面的form表单'''
    operator = forms.CharField(label='操作人：', max_length=100, required=False, widget=forms.TextInput())
    operation_type = forms.CharField(label='操作类型：', required=False, widget=forms.Select(
        choices=[("", "操作类型")],
        attrs={
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    operator_model = forms.CharField(label='操作模块：', max_length=100, required=False, widget=forms.TextInput())
    operation_time_start = forms.CharField(label='操作开始日期：', max_length=100, required=False, widget=forms.TextInput())
    operation_time_finish = forms.CharField(label='操作结束日期：', max_length=100, required=False, widget=forms.TextInput())



    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['operation_type'].widget.choices = [("", "操作类型")] + get_user_action()
        # self.fields['operation_time_start'].value = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime(
        #     "%Y-%m-%d")
        # self.fields['operation_time_finish'].value = (datetime.datetime.now()).strftime(
        #     "%Y-%m-%d")
        self.fields['operation_time_start'].value = (datetime.date.today() - datetime.timedelta(days=7)).strftime(
            "%Y-%m-%d")
        self.fields['operation_time_finish'].value = (datetime.date.today()).strftime(
            "%Y-%m-%d")

