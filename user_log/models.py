from django.db import models


class NewUserLog(models.Model):
    id = models.AutoField(primary_key=True)
    ctime = models.DateTimeField(verbose_name="操作日期", auto_now_add=True)
    model = models.CharField(verbose_name="Model", null=True, blank=True, max_length=255)
    object_id = models.IntegerField(null=True, blank=True)
    object_repr = models.CharField(null=True, blank=True, max_length=255)
    action = models.CharField(verbose_name="动作", null=True, blank=True, max_length=255)
    message = models.CharField(verbose_name="详情", null=True, blank=True, max_length=1023)
    user_id = models.IntegerField(verbose_name="用户ID", null=True, blank=True)
    username = models.CharField(verbose_name="用户名", null=True, blank=True, max_length=255)

    class Meta:
        db_table = 'user_log'
        verbose_name = "用户操作记录"
        verbose_name_plural = verbose_name
        managed = False



