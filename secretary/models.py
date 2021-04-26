# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WkTDinggroup(models.Model):
    did = models.IntegerField(db_column='Did')  # Field name made lowercase.
    dpid = models.IntegerField(db_column='Dpid')  # Field name made lowercase.
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'WK_T_DINGGROUP'


class Salercansee(models.Model):
    salename = models.CharField(db_column='saleName', primary_key=True, max_length=255)  # Field name made lowercase.
    cansee = models.TextField(db_column='canSee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SALERCANSEE'

class SalercanseeNew(models.Model):
    salename = models.CharField(db_column='saleName', primary_key=True, max_length=255)  # Field name made lowercase.
    saleid = models.CharField(db_column='saleId', max_length=50,blank=True, null=True)  # Field name made lowercase.
    cansee = models.TextField(db_column='canSee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SALERCANSEENEW'


"""预处理 —— 钉钉部门成员关系对应表"""
class DingGroupMemberMap(models.Model):
    group_id = models.TextField(verbose_name="钉钉部门ID")
    group_name = models.TextField(verbose_name="钉钉部门名称")
    sub_group_ids = models.TextField(verbose_name="下级部门ID")
    sub_group_names = models.TextField(verbose_name="下级部门名称")
    sub_group_ids_all = models.TextField(verbose_name="所有下级部门ID")
    sub_group_names_all = models.TextField(verbose_name="所有下级部门名称")
    member_ids = models.TextField(verbose_name="部门成员ID")
    member_names = models.TextField(verbose_name="部门成员名字")
    member_ids_all = models.TextField(verbose_name="所有成员ID")
    member_names_all = models.TextField(verbose_name="所有成员名字")
    istarshine_ids = models.TextField(verbose_name='部门成员的星光ID')
    istarshine_ids_all = models.TextField(verbose_name='部门以及下属部门所有成员的星光ID')

    class Meta:
        managed = False
        db_table = 'ding_group_member_map'


class WkTUser(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID', primary_key=True)  # Field name made lowercase.
    ku_lid = models.CharField(db_column='KU_LID', max_length=100)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_passwd = models.CharField(db_column='KU_PASSWD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_regdate = models.CharField(db_column='KU_REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_status = models.CharField(db_column='KU_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_sex = models.CharField(db_column='KU_SEX', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_birthday = models.CharField(db_column='KU_BIRTHDAY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_email = models.CharField(db_column='KU_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_phone = models.CharField(db_column='KU_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_company = models.CharField(db_column='KU_COMPANY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kd_id = models.IntegerField(db_column='KD_ID')  # Field name made lowercase.
    ku_level = models.IntegerField(db_column='KU_LEVEL', blank=True, null=True)  # Field name made lowercase.
    ku_ltime = models.CharField(db_column='KU_LTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_rtime = models.CharField(db_column='KU_RTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_lastaddr = models.CharField(db_column='KU_LASTADDR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_online = models.CharField(db_column='KU_ONLINE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_ltimes = models.IntegerField(db_column='KU_LTIMES', blank=True, null=True)  # Field name made lowercase.
    ku_limit = models.IntegerField(db_column='KU_LIMIT', blank=True, null=True)  # Field name made lowercase.
    ku_style = models.CharField(db_column='KU_STYLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_autoshow = models.CharField(db_column='KU_AUTOSHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_autoenter = models.CharField(db_column='KU_AUTOENTER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_bindtype = models.CharField(db_column='KU_BINDTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_bindaddr = models.CharField(db_column='KU_BINDADDR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_question = models.CharField(db_column='KU_QUESTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ku_answer = models.CharField(db_column='KU_ANSWER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oldlid = models.CharField(db_column='OLDLID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_refname = models.CharField(db_column='KU_REFNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_jzqb = models.CharField(db_column='KU_JZQB', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_xiaoshou = models.CharField(db_column='KU_XIAOSHOU', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_passwdxt = models.CharField(db_column='KU_PASSWDXT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_template = models.CharField(db_column='KU_TEMPLATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_dbname = models.CharField(db_column='KU_DBNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_search = models.CharField(db_column='KU_SEARCH', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER'


class WkTUserservice(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID', primary_key=True)  # Field name made lowercase.
    ku_mailcount = models.IntegerField(db_column='KU_MAILCOUNT')  # Field name made lowercase.
    ku_phonecount = models.IntegerField(db_column='KU_PHONECOUNT')  # Field name made lowercase.
    ku_topiccount = models.IntegerField(db_column='KU_TOPICCOUNT')  # Field name made lowercase.
    ku_tradecount = models.IntegerField(db_column='KU_TRADECOUNT')  # Field name made lowercase.
    ku_dayreport = models.CharField(db_column='KU_DAYREPORT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_weekreport = models.CharField(db_column='KU_WEEKREPORT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_monthreport = models.CharField(db_column='KU_MONTHREPORT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_trysdate = models.CharField(db_column='KU_TRYSDATE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ku_userstatus = models.CharField(db_column='KU_USERSTATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordcount = models.IntegerField(db_column='KU_WORDCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_orientationlevel = models.CharField(db_column='KU_ORIENTATIONLEVEL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_dayreporttime = models.CharField(db_column='KU_DAYREPORTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_t_type = models.CharField(db_column='KU_T_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_t_blog = models.CharField(db_column='KU_T_BLOG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_t_phonecount = models.CharField(db_column='KU_T_PHONECOUNT', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ku_t_showall = models.CharField(db_column='KU_T_SHOWALL', max_length=2)  # Field name made lowercase.
    ku_yjwordcount = models.IntegerField(db_column='KU_YJWORDCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_weiboyj = models.IntegerField(db_column='KU_WEIBOYJ', blank=True, null=True)  # Field name made lowercase.
    ku_overtime = models.CharField(db_column='KU_OVERTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_qq = models.CharField(db_column='KU_QQ', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_bbscount = models.IntegerField(db_column='KU_BBSCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_bbsview = models.CharField(db_column='KU_BBSVIEW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_insertinfo = models.CharField(db_column='KU_INSERTINFO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_showallsub = models.CharField(db_column='KU_SHOWALLSUB', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_single = models.CharField(db_column='KU_SINGLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_reporttitle = models.CharField(db_column='KU_REPORTTITLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_areaset = models.CharField(db_column='KU_AREASET', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_showsource = models.CharField(db_column='KU_SHOWSOURCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_commyj = models.CharField(db_column='KU_COMMYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_sendinfo = models.CharField(db_column='KU_SENDINFO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_bbsallinfo = models.CharField(db_column='KU_BBSALLINFO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_size = models.CharField(db_column='KU_SIZE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_showabs = models.CharField(db_column='KU_SHOWABS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_openzs = models.CharField(db_column='KU_OPENZS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_test = models.CharField(db_column='KU_TEST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_zsdate = models.CharField(db_column='KU_ZSDATE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ku_usertrend = models.CharField(db_column='KU_USERTREND', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_commzt = models.CharField(db_column='KU_COMMZT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_savedays = models.IntegerField(db_column='KU_SAVEDAYS')  # Field name made lowercase.
    ku_sendreport = models.CharField(db_column='KU_SENDREPORT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_localbbsyj = models.CharField(db_column='KU_LOCALBBSYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_sourcetype = models.CharField(db_column='KU_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_userdatatype = models.CharField(db_column='KU_USERDATATYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_openedzsuser = models.CharField(db_column='KU_OPENEDZSUSER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_jingzhun = models.CharField(db_column='KU_JINGZHUN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_tuisongcount = models.IntegerField(db_column='KU_TUISONGCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_sound = models.CharField(db_column='KU_SOUND', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_zfwords = models.CharField(db_column='KU_ZFWORDS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_allexport = models.CharField(db_column='KU_ALLEXPORT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_setreport = models.CharField(db_column='KU_SETREPORT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_showreport = models.CharField(db_column='KU_SHOWREPORT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_reporttemplate = models.CharField(db_column='KU_REPORTTEMPLATE', max_length=100)  # Field name made lowercase.
    ku_weixin = models.CharField(db_column='KU_WEIXIN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_setabstract = models.CharField(db_column='KU_SETABSTRACT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_ordertime = models.CharField(db_column='KU_ORDERTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_classify = models.CharField(db_column='KU_CLASSIFY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_zaoyin = models.CharField(db_column='KU_ZAOYIN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_orderzttj = models.CharField(db_column='KU_ORDERZTTJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_zstime = models.CharField(db_column='KU_ZSTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_sytime = models.CharField(db_column='KU_SYTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_trytime = models.CharField(db_column='KU_TRYTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_repeat = models.CharField(db_column='KU_REPEAT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_car = models.CharField(db_column='KU_CAR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_finance = models.CharField(db_column='KU_FINANCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_travel = models.CharField(db_column='KU_TRAVEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_homequery = models.CharField(db_column='KU_HOMEQUERY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_weixincheck = models.CharField(db_column='KU_WEIXINCHECK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_openhighset = models.CharField(db_column='KU_OPENHIGHSET', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_qqcount = models.IntegerField(db_column='KU_QQCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_weixinnumcount = models.IntegerField(db_column='KU_WEIXINNUMCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_weixingroupcount = models.IntegerField(db_column='KU_WEIXINGROUPCOUNT', blank=True, null=True)  # Field name made lowercase.
    ku_isopensyspass = models.IntegerField(db_column='KU_ISOPENSYSPASS')  # Field name made lowercase.
    ku_xtzaoyin = models.CharField(db_column='KU_XTZAOYIN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_zqrubbish = models.CharField(db_column='KU_ZQRUBBISH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_yjtime = models.CharField(db_column='KU_YJTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_sale = models.CharField(db_column='KU_SALE', max_length=30)  # Field name made lowercase.
    ku_maint = models.CharField(db_column='KU_MAINT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ku_subject = models.IntegerField(db_column='KU_SUBJECT')  # Field name made lowercase.
    ku_moban = models.IntegerField(db_column='KU_MOBAN')  # Field name made lowercase.
    ku_sunmanage = models.IntegerField(db_column='KU_SUNMANAGE')  # Field name made lowercase.
    ku_iszxqy = models.IntegerField(db_column='KU_ISZXQY')  # Field name made lowercase.
    ku_iswf = models.CharField(db_column='KU_ISWF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_valid_email = models.IntegerField(db_column='IS_VALID_EMAIL')  # Field name made lowercase.
    ku_islocationref = models.CharField(db_column='KU_ISLOCATIONREF', max_length=2)  # Field name made lowercase.
    ku_istibetan = models.IntegerField(db_column='KU_ISTIBETAN')  # Field name made lowercase.
    ku_isforlanguage = models.IntegerField(db_column='KU_ISFORLANGUAGE')  # Field name made lowercase.
    ku_usergenre = models.IntegerField(db_column='KU_USERGENRE')  # Field name made lowercase.
    ku_groupid = models.CharField(db_column='KU_GROUPID', max_length=32)  # Field name made lowercase.
    ku_alertwin = models.IntegerField(db_column='KU_ALERTWIN')  # Field name made lowercase.
    ku_iswxpush = models.IntegerField(db_column='KU_ISWXPUSH')  # Field name made lowercase.
    ku_oaid = models.IntegerField(db_column='KU_OAID')  # Field name made lowercase.
    ku_version = models.CharField(db_column='KU_VERSION', max_length=20)  # Field name made lowercase.
    ku_migr = models.IntegerField(db_column='KU_MIGR')  # Field name made lowercase.
    ku_templatetype = models.SmallIntegerField(db_column='KU_TEMPLATETYPE')  # Field name made lowercase.
    ku_comment = models.SmallIntegerField(db_column='KU_COMMENT')  # Field name made lowercase.
    ku_bigv = models.IntegerField(db_column='KU_BIGV')  # Field name made lowercase.
    ku_weibocomment = models.IntegerField(db_column='KU_WEIBOCOMMENT')  # Field name made lowercase.
    ku_issaveoverduedata = models.IntegerField(db_column='KU_ISSAVEOVERDUEDATA')  # Field name made lowercase.
    ku_changeversion = models.IntegerField(db_column='KU_CHANGEVERSION')  # Field name made lowercase.
    ku_kwsdaymaxdata = models.IntegerField(db_column='KU_KWSDAYMAXDATA')  # Field name made lowercase.
    ku_userdaymaxdata = models.IntegerField(db_column='KU_USERDAYMAXDATA')  # Field name made lowercase.
    ku_htrecollect = models.IntegerField(db_column='KU_HTRECOLLECT')  # Field name made lowercase.
    ku_ztrecollect = models.IntegerField(db_column='KU_ZTRECOLLECT')  # Field name made lowercase.
    ku_industry = models.SmallIntegerField(db_column='KU_INDUSTRY')  # Field name made lowercase.
    ku_specialspacing = models.IntegerField(db_column='KU_SPECIALSPACING')  # Field name made lowercase.
    ku_topicrefresh = models.IntegerField(db_column='KU_TOPICREFRESH')  # Field name made lowercase.
    ku_report_condition = models.TextField(db_column='KU_REPORT_CONDITION', blank=True, null=True)  # Field name made lowercase.
    ku_tvisopen = models.IntegerField(db_column='KU_TVISOPEN', blank=True, null=True)  # Field name made lowercase.
    ku_tvkeywsnum = models.IntegerField(db_column='KU_TVKEYWSNUM', blank=True, null=True)  # Field name made lowercase.
    ku_tvdownloadnum = models.IntegerField(db_column='KU_TVDOWNLOADNUM', blank=True, null=True)  # Field name made lowercase.
    ku_tvlastdownloadnum = models.IntegerField(db_column='KU_TVLASTDOWNLOADNUM')  # Field name made lowercase.
    ku_keywordnum = models.IntegerField(db_column='KU_KEYWORDNUM')  # Field name made lowercase.
    ku_xtzhengfu = models.IntegerField(db_column='KU_XTZHENGFU')  # Field name made lowercase.
    ku_user_local = models.TextField(db_column='KU_USER_LOCAL', blank=True, null=True)  # Field name made lowercase.
    ku_opensmallvideo = models.IntegerField(db_column='KU_OPENSMALLVIDEO')  # Field name made lowercase.
    ku_api_status = models.IntegerField(db_column='KU_API_STATUS')  # Field name made lowercase.
    ku_api_trysdate = models.DateField(db_column='KU_API_TRYSDATE', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    open_topic_overseas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_USERSERVICE'


class Crmaccountmapping(models.Model):
    msuid = models.IntegerField(db_column='msUid', primary_key=True)  # Field name made lowercase.
    msname = models.CharField(db_column='msName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city_id = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county_id = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    handlers = models.CharField(max_length=255, blank=True, null=True)
    usergenre = models.IntegerField(db_column='userGenre', blank=True, null=True)  # Field name made lowercase.
    userstatus = models.IntegerField(db_column='userStatus', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.CharField(db_column='updateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opportunitycount = models.CharField(db_column='opportunityCount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ordercount = models.CharField(db_column='orderCount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contractcount = models.CharField(db_column='contractCount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='regDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trysdate = models.CharField(db_column='trysDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastcontractdate = models.CharField(db_column='lastContractDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=255, blank=True, null=True)
    sale = models.CharField(max_length=100, blank=True, null=True)
    callback = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CRMACCOUNTMAPPING'

class UserGroupMap(models.Model):
    duid = models.CharField(max_length=255, blank=True, null=True)
    duname = models.CharField(max_length=255, blank=True, null=True)
    duposition = models.CharField(max_length=255, blank=True, null=True)
    dgid = models.CharField(max_length=255, blank=True, null=True)
    dgname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group_map'
        