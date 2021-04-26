from django.db import models

# Create your models here.

"""客户-微信群-关系表"""
class CrmWechatMapping(models.Model):
    # customer_id = models.BigIntegerField()#客户ID
    customer_id = models.CharField(max_length=255)  # 客户ID
    wechat_group_id = models.CharField(max_length=255)#微信群ID
    ctime = models.CharField(max_length=255)#绑定时间
    # ctime = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField()#绑定状态
    istarshine_id = models.CharField(max_length=255)#操作者
    extend_id = models.CharField(max_length=100, blank=True, null=True)#备用字段
    task_id = models.CharField(max_length=100, blank=True, null=True)#微信群绑定的任务ID，接收自卢达

    class Meta:
        managed = False
        db_table = 'crm_wechat_mapping'

"""微信群消息表"""
class WechatGroupMessage(models.Model):
    customer_id = models.BigIntegerField(blank=True, null=True)
    wechat_group_id = models.CharField(max_length=100)
    wechat_group_nick = models.CharField(max_length=100, blank=True, null=True)
    wechat_id = models.CharField(max_length=100, blank=True, null=True)
    wechat_nick = models.CharField(max_length=100, blank=True, null=True)
    wechat_head_img = models.TextField()
    content = models.TextField()
    type = models.IntegerField(blank=True, null=True)
    data_ex = models.TextField()
    task_id = models.CharField(max_length=100, blank=True, null=True)
    extend_id = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.IntegerField(blank=True, null=True)
    receive_or_send = models.IntegerField(default=1)# 1、收消息，0、发消息
    status = models.IntegerField(blank=True, null=True)#消息是否发送成功
    description = models.CharField(max_length=255, blank=True, null=True)
    istarshine_id = models.CharField(max_length=255, blank=True, null=True)#推送预警信息的实际操作者    
    is_read = models.IntegerField(blank=True, null=True)#消息是否已读

    class Meta:
        managed = False
        db_table = 'wechat_group_message'
