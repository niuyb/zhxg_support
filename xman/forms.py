from django import forms
from django.core.exceptions import ValidationError

class UserNewForm(forms.Form):
    username = forms.CharField(label='用户名：', max_length=100, required=True, widget=forms.TextInput())
    password = forms.CharField(label='密码：', max_length=100, required=True, widget=forms.TextInput())
    email = forms.CharField(label='邮箱：', max_length=100, required=False, widget=forms.TextInput())
    mobile = forms.CharField(label='手机号：', max_length=100, required=True, widget=forms.TextInput())
    dtalkid = forms.CharField(label='钉钉ID：', max_length=100, required=True, widget=forms.TextInput())
    avatar = forms.CharField(label='头像：', max_length=255, required=False, widget=forms.TextInput())
    dingframe = forms.CharField(label='部门：', max_length=100, required=True, widget=forms.TextInput())
    position = forms.CharField(label='职位：', max_length=100, required=False, widget=forms.TextInput())
    is_superuser = forms.IntegerField(label='超级管理员：', required=True, widget=forms.TextInput())
    is_staff = forms.IntegerField(label="后台管理：", required=True, widget=forms.TextInput())
    status = forms.CharField(label='用户状态：', required=True, widget=forms.Select(
        choices=[("1", "1"), ("2", "2"), ("3", "3")], 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    # gids = forms.CharField(label='分组：', max_length=255, required=False, widget=forms.TextInput())
    # pids = forms.CharField(label='权限：', max_length=255, required=False, widget=forms.TextInput())

class UserChangeForm(forms.Form):
    id = forms.IntegerField(label='用户ID：', required=True, widget=forms.TextInput())
    username = forms.CharField(label='用户名：', max_length=100, required=True, widget=forms.TextInput())
    email = forms.CharField(label='邮箱：', max_length=100, required=False, widget=forms.TextInput())
    mobile = forms.CharField(label='手机号：', max_length=100, required=True, widget=forms.TextInput())
    dtalkid = forms.CharField(label='钉钉ID：', max_length=100, required=True, widget=forms.TextInput())
    avatar = forms.CharField(label='头像：', max_length=255, required=False, widget=forms.TextInput())
    dingframe = forms.CharField(label='部门：', max_length=100, required=True, widget=forms.TextInput())
    position = forms.CharField(label='职位：', max_length=100, required=False, widget=forms.TextInput())
    is_superuser = forms.IntegerField(label='超级管理员', required=True, widget=forms.TextInput())
    is_staff = forms.IntegerField(label="后台管理", required=True, widget=forms.TextInput())
    status = forms.CharField(label='用户状态：', required=True, widget=forms.Select(
        choices=[("1", "1"), ("2", "2"), ("3", "3")], 
        attrs={
            "type": "text", 
            "class": "form-control", 
            "style": "padding-top: 2px;",
            # "onchange": "onProvinceChange()"
            }
    ))
    # gids = forms.CharField(label='分组：', max_length=255, required=False, widget=forms.TextInput())
    # pids = forms.CharField(label='权限：', max_length=255, required=False, widget=forms.TextInput())

