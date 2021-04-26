# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
### 33

class SalesOrderDetail(models.Model):
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=100, blank=True, null=False,primary_key=True)  # Field name made lowercase.
    order_onfile_time = models.CharField(max_length=100, blank=True, null=True)
    total_performance = models.FloatField(blank=True, null=True)
    accountname = models.CharField(db_column='accountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    crm_industry_l1 = models.CharField(max_length=100, blank=True, null=True)
    crm_industry_l2 = models.CharField(max_length=100, blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    concode = models.CharField(max_length=100, blank=True, null=True)
    product_type1 = models.CharField(max_length=100, blank=True, null=True)
    product_type2 = models.CharField(max_length=100, blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    stopdate = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales_order_detail'


class SalesPortraitActivity(models.Model):
    activityid = models.CharField(db_column='activityId', primary_key=True, max_length=100)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    belongid = models.BigIntegerField(db_column='belongId', blank=True, null=True)  # Field name made lowercase.
    objectid = models.BigIntegerField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='entityType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    longitude = models.CharField(max_length=60, blank=True, null=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.CharField(db_column='opportunityId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    crm_longitude = models.CharField(max_length=60, blank=True, null=True)
    crm_latitude = models.CharField(max_length=60, blank=True, null=True)
    crm_address = models.TextField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales_portrait_activity'


class SalesPortraitCrm(models.Model):
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=False,primary_key=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fstate = models.IntegerField(db_column='fState', blank=True, null=True)  # Field name made lowercase.
    fcity = models.IntegerField(db_column='fCity', blank=True, null=True)  # Field name made lowercase.
    fdistrict = models.IntegerField(db_column='fDistrict', blank=True, null=True)  # Field name made lowercase.
    highseastatus = models.IntegerField(db_column='highSeaStatus', blank=True, null=True)  # Field name made lowercase.
    crm_industry_l1 = models.CharField(max_length=100, blank=True, null=True)
    crm_industry_l2 = models.CharField(max_length=100, blank=True, null=True)
    opp_num = models.IntegerField(blank=True, null=True)
    ms_num = models.IntegerField(blank=True, null=True)
    jt_num = models.IntegerField(blank=True, null=True)
    tsgz_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales_portrait_crm'


class SalesPortraitOpportunity(models.Model):
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.CharField(db_column='opportunityId', max_length=100, blank=True, null=False,primary_key=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.CharField(db_column='dbcVarchar12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    winrate = models.FloatField(db_column='winRate', blank=True, null=True)  # Field name made lowercase.
    salestageid = models.BigIntegerField(db_column='saleStageId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sales_portrait_opportunity'


class SalesPortraitOrder(models.Model):
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=100, blank=True, null=False,primary_key=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_status = models.IntegerField(blank=True, null=True)
    order_onfile_time = models.CharField(max_length=100, blank=True, null=True)
    total_performance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales_portrait_order'


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


class Account(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    accountname = models.TextField(db_column='accountName', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    parentaccountid = models.CharField(db_column='parentAccountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    industryid = models.IntegerField(db_column='industryId', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    longitude = models.CharField(max_length=60, blank=True, null=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zipcode = models.TextField(db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    weibo = models.TextField(blank=True, null=True)
    employeenumber = models.CharField(db_column='employeeNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    annualrevenue = models.CharField(db_column='annualRevenue', max_length=13, blank=True, null=True)  # Field name made lowercase.
    recentactivityrecordtime = models.CharField(db_column='recentActivityRecordTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    recentactivitycreatedby = models.CharField(db_column='recentActivityCreatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    highseaid = models.CharField(db_column='highSeaId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    highseaaccountsource = models.CharField(db_column='highSeaAccountSource', max_length=255, blank=True, null=True)  # Field name made lowercase.
    claimtime = models.CharField(db_column='claimTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    expiretime = models.CharField(db_column='expireTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    highseastatus = models.IntegerField(db_column='highSeaStatus', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    srcflg = models.IntegerField(db_column='srcFlg', blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.IntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.CharField(db_column='dbcReal2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.IntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcselect6 = models.IntegerField(db_column='dbcSelect6', blank=True, null=True)  # Field name made lowercase.
    dbcselect7 = models.IntegerField(db_column='dbcSelect7', blank=True, null=True)  # Field name made lowercase.
    isdisturb = models.CharField(db_column='isDisturb', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outterdepartid = models.CharField(db_column='outterDepartId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect8 = models.IntegerField(db_column='dbcSelect8', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.IntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcselect10 = models.IntegerField(db_column='dbcSelect10', blank=True, null=True)  # Field name made lowercase.
    dbcselect11 = models.IntegerField(db_column='dbcSelect11', blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.CharField(db_column='dbcRelation1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect12 = models.IntegerField(db_column='dbcSelect12', blank=True, null=True)  # Field name made lowercase.
    dbcselect13 = models.IntegerField(db_column='dbcSelect13', blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.CharField(db_column='dbcRelation2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.TextField(db_column='dbcVarchar5', blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.IntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.IntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar2 = models.CharField(db_column='dbcSVarchar2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.CharField(db_column='dbcVarchar7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.IntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.IntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.CharField(db_column='dbcRelation3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.IntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    totalwonopportunities = models.CharField(db_column='totalWonOpportunities', max_length=15, blank=True, null=True)  # Field name made lowercase.
    iscustomer = models.CharField(db_column='isCustomer', max_length=300, blank=True, null=True)  # Field name made lowercase.
    totalwonopportunityamount = models.CharField(db_column='totalWonOpportunityAmount', max_length=15, blank=True, null=True)  # Field name made lowercase.
    totalcontract = models.CharField(db_column='totalContract', max_length=15, blank=True, null=True)  # Field name made lowercase.
    totalactiveorders = models.CharField(db_column='totalActiveOrders', max_length=15, blank=True, null=True)  # Field name made lowercase.
    totalorderamount = models.CharField(db_column='totalOrderAmount', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accountscore = models.CharField(db_column='accountScore', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fstate = models.BigIntegerField(db_column='fState', blank=True, null=True)  # Field name made lowercase.
    fcity = models.BigIntegerField(db_column='fCity', blank=True, null=True)  # Field name made lowercase.
    fdistrict = models.BigIntegerField(db_column='fDistrict', blank=True, null=True)  # Field name made lowercase.
    leadid = models.BigIntegerField(db_column='leadId', blank=True, null=True)  # Field name made lowercase.
    releasetime = models.CharField(db_column='releaseTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    releasereason = models.BigIntegerField(db_column='releaseReason', blank=True, null=True)  # Field name made lowercase.
    ecouponsaccountlabel = models.CharField(db_column='ecouponsAccountLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class Account20190815(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    accountname = models.TextField(db_column='accountName', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    parentaccountid = models.CharField(db_column='parentAccountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    industryid = models.IntegerField(db_column='industryId', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    longitude = models.CharField(max_length=60, blank=True, null=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zipcode = models.TextField(db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    weibo = models.TextField(blank=True, null=True)
    employeenumber = models.CharField(db_column='employeeNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    annualrevenue = models.CharField(db_column='annualRevenue', max_length=13, blank=True, null=True)  # Field name made lowercase.
    recentactivityrecordtime = models.CharField(db_column='recentActivityRecordTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    recentactivitycreatedby = models.CharField(db_column='recentActivityCreatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    highseaid = models.CharField(db_column='highSeaId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    highseaaccountsource = models.CharField(db_column='highSeaAccountSource', max_length=255, blank=True, null=True)  # Field name made lowercase.
    claimtime = models.CharField(db_column='claimTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    expiretime = models.CharField(db_column='expireTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    highseastatus = models.IntegerField(db_column='highSeaStatus', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    srcflg = models.IntegerField(db_column='srcFlg', blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.IntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.CharField(db_column='dbcReal2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.IntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcselect6 = models.IntegerField(db_column='dbcSelect6', blank=True, null=True)  # Field name made lowercase.
    dbcselect7 = models.IntegerField(db_column='dbcSelect7', blank=True, null=True)  # Field name made lowercase.
    isdisturb = models.CharField(db_column='isDisturb', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outterdepartid = models.CharField(db_column='outterDepartId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect8 = models.IntegerField(db_column='dbcSelect8', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.IntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcselect10 = models.IntegerField(db_column='dbcSelect10', blank=True, null=True)  # Field name made lowercase.
    dbcselect11 = models.IntegerField(db_column='dbcSelect11', blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.CharField(db_column='dbcRelation1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect12 = models.IntegerField(db_column='dbcSelect12', blank=True, null=True)  # Field name made lowercase.
    dbcselect13 = models.IntegerField(db_column='dbcSelect13', blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.CharField(db_column='dbcRelation2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.TextField(db_column='dbcVarchar5', blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.IntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.IntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar2 = models.CharField(db_column='dbcSVarchar2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.CharField(db_column='dbcVarchar7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.IntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.IntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.CharField(db_column='dbcRelation3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.IntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    totalwonopportunities = models.CharField(db_column='totalWonOpportunities', max_length=15, blank=True, null=True)  # Field name made lowercase.
    iscustomer = models.CharField(db_column='isCustomer', max_length=300, blank=True, null=True)  # Field name made lowercase.
    totalwonopportunityamount = models.CharField(db_column='totalWonOpportunityAmount', max_length=15, blank=True, null=True)  # Field name made lowercase.
    totalcontract = models.CharField(db_column='totalContract', max_length=15, blank=True, null=True)  # Field name made lowercase.
    totalactiveorders = models.CharField(db_column='totalActiveOrders', max_length=15, blank=True, null=True)  # Field name made lowercase.
    totalorderamount = models.CharField(db_column='totalOrderAmount', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accountscore = models.CharField(db_column='accountScore', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fstate = models.BigIntegerField(db_column='fState', blank=True, null=True)  # Field name made lowercase.
    fcity = models.BigIntegerField(db_column='fCity', blank=True, null=True)  # Field name made lowercase.
    fdistrict = models.BigIntegerField(db_column='fDistrict', blank=True, null=True)  # Field name made lowercase.
    leadid = models.BigIntegerField(db_column='leadId', blank=True, null=True)  # Field name made lowercase.
    releasetime = models.CharField(db_column='releaseTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    releasereason = models.BigIntegerField(db_column='releaseReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account_20190815'

class AccountBack(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    accountname = models.TextField(db_column='accountName', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    longitude = models.CharField(max_length=60, blank=True, null=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    recentactivityrecordtime = models.CharField(db_column='recentActivityRecordTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.IntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.IntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.CharField(db_column='dbcRelation2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.IntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.CharField(db_column='dbcVarchar7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.CharField(db_column='dbcRelation3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.IntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account_back'


class Activityrecord(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    contactid = models.CharField(db_column='contactId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.BigIntegerField(db_column='dimDepart', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salestageid = models.CharField(db_column='saleStageId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    belongid = models.BigIntegerField(db_column='belongId', blank=True, null=True)  # Field name made lowercase.
    objectid = models.BigIntegerField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(max_length=60, blank=True, null=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    locationdetail = models.TextField(db_column='locationDetail', blank=True, null=True)  # Field name made lowercase.
    contactname = models.TextField(db_column='contactName', blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='contactPhone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    calllink = models.CharField(db_column='callLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.BigIntegerField(blank=True, null=True)
    intentionaldegree = models.BigIntegerField(db_column='intentionalDegree', blank=True, null=True)  # Field name made lowercase.
    needfollow = models.CharField(db_column='needFollow', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nextcalltime = models.CharField(db_column='nextCallTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation26 = models.BigIntegerField(db_column='dbcRelation26', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbctextarea1 = models.TextField(db_column='dbcTextarea1', blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbctextarea3 = models.TextField(db_column='dbcTextarea3', blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activityrecord'


class ActivityrecordMapping(models.Model):
    activityid = models.BigIntegerField(db_column='activityId', blank=True, null=True)  # Field name made lowercase.
    accountid = models.BigIntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.CharField(db_column='updateTime', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activityrecord_mapping'


class Apicount(models.Model):
    # id = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apiCount'


class ApprovalRecords(models.Model):
    model = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    status = models.IntegerField()
    record_name = models.CharField(max_length=50)
    get_month = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval_records'


class AreaMonthAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    area = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_month_achievement'


class AreaNewAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    area = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_new_achievement'


class AreaRenewAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    area = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_renew_achievement'


class ChanceCountCheck(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    target_name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    target = models.FloatField(blank=True, null=True)
    complete = models.FloatField(blank=True, null=True)
    per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chance_count_check'


class ChancePushCheck(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    target_name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chance_push_check'


class CommissionApproveMonth(models.Model):
    name = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=20)
    commission_all = models.FloatField(blank=True, null=True)
    commission_80 = models.FloatField(blank=True, null=True)
    commission_20 = models.FloatField(blank=True, null=True)
    get_month = models.CharField(max_length=10)
    season = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    approve_status = models.IntegerField()
    approve_quarter_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'commission_approve_month'


class CommissionApproveMonthTest(models.Model):
    name = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=20)
    commission_all = models.FloatField(blank=True, null=True)
    commission_80 = models.FloatField(blank=True, null=True)
    commission_20 = models.FloatField(blank=True, null=True)
    get_month = models.CharField(max_length=10)
    season = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    approve_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'commission_approve_month_test'


class CommissionConfirm(models.Model):
    payment_id = models.CharField(max_length=20)
    order_po = models.CharField(max_length=20)
    payment_date = models.CharField(max_length=20)
    payment_attribute = models.IntegerField()
    payment_amount = models.FloatField()
    contract_number = models.CharField(max_length=50)
    payment_customer = models.CharField(max_length=50)
    order_amount = models.FloatField()
    file_date = models.CharField(max_length=20)
    achievement_calculation = models.FloatField()
    commission_base = models.FloatField()
    commissioner_1 = models.CharField(max_length=255, blank=True, null=True)
    commissioner_1_per = models.FloatField(blank=True, null=True)
    commissioner_1_all = models.FloatField(blank=True, null=True)
    commissioner_1_80 = models.FloatField(blank=True, null=True)
    commissioner_1_20 = models.FloatField(blank=True, null=True)
    commissioner_2 = models.CharField(max_length=255, blank=True, null=True)
    commissioner_2_per = models.FloatField(blank=True, null=True)
    commissioner_2_all = models.FloatField(blank=True, null=True)
    commissioner_2_80 = models.FloatField(blank=True, null=True)
    commissioner_2_20 = models.FloatField(blank=True, null=True)
    commissioner_3 = models.CharField(max_length=255, blank=True, null=True)
    commissioner_3_per = models.FloatField(blank=True, null=True)
    commissioner_3_all = models.FloatField(blank=True, null=True)
    commissioner_3_80 = models.FloatField(blank=True, null=True)
    commissioner_3_20 = models.FloatField(blank=True, null=True)
    top_department = models.CharField(max_length=255, blank=True, null=True)
    l3_department = models.CharField(max_length=255, blank=True, null=True)
    deduction = models.FloatField(blank=True, null=True)
    deduction_info = models.CharField(max_length=255, blank=True, null=True)
    order_abnormal = models.CharField(max_length=50, blank=True, null=True)
    confirm_status = models.IntegerField()
    refuse_info = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    order_attribute = models.IntegerField(blank=True, null=True)
    saler_commission_per = models.FloatField(blank=True, null=True)
    commission_all = models.FloatField(blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_confirm'


class CommissionConfirmTest(models.Model):
    payment_id = models.CharField(max_length=20)
    order_po = models.CharField(max_length=20)
    payment_date = models.CharField(max_length=20)
    payment_attribute = models.IntegerField()
    payment_amount = models.FloatField()
    contract_number = models.CharField(max_length=50)
    payment_customer = models.CharField(max_length=50)
    order_amount = models.FloatField()
    file_date = models.CharField(max_length=20)
    achievement_calculation = models.FloatField()
    commission_base = models.FloatField()
    commissioner_1 = models.CharField(max_length=255, blank=True, null=True)
    commissioner_1_per = models.FloatField(blank=True, null=True)
    commissioner_1_all = models.FloatField(blank=True, null=True)
    commissioner_1_80 = models.FloatField(blank=True, null=True)
    commissioner_1_20 = models.FloatField(blank=True, null=True)
    commissioner_2 = models.CharField(max_length=255, blank=True, null=True)
    commissioner_2_per = models.FloatField(blank=True, null=True)
    commissioner_2_all = models.FloatField(blank=True, null=True)
    commissioner_2_80 = models.FloatField(blank=True, null=True)
    commissioner_2_20 = models.FloatField(blank=True, null=True)
    commissioner_3 = models.CharField(max_length=255, blank=True, null=True)
    commissioner_3_per = models.FloatField(blank=True, null=True)
    commissioner_3_all = models.FloatField(blank=True, null=True)
    commissioner_3_80 = models.FloatField(blank=True, null=True)
    commissioner_3_20 = models.FloatField(blank=True, null=True)
    top_department = models.CharField(max_length=255, blank=True, null=True)
    l3_department = models.CharField(max_length=255, blank=True, null=True)
    deduction = models.FloatField(blank=True, null=True)
    deduction_info = models.CharField(max_length=255, blank=True, null=True)
    order_abnormal = models.CharField(max_length=50, blank=True, null=True)
    confirm_status = models.IntegerField()
    refuse_info = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    order_attribute = models.IntegerField(blank=True, null=True)
    saler_commission_per = models.FloatField(blank=True, null=True)
    commission_all = models.FloatField(blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_confirm_test'


class CommissionProcessLog(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    action_date = models.CharField(max_length=255, blank=True, null=True)
    action_user = models.CharField(max_length=255, blank=True, null=True)
    action_type = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_process_log'


class CommissionsDepartmentL3(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    department_l1 = models.CharField(max_length=255, blank=True, null=True)
    department_l3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commissions_department_l3'


class CommissionsDepartmentL4(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    department_l1 = models.CharField(max_length=255, blank=True, null=True)
    department_l4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commissions_department_l4'


class CommissionsInfo(models.Model):
    pid = models.IntegerField()
    oid = models.IntegerField()
    name = models.CharField(max_length=255)
    money = models.FloatField()
    type = models.CharField(max_length=5)
    get_month = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField()
    c_type = models.IntegerField()
    season = models.CharField(max_length=4, blank=True, null=True)
    money_base = models.FloatField(blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    confirm_month = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commissions_info'


class Contact(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    contactname = models.TextField(db_column='contactName', blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    depart = models.TextField(blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    mobile = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    weibo = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zipcode = models.TextField(db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=19, blank=True, null=True)
    recentactivityrecordtime = models.CharField(db_column='recentActivityRecordTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    isdisturb = models.CharField(db_column='isDisturb', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pinyin = models.TextField(blank=True, null=True)
    contactrole = models.IntegerField(db_column='contactRole', blank=True, null=True)  # Field name made lowercase.
    contactscore = models.CharField(db_column='contactScore', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'


class Contract(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    accountid = models.CharField(db_column='accountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.CharField(db_column='opportunityId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    campaignid = models.CharField(db_column='campaignId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    contracttype = models.IntegerField(db_column='contractType', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    paymode = models.IntegerField(db_column='payMode', blank=True, null=True)  # Field name made lowercase.
    startdate = models.CharField(db_column='startDate', max_length=19, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='endDate', max_length=19, blank=True, null=True)  # Field name made lowercase.
    invoiceamount = models.CharField(db_column='invoiceAmount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payback = models.CharField(db_column='payBack', max_length=20, blank=True, null=True)  # Field name made lowercase.
    overduestatus = models.IntegerField(db_column='overdueStatus', blank=True, null=True)  # Field name made lowercase.
    paymentpercent = models.CharField(db_column='paymentPercent', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.IntegerField(db_column='paymentStatus', blank=True, null=True)  # Field name made lowercase.
    notpayment = models.CharField(db_column='notPayment', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contractcode = models.TextField(db_column='contractCode', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    participants = models.CharField(max_length=19, blank=True, null=True)
    customersigner = models.TextField(db_column='customerSigner', blank=True, null=True)  # Field name made lowercase.
    signerid = models.CharField(db_column='signerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    signdate = models.CharField(db_column='signDate', max_length=19, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.CharField(db_column='dbcJoin2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.CharField(db_column='dbcJoin3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin4 = models.CharField(db_column='dbcJoin4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.TextField(db_column='dbcVarchar5', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.BigIntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.TextField(db_column='dbcVarchar7', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contract'


class Contractranking(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    departname = models.CharField(db_column='departName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parentdepartid = models.IntegerField(db_column='parentDepartId', blank=True, null=True)  # Field name made lowercase.
    bm0 = models.CharField(max_length=20, blank=True, null=True)
    bm1 = models.CharField(max_length=20, blank=True, null=True)
    bm2 = models.CharField(max_length=20, blank=True, null=True)
    bm3 = models.CharField(max_length=20, blank=True, null=True)
    bm0id = models.IntegerField(blank=True, null=True)
    bm1id = models.IntegerField(blank=True, null=True)
    bm2id = models.IntegerField(blank=True, null=True)
    bm3id = models.IntegerField(blank=True, null=True)
    thisweek = models.IntegerField(db_column='thisWeek', blank=True, null=True)  # Field name made lowercase.
    thisweekjie = models.IntegerField(db_column='thisWeekjie', blank=True, null=True)  # Field name made lowercase.
    january = models.IntegerField(blank=True, null=True)
    januaryjie = models.IntegerField(blank=True, null=True)
    february = models.IntegerField(blank=True, null=True)
    februaryjie = models.IntegerField(blank=True, null=True)
    march = models.IntegerField(blank=True, null=True)
    marchjie = models.IntegerField(blank=True, null=True)
    april = models.IntegerField(blank=True, null=True)
    apriljie = models.IntegerField(blank=True, null=True)
    may = models.IntegerField(blank=True, null=True)
    mayjie = models.IntegerField(blank=True, null=True)
    junejie = models.IntegerField(blank=True, null=True)
    june = models.IntegerField(blank=True, null=True)
    july = models.IntegerField(blank=True, null=True)
    julyjie = models.IntegerField(blank=True, null=True)
    august = models.IntegerField(blank=True, null=True)
    augustjie = models.IntegerField(blank=True, null=True)
    september = models.IntegerField(blank=True, null=True)
    septemberjie = models.IntegerField(blank=True, null=True)
    october = models.IntegerField(blank=True, null=True)
    octoberjie = models.IntegerField(blank=True, null=True)
    november = models.IntegerField(blank=True, null=True)
    novemberjie = models.IntegerField(blank=True, null=True)
    december = models.IntegerField(blank=True, null=True)
    decemberjie = models.IntegerField(blank=True, null=True)
    monthlytotal = models.IntegerField(blank=True, null=True)
    monthlytotaljjie = models.IntegerField(blank=True, null=True)
    efficiency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contractranking'


class CrmIndustryL1(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_industry_l1'


class CrmIndustryL2(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_industry_l2'


class CrmLocationCity(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_location_City'


class CrmLocationDistrict(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_location_District'


class CrmLocationState(models.Model):
    lid = models.IntegerField(primary_key=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_location_State'


class Customentity1(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem1 = models.CharField(db_column='customItem1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem3 = models.TextField(db_column='customItem3', blank=True, null=True)  # Field name made lowercase.
    workflowstagename = models.TextField(db_column='workflowStageName', blank=True, null=True)  # Field name made lowercase.
    customitem4 = models.TextField(db_column='customItem4', blank=True, null=True)  # Field name made lowercase.
    customitem5 = models.CharField(db_column='customItem5', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem6 = models.CharField(db_column='customItem6', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem7 = models.CharField(db_column='customItem7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    customitem8 = models.CharField(db_column='customItem8', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem9 = models.CharField(db_column='customItem9', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem10 = models.CharField(db_column='customItem10', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem11 = models.CharField(db_column='customItem11', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem12 = models.CharField(db_column='customItem12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    customitem13 = models.IntegerField(db_column='customItem13', blank=True, null=True)  # Field name made lowercase.
    customitem14 = models.IntegerField(db_column='customItem14', blank=True, null=True)  # Field name made lowercase.
    customitem16_c = models.IntegerField(db_column='customItem16__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'customEntity1'


class Customentity12(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    customitem1 = models.CharField(db_column='customItem1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    workflowstagename = models.TextField(db_column='workflowStageName', blank=True, null=True)  # Field name made lowercase.
    customitem5 = models.TextField(db_column='customItem5', blank=True, null=True)  # Field name made lowercase.
    customitem8 = models.CharField(db_column='customItem8', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem9 = models.IntegerField(db_column='customItem9', blank=True, null=True)  # Field name made lowercase.
    customitem11 = models.CharField(db_column='customItem11', max_length=19, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    customitem16_c = models.IntegerField(db_column='customItem16__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem17_c = models.IntegerField(db_column='customItem17__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem18_c = models.CharField(db_column='customItem18__c', max_length=19, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem19_c = models.CharField(db_column='customItem19__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem20_c = models.CharField(db_column='customItem20__c', max_length=19, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem21_c = models.CharField(db_column='customItem21__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem22_c = models.CharField(db_column='customItem22__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem23_c = models.TextField(db_column='customItem23__c', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem26_c = models.CharField(db_column='customItem26__c', max_length=19, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem27_c = models.CharField(db_column='customItem27__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem28_c = models.CharField(db_column='customItem28__c', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'customEntity12'


class Customentity8(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem1 = models.CharField(db_column='customItem1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    workflowstagename = models.TextField(db_column='workflowStageName', blank=True, null=True)  # Field name made lowercase.
    customitem6 = models.CharField(db_column='customItem6', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem13 = models.CharField(db_column='customItem13', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem15 = models.CharField(db_column='customItem15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    customitem16_c = models.CharField(db_column='customItem16__c', max_length=19, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem17_c = models.CharField(db_column='customItem17__c', max_length=19, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem18_c = models.CharField(db_column='customItem18__c', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'customEntity8'


class Customentity9(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    customitem1 = models.CharField(db_column='customItem1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem2 = models.CharField(db_column='customItem2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    workflowstagename = models.TextField(db_column='workflowStageName', blank=True, null=True)  # Field name made lowercase.
    customitem5 = models.CharField(db_column='customItem5', max_length=13, blank=True, null=True)  # Field name made lowercase.
    customitem7 = models.IntegerField(db_column='customItem7', blank=True, null=True)  # Field name made lowercase.
    customitem8 = models.IntegerField(db_column='customItem8', blank=True, null=True)  # Field name made lowercase.
    customitem9 = models.IntegerField(db_column='customItem9', blank=True, null=True)  # Field name made lowercase.
    customitem11 = models.CharField(db_column='customItem11', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem14 = models.TextField(db_column='customItem14', blank=True, null=True)  # Field name made lowercase.
    customitem16 = models.CharField(db_column='customItem16', max_length=300, blank=True, null=True)  # Field name made lowercase.
    customitem17 = models.CharField(db_column='customItem17', max_length=19, blank=True, null=True)  # Field name made lowercase.
    customitem18 = models.FloatField(db_column='customItem18', blank=True, null=True)  # Field name made lowercase.
    customitem19_c = models.CharField(db_column='customItem19__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem20_c = models.CharField(db_column='customItem20__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem21_c = models.CharField(db_column='customItem21__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem22_c = models.CharField(db_column='customItem22__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem23_c = models.CharField(db_column='customItem23__c', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    customitem24_c = models.CharField(db_column='customItem24__c', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'customEntity9'


class Customentity(models.Model):
    belongid = models.BigIntegerField(db_column='belongId', blank=True, null=True)  # Field name made lowercase.
    belongname = models.CharField(db_column='belongName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    custom = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customentity'


class Department(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    departcode = models.TextField(db_column='departCode', blank=True, null=True)  # Field name made lowercase.
    departname = models.TextField(db_column='departName', blank=True, null=True)  # Field name made lowercase.
    parentdepartid = models.BigIntegerField(db_column='parentDepartId', blank=True, null=True)  # Field name made lowercase.
    departtype = models.BigIntegerField(db_column='departType', blank=True, null=True)  # Field name made lowercase.
    specialtype = models.BigIntegerField(db_column='specialType', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentL3Completion(models.Model):
    department_l1 = models.CharField(max_length=255, blank=True, null=True)
    department_l3 = models.CharField(max_length=255, blank=True, null=True)
    q1_per = models.FloatField(blank=True, null=True)
    q2_per = models.FloatField(blank=True, null=True)
    q3_per = models.FloatField(blank=True, null=True)
    q4_per = models.FloatField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_l3_completion'


class DepartmentL4Completion(models.Model):
    department_l1 = models.CharField(max_length=255, blank=True, null=True)
    department_l4 = models.CharField(max_length=255, blank=True, null=True)
    q1_per = models.FloatField(blank=True, null=True)
    q2_per = models.FloatField(blank=True, null=True)
    q3_per = models.FloatField(blank=True, null=True)
    q4_per = models.FloatField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_l4_completion'


class DepartmentMonthAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    department = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_month_achievement'


class DepartmentNewAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    department = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_new_achievement'


class DepartmentRenewAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    department = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_renew_achievement'


class Frameinfo(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    partname = models.CharField(max_length=50, blank=True, null=True)
    pinyin = models.CharField(max_length=60, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frameinfo'


class ImplementCommission(models.Model):
    implement_date = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    contract = models.CharField(max_length=50, blank=True, null=True)
    customer = models.CharField(max_length=50, blank=True, null=True)
    progress_table = models.CharField(max_length=50, blank=True, null=True)
    project_type = models.CharField(max_length=50, blank=True, null=True)
    project_money = models.FloatField(blank=True, null=True)
    implement_share = models.FloatField(blank=True, null=True)
    implement_submit_date = models.CharField(max_length=50, blank=True, null=True)
    implement_person = models.CharField(max_length=50, blank=True, null=True)
    implement_manage = models.CharField(max_length=50, blank=True, null=True)
    implement_commission = models.FloatField(blank=True, null=True)
    implement_manage_commission = models.FloatField(blank=True, null=True)
    bonus_base = models.FloatField(blank=True, null=True)
    commission_date = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    approve_status = models.IntegerField(blank=True, null=True)
    approve_implementing_status = models.IntegerField(db_column='approve_Implementing_status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'implement_commission'


class Largearea(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    dependentvalue = models.CharField(db_column='dependentValue', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'largearea'


class Linshi(models.Model):
    cid = models.CharField(max_length=255, blank=True, null=True)
    paymoney = models.IntegerField(blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linshi'


class Location(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    dependentvalue = models.CharField(db_column='dependentValue', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class MonthCommissionGetDate(models.Model):
    # id = models.IntegerField()
    pid = models.IntegerField()
    oid = models.IntegerField()
    c1 = models.CharField(max_length=255, blank=True, null=True)
    c1_money = models.CharField(max_length=255, blank=True, null=True)
    c2 = models.CharField(max_length=255, blank=True, null=True)
    c2_money = models.CharField(max_length=255, blank=True, null=True)
    c3 = models.CharField(max_length=255, blank=True, null=True)
    c3_money = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    get_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'month_commission_get_date'


class MonthVistorCheck(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    target_name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'month_vistor_check'


class NewChanceCheck(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    target_name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_chance_check'


class NewTestCheck(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    target_name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_test_check'


class Newsingle(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    departname = models.CharField(db_column='departName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parentdepartid = models.IntegerField(db_column='parentDepartId', blank=True, null=True)  # Field name made lowercase.
    bm0 = models.CharField(max_length=20, blank=True, null=True)
    bm1 = models.CharField(max_length=20, blank=True, null=True)
    bm2 = models.CharField(max_length=20, blank=True, null=True)
    bm3 = models.CharField(max_length=20, blank=True, null=True)
    bm0id = models.IntegerField(blank=True, null=True)
    bm1id = models.IntegerField(blank=True, null=True)
    bm2id = models.IntegerField(blank=True, null=True)
    bm3id = models.IntegerField(blank=True, null=True)
    thisweek = models.IntegerField(db_column='thisWeek', blank=True, null=True)  # Field name made lowercase.
    thisweekjie = models.IntegerField(db_column='thisWeekjie', blank=True, null=True)  # Field name made lowercase.
    january = models.IntegerField(blank=True, null=True)
    januaryjie = models.IntegerField(blank=True, null=True)
    february = models.IntegerField(blank=True, null=True)
    februaryjie = models.IntegerField(blank=True, null=True)
    march = models.IntegerField(blank=True, null=True)
    marchjie = models.IntegerField(blank=True, null=True)
    april = models.IntegerField(blank=True, null=True)
    apriljie = models.IntegerField(blank=True, null=True)
    may = models.IntegerField(blank=True, null=True)
    mayjie = models.IntegerField(blank=True, null=True)
    junejie = models.IntegerField(blank=True, null=True)
    june = models.IntegerField(blank=True, null=True)
    july = models.IntegerField(blank=True, null=True)
    julyjie = models.IntegerField(blank=True, null=True)
    august = models.IntegerField(blank=True, null=True)
    augustjie = models.IntegerField(blank=True, null=True)
    september = models.IntegerField(blank=True, null=True)
    septemberjie = models.IntegerField(blank=True, null=True)
    october = models.IntegerField(blank=True, null=True)
    octoberjie = models.IntegerField(blank=True, null=True)
    november = models.IntegerField(blank=True, null=True)
    novemberjie = models.IntegerField(blank=True, null=True)
    december = models.IntegerField(blank=True, null=True)
    decemberjie = models.IntegerField(blank=True, null=True)
    monthlytotal = models.IntegerField(blank=True, null=True)
    monthlytotaljjie = models.IntegerField(blank=True, null=True)
    efficiency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsingle'


class Opportunity(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.TextField(db_column='opportunityName', blank=True, null=True)  # Field name made lowercase.
    priceid = models.CharField(db_column='priceId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    opportunitytype = models.IntegerField(db_column='opportunityType', blank=True, null=True)  # Field name made lowercase.
    money = models.CharField(max_length=20, blank=True, null=True)
    loststageid = models.IntegerField(db_column='lostStageId', blank=True, null=True)  # Field name made lowercase.
    salestageid = models.IntegerField(db_column='saleStageId', blank=True, null=True)  # Field name made lowercase.
    winrate = models.IntegerField(db_column='winRate', blank=True, null=True)  # Field name made lowercase.
    reasondesc = models.TextField(db_column='reasonDesc', blank=True, null=True)  # Field name made lowercase.
    closedate = models.CharField(db_column='closeDate', max_length=19, blank=True, null=True)  # Field name made lowercase.
    commitmentflg = models.IntegerField(db_column='commitmentFlg', blank=True, null=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceId', blank=True, null=True)  # Field name made lowercase.
    projectbudget = models.CharField(db_column='projectBudget', max_length=20, blank=True, null=True)  # Field name made lowercase.
    actualcost = models.CharField(db_column='actualCost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recentactivityrecordtime = models.CharField(db_column='recentActivityRecordTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    stageupdatedat = models.CharField(db_column='stageUpdatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.CharField(db_column='campaignId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custcheckbox2 = models.CharField(db_column='custCheckbox2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custcheckbox3 = models.CharField(db_column='custCheckbox3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbctextarea1 = models.TextField(db_column='dbcTextarea1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.TextField(db_column='dbcVarchar7', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.TextField(db_column='dbcVarchar8', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.TextField(db_column='dbcVarchar9', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.TextField(db_column='dbcVarchar10', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbctextarea2 = models.TextField(db_column='dbcTextarea2', blank=True, null=True)  # Field name made lowercase.
    custcheckbox4 = models.CharField(db_column='custCheckbox4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbctextarea3 = models.TextField(db_column='dbcTextarea3', blank=True, null=True)  # Field name made lowercase.
    dbctextarea4 = models.TextField(db_column='dbcTextarea4', blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.CharField(db_column='dbcJoin3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.CharField(db_column='dbcJoin2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    custcheckbox5 = models.CharField(db_column='custCheckbox5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin4 = models.CharField(db_column='dbcJoin4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin5 = models.CharField(db_column='dbcJoin5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.CharField(db_column='dbcVarchar5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.IntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.IntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcjoin6 = models.CharField(db_column='dbcJoin6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.CharField(db_column='dbcRelation1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect6 = models.IntegerField(db_column='dbcSelect6', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect7 = models.IntegerField(db_column='dbcSelect7', blank=True, null=True)  # Field name made lowercase.
    dbcselect8 = models.IntegerField(db_column='dbcSelect8', blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin8 = models.CharField(db_column='dbcJoin8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin9 = models.CharField(db_column='dbcJoin9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.CharField(db_column='dbcDate6', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate7 = models.CharField(db_column='dbcDate7', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate8 = models.CharField(db_column='dbcDate8', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate9 = models.CharField(db_column='dbcDate9', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect12 = models.IntegerField(db_column='dbcSelect12', blank=True, null=True)  # Field name made lowercase.
    dbcselect11 = models.IntegerField(db_column='dbcSelect11', blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.CharField(db_column='dbcReal2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal7 = models.CharField(db_column='dbcReal7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal8 = models.CharField(db_column='dbcReal8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.IntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcdate10 = models.CharField(db_column='dbcDate10', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.CharField(db_column='dbcRelation2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect10 = models.IntegerField(db_column='dbcSelect10', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.CharField(db_column='dbcVarchar11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect13 = models.IntegerField(db_column='dbcSelect13', blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.IntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcjoin10 = models.CharField(db_column='dbcJoin10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.IntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.CharField(db_column='dbcRelation3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.IntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    dbcjoin11 = models.CharField(db_column='dbcJoin11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.IntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.IntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.CharField(db_column='dbcVarchar12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin12 = models.CharField(db_column='dbcJoin12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin13 = models.CharField(db_column='dbcJoin13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal9 = models.CharField(db_column='dbcReal9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fcastmoney = models.CharField(db_column='fcastMoney', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.CharField(db_column='dbcVarchar13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.CharField(db_column='dbcVarchar14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.CharField(db_column='dbcVarchar15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin7 = models.CharField(db_column='dbcJoin7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    opportunityscore = models.CharField(db_column='opportunityScore', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcrelation4 = models.CharField(db_column='dbcRelation4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect19 = models.IntegerField(db_column='dbcSelect19', blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate12 = models.CharField(db_column='dbcDate12', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin14 = models.CharField(db_column='dbcJoin14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reason = models.BigIntegerField(blank=True, null=True)
    dbcdate13 = models.CharField(db_column='dbcDate13', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect20 = models.BigIntegerField(db_column='dbcSelect20', blank=True, null=True)  # Field name made lowercase.
    dbcselect21 = models.BigIntegerField(db_column='dbcSelect21', blank=True, null=True)  # Field name made lowercase.
    dbcdate14 = models.CharField(db_column='dbcDate14', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate16 = models.CharField(db_column='dbcDate16', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate17 = models.CharField(db_column='dbcDate17', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect22 = models.BigIntegerField(db_column='dbcSelect22', blank=True, null=True)  # Field name made lowercase.
    dbcselect23 = models.BigIntegerField(db_column='dbcSelect23', blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leadid = models.BigIntegerField(db_column='leadId', blank=True, null=True)  # Field name made lowercase.
    dbcjoin15 = models.CharField(db_column='dbcJoin15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin16 = models.CharField(db_column='dbcJoin16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin17 = models.CharField(db_column='dbcJoin17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect24 = models.BigIntegerField(db_column='dbcSelect24', blank=True, null=True)  # Field name made lowercase.
    custcheckbox6 = models.CharField(db_column='custCheckbox6', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opportunity'


class Opportunity20190815(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.TextField(db_column='opportunityName', blank=True, null=True)  # Field name made lowercase.
    priceid = models.CharField(db_column='priceId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    opportunitytype = models.IntegerField(db_column='opportunityType', blank=True, null=True)  # Field name made lowercase.
    money = models.CharField(max_length=20, blank=True, null=True)
    loststageid = models.IntegerField(db_column='lostStageId', blank=True, null=True)  # Field name made lowercase.
    salestageid = models.IntegerField(db_column='saleStageId', blank=True, null=True)  # Field name made lowercase.
    winrate = models.IntegerField(db_column='winRate', blank=True, null=True)  # Field name made lowercase.
    reasondesc = models.TextField(db_column='reasonDesc', blank=True, null=True)  # Field name made lowercase.
    closedate = models.CharField(db_column='closeDate', max_length=19, blank=True, null=True)  # Field name made lowercase.
    commitmentflg = models.IntegerField(db_column='commitmentFlg', blank=True, null=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceId', blank=True, null=True)  # Field name made lowercase.
    projectbudget = models.CharField(db_column='projectBudget', max_length=20, blank=True, null=True)  # Field name made lowercase.
    actualcost = models.CharField(db_column='actualCost', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recentactivityrecordtime = models.CharField(db_column='recentActivityRecordTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    stageupdatedat = models.CharField(db_column='stageUpdatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.CharField(db_column='campaignId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custcheckbox2 = models.CharField(db_column='custCheckbox2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custcheckbox3 = models.CharField(db_column='custCheckbox3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbctextarea1 = models.TextField(db_column='dbcTextarea1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.TextField(db_column='dbcVarchar7', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.TextField(db_column='dbcVarchar8', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.TextField(db_column='dbcVarchar9', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.TextField(db_column='dbcVarchar10', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbctextarea2 = models.TextField(db_column='dbcTextarea2', blank=True, null=True)  # Field name made lowercase.
    custcheckbox4 = models.CharField(db_column='custCheckbox4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbctextarea3 = models.TextField(db_column='dbcTextarea3', blank=True, null=True)  # Field name made lowercase.
    dbctextarea4 = models.TextField(db_column='dbcTextarea4', blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.CharField(db_column='dbcJoin3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.CharField(db_column='dbcJoin2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    custcheckbox5 = models.CharField(db_column='custCheckbox5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin4 = models.CharField(db_column='dbcJoin4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin5 = models.CharField(db_column='dbcJoin5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.CharField(db_column='dbcVarchar5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.IntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.IntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcjoin6 = models.CharField(db_column='dbcJoin6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.CharField(db_column='dbcRelation1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect6 = models.IntegerField(db_column='dbcSelect6', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect7 = models.IntegerField(db_column='dbcSelect7', blank=True, null=True)  # Field name made lowercase.
    dbcselect8 = models.IntegerField(db_column='dbcSelect8', blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin8 = models.CharField(db_column='dbcJoin8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin9 = models.CharField(db_column='dbcJoin9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.CharField(db_column='dbcDate6', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate7 = models.CharField(db_column='dbcDate7', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate8 = models.CharField(db_column='dbcDate8', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate9 = models.CharField(db_column='dbcDate9', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect12 = models.IntegerField(db_column='dbcSelect12', blank=True, null=True)  # Field name made lowercase.
    dbcselect11 = models.IntegerField(db_column='dbcSelect11', blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.CharField(db_column='dbcReal2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal7 = models.CharField(db_column='dbcReal7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal8 = models.CharField(db_column='dbcReal8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.IntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcdate10 = models.CharField(db_column='dbcDate10', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.CharField(db_column='dbcRelation2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect10 = models.IntegerField(db_column='dbcSelect10', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.CharField(db_column='dbcVarchar11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect13 = models.IntegerField(db_column='dbcSelect13', blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.IntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcjoin10 = models.CharField(db_column='dbcJoin10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.IntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.CharField(db_column='dbcRelation3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.IntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    dbcjoin11 = models.CharField(db_column='dbcJoin11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.IntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.IntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.CharField(db_column='dbcVarchar12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin12 = models.CharField(db_column='dbcJoin12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin13 = models.CharField(db_column='dbcJoin13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal9 = models.CharField(db_column='dbcReal9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fcastmoney = models.CharField(db_column='fcastMoney', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.CharField(db_column='dbcVarchar13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.CharField(db_column='dbcVarchar14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.CharField(db_column='dbcVarchar15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin7 = models.CharField(db_column='dbcJoin7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    opportunityscore = models.CharField(db_column='opportunityScore', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dbcrelation4 = models.CharField(db_column='dbcRelation4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect19 = models.IntegerField(db_column='dbcSelect19', blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate12 = models.CharField(db_column='dbcDate12', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcjoin14 = models.CharField(db_column='dbcJoin14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reason = models.BigIntegerField(blank=True, null=True)
    dbcdate13 = models.CharField(db_column='dbcDate13', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect20 = models.BigIntegerField(db_column='dbcSelect20', blank=True, null=True)  # Field name made lowercase.
    dbcselect21 = models.BigIntegerField(db_column='dbcSelect21', blank=True, null=True)  # Field name made lowercase.
    dbcdate14 = models.CharField(db_column='dbcDate14', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate16 = models.CharField(db_column='dbcDate16', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate17 = models.CharField(db_column='dbcDate17', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect22 = models.BigIntegerField(db_column='dbcSelect22', blank=True, null=True)  # Field name made lowercase.
    dbcselect23 = models.BigIntegerField(db_column='dbcSelect23', blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leadid = models.BigIntegerField(db_column='leadId', blank=True, null=True)  # Field name made lowercase.
    dbcjoin15 = models.CharField(db_column='dbcJoin15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin16 = models.CharField(db_column='dbcJoin16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin17 = models.CharField(db_column='dbcJoin17', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opportunity_20190815'


class OpportunityBack(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.TextField(db_column='opportunityName', blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    money = models.CharField(max_length=20, blank=True, null=True)
    salestageid = models.IntegerField(db_column='saleStageId', blank=True, null=True)  # Field name made lowercase.
    winrate = models.IntegerField(db_column='winRate', blank=True, null=True)  # Field name made lowercase.
    closedate = models.CharField(db_column='closeDate', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    custcheckbox5 = models.CharField(db_column='custCheckbox5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.CharField(db_column='dbcRelation1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate7 = models.CharField(db_column='dbcDate7', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate8 = models.CharField(db_column='dbcDate8', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate10 = models.CharField(db_column='dbcDate10', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.CharField(db_column='dbcVarchar12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcrelation4 = models.CharField(db_column='dbcRelation4', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect19 = models.IntegerField(db_column='dbcSelect19', blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate12 = models.CharField(db_column='dbcDate12', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect20 = models.BigIntegerField(db_column='dbcSelect20', blank=True, null=True)  # Field name made lowercase.
    dbcselect21 = models.BigIntegerField(db_column='dbcSelect21', blank=True, null=True)  # Field name made lowercase.
    dbcdate14 = models.CharField(db_column='dbcDate14', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect22 = models.BigIntegerField(db_column='dbcSelect22', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opportunity_back'


class Order(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    fscwhethertrackedasset = models.BigIntegerField(db_column='fscWhetherTrackedAsset', blank=True, null=True)  # Field name made lowercase.
    po = models.TextField(blank=True, null=True)
    ro = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    accountid = models.BigIntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    postatus = models.BigIntegerField(db_column='poStatus', blank=True, null=True)  # Field name made lowercase.
    priceid = models.BigIntegerField(db_column='priceId', blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    contractid = models.BigIntegerField(db_column='contractId', blank=True, null=True)  # Field name made lowercase.
    rostatus = models.BigIntegerField(db_column='roStatus', blank=True, null=True)  # Field name made lowercase.
    initamount = models.FloatField(db_column='initAmount', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(blank=True, null=True)
    effectivedate = models.CharField(db_column='effectiveDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productsamount = models.FloatField(db_column='productsAmount', blank=True, null=True)  # Field name made lowercase.
    contactname = models.TextField(db_column='contactName', blank=True, null=True)  # Field name made lowercase.
    contacttel = models.TextField(db_column='contactTel', blank=True, null=True)  # Field name made lowercase.
    contactaddress = models.TextField(db_column='contactAddress', blank=True, null=True)  # Field name made lowercase.
    orderrelquotationentity = models.BigIntegerField(db_column='orderRelQuotationEntity', blank=True, null=True)  # Field name made lowercase.
    payments = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    paymentpercent = models.FloatField(db_column='paymentPercent', blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.BigIntegerField(db_column='paymentStatus', blank=True, null=True)  # Field name made lowercase.
    overduestatus = models.BigIntegerField(db_column='overdueStatus', blank=True, null=True)  # Field name made lowercase.
    cancelreason = models.BigIntegerField(db_column='cancelReason', blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    dimdepart = models.CharField(db_column='dimDepart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.BigIntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.BigIntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.BigIntegerField(db_column='applicantId', blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.BigIntegerField(db_column='dbcRelation1', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.CharField(db_column='transactionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    listtotal = models.FloatField(db_column='listTotal', blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.FloatField(db_column='totalDiscountAmount', blank=True, null=True)  # Field name made lowercase.
    orderversion = models.BigIntegerField(db_column='orderVersion', blank=True, null=True)  # Field name made lowercase.
    originalorderversion = models.BigIntegerField(db_column='originalOrderVersion', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    co = models.CharField(max_length=300, blank=True, null=True)
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalorderid = models.BigIntegerField(db_column='originalOrderId', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.CharField(db_column='dbcDate6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.BigIntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.BigIntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.BigIntegerField(db_column='dbcRelation2', blank=True, null=True)  # Field name made lowercase.
    dbcselect6 = models.BigIntegerField(db_column='dbcSelect6', blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.FloatField(db_column='dbcReal2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcselect7 = models.BigIntegerField(db_column='dbcSelect7', blank=True, null=True)  # Field name made lowercase.
    dbcselect8 = models.BigIntegerField(db_column='dbcSelect8', blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.CharField(db_column='dbcJoin2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.CharField(db_column='dbcJoin3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin4 = models.CharField(db_column='dbcJoin4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.FloatField(db_column='dbcReal3', blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.BigIntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcselect10 = models.BigIntegerField(db_column='dbcSelect10', blank=True, null=True)  # Field name made lowercase.
    dbcselect11 = models.BigIntegerField(db_column='dbcSelect11', blank=True, null=True)  # Field name made lowercase.
    dbcselect12 = models.BigIntegerField(db_column='dbcSelect12', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcdate7 = models.CharField(db_column='dbcDate7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.BigIntegerField(db_column='dbcRelation3', blank=True, null=True)  # Field name made lowercase.
    dbcrelation4 = models.BigIntegerField(db_column='dbcRelation4', blank=True, null=True)  # Field name made lowercase.
    dbcrelation5 = models.BigIntegerField(db_column='dbcRelation5', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.FloatField(db_column='dbcReal1', blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.FloatField(db_column='dbcReal4', blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.FloatField(db_column='dbcReal5', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.TextField(db_column='dbcVarchar5', blank=True, null=True)  # Field name made lowercase.
    dbcdate8 = models.CharField(db_column='dbcDate8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcrelation6 = models.BigIntegerField(db_column='dbcRelation6', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.TextField(db_column='dbcVarchar7', blank=True, null=True)  # Field name made lowercase.
    dbcselect13 = models.BigIntegerField(db_column='dbcSelect13', blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.BigIntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcdate9 = models.CharField(db_column='dbcDate9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate10 = models.CharField(db_column='dbcDate10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation7 = models.BigIntegerField(db_column='dbcRelation7', blank=True, null=True)  # Field name made lowercase.
    dbcjoin5 = models.CharField(db_column='dbcJoin5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin6 = models.CharField(db_column='dbcJoin6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation8 = models.BigIntegerField(db_column='dbcRelation8', blank=True, null=True)  # Field name made lowercase.
    dbcrelation9 = models.BigIntegerField(db_column='dbcRelation9', blank=True, null=True)  # Field name made lowercase.
    dbcrelation10 = models.BigIntegerField(db_column='dbcRelation10', blank=True, null=True)  # Field name made lowercase.
    dbcreal7 = models.FloatField(db_column='dbcReal7', blank=True, null=True)  # Field name made lowercase.
    dbcreal8 = models.FloatField(db_column='dbcReal8', blank=True, null=True)  # Field name made lowercase.
    dbcreal9 = models.FloatField(db_column='dbcReal9', blank=True, null=True)  # Field name made lowercase.
    dbcjoin7 = models.CharField(db_column='dbcJoin7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal10 = models.CharField(db_column='dbcReal10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate12 = models.CharField(db_column='dbcDate12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal11 = models.CharField(db_column='dbcReal11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.CharField(db_column='dbcVarchar8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin8 = models.CharField(db_column='dbcJoin8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal12 = models.CharField(db_column='dbcReal12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.BigIntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.BigIntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin9 = models.CharField(db_column='dbcJoin9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin10 = models.CharField(db_column='dbcJoin10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.CharField(db_column='dbcVarchar9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin11 = models.CharField(db_column='dbcJoin11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate13 = models.CharField(db_column='dbcDate13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate14 = models.CharField(db_column='dbcDate14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate16 = models.CharField(db_column='dbcDate16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.TextField(db_column='dbcVarchar11', blank=True, null=True)  # Field name made lowercase.
    dbctextarea1 = models.TextField(db_column='dbcTextarea1', blank=True, null=True)  # Field name made lowercase.
    dbcjoin12 = models.CharField(db_column='dbcJoin12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.BigIntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.TextField(db_column='dbcVarchar10', blank=True, null=True)  # Field name made lowercase.
    dbcreal13 = models.CharField(db_column='dbcReal13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal14 = models.CharField(db_column='dbcReal14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate17 = models.CharField(db_column='dbcDate17', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.BigIntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    dbcselect19 = models.BigIntegerField(db_column='dbcSelect19', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.TextField(db_column='dbcVarchar12', blank=True, null=True)  # Field name made lowercase.
    dbcjoin13 = models.CharField(db_column='dbcJoin13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.TextField(db_column='dbcVarchar13', blank=True, null=True)  # Field name made lowercase.
    dbcjoin14 = models.CharField(db_column='dbcJoin14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.CharField(db_column='dbcVarchar14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.CharField(db_column='dbcVarchar15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin15 = models.CharField(db_column='dbcJoin15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin16 = models.CharField(db_column='dbcJoin16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal15 = models.FloatField(db_column='dbcReal15', blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcselect20 = models.BigIntegerField(db_column='dbcSelect20', blank=True, null=True)  # Field name made lowercase.
    dbcreal16 = models.FloatField(db_column='dbcReal16', blank=True, null=True)  # Field name made lowercase.
    dbcselect21 = models.BigIntegerField(db_column='dbcSelect21', blank=True, null=True)  # Field name made lowercase.
    dbcdate18 = models.CharField(db_column='dbcDate18', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderproduct(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    unitprice = models.FloatField(db_column='unitPrice', blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    pricetotal = models.FloatField(db_column='priceTotal', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    standardprice = models.FloatField(db_column='standardPrice', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.BigIntegerField(db_column='productId', blank=True, null=True)  # Field name made lowercase.
    orderproductid = models.BigIntegerField(db_column='orderProductId', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.FloatField(db_column='dbcReal1', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.CharField(db_column='transactionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    listtotal = models.FloatField(db_column='listTotal', blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.FloatField(db_column='dbcReal2', blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.FloatField(db_column='totalDiscountAmount', blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.FloatField(db_column='dbcReal3', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.FloatField(db_column='dbcReal4', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    deltaquantity = models.FloatField(db_column='deltaQuantity', blank=True, null=True)  # Field name made lowercase.
    deltaamount = models.FloatField(db_column='deltaAmount', blank=True, null=True)  # Field name made lowercase.
    orderversion = models.BigIntegerField(db_column='orderVersion', blank=True, null=True)  # Field name made lowercase.
    changetype = models.BigIntegerField(db_column='changeType', blank=True, null=True)  # Field name made lowercase.
    originalorderid = models.BigIntegerField(db_column='originalOrderId', blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.CharField(db_column='dbcVarchar1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.CharField(db_column='dbcVarchar2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.CharField(db_column='dbcVarchar3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.CharField(db_column='dbcVarchar4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.CharField(db_column='dbcVarchar5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.CharField(db_column='dbcVarchar6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    originalorderproductapiid = models.TextField(db_column='originalOrderProductAPIId', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.CharField(db_column='dbcVarchar7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.CharField(db_column='dbcVarchar8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.CharField(db_column='dbcVarchar10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.CharField(db_column='dbcVarchar11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.CharField(db_column='dbcVarchar12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.CharField(db_column='dbcVarchar13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.CharField(db_column='dbcVarchar14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.CharField(db_column='dbcVarchar9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.CharField(db_column='dbcVarchar15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar16 = models.CharField(db_column='dbcVarchar16', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.CharField(db_column='dbcJoin2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.BigIntegerField(db_column='dbcRelation1', blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.CharField(db_column='dbcJoin3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalorderproductid = models.BigIntegerField(db_column='originalOrderProductId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderProduct'


class OrderproductBack(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    unitprice = models.CharField(db_column='unitPrice', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quantity = models.CharField(max_length=255, blank=True, null=True)
    pricetotal = models.CharField(db_column='priceTotal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    standardprice = models.CharField(db_column='standardPrice', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='productId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    listtotal = models.CharField(db_column='listTotal', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    originalorderid = models.CharField(db_column='originalOrderId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    originalorderproductid = models.CharField(db_column='originalOrderProductId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.CharField(db_column='dbcVarchar1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.CharField(db_column='dbcVarchar2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.CharField(db_column='dbcVarchar3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.CharField(db_column='dbcVarchar4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.CharField(db_column='dbcVarchar7', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderProduct_back'


class OrderBack(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    po = models.TextField(blank=True, null=True)
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    accountid = models.BigIntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    postatus = models.BigIntegerField(db_column='poStatus', blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(blank=True, null=True)
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.BigIntegerField(db_column='dbcRelation1', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.CharField(db_column='dbcDate6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.BigIntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.FloatField(db_column='dbcReal2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal10 = models.CharField(db_column='dbcReal10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate16 = models.CharField(db_column='dbcDate16', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_back'


class OrderTest(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    fscwhethertrackedasset = models.BigIntegerField(db_column='fscWhetherTrackedAsset', blank=True, null=True)  # Field name made lowercase.
    po = models.TextField(blank=True, null=True)
    ro = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    accountid = models.BigIntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    postatus = models.BigIntegerField(db_column='poStatus', blank=True, null=True)  # Field name made lowercase.
    priceid = models.BigIntegerField(db_column='priceId', blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    contractid = models.BigIntegerField(db_column='contractId', blank=True, null=True)  # Field name made lowercase.
    rostatus = models.BigIntegerField(db_column='roStatus', blank=True, null=True)  # Field name made lowercase.
    initamount = models.CharField(db_column='initAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(max_length=255, blank=True, null=True)
    effectivedate = models.CharField(db_column='effectiveDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productsamount = models.CharField(db_column='productsAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactname = models.TextField(db_column='contactName', blank=True, null=True)  # Field name made lowercase.
    contacttel = models.TextField(db_column='contactTel', blank=True, null=True)  # Field name made lowercase.
    contactaddress = models.TextField(db_column='contactAddress', blank=True, null=True)  # Field name made lowercase.
    orderrelquotationentity = models.BigIntegerField(db_column='orderRelQuotationEntity', blank=True, null=True)  # Field name made lowercase.
    payments = models.CharField(max_length=255, blank=True, null=True)
    balance = models.CharField(max_length=255, blank=True, null=True)
    paymentpercent = models.CharField(db_column='paymentPercent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.BigIntegerField(db_column='paymentStatus', blank=True, null=True)  # Field name made lowercase.
    overduestatus = models.BigIntegerField(db_column='overdueStatus', blank=True, null=True)  # Field name made lowercase.
    cancelreason = models.BigIntegerField(db_column='cancelReason', blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    dimdepart = models.CharField(db_column='dimDepart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.BigIntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.BigIntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.BigIntegerField(db_column='applicantId', blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.BigIntegerField(db_column='dbcRelation1', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.CharField(db_column='transactionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    listtotal = models.CharField(db_column='listTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.CharField(db_column='totalDiscountAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderversion = models.BigIntegerField(db_column='orderVersion', blank=True, null=True)  # Field name made lowercase.
    originalorderversion = models.BigIntegerField(db_column='originalOrderVersion', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    co = models.CharField(max_length=255, blank=True, null=True)
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalorderid = models.BigIntegerField(db_column='originalOrderId', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate4 = models.CharField(db_column='dbcDate4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.CharField(db_column='dbcDate5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.CharField(db_column='dbcDate6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.BigIntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.BigIntegerField(db_column='dbcJoin1', blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.BigIntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.
    dbcrelation2 = models.BigIntegerField(db_column='dbcRelation2', blank=True, null=True)  # Field name made lowercase.
    dbcselect6 = models.BigIntegerField(db_column='dbcSelect6', blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.CharField(db_column='dbcReal2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcselect7 = models.BigIntegerField(db_column='dbcSelect7', blank=True, null=True)  # Field name made lowercase.
    dbcselect8 = models.BigIntegerField(db_column='dbcSelect8', blank=True, null=True)  # Field name made lowercase.
    dbcjoin2 = models.BigIntegerField(db_column='dbcJoin2', blank=True, null=True)  # Field name made lowercase.
    dbcjoin3 = models.BigIntegerField(db_column='dbcJoin3', blank=True, null=True)  # Field name made lowercase.
    dbcjoin4 = models.BigIntegerField(db_column='dbcJoin4', blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.CharField(db_column='dbcReal3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect9 = models.BigIntegerField(db_column='dbcSelect9', blank=True, null=True)  # Field name made lowercase.
    dbcselect10 = models.BigIntegerField(db_column='dbcSelect10', blank=True, null=True)  # Field name made lowercase.
    dbcselect11 = models.BigIntegerField(db_column='dbcSelect11', blank=True, null=True)  # Field name made lowercase.
    dbcselect12 = models.BigIntegerField(db_column='dbcSelect12', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcdate7 = models.CharField(db_column='dbcDate7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation3 = models.BigIntegerField(db_column='dbcRelation3', blank=True, null=True)  # Field name made lowercase.
    dbcrelation4 = models.BigIntegerField(db_column='dbcRelation4', blank=True, null=True)  # Field name made lowercase.
    dbcrelation5 = models.BigIntegerField(db_column='dbcRelation5', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.CharField(db_column='dbcReal4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal5 = models.CharField(db_column='dbcReal5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.TextField(db_column='dbcVarchar5', blank=True, null=True)  # Field name made lowercase.
    dbcdate8 = models.CharField(db_column='dbcDate8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcrelation6 = models.BigIntegerField(db_column='dbcRelation6', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.TextField(db_column='dbcVarchar7', blank=True, null=True)  # Field name made lowercase.
    dbcselect13 = models.BigIntegerField(db_column='dbcSelect13', blank=True, null=True)  # Field name made lowercase.
    dbcselect14 = models.BigIntegerField(db_column='dbcSelect14', blank=True, null=True)  # Field name made lowercase.
    dbcdate9 = models.CharField(db_column='dbcDate9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate10 = models.CharField(db_column='dbcDate10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation7 = models.BigIntegerField(db_column='dbcRelation7', blank=True, null=True)  # Field name made lowercase.
    dbcjoin5 = models.BigIntegerField(db_column='dbcJoin5', blank=True, null=True)  # Field name made lowercase.
    dbcjoin6 = models.BigIntegerField(db_column='dbcJoin6', blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation8 = models.BigIntegerField(db_column='dbcRelation8', blank=True, null=True)  # Field name made lowercase.
    dbcrelation9 = models.BigIntegerField(db_column='dbcRelation9', blank=True, null=True)  # Field name made lowercase.
    dbcrelation10 = models.BigIntegerField(db_column='dbcRelation10', blank=True, null=True)  # Field name made lowercase.
    dbcreal7 = models.CharField(db_column='dbcReal7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal8 = models.CharField(db_column='dbcReal8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal9 = models.CharField(db_column='dbcReal9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin7 = models.BigIntegerField(db_column='dbcJoin7', blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal10 = models.CharField(db_column='dbcReal10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate12 = models.CharField(db_column='dbcDate12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal11 = models.CharField(db_column='dbcReal11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.TextField(db_column='dbcVarchar8', blank=True, null=True)  # Field name made lowercase.
    dbcjoin8 = models.BigIntegerField(db_column='dbcJoin8', blank=True, null=True)  # Field name made lowercase.
    dbcreal12 = models.CharField(db_column='dbcReal12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.BigIntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.BigIntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin9 = models.BigIntegerField(db_column='dbcJoin9', blank=True, null=True)  # Field name made lowercase.
    dbcjoin10 = models.BigIntegerField(db_column='dbcJoin10', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.TextField(db_column='dbcVarchar9', blank=True, null=True)  # Field name made lowercase.
    dbcjoin11 = models.BigIntegerField(db_column='dbcJoin11', blank=True, null=True)  # Field name made lowercase.
    dbcdate13 = models.CharField(db_column='dbcDate13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate14 = models.CharField(db_column='dbcDate14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate16 = models.CharField(db_column='dbcDate16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.TextField(db_column='dbcVarchar11', blank=True, null=True)  # Field name made lowercase.
    dbctextarea1 = models.TextField(db_column='dbcTextarea1', blank=True, null=True)  # Field name made lowercase.
    dbcjoin12 = models.BigIntegerField(db_column='dbcJoin12', blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.BigIntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.TextField(db_column='dbcVarchar10', blank=True, null=True)  # Field name made lowercase.
    dbcreal13 = models.CharField(db_column='dbcReal13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal14 = models.CharField(db_column='dbcReal14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate17 = models.CharField(db_column='dbcDate17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.BigIntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    dbcselect19 = models.BigIntegerField(db_column='dbcSelect19', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.TextField(db_column='dbcVarchar12', blank=True, null=True)  # Field name made lowercase.
    dbcjoin13 = models.BigIntegerField(db_column='dbcJoin13', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.TextField(db_column='dbcVarchar13', blank=True, null=True)  # Field name made lowercase.
    dbcjoin14 = models.BigIntegerField(db_column='dbcJoin14', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.TextField(db_column='dbcVarchar14', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.TextField(db_column='dbcVarchar15', blank=True, null=True)  # Field name made lowercase.
    dbcjoin15 = models.BigIntegerField(db_column='dbcJoin15', blank=True, null=True)  # Field name made lowercase.
    dbcjoin16 = models.BigIntegerField(db_column='dbcJoin16', blank=True, null=True)  # Field name made lowercase.
    dbcreal15 = models.CharField(db_column='dbcReal15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect20 = models.BigIntegerField(db_column='dbcSelect20', blank=True, null=True)  # Field name made lowercase.
    dbcreal16 = models.CharField(db_column='dbcReal16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect21 = models.BigIntegerField(db_column='dbcSelect21', blank=True, null=True)  # Field name made lowercase.
    dbcdate18 = models.CharField(db_column='dbcDate18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation11 = models.BigIntegerField(db_column='dbcRelation11', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_test'


class Payment(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    stage = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    actualtime = models.CharField(db_column='actualTime', max_length=19, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    contractid = models.CharField(db_column='contractId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.CharField(db_column='totalAmount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentpercent = models.CharField(db_column='paymentPercent', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.IntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.CharField(db_column='applicantId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    invoiceflg = models.IntegerField(db_column='invoiceFlg', blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.IntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.CharField(db_column='dbcVarchar1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin1 = models.CharField(db_column='dbcJoin1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.CharField(db_column='dbcVarchar2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.CharField(db_column='dbcVarchar3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.CharField(db_column='dbcVarchar4', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentDeduction(models.Model):
    # id = models.BigAutoField(primary_key=True)
    pid = models.IntegerField()
    deduction_fund = models.FloatField()
    oid = models.IntegerField()
    etime = models.CharField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_deduction'


class PaymentsStatus(models.Model):
    pid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payments_status'


class PaymentsStatusList(models.Model):
    pid = models.IntegerField()
    oid = models.IntegerField()
    c1_name = models.CharField(max_length=255, blank=True, null=True)
    c1_all = models.FloatField(blank=True, null=True)
    c1_80 = models.FloatField(blank=True, null=True)
    c1_20_base = models.FloatField(blank=True, null=True)
    c2_name = models.CharField(max_length=255, blank=True, null=True)
    c2_all = models.FloatField(blank=True, null=True)
    c2_80 = models.FloatField(blank=True, null=True)
    c2_20_base = models.FloatField(blank=True, null=True)
    c3_name = models.CharField(max_length=255, blank=True, null=True)
    c3_all = models.FloatField(blank=True, null=True)
    c3_80 = models.FloatField(blank=True, null=True)
    c3_20_base = models.FloatField(blank=True, null=True)
    l4_name = models.CharField(max_length=255, blank=True, null=True)
    l4_all = models.FloatField(blank=True, null=True)
    l4_80_base = models.FloatField(blank=True, null=True)
    l4_20_base = models.FloatField(blank=True, null=True)
    l3_name = models.CharField(max_length=255, blank=True, null=True)
    l3_all = models.FloatField(blank=True, null=True)
    l3_80_base = models.FloatField(blank=True, null=True)
    l3_20_base = models.FloatField(blank=True, null=True)
    renew_name = models.CharField(max_length=255, blank=True, null=True)
    renew_all = models.FloatField(blank=True, null=True)
    renew_80_base = models.FloatField(blank=True, null=True)
    renew_20_base = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    order_all_price = models.FloatField(blank=True, null=True)
    achievement_all_money = models.FloatField(blank=True, null=True)
    commission_base = models.FloatField(blank=True, null=True)
    payment_money = models.FloatField(blank=True, null=True)
    saler_commissions_all = models.FloatField(blank=True, null=True)
    manage_commissions_all = models.FloatField(blank=True, null=True)
    payment_date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments_status_list'


class PaymentsUserInfo(models.Model):
    pid = models.CharField(max_length=255)
    oid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'payments_user_info'


class Product(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    productname = models.TextField(db_column='productName', blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='parentId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='ownerId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    priceunit = models.CharField(db_column='priceUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unit = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    enablestatus = models.IntegerField(db_column='enableStatus', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    dimdepart = models.CharField(db_column='dimDepart', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.IntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.CharField(db_column='dbcReal2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar2 = models.TextField(db_column='dbcVarchar2', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar3 = models.TextField(db_column='dbcVarchar3', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar4 = models.TextField(db_column='dbcVarchar4', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar5 = models.TextField(db_column='dbcVarchar5', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar6 = models.TextField(db_column='dbcVarchar6', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar7 = models.TextField(db_column='dbcVarchar7', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.TextField(db_column='dbcVarchar8', blank=True, null=True)  # Field name made lowercase.
    fsctrackedasasset = models.BigIntegerField(db_column='fscTrackedAsAsset', blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.BigIntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.BigIntegerField(db_column='applicantId', blank=True, null=True)  # Field name made lowercase.
    dbcselect3 = models.BigIntegerField(db_column='dbcSelect3', blank=True, null=True)  # Field name made lowercase.
    dbcselect4 = models.BigIntegerField(db_column='dbcSelect4', blank=True, null=True)  # Field name made lowercase.
    dbcselect5 = models.BigIntegerField(db_column='dbcSelect5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Productinfo(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    orderproductid = models.IntegerField(db_column='orderProductId', blank=True, null=True)  # Field name made lowercase.
    po = models.CharField(max_length=255, blank=True, null=True)
    productid = models.IntegerField(db_column='productId', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.CharField(db_column='unitPrice', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quantity = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=20, blank=True, null=True)
    pricetotal = models.CharField(db_column='priceTotal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    createdby = models.CharField(db_column='createdBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    standardprice = models.CharField(db_column='standardPrice', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=19, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=19, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcreal1 = models.CharField(db_column='dbcReal1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    dbcreal2 = models.FloatField(db_column='dbcReal2', blank=True, null=True)  # Field name made lowercase.
    dbcreal3 = models.FloatField(db_column='dbcReal3', blank=True, null=True)  # Field name made lowercase.
    dbcreal4 = models.FloatField(db_column='dbcReal4', blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.IntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productinfo'


class QuarterlyResults(models.Model):
    name = models.CharField(max_length=50)
    q1 = models.CharField(db_column='Q1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q2 = models.CharField(db_column='Q2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q3 = models.CharField(db_column='Q3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q4 = models.CharField(db_column='Q4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q5 = models.CharField(db_column='Q5', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quarterly_results'


class QuarterlyResultsCopy(models.Model):
    name = models.CharField(max_length=50)
    q1 = models.CharField(db_column='Q1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q2 = models.CharField(db_column='Q2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q3 = models.CharField(db_column='Q3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q4 = models.CharField(db_column='Q4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q5 = models.CharField(db_column='Q5', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quarterly_results_copy'


class QuarterlyResultsCopy1(models.Model):
    name = models.CharField(max_length=50)
    q1 = models.CharField(db_column='Q1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q2 = models.CharField(db_column='Q2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q3 = models.CharField(db_column='Q3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q4 = models.CharField(db_column='Q4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    q5 = models.CharField(db_column='Q5', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quarterly_results_copy1'


class RenewCompletion(models.Model):
    department_l1 = models.CharField(max_length=255, blank=True, null=True)
    q1_per = models.FloatField(blank=True, null=True)
    q2_per = models.FloatField(blank=True, null=True)
    q3_per = models.FloatField(blank=True, null=True)
    q4_per = models.FloatField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'renew_completion'


class Renewsingle(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    departname = models.CharField(db_column='departName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parentdepartid = models.IntegerField(db_column='parentDepartId', blank=True, null=True)  # Field name made lowercase.
    bm0 = models.CharField(max_length=20, blank=True, null=True)
    bm1 = models.CharField(max_length=20, blank=True, null=True)
    bm2 = models.CharField(max_length=20, blank=True, null=True)
    bm3 = models.CharField(max_length=20, blank=True, null=True)
    bm0id = models.IntegerField(blank=True, null=True)
    bm1id = models.IntegerField(blank=True, null=True)
    bm2id = models.IntegerField(blank=True, null=True)
    bm3id = models.IntegerField(blank=True, null=True)
    thisweek = models.IntegerField(db_column='thisWeek', blank=True, null=True)  # Field name made lowercase.
    thisweekjie = models.IntegerField(db_column='thisWeekjie', blank=True, null=True)  # Field name made lowercase.
    january = models.IntegerField(blank=True, null=True)
    januaryjie = models.IntegerField(blank=True, null=True)
    february = models.IntegerField(blank=True, null=True)
    februaryjie = models.IntegerField(blank=True, null=True)
    march = models.IntegerField(blank=True, null=True)
    marchjie = models.IntegerField(blank=True, null=True)
    april = models.IntegerField(blank=True, null=True)
    apriljie = models.IntegerField(blank=True, null=True)
    may = models.IntegerField(blank=True, null=True)
    mayjie = models.IntegerField(blank=True, null=True)
    junejie = models.IntegerField(blank=True, null=True)
    june = models.IntegerField(blank=True, null=True)
    july = models.IntegerField(blank=True, null=True)
    julyjie = models.IntegerField(blank=True, null=True)
    august = models.IntegerField(blank=True, null=True)
    augustjie = models.IntegerField(blank=True, null=True)
    september = models.IntegerField(blank=True, null=True)
    septemberjie = models.IntegerField(blank=True, null=True)
    october = models.IntegerField(blank=True, null=True)
    octoberjie = models.IntegerField(blank=True, null=True)
    november = models.IntegerField(blank=True, null=True)
    novemberjie = models.IntegerField(blank=True, null=True)
    december = models.IntegerField(blank=True, null=True)
    decemberjie = models.IntegerField(blank=True, null=True)
    monthlytotal = models.IntegerField(blank=True, null=True)
    monthlytotaljjie = models.IntegerField(blank=True, null=True)
    efficiency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'renewsingle'


class SaleMothAchievement(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    year = models.CharField(max_length=4)
    department = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    m1_target = models.FloatField(blank=True, null=True)
    m1_complete = models.FloatField(blank=True, null=True)
    m1_per = models.FloatField(blank=True, null=True)
    m2_target = models.FloatField(blank=True, null=True)
    m2_complete = models.FloatField(blank=True, null=True)
    m2_per = models.FloatField(blank=True, null=True)
    m3_target = models.FloatField(blank=True, null=True)
    m3_complete = models.FloatField(blank=True, null=True)
    m3_per = models.FloatField(blank=True, null=True)
    m4_target = models.FloatField(blank=True, null=True)
    m4_complete = models.FloatField(blank=True, null=True)
    m4_per = models.FloatField(blank=True, null=True)
    m5_target = models.FloatField(blank=True, null=True)
    m5_complete = models.FloatField(blank=True, null=True)
    m5_per = models.FloatField(blank=True, null=True)
    m6_target = models.FloatField(blank=True, null=True)
    m6_complete = models.FloatField(blank=True, null=True)
    m6_per = models.FloatField(blank=True, null=True)
    m7_target = models.FloatField(blank=True, null=True)
    m7_complete = models.FloatField(blank=True, null=True)
    m7_per = models.FloatField(blank=True, null=True)
    m8_target = models.FloatField(blank=True, null=True)
    m8_complete = models.FloatField(blank=True, null=True)
    m8_per = models.FloatField(blank=True, null=True)
    m9_target = models.FloatField(blank=True, null=True)
    m9_complete = models.FloatField(blank=True, null=True)
    m9_per = models.FloatField(blank=True, null=True)
    m10_target = models.FloatField(blank=True, null=True)
    m10_complete = models.FloatField(blank=True, null=True)
    m10_per = models.FloatField(blank=True, null=True)
    m11_target = models.FloatField(blank=True, null=True)
    m11_complete = models.FloatField(blank=True, null=True)
    m11_per = models.FloatField(blank=True, null=True)
    m12_target = models.FloatField(blank=True, null=True)
    m12_complete = models.FloatField(blank=True, null=True)
    m12_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_moth_achievement'


class SoftwareCopyright(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    dependentvalue = models.CharField(db_column='dependentValue', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'software_copyright'


class StaffMember(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=255)
    department_l1 = models.CharField(max_length=255)
    department_l2 = models.CharField(max_length=255, blank=True, null=True)
    department_l3 = models.CharField(max_length=255, blank=True, null=True)
    department_l4 = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    commissions_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_member'


class StaffMemberCopy(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=255)
    department_l1 = models.CharField(max_length=255)
    department_l2 = models.CharField(max_length=255, blank=True, null=True)
    department_l3 = models.CharField(max_length=255, blank=True, null=True)
    department_l4 = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    commissions_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_member_copy'


class SummaryOfAccounts(models.Model):
    accountid = models.BigIntegerField(db_column='accountId')  # Field name made lowercase.
    contractnum = models.CharField(db_column='contractNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(max_length=100, blank=True, null=True)
    dbcdate8 = models.DateTimeField(db_column='dbcDate8', blank=True, null=True)  # Field name made lowercase.
    dbcdate5 = models.DateTimeField(db_column='dbcDate5', blank=True, null=True)  # Field name made lowercase.
    contrgdnum = models.CharField(db_column='contrGdnum', max_length=11, blank=True, null=True)  # Field name made lowercase.
    dbcdate6 = models.DateTimeField(db_column='dbcDate6', blank=True, null=True)  # Field name made lowercase.
    contrtype = models.CharField(db_column='contrType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bdcontrname = models.CharField(db_column='bdContrName', max_length=11, blank=True, null=True)  # Field name made lowercase.
    sealname = models.CharField(db_column='sealName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    finaluser = models.BigIntegerField(db_column='finalUser', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(max_length=32, blank=True, null=True)
    actualmoney = models.CharField(db_column='actualMoney', max_length=32, blank=True, null=True)  # Field name made lowercase.
    contrbengtime = models.DateTimeField(db_column='contrBengTime', blank=True, null=True)  # Field name made lowercase.
    contrendtime = models.DateTimeField(db_column='contrEndTime', blank=True, null=True)  # Field name made lowercase.
    givebentime = models.DateTimeField(db_column='giveBenTime', blank=True, null=True)  # Field name made lowercase.
    giveendtime = models.DateTimeField(db_column='giveEndTime', blank=True, null=True)  # Field name made lowercase.
    finalovertime = models.CharField(db_column='finalOverTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ifforeign = models.CharField(db_column='ifForeign', max_length=10, blank=True, null=True)  # Field name made lowercase.
    salesman = models.CharField(db_column='salesMan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    salesbm = models.CharField(db_column='salesBm', max_length=32, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=32, blank=True, null=True)
    contractattribute = models.CharField(db_column='contractAttribute', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contractstatus = models.CharField(db_column='contractStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ordercomment = models.TextField(db_column='orderComment', blank=True, null=True)  # Field name made lowercase.
    orderxdnum = models.CharField(db_column='orderXdnum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    backmethod = models.CharField(db_column='backMethod', max_length=11, blank=True, null=True)  # Field name made lowercase.
    orderrelquotationentity = models.CharField(db_column='orderRelQuotationEntity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contractid = models.BigIntegerField(db_column='contractId', blank=True, null=True)  # Field name made lowercase.
    effectivedate = models.DateTimeField(db_column='effectiveDate', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    oneindustry = models.CharField(db_column='oneIndustry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    towindustry = models.CharField(db_column='towIndustry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cumulativeback = models.CharField(db_column='cumulativeBack', max_length=255, blank=True, null=True)  # Field name made lowercase.
    finalindustry = models.CharField(db_column='finalIndustry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contmonth = models.CharField(db_column='contMonth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contyear = models.CharField(db_column='contYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ljmoney = models.CharField(max_length=255, blank=True, null=True)
    ljbackmoney = models.CharField(max_length=255, blank=True, null=True)
    waifind = models.CharField(db_column='waiFind', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=255, blank=True, null=True)
    agentname = models.CharField(db_column='agentName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    givemonth = models.CharField(db_column='giveMonth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    giveterm = models.CharField(db_column='giveTerm', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'summary_of_accounts'


class TokenInfo(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    access_token = models.CharField(max_length=64, blank=True, null=True)
    access_token_time = models.DateTimeField(blank=True, null=True)
    redirect_uri = models.CharField(max_length=32, blank=True, null=True)
    issued_at = models.CharField(max_length=32, blank=True, null=True)
    token_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token_info'


class User(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    departid = models.CharField(db_column='departId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employeecode = models.TextField(db_column='employeeCode', blank=True, null=True)  # Field name made lowercase.
    unionid = models.TextField(db_column='unionId', blank=True, null=True)  # Field name made lowercase.
    gender = models.BigIntegerField(blank=True, null=True)
    joinatstr = models.CharField(db_column='joinAtStr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(max_length=255, blank=True, null=True)
    passwordruleid = models.BigIntegerField(db_column='passwordRuleId', blank=True, null=True)  # Field name made lowercase.
    hiddenyearflg = models.CharField(db_column='hiddenYearFlg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    positionname = models.TextField(db_column='positionName', blank=True, null=True)  # Field name made lowercase.
    rankid = models.BigIntegerField(db_column='rankId', blank=True, null=True)  # Field name made lowercase.
    usermanagerid = models.BigIntegerField(db_column='userManagerId', blank=True, null=True)  # Field name made lowercase.
    languagecode = models.TextField(db_column='languageCode', blank=True, null=True)  # Field name made lowercase.
    timezone = models.TextField(blank=True, null=True)
    mobilelocationstatus = models.CharField(db_column='mobileLocationStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nickname = models.TextField(db_column='nickName', blank=True, null=True)  # Field name made lowercase.
    statusint = models.BigIntegerField(db_column='statusInt', blank=True, null=True)  # Field name made lowercase.
    lastestloginat = models.CharField(db_column='lastestLoginAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selfintro = models.TextField(db_column='selfIntro', blank=True, null=True)  # Field name made lowercase.
    telephone = models.TextField(blank=True, null=True)
    extno = models.TextField(db_column='extNo', blank=True, null=True)  # Field name made lowercase.
    expertise = models.TextField(blank=True, null=True)
    hometown = models.TextField(blank=True, null=True)
    im = models.TextField(blank=True, null=True)
    weibo = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class User20190815(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    entitytype = models.CharField(db_column='entityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    departid = models.CharField(db_column='departId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employeecode = models.TextField(db_column='employeeCode', blank=True, null=True)  # Field name made lowercase.
    unionid = models.TextField(db_column='unionId', blank=True, null=True)  # Field name made lowercase.
    gender = models.BigIntegerField(blank=True, null=True)
    joinatstr = models.CharField(db_column='joinAtStr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(max_length=255, blank=True, null=True)
    passwordruleid = models.BigIntegerField(db_column='passwordRuleId', blank=True, null=True)  # Field name made lowercase.
    hiddenyearflg = models.CharField(db_column='hiddenYearFlg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    positionname = models.TextField(db_column='positionName', blank=True, null=True)  # Field name made lowercase.
    rankid = models.BigIntegerField(db_column='rankId', blank=True, null=True)  # Field name made lowercase.
    usermanagerid = models.BigIntegerField(db_column='userManagerId', blank=True, null=True)  # Field name made lowercase.
    languagecode = models.TextField(db_column='languageCode', blank=True, null=True)  # Field name made lowercase.
    timezone = models.TextField(blank=True, null=True)
    mobilelocationstatus = models.CharField(db_column='mobileLocationStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nickname = models.TextField(db_column='nickName', blank=True, null=True)  # Field name made lowercase.
    statusint = models.BigIntegerField(db_column='statusInt', blank=True, null=True)  # Field name made lowercase.
    lastestloginat = models.CharField(db_column='lastestLoginAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selfintro = models.TextField(db_column='selfIntro', blank=True, null=True)  # Field name made lowercase.
    telephone = models.TextField(blank=True, null=True)
    extno = models.TextField(db_column='extNo', blank=True, null=True)  # Field name made lowercase.
    expertise = models.TextField(blank=True, null=True)
    hometown = models.TextField(blank=True, null=True)
    im = models.TextField(blank=True, null=True)
    weibo = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    createdat = models.CharField(db_column='createdAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_20190815'


class Userinfo(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    tenantid = models.IntegerField(db_column='tenantId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    icon = models.CharField(max_length=150, blank=True, null=True)
    unionid = models.IntegerField(db_column='unionId', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    statusint = models.IntegerField(db_column='statusInt', blank=True, null=True)  # Field name made lowercase.
    employeecode = models.CharField(db_column='employeeCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    usermanagerid = models.IntegerField(db_column='userManagerId', blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(max_length=10, blank=True, null=True)
    departid = models.IntegerField(db_column='departId', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(max_length=20, blank=True, null=True)
    joinatstr = models.CharField(db_column='joinAtStr', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'

