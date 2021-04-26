from django import forms

"""微信群消息推送表单"""
class WechatMessagePushForm(forms.Form):
    customerIds = forms.CharField(label='客户Ids：', max_length=255, required=False, widget=forms.TextInput())
    pushType = forms.CharField(label='推送多少客户：', required=True, widget=forms.Select(
        choices=[("1", "单独1个"), ("2", "批量"), ("3", "全部")], 
        attrs={"type": "text", "class": "form-control", "style": "padding-top: 2px;"}
    ))
    fileId = forms.CharField(label='文件ID：', required=False, widget=forms.TextInput())#当选择从资料库里面选择文件向微信群推送时
    messageType = forms.CharField(label='消息类型：', required=False, widget=forms.TextInput())#1，文本 2，图片 3，音频 4，视频
    messageTitle = forms.CharField(label='消息标题：', required=False, widget=forms.TextInput())
    messageContent = forms.CharField(label='消息内容：', required=True, widget=forms.TextInput())
    messageUrl = forms.CharField(label='消息链接：', required=False, widget=forms.TextInput())
    