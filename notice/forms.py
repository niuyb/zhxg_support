import datetime

from django import forms
from django.core.exceptions import ValidationError

from public.utils import get_value_list
from notice.models import NoticeList, NoticeSetting, NoticeType
from notice.apps import NoticeConfig

"""钉钉通知消息筛选表单"""
class NoticeListSelectForm(forms.Form):
    ding_user = forms.CharField(label='用户：', max_length=100, required=False, widget=forms.TextInput())
    notice_type = forms.CharField(label='消息类型：', required=False, widget=forms.Select(
        choices=[("", "--------")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    content = forms.CharField(label='消息内容：', max_length=100, required=False, widget=forms.TextInput())
    department = forms.CharField(label='部门：', max_length=100, required=False, widget=forms.TextInput())
    status = forms.CharField(label='发送状态：', required=False, widget=forms.Select(
        choices=[("", "--------")] + list(NoticeConfig.notice_sending_status_choices), 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notice_type'].widget.choices = [("", "--------")] + get_value_list(NoticeType, {}, ["id", "name"])

"""消息设置表单"""
class NoticeSettingForm(forms.Form):
    ding_user_id = forms.CharField(label='用户钉ID', required=False)
    notice_type_id = forms.CharField(label='消息类型：', required=True, widget=forms.Select(
        choices=[("", "--------")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    status = forms.IntegerField(label="是否接收消息", required=True)

    # 重写父类的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notice_type_id'].widget.choices = [("", "--------")] + get_value_list(NoticeType, {}, ["id", "name"])
