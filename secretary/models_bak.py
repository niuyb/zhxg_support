# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SalesPortraitSaler(models.Model):
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    positionname = models.CharField(db_column='positionName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departname_x = models.CharField(db_column='departName_x', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departname_y = models.CharField(db_column='departName_y', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dtalkid = models.CharField(db_column='Dtalkid', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(max_length=100, blank=True, null=True)
    hireddate = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(db_column='workPlace', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales_portrait_saler'
