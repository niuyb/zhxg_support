# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# python manage.py inspectdb  --database  contract_33 crm_competitor_map competitor >competitor/models_bak.py

from django.db import models


class CrmCompetitorMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    accountid = models.BigIntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    competitorid = models.BigIntegerField(db_column='competitorId', blank=True, null=True)  # Field name made lowercase.
    competitorproductid = models.BigIntegerField(db_column='competitorProductId', blank=True, null=True)  # Field name made lowercase.
    competitormoney = models.FloatField(db_column='competitorMoney', blank=True, null=True)  # Field name made lowercase.
    competitorstartdate = models.CharField(db_column='competitorStartDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    competitorfindate = models.CharField(db_column='competitorFinDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountstatus = models.IntegerField(db_column='accountStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_competitor_map'


class Competitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    competitorid = models.BigIntegerField(db_column='competitorId', blank=True, null=True)  # Field name made lowercase.
    competitorname = models.CharField(db_column='competitorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    competitorproductid = models.BigIntegerField(db_column='competitorProductId', blank=True, null=True)  # Field name made lowercase.
    competitorproduct = models.CharField(db_column='competitorProduct', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competitor'
