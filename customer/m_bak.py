develop
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Paymentplan(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    stage = models.BigIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    plantime = models.CharField(db_column='planTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    contractid = models.BigIntegerField(db_column='contractId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    accountid = models.BigIntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(blank=True, null=True)
    totalamount = models.FloatField(db_column='totalAmount', blank=True, null=True)  # Field name made lowercase.
    actualamount = models.FloatField(db_column='actualAmount', blank=True, null=True)  # Field name made lowercase.
    status = models.BigIntegerField(blank=True, null=True)
    overduestatus = models.BigIntegerField(db_column='overdueStatus', blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.BigIntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.BigIntegerField(db_column='applicantId', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.BigIntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.CharField(db_column='dbcVarchar1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.CharField(db_column='dbcVarchar5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.FloatField(db_column='dbcReal2', blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.CharField(db_column='dbcDate6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.CharField(db_column='dbcVarchar6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.CharField(db_column='dbcVarchar7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.TextField(db_column='dbcVarchar8', blank=True, null=True)  # Field name made lowercase.
    dbcdate7 = models.CharField(db_column='dbcDate7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.TextField(db_column='dbcVarchar9', blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.CharField(db_column='dbcVarchar10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.TextField(db_column='dbcVarchar11', blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.CharField(db_column='dbcVarchar13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.CharField(db_column='dbcVarchar14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.CharField(db_column='dbcVarchar15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar16 = models.CharField(db_column='dbcVarchar16', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate8 = models.CharField(db_column='dbcDate8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.CharField(db_column='dbcJoin2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal7 = models.CharField(db_column='dbcReal7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.CharField(db_column='dbcVarchar2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.CharField(db_column='dbcJoin3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.BigIntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcdate9 = models.CharField(db_column='dbcDate9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate10 = models.CharField(db_column='dbcDate10', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentplan'
