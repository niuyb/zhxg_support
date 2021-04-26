from django.db import models
from django.contrib.auth import get_user_model

from notice.apps import NoticeConfig

# Create your models here.

User = get_user_model()

"""通知消息的类型"""
class NoticeType(models.Model):
    name = models.CharField(verbose_name="钉钉通知的类型名称", unique=True, max_length=255, blank=True, null=True)
    comment = models.CharField(verbose_name="关于此消息类型的具体描述", max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notice_type'
        verbose_name = "钉钉通知类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

"""消息通知设置"""
class NoticeSetting(models.Model):
    # ding_id = models.CharField(verbose_name="钉钉用户ID", max_length=255, blank=True, null=True)
    ding_user = models.ForeignKey(User, to_field="dtalkid", verbose_name="钉钉用户", blank=True, null=True, on_delete=models.DO_NOTHING) #这条消息设置属于谁
    notice_type = models.ForeignKey(NoticeType, db_column="notice_type", verbose_name="消息类型", blank=True, null=True, on_delete=models.DO_NOTHING)
    status = models.IntegerField(verbose_name="是否接收消息", choices=NoticeConfig.notice_setting_status_choices, blank=True, null=True)# 0、关闭，1、开启

    class Meta:
        managed = True
        db_table = 'notice_setting'
        verbose_name = "钉钉通知设置"
        verbose_name_plural = verbose_name

"""消息详情列表"""
class NoticeList(models.Model):
    # ding_id = models.CharField(verbose_name="钉钉用户ID", max_length=255, blank=True, null=True)
    ding_user = models.ForeignKey(User, to_field="dtalkid", verbose_name="钉钉用户", blank=True, null=True, on_delete=models.DO_NOTHING) # 消息发送给谁
    content = models.TextField(verbose_name="消息内容", blank=True, null=True)
    notice_type = models.ForeignKey(NoticeType, db_column="notice_type", verbose_name="消息类型", blank=True, null=True, on_delete=models.DO_NOTHING)
    object_type = models.IntegerField(verbose_name="关联对像的类型", blank=True, null=True)
    object_id = models.IntegerField(verbose_name="关联对像的ID", blank=True, null=True)
    ctime = models.DateTimeField(verbose_name="发送时间", blank=True, null=True)
    # 0、不发送（对应用户已经设置了禁止钉钉发送通知的情况），1、发送成功，2、发送失败
    status = models.IntegerField(verbose_name="发送状态", choices=NoticeConfig.notice_sending_status_choices, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'notice_list'
        verbose_name = "钉钉通知列表"
        verbose_name_plural = verbose_name

