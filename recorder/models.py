# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WkTUseractivity(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=255)
    status = models.IntegerField()
    genre = models.IntegerField()
    activity = models.IntegerField()
    self = models.IntegerField()
    other = models.IntegerField()
    backendjump = models.IntegerField()
    saler = models.CharField(max_length=255)
    saler_frame = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    regdate = models.CharField(max_length=255, blank=True, null=True)
    trysdate = models.CharField(max_length=255, blank=True, null=True)
    saler_frame_id = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    activity_self = models.IntegerField(blank=True, null=True)
    wechat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_USERACTIVITY'