
from django import forms
from customer.utils import get_states
from competitor.utils import *
import datetime

from public.config import problem_content1


class VisitSelectForm(forms.Form):
    '''签到总览的地图中筛选form表单'''
    saler = forms.CharField(label='商务：', max_length=100, required=False, widget=forms.TextInput())
    activity_start = forms.CharField(label='签到开始日期：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    activity_finish = forms.CharField(label='签到结束日期：', max_length=100, required=False, widget=forms.TextInput(
        attrs={"placeholder": "----------"}
    ))
    no_service_time = forms.CharField(label='无竞品服务日期：', required=False, widget=forms.CheckboxInput())
    # department = forms.CharField(label='部门：', max_length=100, required=False, widget=forms.TextInput())
    department = forms.CharField(label='部门：', max_length=100,required=False, widget=forms.TextInput(
        attrs={
            "id": "department-value",
            "type": "text",
        }
    ))

    # department1 = forms.CharField(label='部门：', max_length=100, required=False, widget=forms.Select(
    #     choices=[("", "全部")],
    #     attrs={
    #         "id": "department-1",
    #         "type": "text",
    #         "class": "form-control",
    #         "style": "padding-top: 2px;",
    #         "onchange": "onDepartmentChange1()"
    #     }
    # ))

    # department2 = forms.CharField(label='二级部门：', max_length=100, required=False, widget=forms.Select(
    #     choices=[("", "全部")],
    #     attrs={
    #         "id": "department-2",
    #         "type": "text",
    #         "class": "form-control",
    #         "style": "padding-top: 2px;",
    #         "onchange": "onDepartmentChange2()"
    #     }
    # ))
    #
    # department3 = forms.CharField(label='三级部门：', max_length=100, required=False, widget=forms.Select(
    #     choices=[("", "全部")],
    #     attrs={
    #         "id": "department-3",
    #         "type": "text",
    #         "class": "form-control",
    #         "style": "padding-top: 2px;",
    #         "onchange": "onDepartmentChange3()"
    #     }
    # ))

    problem_type = forms.CharField(label='签到问题：', max_length=100, required=False, widget=forms.Select(
        choices=[("", "全部")],
        attrs={
            "id": "problem_type",
            "type": "text",
            "class": "form-control",
            "style": "padding-top: 2px;"
        }
    ))


    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['lang_code'].widget.choices = [("", "--------")] + language_list
        self.fields['activity_start'].value = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d")
        self.fields['activity_finish'].value = datetime.datetime.now().strftime("%Y-%m-%d")
        self.fields['problem_type'].widget.choices = [("", "全部")] + [(k,v) for k,v in problem_content1.items()]

    # 设置商务
    def input_saler(self,saler):
        self.initial["saler"] = saler

    # 设置最终的部门id
    def select_department(self,department):
        self.initial["department"] = department

    # 设置签到开始日期
    def input_activity_start(self,activity_start):
        self.initial['activity_start'] = activity_start

    # 设置签到结束日期
    def input_activity_finish(self,activity_finish):
        self.initial['activity_finish'] = activity_finish

    # 设置页面展示的一级部门
    def input_department1(self,department1):
        self.initial['department1'] = department1

    # 设置页面展示的二级部门
    def input_department2(self,department2):
        self.initial['department2'] = department2

    # 设置页面展示的三级部门
    def input_department3(self,department3):
        self.initial['department3'] = department3



