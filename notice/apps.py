from django.apps import AppConfig


class NoticeConfig(AppConfig):
    name = 'notice'
    notice_sending_status_choices = (
        (0, "不发送"), (1, "发送成功"), (2, "发送失败")
    )
    notice_setting_status_choices = (
        (0, "关闭"), (1, "开启")
    )
