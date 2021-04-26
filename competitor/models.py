# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# python manage.py inspectdb  --database  contract_33 crm_competitor_map competitor >competitor/models_bak.py

from django.db import models

class CrmIndustryL1(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_industry_l1'


class CrmIndustryL2(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_industry_l2'

class CrmLocationState(models.Model):
    lid = models.IntegerField(primary_key=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_location_State'

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
    id = models.BigIntegerField(blank=True, primary_key=True)
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
        db_table = 'account'



class Product(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
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


class SalesPortraitCrm(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
    ownerid = models.CharField(db_column='ownerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdat = models.CharField(db_column='createdAt', max_length=100, blank=True, null=True)  # Field name made lowercase.
    crm_industry_l1 = models.CharField(max_length=100, blank=True, null=True)
    crm_industry_l2 = models.CharField(max_length=100, blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    highseastatus = models.IntegerField(db_column='highSeaStatus', blank=True, null=True)  # Field name made lowercase.
    crm_industry_l1_name = models.CharField(max_length=100, blank=True, null=True)
    crm_industry_l2_name = models.CharField(max_length=100, blank=True, null=True)
    provincename = models.CharField(db_column='provinceName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='cityName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    districtname = models.CharField(db_column='districtName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    opp_num = models.IntegerField(blank=True, null=True)
    ms_num = models.IntegerField(blank=True, null=True)
    jt_num = models.IntegerField(blank=True, null=True)
    tsgz_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales_portrait_crm'


class Competitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    competitorid = models.BigIntegerField(db_column='competitorId', blank=True, null=True)  # Field name made lowercase.
    competitorname = models.CharField(db_column='competitorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    competitorproductid = models.BigIntegerField(db_column='competitorProductId', blank=True, null=True)  # Field name made lowercase.
    competitorproduct = models.CharField(db_column='competitorProduct', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='remark', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source_type = models.IntegerField(db_column='source_type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'competitor'


class CrmCompetitorMap(models.Model):
    id = models.BigIntegerField(primary_key=True)
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


class User(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
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



class Order(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
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
    receiptamount = models.CharField(db_column='receiptAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lockstatus = models.BigIntegerField(db_column='lockStatus', blank=True, null=True)  # Field name made lowercase.
    receiptbalance = models.CharField(db_column='receiptBalance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.BigIntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    applicantid = models.BigIntegerField(db_column='applicantId', blank=True, null=True)  # Field name made lowercase.
    amountinvoiced = models.CharField(db_column='amountInvoiced', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation1 = models.BigIntegerField(db_column='dbcRelation1', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.CharField(db_column='transactionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    listtotal = models.FloatField(db_column='listTotal', blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.FloatField(db_column='totalDiscountAmount', blank=True, null=True)  # Field name made lowercase.
    orderversion = models.BigIntegerField(db_column='orderVersion', blank=True, null=True)  # Field name made lowercase.
    totalinvoiceadjustmentamount = models.CharField(db_column='totalInvoiceAdjustmentAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalorderversion = models.BigIntegerField(db_column='originalOrderVersion', blank=True, null=True)  # Field name made lowercase.
    actualinvoicedamount = models.CharField(db_column='actualInvoicedAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar1 = models.TextField(db_column='dbcVarchar1', blank=True, null=True)  # Field name made lowercase.
    co = models.CharField(max_length=300, blank=True, null=True)
    amountunbilled = models.CharField(db_column='amountUnbilled', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcselect1 = models.BigIntegerField(db_column='dbcSelect1', blank=True, null=True)  # Field name made lowercase.
    totalpaymentamount = models.CharField(db_column='totalPaymentAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate1 = models.CharField(db_column='dbcDate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    totalrefundamount = models.CharField(db_column='totalRefundAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate2 = models.CharField(db_column='dbcDate2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.CharField(db_column='paidAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalorderid = models.BigIntegerField(db_column='originalOrderId', blank=True, null=True)  # Field name made lowercase.
    dbcselect2 = models.BigIntegerField(db_column='dbcSelect2', blank=True, null=True)  # Field name made lowercase.
    paymentbalance = models.CharField(db_column='paymentBalance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate3 = models.CharField(db_column='dbcDate3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoicebalance = models.CharField(db_column='invoiceBalance', max_length=255, blank=True, null=True)  # Field name made lowercase.
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
    dbcjoin6 = models.CharField(db_column='dbcJoin6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal6 = models.CharField(db_column='dbcReal6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcrelation8 = models.BigIntegerField(db_column='dbcRelation8', blank=True, null=True)  # Field name made lowercase.
    dbcrelation9 = models.BigIntegerField(db_column='dbcRelation9', blank=True, null=True)  # Field name made lowercase.
    dbcrelation10 = models.BigIntegerField(db_column='dbcRelation10', blank=True, null=True)  # Field name made lowercase.
    dbcreal7 = models.FloatField(db_column='dbcReal7', blank=True, null=True)  # Field name made lowercase.
    dbcreal8 = models.FloatField(db_column='dbcReal8', blank=True, null=True)  # Field name made lowercase.
    dbcreal9 = models.FloatField(db_column='dbcReal9', blank=True, null=True)  # Field name made lowercase.
    dbcjoin7 = models.CharField(db_column='dbcJoin7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate11 = models.CharField(db_column='dbcDate11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal10 = models.CharField(db_column='dbcReal10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate12 = models.CharField(db_column='dbcDate12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal11 = models.CharField(db_column='dbcReal11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar8 = models.CharField(db_column='dbcVarchar8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin8 = models.CharField(db_column='dbcJoin8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal12 = models.CharField(db_column='dbcReal12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect15 = models.BigIntegerField(db_column='dbcSelect15', blank=True, null=True)  # Field name made lowercase.
    dbcselect16 = models.BigIntegerField(db_column='dbcSelect16', blank=True, null=True)  # Field name made lowercase.
    custcheckbox1 = models.CharField(db_column='custCheckbox1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcjoin9 = models.CharField(db_column='dbcJoin9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin10 = models.CharField(db_column='dbcJoin10', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar9 = models.CharField(db_column='dbcVarchar9', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin11 = models.CharField(db_column='dbcJoin11', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate13 = models.CharField(db_column='dbcDate13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate14 = models.CharField(db_column='dbcDate14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate15 = models.CharField(db_column='dbcDate15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcdate16 = models.CharField(db_column='dbcDate16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar11 = models.TextField(db_column='dbcVarchar11', blank=True, null=True)  # Field name made lowercase.
    dbctextarea1 = models.TextField(db_column='dbcTextarea1', blank=True, null=True)  # Field name made lowercase.
    dbcjoin12 = models.CharField(db_column='dbcJoin12', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect17 = models.BigIntegerField(db_column='dbcSelect17', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar10 = models.TextField(db_column='dbcVarchar10', blank=True, null=True)  # Field name made lowercase.
    dbcreal13 = models.CharField(db_column='dbcReal13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbcreal14 = models.CharField(db_column='dbcReal14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcdate17 = models.CharField(db_column='dbcDate17', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect18 = models.BigIntegerField(db_column='dbcSelect18', blank=True, null=True)  # Field name made lowercase.
    dbcselect19 = models.BigIntegerField(db_column='dbcSelect19', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar12 = models.TextField(db_column='dbcVarchar12', blank=True, null=True)  # Field name made lowercase.
    dbcjoin13 = models.CharField(db_column='dbcJoin13', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar13 = models.TextField(db_column='dbcVarchar13', blank=True, null=True)  # Field name made lowercase.
    dbcjoin14 = models.CharField(db_column='dbcJoin14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar14 = models.CharField(db_column='dbcVarchar14', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcvarchar15 = models.CharField(db_column='dbcVarchar15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin15 = models.CharField(db_column='dbcJoin15', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin16 = models.CharField(db_column='dbcJoin16', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcreal15 = models.FloatField(db_column='dbcReal15', blank=True, null=True)  # Field name made lowercase.
    dbcsvarchar1 = models.CharField(db_column='dbcSVarchar1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbcselect20 = models.BigIntegerField(db_column='dbcSelect20', blank=True, null=True)  # Field name made lowercase.
    dbcreal16 = models.FloatField(db_column='dbcReal16', blank=True, null=True)  # Field name made lowercase.
    dbcselect21 = models.BigIntegerField(db_column='dbcSelect21', blank=True, null=True)  # Field name made lowercase.
    dbcdate18 = models.CharField(db_column='dbcDate18', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect22 = models.BigIntegerField(db_column='dbcSelect22', blank=True, null=True)  # Field name made lowercase.
    dbcjoin17 = models.CharField(db_column='dbcJoin17', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin18 = models.CharField(db_column='dbcJoin18', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcjoin19 = models.CharField(db_column='dbcJoin19', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dbcselect23 = models.BigIntegerField(db_column='dbcSelect23', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar16 = models.TextField(db_column='dbcVarchar16', blank=True, null=True)  # Field name made lowercase.
    dbcvarchar17 = models.TextField(db_column='dbcVarchar17', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'
