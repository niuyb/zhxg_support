# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apachelog(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APACHELOG'


class Customertag(models.Model):
    crmuid = models.BigIntegerField(db_column='crmUid', unique=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_tag = models.CharField(max_length=255, blank=True, null=True)
    ms_tag = models.CharField(max_length=255, blank=True, null=True)
    opportunity_tag = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerTag'


class JavalogGetDj2Xq(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_state = models.CharField(db_column='KR_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_islocal = models.CharField(db_column='KR_ISLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg3 = models.CharField(db_column='ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isyj = models.IntegerField(db_column='ISYJ', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    ismyattention = models.IntegerField(db_column='ISMYATTENTION', blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.IntegerField(db_column='ISFEEDBACK', blank=True, null=True)  # Field name made lowercase.
    arg4 = models.CharField(db_column='ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg5 = models.CharField(db_column='ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_collecttime = models.CharField(db_column='KV_COLLECTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_hot = models.IntegerField(db_column='KV_HOT', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    isusermain = models.IntegerField(db_column='ISUSERMAIN', blank=True, null=True)  # Field name made lowercase.
    ismainsimhash = models.IntegerField(db_column='ISMAINSIMHASH', blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ispic = models.IntegerField(db_column='KV_ISPIC', blank=True, null=True)  # Field name made lowercase.
    kv_isvideo = models.IntegerField(db_column='KV_ISVIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_imgurl = models.CharField(db_column='KV_IMGURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_vedeourl = models.CharField(db_column='KV_VEDEOURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_stateonly = models.CharField(db_column='KR_STATEONLY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME', blank=True, null=True)  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME', blank=True, null=True)  # Field name made lowercase.
    hotsimhash = models.CharField(db_column='HOTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webchannel = models.CharField(db_column='KV_WEBCHANNEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_hotkeyword = models.CharField(db_column='KV_HOTKEYWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_informationstate = models.CharField(db_column='KV_INFORMATIONSTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kv_extend_field = models.TextField(db_column='KV_EXTEND_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kv_inputdatatype = models.IntegerField(db_column='KV_INPUTDATATYPE', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    ts_tag = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.IntegerField(blank=True, null=True)
    is_comment = models.CharField(max_length=255, blank=True, null=True)
    delete_time = models.CharField(max_length=255, blank=True, null=True)
    defender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_DJ2XQ'


class JavalogGetDjxq(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.IntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.IntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.IntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_templet = models.CharField(db_column='KV_TEMPLET', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_sna_flag = models.CharField(db_column='KV_SNA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_index_flag = models.CharField(db_column='KV_INDEX_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kv_insert_time = models.CharField(db_column='KV_INSERT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_qc_time = models.CharField(db_column='KV_QC_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dy_time = models.CharField(db_column='KV_DY_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_zf_time = models.CharField(db_column='KV_ZF_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dk_time = models.CharField(db_column='KV_DK_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_titlesimhash = models.CharField(db_column='KV_TITLESIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_titlekeywords = models.CharField(db_column='KV_TITLEKEYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_insideforwardstatus = models.IntegerField(db_column='KV_INSIDEFORWARDSTATUS', blank=True, null=True)  # Field name made lowercase.
    kv_insideforwardcount = models.IntegerField(db_column='KV_INSIDEFORWARDCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_contentsimhash = models.CharField(db_column='KV_CONTENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_contentkeywords = models.CharField(db_column='KV_CONTENTKEYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_titlerefhash = models.CharField(db_column='KV_TITLEREFHASH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    kv_procince = models.TextField(db_column='KV_PROCINCE', blank=True, null=True)  # Field name made lowercase.
    kv_cite = models.TextField(db_column='KV_CITE', blank=True, null=True)  # Field name made lowercase.
    kv_county = models.TextField(db_column='KV_COUNTY', blank=True, null=True)  # Field name made lowercase.
    kv_fansnum = models.IntegerField(db_column='KV_FANSNUM', blank=True, null=True)  # Field name made lowercase.
    kv_area = models.CharField(db_column='KV_AREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_messagenum = models.IntegerField(db_column='KV_MESSAGENUM', blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_isyj = models.CharField(db_column='KV_ISYJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_DJXQ'


class JavalogGetDodeletexx(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_state = models.CharField(db_column='KR_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_islocal = models.CharField(db_column='KR_ISLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg3 = models.CharField(db_column='ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isyj = models.IntegerField(db_column='ISYJ', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    ismyattention = models.IntegerField(db_column='ISMYATTENTION', blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.IntegerField(db_column='ISFEEDBACK', blank=True, null=True)  # Field name made lowercase.
    arg4 = models.CharField(db_column='ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg5 = models.CharField(db_column='ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_collecttime = models.CharField(db_column='KV_COLLECTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_hot = models.IntegerField(db_column='KV_HOT', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    isusermain = models.IntegerField(db_column='ISUSERMAIN', blank=True, null=True)  # Field name made lowercase.
    ismainsimhash = models.IntegerField(db_column='ISMAINSIMHASH', blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ispic = models.IntegerField(db_column='KV_ISPIC')  # Field name made lowercase.
    kv_isvideo = models.IntegerField(db_column='KV_ISVIDEO')  # Field name made lowercase.
    kv_imgurl = models.CharField(db_column='KV_IMGURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_vedeourl = models.CharField(db_column='KV_VEDEOURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_stateonly = models.CharField(db_column='KR_STATEONLY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=2)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX')  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX')  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=2)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=2)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=2)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=2)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=2)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    hotsimhash = models.CharField(db_column='HOTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webchannel = models.CharField(db_column='KV_WEBCHANNEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_hotkeyword = models.CharField(db_column='KV_HOTKEYWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_informationstate = models.CharField(db_column='KV_INFORMATIONSTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    duid = models.IntegerField(blank=True, null=True)
    deltime = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    kv_extend_field = models.TextField(db_column='KV_EXTEND_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kv_inputdatatype = models.CharField(db_column='KV_INPUTDATATYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kv_provinceid = models.CharField(db_column='KV_PROVINCEID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_DODELETEXX'


class JavalogGetJbxq(models.Model):
    km_uuid = models.CharField(db_column='KM_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ky_uuid = models.CharField(db_column='KY_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=600, blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.IntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.IntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.IntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_templet = models.CharField(db_column='KV_TEMPLET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_sna_flag = models.CharField(db_column='KV_SNA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_index_flag = models.CharField(db_column='KV_INDEX_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kv_insert_time = models.CharField(db_column='KV_INSERT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    closecj = models.CharField(db_column='CLOSECJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    luser = models.CharField(db_column='LUSER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_JBXQ'


class JavalogGetJzxx(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_state = models.CharField(db_column='KR_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_islocal = models.CharField(db_column='KR_ISLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg3 = models.CharField(db_column='ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isyj = models.IntegerField(db_column='ISYJ', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    ismyattention = models.IntegerField(db_column='ISMYATTENTION', blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.IntegerField(db_column='ISFEEDBACK', blank=True, null=True)  # Field name made lowercase.
    arg4 = models.CharField(db_column='ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg5 = models.CharField(db_column='ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_collecttime = models.CharField(db_column='KV_COLLECTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_hot = models.IntegerField(db_column='KV_HOT', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    isusermain = models.IntegerField(db_column='ISUSERMAIN', blank=True, null=True)  # Field name made lowercase.
    ismainsimhash = models.IntegerField(db_column='ISMAINSIMHASH', blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_ispic = models.IntegerField(db_column='KV_ISPIC')  # Field name made lowercase.
    kv_isvideo = models.IntegerField(db_column='KV_ISVIDEO')  # Field name made lowercase.
    kv_imgurl = models.CharField(db_column='KV_IMGURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_vedeourl = models.CharField(db_column='KV_VEDEOURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_stateonly = models.CharField(db_column='KR_STATEONLY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=2)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX')  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX')  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=2)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=2)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=2)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=2)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=2)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    hotsimhash = models.CharField(db_column='HOTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webchannel = models.CharField(db_column='KV_WEBCHANNEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_hotkeyword = models.CharField(db_column='KV_HOTKEYWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_informationstate = models.CharField(db_column='KV_INFORMATIONSTATE', max_length=30)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    luser = models.CharField(db_column='LUSER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    mongodata = models.TextField(blank=True, null=True)
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT')  # Field name made lowercase.
    kv_extend_field = models.TextField(db_column='KV_EXTEND_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kv_inputdatatype = models.IntegerField(db_column='KV_INPUTDATATYPE', blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_JZXX'


class JavalogGetMyattionxq(models.Model):
    km_uuid = models.CharField(db_column='KM_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=600, blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.IntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.IntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.IntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_templet = models.CharField(db_column='KV_TEMPLET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_sna_flag = models.CharField(db_column='KV_SNA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_index_flag = models.CharField(db_column='KV_INDEX_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kv_insert_time = models.CharField(db_column='KV_INSERT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    closecj = models.CharField(db_column='CLOSECJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    km_id = models.CharField(db_column='KM_ID', max_length=50)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=200)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    luser = models.CharField(db_column='LUSER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    topic_id = models.CharField(db_column='TOPIC_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kv_type = models.CharField(db_column='KV_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_MYATTIONXQ'


class JavalogGetNegativexq(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_state = models.CharField(db_column='KR_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_islocal = models.CharField(db_column='KR_ISLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg3 = models.CharField(db_column='ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isyj = models.IntegerField(db_column='ISYJ', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    ismyattention = models.IntegerField(db_column='ISMYATTENTION', blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.IntegerField(db_column='ISFEEDBACK', blank=True, null=True)  # Field name made lowercase.
    arg4 = models.CharField(db_column='ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg5 = models.CharField(db_column='ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_collecttime = models.CharField(db_column='KV_COLLECTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_hot = models.IntegerField(db_column='KV_HOT', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    isusermain = models.IntegerField(db_column='ISUSERMAIN', blank=True, null=True)  # Field name made lowercase.
    ismainsimhash = models.IntegerField(db_column='ISMAINSIMHASH', blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ispic = models.IntegerField(db_column='KV_ISPIC')  # Field name made lowercase.
    kv_isvideo = models.IntegerField(db_column='KV_ISVIDEO')  # Field name made lowercase.
    kv_imgurl = models.CharField(db_column='KV_IMGURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_vedeourl = models.CharField(db_column='KV_VEDEOURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_stateonly = models.CharField(db_column='KR_STATEONLY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=2)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=2)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=2)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=2)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=2)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=2)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    hotsimhash = models.CharField(db_column='HOTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webchannel = models.CharField(db_column='KV_WEBCHANNEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_hotkeyword = models.CharField(db_column='KV_HOTKEYWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_informationstate = models.CharField(db_column='KV_INFORMATIONSTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    luser = models.CharField(db_column='LUSER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT')  # Field name made lowercase.
    kv_extend_field = models.TextField(db_column='KV_EXTEND_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kv_inputdatatype = models.IntegerField(db_column='KV_INPUTDATATYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_NEGATIVEXQ'


class JavalogGetYjxq(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_info = models.CharField(db_column='KS_INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ks_state = models.CharField(db_column='KS_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_flag = models.CharField(db_column='KS_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_check = models.CharField(db_column='KS_CHECK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_checkdel = models.CharField(db_column='KS_CHECKDEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_late = models.CharField(db_column='KS_LATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_aoto = models.CharField(db_column='KS_AOTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_simhash = models.CharField(db_column='KS_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_title = models.CharField(db_column='KS_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ks_ctime = models.CharField(db_column='KS_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ks_sourcetype = models.CharField(db_column='kS_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_infotype = models.CharField(db_column='KS_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_kid = models.CharField(db_column='KS_KID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg5 = models.CharField(db_column='KV_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME', blank=True, null=True)  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME', blank=True, null=True)  # Field name made lowercase.
    luser = models.CharField(db_column='LUSER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    browsetype = models.IntegerField(db_column='BROWSETYPE', blank=True, null=True)  # Field name made lowercase.
    warning_level = models.CharField(max_length=255, blank=True, null=True)
    proposal = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    is_oversea = models.CharField(max_length=255, blank=True, null=True)
    main_part = models.CharField(max_length=255, blank=True, null=True)
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    module_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_YJXQ'


class JavalogGetZgxx(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_state = models.CharField(db_column='KR_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_islocal = models.CharField(db_column='KR_ISLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg3 = models.CharField(db_column='ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isyj = models.IntegerField(db_column='ISYJ', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    ismyattention = models.IntegerField(db_column='ISMYATTENTION', blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.IntegerField(db_column='ISFEEDBACK', blank=True, null=True)  # Field name made lowercase.
    arg4 = models.CharField(db_column='ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg5 = models.CharField(db_column='ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_collecttime = models.CharField(db_column='KV_COLLECTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_hot = models.IntegerField(db_column='KV_HOT', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    isusermain = models.IntegerField(db_column='ISUSERMAIN', blank=True, null=True)  # Field name made lowercase.
    ismainsimhash = models.IntegerField(db_column='ISMAINSIMHASH', blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_ispic = models.IntegerField(db_column='KV_ISPIC')  # Field name made lowercase.
    kv_isvideo = models.IntegerField(db_column='KV_ISVIDEO')  # Field name made lowercase.
    kv_imgurl = models.CharField(db_column='KV_IMGURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_vedeourl = models.CharField(db_column='KV_VEDEOURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_stateonly = models.CharField(db_column='KR_STATEONLY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=2)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX')  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX')  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=2)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=2)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=2)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=2)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=2)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    hotsimhash = models.CharField(db_column='HOTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webchannel = models.CharField(db_column='KV_WEBCHANNEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_hotkeyword = models.CharField(db_column='KV_HOTKEYWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_informationstate = models.CharField(db_column='KV_INFORMATIONSTATE', max_length=30)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    luser = models.CharField(db_column='LUSER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lip = models.CharField(db_column='LIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT')  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kv_extend_field = models.TextField(db_column='KV_EXTEND_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kv_inputdatatype = models.IntegerField(db_column='KV_INPUTDATATYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_GET_ZGXX'


class JavalogManualWarning(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=10)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_info = models.CharField(db_column='KS_INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ks_state = models.CharField(db_column='KS_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_flag = models.CharField(db_column='KS_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_check = models.CharField(db_column='KS_CHECK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_checkdel = models.CharField(db_column='KS_CHECKDEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_late = models.CharField(db_column='KS_LATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_aoto = models.CharField(db_column='KS_AOTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_simhash = models.CharField(db_column='KS_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_mustkeys = models.CharField(db_column='KS_MUSTKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_shouldkeys = models.CharField(db_column='KS_SHOULDKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_eventkeys = models.CharField(db_column='KS_EVENTKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_yjkid = models.CharField(db_column='KS_YJKID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_calinfo = models.CharField(db_column='KS_CALINFO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ks_usercommyjtype = models.CharField(db_column='KS_USERCOMMYJTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_userweiboyjtype = models.CharField(db_column='KS_USERWEIBOYJTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_calcommyj = models.CharField(db_column='KS_CALCOMMYJ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_calzhutiyj = models.CharField(db_column='KS_CALZHUTIYJ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_title = models.CharField(db_column='KS_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ks_ctime = models.CharField(db_column='KS_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ks_sourcetype = models.CharField(db_column='kS_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_infotype = models.CharField(db_column='KS_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_kid = models.CharField(db_column='KS_KID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    ks_userlocalbbstype = models.CharField(db_column='KS_USERLOCALBBSTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_kidallowourcetype = models.CharField(db_column='KS_KIDALLOWOURCETYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_uidallowourcetype = models.CharField(db_column='KS_UIDALLOWOURCETYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_shielddata = models.CharField(db_column='KS_SHIELDDATA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg5 = models.CharField(db_column='KV_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_MANUAL_WARNING'


class JavalogManWarning(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=10)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_info = models.CharField(db_column='KS_INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ks_state = models.CharField(db_column='KS_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_flag = models.CharField(db_column='KS_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_check = models.CharField(db_column='KS_CHECK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_checkdel = models.CharField(db_column='KS_CHECKDEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_late = models.CharField(db_column='KS_LATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_aoto = models.CharField(db_column='KS_AOTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_simhash = models.CharField(db_column='KS_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_mustkeys = models.CharField(db_column='KS_MUSTKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_shouldkeys = models.CharField(db_column='KS_SHOULDKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_eventkeys = models.CharField(db_column='KS_EVENTKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_yjkid = models.CharField(db_column='KS_YJKID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_calinfo = models.CharField(db_column='KS_CALINFO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ks_usercommyjtype = models.CharField(db_column='KS_USERCOMMYJTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_userweiboyjtype = models.CharField(db_column='KS_USERWEIBOYJTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_calcommyj = models.CharField(db_column='KS_CALCOMMYJ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_calzhutiyj = models.CharField(db_column='KS_CALZHUTIYJ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_title = models.CharField(db_column='KS_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ks_ctime = models.CharField(db_column='KS_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ks_sourcetype = models.CharField(db_column='kS_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_infotype = models.CharField(db_column='KS_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_kid = models.CharField(db_column='KS_KID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3)  # Field name made lowercase.
    ks_userlocalbbstype = models.CharField(db_column='KS_USERLOCALBBSTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_kidallowourcetype = models.CharField(db_column='KS_KIDALLOWOURCETYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_uidallowourcetype = models.CharField(db_column='KS_UIDALLOWOURCETYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_shielddata = models.CharField(db_column='KS_SHIELDDATA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg5 = models.CharField(db_column='KV_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=270, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    luser = models.CharField(max_length=255, blank=True, null=True)
    lip = models.CharField(max_length=255, blank=True, null=True)
    ltime = models.CharField(max_length=255, blank=True, null=True)
    warning_level = models.IntegerField(blank=True, null=True)
    proposal = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    is_oversea = models.IntegerField(blank=True, null=True)
    main_part = models.CharField(max_length=255, blank=True, null=True)
    isdelete = models.CharField(db_column='isDelete', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JAVALOG_MAN_WARNING'


class WarningCount(models.Model):
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_uuid = models.CharField(db_column='KS_UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_read = models.IntegerField(db_column='IS_READ', blank=True, null=True)  # Field name made lowercase.
    pc_readtime = models.CharField(db_column='PC_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aoto = models.CharField(db_column='AOTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pc_read = models.IntegerField(db_column='PC_READ', blank=True, null=True)  # Field name made lowercase.
    app_read = models.IntegerField(db_column='APP_READ', blank=True, null=True)  # Field name made lowercase.
    wechat_read = models.IntegerField(db_column='WECHAT_READ', blank=True, null=True)  # Field name made lowercase.
    app_readtime = models.CharField(db_column='APP_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_readtime = models.CharField(db_column='WECHAT_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WARNING_COUNT'


class WarningCount1721(models.Model):
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_uuid = models.CharField(db_column='KS_UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_read = models.IntegerField(db_column='IS_READ', blank=True, null=True)  # Field name made lowercase.
    pc_readtime = models.CharField(db_column='PC_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aoto = models.CharField(db_column='AOTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pc_read = models.IntegerField(db_column='PC_READ', blank=True, null=True)  # Field name made lowercase.
    app_read = models.IntegerField(db_column='APP_READ', blank=True, null=True)  # Field name made lowercase.
    wechat_read = models.IntegerField(db_column='WECHAT_READ', blank=True, null=True)  # Field name made lowercase.
    app_readtime = models.CharField(db_column='APP_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_readtime = models.CharField(db_column='WECHAT_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WARNING_COUNT_1721'


class WarningCount7812(models.Model):
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_uuid = models.CharField(db_column='KS_UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_read = models.IntegerField(db_column='IS_READ', blank=True, null=True)  # Field name made lowercase.
    pc_readtime = models.CharField(db_column='PC_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aoto = models.CharField(db_column='AOTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pc_read = models.IntegerField(db_column='PC_READ', blank=True, null=True)  # Field name made lowercase.
    app_read = models.IntegerField(db_column='APP_READ', blank=True, null=True)  # Field name made lowercase.
    wechat_read = models.IntegerField(db_column='WECHAT_READ', blank=True, null=True)  # Field name made lowercase.
    app_readtime = models.CharField(db_column='APP_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_readtime = models.CharField(db_column='WECHAT_READTIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attention = models.IntegerField(blank=True, null=True)
    copy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_COUNT_7812'


class WarningUrlCount(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    all_count = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    pc_read_count = models.IntegerField(blank=True, null=True)
    app_read_count = models.IntegerField(blank=True, null=True)
    wechat_read_count = models.IntegerField(blank=True, null=True)
    manwarning_count = models.IntegerField(blank=True, null=True)
    manwarning_read_count = models.IntegerField(blank=True, null=True)
    manwarning_read_pc_count = models.IntegerField(blank=True, null=True)
    manwarning_read_app_count = models.IntegerField(blank=True, null=True)
    manwarning_read_wechat_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_URL_COUNT'


class WarningUrlCountAlltypes(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    all_count = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    pc_read_count = models.IntegerField(blank=True, null=True)
    app_read_count = models.IntegerField(blank=True, null=True)
    wechat_read_count = models.IntegerField(blank=True, null=True)
    manwarning_count = models.IntegerField(blank=True, null=True)
    manwarning_read_count = models.IntegerField(blank=True, null=True)
    manwarning_read_pc_count = models.IntegerField(blank=True, null=True)
    manwarning_read_app_count = models.IntegerField(blank=True, null=True)
    manwarning_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto1_count = models.IntegerField(blank=True, null=True)
    aoto1_read_count = models.IntegerField(blank=True, null=True)
    aoto1_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto1_read_app_count = models.IntegerField(blank=True, null=True)
    aoto1_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto2_count = models.IntegerField(blank=True, null=True)
    aoto2_read_count = models.IntegerField(blank=True, null=True)
    aoto2_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto2_read_app_count = models.IntegerField(blank=True, null=True)
    aoto2_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto3_count = models.IntegerField(blank=True, null=True)
    aoto3_read_count = models.IntegerField(blank=True, null=True)
    aoto3_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto3_read_app_count = models.IntegerField(blank=True, null=True)
    aoto3_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto4_count = models.IntegerField(blank=True, null=True)
    aoto4_read_count = models.IntegerField(blank=True, null=True)
    aoto4_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto4_read_app_count = models.IntegerField(blank=True, null=True)
    aoto4_read_wechat_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_URL_COUNT_ALLTYPES'


class WarningUrlCountAlltypes1721(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    all_count = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    pc_read_count = models.IntegerField(blank=True, null=True)
    app_read_count = models.IntegerField(blank=True, null=True)
    wechat_read_count = models.IntegerField(blank=True, null=True)
    manwarning_count = models.IntegerField(blank=True, null=True)
    manwarning_read_count = models.IntegerField(blank=True, null=True)
    manwarning_read_pc_count = models.IntegerField(blank=True, null=True)
    manwarning_read_app_count = models.IntegerField(blank=True, null=True)
    manwarning_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto1_count = models.IntegerField(blank=True, null=True)
    aoto1_read_count = models.IntegerField(blank=True, null=True)
    aoto1_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto1_read_app_count = models.IntegerField(blank=True, null=True)
    aoto1_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto2_count = models.IntegerField(blank=True, null=True)
    aoto2_read_count = models.IntegerField(blank=True, null=True)
    aoto2_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto2_read_app_count = models.IntegerField(blank=True, null=True)
    aoto2_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto3_count = models.IntegerField(blank=True, null=True)
    aoto3_read_count = models.IntegerField(blank=True, null=True)
    aoto3_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto3_read_app_count = models.IntegerField(blank=True, null=True)
    aoto3_read_wechat_count = models.IntegerField(blank=True, null=True)
    aoto4_count = models.IntegerField(blank=True, null=True)
    aoto4_read_count = models.IntegerField(blank=True, null=True)
    aoto4_read_pc_count = models.IntegerField(blank=True, null=True)
    aoto4_read_app_count = models.IntegerField(blank=True, null=True)
    aoto4_read_wechat_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_URL_COUNT_ALLTYPES_1721'


class WarningUserCount(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.CharField(max_length=255, blank=True, null=True)
    trysdate = models.CharField(max_length=255, blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    warning_all_count = models.IntegerField(blank=True, null=True)
    read_all_count = models.IntegerField(blank=True, null=True)
    pc_read_all_count = models.IntegerField(blank=True, null=True)
    app_read_all_count = models.IntegerField(blank=True, null=True)
    wechat_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_all_count = models.IntegerField(blank=True, null=True)
    manwarning_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_pc_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_app_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_wechat_read_all_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_USER_COUNT'


class WarningUserCount1721(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.CharField(max_length=255, blank=True, null=True)
    trysdate = models.CharField(max_length=255, blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    warning_all_count = models.IntegerField(blank=True, null=True)
    read_all_count = models.IntegerField(blank=True, null=True)
    pc_read_all_count = models.IntegerField(blank=True, null=True)
    app_read_all_count = models.IntegerField(blank=True, null=True)
    wechat_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_all_count = models.IntegerField(blank=True, null=True)
    manwarning_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_pc_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_app_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_wechat_read_all_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_USER_COUNT_1721'


class WarningUserCount7812(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.CharField(max_length=255, blank=True, null=True)
    trysdate = models.CharField(max_length=255, blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    warning_all_count = models.IntegerField(blank=True, null=True)
    read_all_count = models.IntegerField(blank=True, null=True)
    pc_read_all_count = models.IntegerField(blank=True, null=True)
    app_read_all_count = models.IntegerField(blank=True, null=True)
    wechat_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_all_count = models.IntegerField(blank=True, null=True)
    manwarning_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_pc_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_app_read_all_count = models.IntegerField(blank=True, null=True)
    manwarning_wechat_read_all_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WARNING_USER_COUNT_7812'


class WkTCopylog(models.Model):
    uid = models.IntegerField()
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    ctime = models.CharField(max_length=255, blank=True, null=True)
    kv_uuid = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    negative = models.IntegerField(blank=True, null=True)
    webname = models.CharField(max_length=255, blank=True, null=True)
    importance_weight = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    sourcetype = models.CharField(max_length=255, blank=True, null=True)
    from_mod = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(db_column='UUID', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_COPYLOG'


class WkTExpertlog20190101(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190101'


class WkTExpertlog20190102(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190102'


class WkTExpertlog20190103(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190103'


class WkTExpertlog20190104(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190104'


class WkTExpertlog20190105(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190105'


class WkTExpertlog20190106(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190106'


class WkTExpertlog20190107(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190107'


class WkTExpertlog20190108(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190108'


class WkTExpertlog20190109(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190109'


class WkTExpertlog20190110(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190110'


class WkTExpertlog20190111(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190111'


class WkTExpertlog20190112(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190112'


class WkTExpertlog20190113(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190113'


class WkTExpertlog20190114(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190114'


class WkTExpertlog20190115(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190115'


class WkTExpertlog20190116(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190116'


class WkTExpertlog20190117(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190117'


class WkTExpertlog20190118(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190118'


class WkTExpertlog20190119(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190119'


class WkTExpertlog20190120(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190120'


class WkTExpertlog20190121(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190121'


class WkTExpertlog20190122(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190122'


class WkTExpertlog20190123(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190123'


class WkTExpertlog20190124(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190124'


class WkTExpertlog20190125(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190125'


class WkTExpertlog20190126(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190126'


class WkTExpertlog20190127(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190127'


class WkTExpertlog20190128(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190128'


class WkTExpertlog20190129(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190129'


class WkTExpertlog20190130(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190130'


class WkTExpertlog20190131(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190131'


class WkTExpertlog20190201(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190201'


class WkTExpertlog20190202(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190202'


class WkTExpertlog20190203(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190203'


class WkTExpertlog20190204(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190204'


class WkTExpertlog20190205(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190205'


class WkTExpertlog20190206(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190206'


class WkTExpertlog20190207(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190207'


class WkTExpertlog20190208(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190208'


class WkTExpertlog20190209(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190209'


class WkTExpertlog20190210(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190210'


class WkTExpertlog20190211(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190211'


class WkTExpertlog20190212(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190212'


class WkTExpertlog20190213(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190213'


class WkTExpertlog20190214(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190214'


class WkTExpertlog20190215(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190215'


class WkTExpertlog20190216(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190216'


class WkTExpertlog20190217(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190217'


class WkTExpertlog20190218(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190218'


class WkTExpertlog20190219(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190219'


class WkTExpertlog20190220(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190220'


class WkTExpertlog20190221(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190221'


class WkTExpertlog20190222(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190222'


class WkTExpertlog20190223(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190223'


class WkTExpertlog20190224(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190224'


class WkTExpertlog20190225(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190225'


class WkTExpertlog20190226(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190226'


class WkTExpertlog20190227(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190227'


class WkTExpertlog20190228(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190228'


class WkTExpertlog20190301(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190301'


class WkTExpertlog20190302(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190302'


class WkTExpertlog20190303(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190303'


class WkTExpertlog20190304(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190304'


class WkTExpertlog20190305(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190305'


class WkTExpertlog20190306(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190306'


class WkTExpertlog20190307(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190307'


class WkTExpertlog20190308(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190308'


class WkTExpertlog20190309(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190309'


class WkTExpertlog20190310(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190310'


class WkTExpertlog20190311(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190311'


class WkTExpertlog20190312(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190312'


class WkTExpertlog20190313(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190313'


class WkTExpertlog20190314(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190314'


class WkTExpertlog20190315(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190315'


class WkTExpertlog20190316(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190316'


class WkTExpertlog20190317(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190317'


class WkTExpertlog20190318(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190318'


class WkTExpertlog20190319(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190319'


class WkTExpertlog20190320(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190320'


class WkTExpertlog20190321(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190321'


class WkTExpertlog20190322(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190322'


class WkTExpertlog20190323(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190323'


class WkTExpertlog20190324(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190324'


class WkTExpertlog20190325(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190325'


class WkTExpertlog20190326(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190326'


class WkTExpertlog20190327(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190327'


class WkTExpertlog20190328(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190328'


class WkTExpertlog20190329(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190329'


class WkTExpertlog20190330(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190330'


class WkTExpertlog20190331(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190331'


class WkTExpertlog20190401(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190401'


class WkTExpertlog20190402(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190402'


class WkTExpertlog20190403(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190403'


class WkTExpertlog20190404(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190404'


class WkTExpertlog20190405(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190405'


class WkTExpertlog20190406(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190406'


class WkTExpertlog20190407(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190407'


class WkTExpertlog20190408(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190408'


class WkTExpertlog20190409(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190409'


class WkTExpertlog20190410(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190410'


class WkTExpertlog20190411(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190411'


class WkTExpertlog20190412(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190412'


class WkTExpertlog20190413(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190413'


class WkTExpertlog20190414(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190414'


class WkTExpertlog20190415(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190415'


class WkTExpertlog20190416(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190416'


class WkTExpertlog20190417(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190417'


class WkTExpertlog20190418(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190418'


class WkTExpertlog20190419(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190419'


class WkTExpertlog20190420(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190420'


class WkTExpertlog20190421(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190421'


class WkTExpertlog20190422(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190422'


class WkTExpertlog20190423(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190423'


class WkTExpertlog20190424(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190424'


class WkTExpertlog20190425(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190425'


class WkTExpertlog20190426(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190426'


class WkTExpertlog20190427(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190427'


class WkTExpertlog20190428(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190428'


class WkTExpertlog20190429(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190429'


class WkTExpertlog20190430(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190430'


class WkTExpertlog20190501(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190501'


class WkTExpertlog20190502(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190502'


class WkTExpertlog20190503(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190503'


class WkTExpertlog20190504(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190504'


class WkTExpertlog20190505(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190505'


class WkTExpertlog20190506(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190506'


class WkTExpertlog20190507(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190507'


class WkTExpertlog20190508(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190508'


class WkTExpertlog20190509(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190509'


class WkTExpertlog20190510(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190510'


class WkTExpertlog20190511(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190511'


class WkTExpertlog20190512(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190512'


class WkTExpertlog20190513(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190513'


class WkTExpertlog20190514(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190514'


class WkTExpertlog20190515(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190515'


class WkTExpertlog20190516(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190516'


class WkTExpertlog20190517(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190517'


class WkTExpertlog20190518(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190518'


class WkTExpertlog20190519(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190519'


class WkTExpertlog20190520(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190520'


class WkTExpertlog20190521(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190521'


class WkTExpertlog20190522(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190522'


class WkTExpertlog20190523(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190523'


class WkTExpertlog20190524(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190524'


class WkTExpertlog20190525(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190525'


class WkTExpertlog20190526(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190526'


class WkTExpertlog20190527(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190527'


class WkTExpertlog20190528(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190528'


class WkTExpertlog20190529(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190529'


class WkTExpertlog20190530(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190530'


class WkTExpertlog20190531(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190531'


class WkTExpertlog20190601(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190601'


class WkTExpertlog20190602(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190602'


class WkTExpertlog20190603(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190603'


class WkTExpertlog20190604(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190604'


class WkTExpertlog20190605(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190605'


class WkTExpertlog20190606(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190606'


class WkTExpertlog20190607(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190607'


class WkTExpertlog20190608(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190608'


class WkTExpertlog20190609(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190609'


class WkTExpertlog20190610(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190610'


class WkTExpertlog20190611(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190611'


class WkTExpertlog20190612(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190612'


class WkTExpertlog20190613(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190613'


class WkTExpertlog20190614(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190614'


class WkTExpertlog20190615(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190615'


class WkTExpertlog20190616(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190616'


class WkTExpertlog20190617(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190617'


class WkTExpertlog20190618(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190618'


class WkTExpertlog20190619(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190619'


class WkTExpertlog20190620(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190620'


class WkTExpertlog20190621(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190621'


class WkTExpertlog20190622(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190622'


class WkTExpertlog20190623(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190623'


class WkTExpertlog20190624(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190624'


class WkTExpertlog20190625(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190625'


class WkTExpertlog20190626(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190626'


class WkTExpertlog20190627(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190627'


class WkTExpertlog20190628(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190628'


class WkTExpertlog20190629(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190629'


class WkTExpertlog20190630(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190630'


class WkTExpertlog20190701(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190701'


class WkTExpertlog20190702(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190702'


class WkTExpertlog20190703(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190703'


class WkTExpertlog20190704(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190704'


class WkTExpertlog20190705(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190705'


class WkTExpertlog20190706(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190706'


class WkTExpertlog20190707(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190707'


class WkTExpertlog20190708(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190708'


class WkTExpertlog20190709(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190709'


class WkTExpertlog20190710(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190710'


class WkTExpertlog20190711(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190711'


class WkTExpertlog20190712(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190712'


class WkTExpertlog20190713(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190713'


class WkTExpertlog20190714(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190714'


class WkTExpertlog20190715(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190715'


class WkTExpertlog20190716(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190716'


class WkTExpertlog20190717(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190717'


class WkTExpertlog20190718(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190718'


class WkTExpertlog20190719(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190719'


class WkTExpertlog20190720(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190720'


class WkTExpertlog20190721(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190721'


class WkTExpertlog20190722(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190722'


class WkTExpertlog20190723(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190723'


class WkTExpertlog20190724(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190724'


class WkTExpertlog20190725(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190725'


class WkTExpertlog20190726(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190726'


class WkTExpertlog20190727(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190727'


class WkTExpertlog20190728(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190728'


class WkTExpertlog20190729(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190729'


class WkTExpertlog20190730(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190730'


class WkTExpertlog20190731(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190731'


class WkTExpertlog20190801(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190801'


class WkTExpertlog20190802(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190802'


class WkTExpertlog20190803(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190803'


class WkTExpertlog20190804(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190804'


class WkTExpertlog20190805(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190805'


class WkTExpertlog20190806(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190806'


class WkTExpertlog20190807(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190807'


class WkTExpertlog20190808(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190808'


class WkTExpertlog20190809(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190809'


class WkTExpertlog20190810(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190810'


class WkTExpertlog20190811(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190811'


class WkTExpertlog20190812(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190812'


class WkTExpertlog20190813(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190813'


class WkTExpertlog20190814(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190814'


class WkTExpertlog20190815(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190815'


class WkTExpertlog20190816(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190816'


class WkTExpertlog20190817(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190817'


class WkTExpertlog20190818(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190818'


class WkTExpertlog20190819(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190819'


class WkTExpertlog20190820(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190820'


class WkTExpertlog20190821(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190821'


class WkTExpertlog20190822(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190822'


class WkTExpertlog20190823(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190823'


class WkTExpertlog20190824(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190824'


class WkTExpertlog20190825(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190825'


class WkTExpertlog20190826(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190826'


class WkTExpertlog20190827(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190827'


class WkTExpertlog20190828(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190828'


class WkTExpertlog20190829(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190829'


class WkTExpertlog20190830(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190830'


class WkTExpertlog20190831(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190831'


class WkTExpertlog20190901(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190901'


class WkTExpertlog20190902(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190902'


class WkTExpertlog20190903(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190903'


class WkTExpertlog20190904(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190904'


class WkTExpertlog20190905(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190905'


class WkTExpertlog20190906(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190906'


class WkTExpertlog20190907(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190907'


class WkTExpertlog20190908(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190908'


class WkTExpertlog20190909(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190909'


class WkTExpertlog20190910(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190910'


class WkTExpertlog20190911(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190911'


class WkTExpertlog20190912(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190912'


class WkTExpertlog20190913(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190913'


class WkTExpertlog20190914(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190914'


class WkTExpertlog20190915(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190915'


class WkTExpertlog20190916(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190916'


class WkTExpertlog20190917(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190917'


class WkTExpertlog20190918(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190918'


class WkTExpertlog20190919(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190919'


class WkTExpertlog20190920(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190920'


class WkTExpertlog20190921(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190921'


class WkTExpertlog20190922(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190922'


class WkTExpertlog20190923(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190923'


class WkTExpertlog20190924(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190924'


class WkTExpertlog20190925(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190925'


class WkTExpertlog20190926(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190926'


class WkTExpertlog20190927(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190927'


class WkTExpertlog20190928(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190928'


class WkTExpertlog20190929(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190929'


class WkTExpertlog20190930(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20190930'


class WkTExpertlog20191001(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191001'


class WkTExpertlog20191002(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191002'


class WkTExpertlog20191003(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191003'


class WkTExpertlog20191004(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191004'


class WkTExpertlog20191005(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191005'


class WkTExpertlog20191006(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191006'


class WkTExpertlog20191007(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191007'


class WkTExpertlog20191008(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191008'


class WkTExpertlog20191009(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191009'


class WkTExpertlog20191010(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191010'


class WkTExpertlog20191011(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191011'


class WkTExpertlog20191012(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191012'


class WkTExpertlog20191013(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191013'


class WkTExpertlog20191014(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191014'


class WkTExpertlog20191015(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191015'


class WkTExpertlog20191016(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191016'


class WkTExpertlog20191017(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191017'


class WkTExpertlog20191018(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191018'


class WkTExpertlog20191019(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191019'


class WkTExpertlog20191020(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191020'


class WkTExpertlog20191021(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191021'


class WkTExpertlog20191022(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191022'


class WkTExpertlog20191023(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191023'


class WkTExpertlog20191024(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191024'


class WkTExpertlog20191025(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191025'


class WkTExpertlog20191026(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191026'


class WkTExpertlog20191027(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191027'


class WkTExpertlog20191028(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191028'


class WkTExpertlog20191029(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191029'


class WkTExpertlog20191030(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191030'


class WkTExpertlog20191031(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191031'


class WkTExpertlog20191101(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191101'


class WkTExpertlog20191102(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191102'


class WkTExpertlog20191103(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191103'


class WkTExpertlog20191104(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191104'


class WkTExpertlog20191105(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191105'


class WkTExpertlog20191106(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191106'


class WkTExpertlog20191107(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191107'


class WkTExpertlog20191108(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191108'


class WkTExpertlog20191109(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191109'


class WkTExpertlog20191110(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191110'


class WkTExpertlog20191111(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191111'


class WkTExpertlog20191112(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191112'


class WkTExpertlog20191113(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191113'


class WkTExpertlog20191114(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191114'


class WkTExpertlog20191115(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191115'


class WkTExpertlog20191116(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191116'


class WkTExpertlog20191117(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191117'


class WkTExpertlog20191118(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191118'


class WkTExpertlog20191119(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191119'


class WkTExpertlog20191120(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191120'


class WkTExpertlog20191121(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191121'


class WkTExpertlog20191122(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191122'


class WkTExpertlog20191123(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191123'


class WkTExpertlog20191124(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191124'


class WkTExpertlog20191125(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191125'


class WkTExpertlog20191126(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191126'


class WkTExpertlog20191127(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191127'


class WkTExpertlog20191128(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191128'


class WkTExpertlog20191129(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191129'


class WkTExpertlog20191130(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191130'


class WkTExpertlog20191201(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191201'


class WkTExpertlog20191202(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191202'


class WkTExpertlog20191203(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191203'


class WkTExpertlog20191204(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191204'


class WkTExpertlog20191205(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191205'


class WkTExpertlog20191206(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191206'


class WkTExpertlog20191207(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191207'


class WkTExpertlog20191208(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191208'


class WkTExpertlog20191209(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191209'


class WkTExpertlog20191210(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191210'


class WkTExpertlog20191211(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191211'


class WkTExpertlog20191212(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191212'


class WkTExpertlog20191213(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191213'


class WkTExpertlog20191214(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191214'


class WkTExpertlog20191215(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191215'


class WkTExpertlog20191216(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191216'


class WkTExpertlog20191217(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191217'


class WkTExpertlog20191218(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191218'


class WkTExpertlog20191219(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191219'


class WkTExpertlog20191220(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191220'


class WkTExpertlog20191221(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191221'


class WkTExpertlog20191222(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191222'


class WkTExpertlog20191223(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191223'


class WkTExpertlog20191224(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191224'


class WkTExpertlog20191225(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191225'


class WkTExpertlog20191226(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191226'


class WkTExpertlog20191227(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191227'


class WkTExpertlog20191228(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191228'


class WkTExpertlog20191229(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191229'


class WkTExpertlog20191230(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191230'


class WkTExpertlog20191231(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20191231'


class WkTExpertlog20200101(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200101'


class WkTExpertlog20200102(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200102'


class WkTExpertlog20200103(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200103'


class WkTExpertlog20200104(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200104'


class WkTExpertlog20200105(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200105'


class WkTExpertlog20200106(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200106'


class WkTExpertlog20200107(models.Model):
    customerid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'WK_T_EXPERTLOG_20200107'


class WkTJavalogcount(models.Model):
    # id = models.AutoField(unique=True)
    count_date = models.CharField(max_length=8)
    total_count = models.IntegerField()
    sale_count = models.IntegerField()
    user_count = models.IntegerField()
    formal_count = models.IntegerField()
    try_count = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOGCOUNT'


class WkTJavalog20190101(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190101'


class WkTJavalog20190102(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190102'


class WkTJavalog20190103(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190103'


class WkTJavalog20190104(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190104'


class WkTJavalog20190105(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190105'


class WkTJavalog20190106(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190106'


class WkTJavalog20190107(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190107'


class WkTJavalog20190108(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190108'


class WkTJavalog20190109(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190109'


class WkTJavalog20190110(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190110'


class WkTJavalog20190111(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190111'


class WkTJavalog20190112(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190112'


class WkTJavalog20190113(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190113'


class WkTJavalog20190114(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190114'


class WkTJavalog20190115(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190115'


class WkTJavalog20190116(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190116'


class WkTJavalog20190117(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190117'


class WkTJavalog20190118(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190118'


class WkTJavalog20190119(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190119'


class WkTJavalog20190120(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190120'


class WkTJavalog20190121(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190121'


class WkTJavalog20190122(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190122'


class WkTJavalog20190123(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190123'


class WkTJavalog20190124(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190124'


class WkTJavalog20190125(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190125'


class WkTJavalog20190126(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190126'


class WkTJavalog20190127(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190127'


class WkTJavalog20190128(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190128'


class WkTJavalog20190129(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190129'


class WkTJavalog20190130(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190130'


class WkTJavalog20190131(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190131'


class WkTJavalog20190201(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190201'


class WkTJavalog20190202(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190202'


class WkTJavalog20190203(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190203'


class WkTJavalog20190204(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190204'


class WkTJavalog20190205(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190205'


class WkTJavalog20190206(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190206'


class WkTJavalog20190207(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190207'


class WkTJavalog20190208(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190208'


class WkTJavalog20190209(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190209'


class WkTJavalog20190210(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190210'


class WkTJavalog20190211(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190211'


class WkTJavalog20190212(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190212'


class WkTJavalog20190213(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190213'


class WkTJavalog20190214(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190214'


class WkTJavalog20190215(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190215'


class WkTJavalog20190216(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190216'


class WkTJavalog20190217(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190217'


class WkTJavalog20190218(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190218'


class WkTJavalog20190219(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190219'


class WkTJavalog20190220(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190220'


class WkTJavalog20190221(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190221'


class WkTJavalog20190222(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190222'


class WkTJavalog20190223(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190223'


class WkTJavalog20190224(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190224'


class WkTJavalog20190225(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190225'


class WkTJavalog20190226(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190226'


class WkTJavalog20190227(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190227'


class WkTJavalog20190228(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190228'


class WkTJavalog20190301(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190301'


class WkTJavalog20190302(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190302'


class WkTJavalog20190303(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190303'


class WkTJavalog20190304(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190304'


class WkTJavalog20190305(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190305'


class WkTJavalog20190306(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190306'


class WkTJavalog20190307(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190307'


class WkTJavalog20190308(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190308'


class WkTJavalog20190309(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190309'


class WkTJavalog20190310(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190310'


class WkTJavalog20190311(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190311'


class WkTJavalog20190312(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190312'


class WkTJavalog20190313(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190313'


class WkTJavalog20190314(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190314'


class WkTJavalog20190315(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190315'


class WkTJavalog20190316(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190316'


class WkTJavalog20190317(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190317'


class WkTJavalog20190318(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190318'


class WkTJavalog20190319(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190319'


class WkTJavalog20190320(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190320'


class WkTJavalog20190321(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190321'


class WkTJavalog20190322(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190322'


class WkTJavalog20190323(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190323'


class WkTJavalog20190324(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190324'


class WkTJavalog20190325(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190325'


class WkTJavalog20190326(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190326'


class WkTJavalog20190327(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190327'


class WkTJavalog20190328(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190328'


class WkTJavalog20190329(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190329'


class WkTJavalog20190330(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190330'


class WkTJavalog20190331(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190331'


class WkTJavalog20190401(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190401'


class WkTJavalog20190402(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190402'


class WkTJavalog20190403(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190403'


class WkTJavalog20190404(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190404'


class WkTJavalog20190405(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190405'


class WkTJavalog20190406(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190406'


class WkTJavalog20190407(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190407'


class WkTJavalog20190408(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190408'


class WkTJavalog20190409(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190409'


class WkTJavalog20190410(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190410'


class WkTJavalog20190411(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190411'


class WkTJavalog20190412(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190412'


class WkTJavalog20190413(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190413'


class WkTJavalog20190414(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190414'


class WkTJavalog20190415(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190415'


class WkTJavalog20190416(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190416'


class WkTJavalog20190417(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190417'


class WkTJavalog20190418(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190418'


class WkTJavalog20190419(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190419'


class WkTJavalog20190420(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190420'


class WkTJavalog20190421(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190421'


class WkTJavalog20190422(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190422'


class WkTJavalog20190423(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190423'


class WkTJavalog20190424(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190424'


class WkTJavalog20190425(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190425'


class WkTJavalog20190426(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190426'


class WkTJavalog20190427(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190427'


class WkTJavalog20190428(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190428'


class WkTJavalog20190429(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190429'


class WkTJavalog20190430(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190430'


class WkTJavalog20190501(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190501'


class WkTJavalog20190502(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190502'


class WkTJavalog20190503(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190503'


class WkTJavalog20190504(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190504'


class WkTJavalog20190505(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190505'


class WkTJavalog20190506(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190506'


class WkTJavalog20190507(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190507'


class WkTJavalog20190508(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190508'


class WkTJavalog20190509(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190509'


class WkTJavalog20190510(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190510'


class WkTJavalog20190511(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190511'


class WkTJavalog20190512(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190512'


class WkTJavalog20190513(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190513'


class WkTJavalog20190514(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190514'


class WkTJavalog20190515(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190515'


class WkTJavalog20190516(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190516'


class WkTJavalog20190517(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190517'


class WkTJavalog20190518(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190518'


class WkTJavalog20190519(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190519'


class WkTJavalog20190520(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190520'


class WkTJavalog20190521(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190521'


class WkTJavalog20190522(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190522'


class WkTJavalog20190523(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190523'


class WkTJavalog20190524(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190524'


class WkTJavalog20190525(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190525'


class WkTJavalog20190526(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190526'


class WkTJavalog20190527(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190527'


class WkTJavalog20190528(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190528'


class WkTJavalog20190529(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190529'


class WkTJavalog20190530(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190530'


class WkTJavalog20190531(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190531'


class WkTJavalog20190601(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190601'


class WkTJavalog20190602(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190602'


class WkTJavalog20190603(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190603'


class WkTJavalog20190604(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190604'


class WkTJavalog20190605(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190605'


class WkTJavalog20190606(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190606'


class WkTJavalog20190607(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190607'


class WkTJavalog20190608(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190608'


class WkTJavalog20190609(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190609'


class WkTJavalog20190610(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190610'


class WkTJavalog20190611(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190611'


class WkTJavalog20190612(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190612'


class WkTJavalog20190613(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190613'


class WkTJavalog20190614(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190614'


class WkTJavalog20190615(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190615'


class WkTJavalog20190616(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190616'


class WkTJavalog20190617(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190617'


class WkTJavalog20190618(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190618'


class WkTJavalog20190619(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190619'


class WkTJavalog20190620(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190620'


class WkTJavalog20190621(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190621'


class WkTJavalog20190622(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190622'


class WkTJavalog20190623(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190623'


class WkTJavalog20190624(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190624'


class WkTJavalog20190625(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190625'


class WkTJavalog20190626(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190626'


class WkTJavalog20190627(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190627'


class WkTJavalog20190628(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190628'


class WkTJavalog20190629(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190629'


class WkTJavalog20190630(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190630'


class WkTJavalog20190701(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190701'


class WkTJavalog20190702(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190702'


class WkTJavalog20190703(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190703'


class WkTJavalog20190704(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190704'


class WkTJavalog20190705(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190705'


class WkTJavalog20190706(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190706'


class WkTJavalog20190707(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190707'


class WkTJavalog20190708(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190708'


class WkTJavalog20190709(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190709'


class WkTJavalog20190710(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190710'


class WkTJavalog20190711(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190711'


class WkTJavalog20190712(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190712'


class WkTJavalog20190713(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190713'


class WkTJavalog20190714(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190714'


class WkTJavalog20190715(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190715'


class WkTJavalog20190716(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190716'


class WkTJavalog20190717(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190717'


class WkTJavalog20190718(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190718'


class WkTJavalog20190719(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190719'


class WkTJavalog20190720(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190720'


class WkTJavalog20190721(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190721'


class WkTJavalog20190722(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190722'


class WkTJavalog20190723(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190723'


class WkTJavalog20190724(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190724'


class WkTJavalog20190725(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190725'


class WkTJavalog20190726(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190726'


class WkTJavalog20190727(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190727'


class WkTJavalog20190728(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190728'


class WkTJavalog20190729(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190729'


class WkTJavalog20190730(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190730'


class WkTJavalog20190731(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190731'


class WkTJavalog20190801(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190801'


class WkTJavalog20190802(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190802'


class WkTJavalog20190803(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190803'


class WkTJavalog20190804(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190804'


class WkTJavalog20190805(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190805'


class WkTJavalog20190806(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190806'


class WkTJavalog20190807(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190807'


class WkTJavalog20190808(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190808'


class WkTJavalog20190809(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190809'


class WkTJavalog20190810(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190810'


class WkTJavalog20190811(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190811'


class WkTJavalog20190812(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190812'


class WkTJavalog20190813(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190813'


class WkTJavalog20190814(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190814'


class WkTJavalog20190815(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190815'


class WkTJavalog20190816(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190816'


class WkTJavalog20190817(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190817'


class WkTJavalog20190818(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190818'


class WkTJavalog20190819(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190819'


class WkTJavalog20190820(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190820'


class WkTJavalog20190821(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190821'


class WkTJavalog20190822(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190822'


class WkTJavalog20190823(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190823'


class WkTJavalog20190824(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190824'


class WkTJavalog20190825(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190825'


class WkTJavalog20190826(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190826'


class WkTJavalog20190827(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190827'


class WkTJavalog20190828(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190828'


class WkTJavalog20190829(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190829'


class WkTJavalog20190830(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190830'


class WkTJavalog20190831(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190831'


class WkTJavalog20190901(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190901'


class WkTJavalog20190902(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190902'


class WkTJavalog20190903(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190903'


class WkTJavalog20190904(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190904'


class WkTJavalog20190905(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190905'


class WkTJavalog20190906(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190906'


class WkTJavalog20190907(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190907'


class WkTJavalog20190908(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190908'


class WkTJavalog20190909(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190909'


class WkTJavalog20190910(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190910'


class WkTJavalog20190911(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190911'


class WkTJavalog20190912(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190912'


class WkTJavalog20190913(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190913'


class WkTJavalog20190914(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190914'


class WkTJavalog20190915(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190915'


class WkTJavalog20190916(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190916'


class WkTJavalog20190917(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190917'


class WkTJavalog20190918(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190918'


class WkTJavalog20190919(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190919'


class WkTJavalog20190920(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190920'


class WkTJavalog20190921(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190921'


class WkTJavalog20190922(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190922'


class WkTJavalog20190923(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190923'


class WkTJavalog20190924(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190924'


class WkTJavalog20190925(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190925'


class WkTJavalog20190926(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190926'


class WkTJavalog20190927(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190927'


class WkTJavalog20190928(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190928'


class WkTJavalog20190929(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190929'


class WkTJavalog20190930(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20190930'


class WkTJavalog20191001(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191001'


class WkTJavalog20191002(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191002'


class WkTJavalog20191003(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191003'


class WkTJavalog20191004(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191004'


class WkTJavalog20191005(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191005'


class WkTJavalog20191006(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191006'


class WkTJavalog20191007(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191007'


class WkTJavalog20191008(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191008'


class WkTJavalog20191009(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191009'


class WkTJavalog20191010(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191010'


class WkTJavalog20191011(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191011'


class WkTJavalog20191012(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191012'


class WkTJavalog20191013(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191013'


class WkTJavalog20191014(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191014'


class WkTJavalog20191015(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191015'


class WkTJavalog20191016(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191016'


class WkTJavalog20191017(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191017'


class WkTJavalog20191018(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191018'


class WkTJavalog20191019(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191019'


class WkTJavalog20191020(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191020'


class WkTJavalog20191021(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191021'


class WkTJavalog20191022(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191022'


class WkTJavalog20191023(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191023'


class WkTJavalog20191024(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191024'


class WkTJavalog20191025(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191025'


class WkTJavalog20191026(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191026'


class WkTJavalog20191027(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191027'


class WkTJavalog20191028(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191028'


class WkTJavalog20191029(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191029'


class WkTJavalog20191030(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191030'


class WkTJavalog20191031(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191031'


class WkTJavalog20191101(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191101'


class WkTJavalog20191102(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191102'


class WkTJavalog20191103(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191103'


class WkTJavalog20191104(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191104'


class WkTJavalog20191105(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191105'


class WkTJavalog20191106(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191106'


class WkTJavalog20191107(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191107'


class WkTJavalog20191108(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191108'


class WkTJavalog20191109(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191109'


class WkTJavalog20191110(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191110'


class WkTJavalog20191111(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191111'


class WkTJavalog20191112(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191112'


class WkTJavalog20191113(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191113'


class WkTJavalog20191114(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191114'


class WkTJavalog20191115(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191115'


class WkTJavalog20191116(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191116'


class WkTJavalog20191117(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191117'


class WkTJavalog20191118(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191118'


class WkTJavalog20191119(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191119'


class WkTJavalog20191120(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191120'


class WkTJavalog20191121(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191121'


class WkTJavalog20191122(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191122'


class WkTJavalog20191123(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191123'


class WkTJavalog20191124(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191124'


class WkTJavalog20191125(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191125'


class WkTJavalog20191126(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191126'


class WkTJavalog20191127(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191127'


class WkTJavalog20191128(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191128'


class WkTJavalog20191129(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191129'


class WkTJavalog20191130(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191130'


class WkTJavalog20191201(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191201'


class WkTJavalog20191202(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191202'


class WkTJavalog20191203(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191203'


class WkTJavalog20191204(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191204'


class WkTJavalog20191205(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191205'


class WkTJavalog20191206(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191206'


class WkTJavalog20191207(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191207'


class WkTJavalog20191208(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191208'


class WkTJavalog20191209(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191209'


class WkTJavalog20191210(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191210'


class WkTJavalog20191211(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191211'


class WkTJavalog20191212(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191212'


class WkTJavalog20191213(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191213'


class WkTJavalog20191214(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191214'


class WkTJavalog20191215(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191215'


class WkTJavalog20191216(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191216'


class WkTJavalog20191217(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191217'


class WkTJavalog20191218(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191218'


class WkTJavalog20191219(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191219'


class WkTJavalog20191220(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191220'


class WkTJavalog20191221(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191221'


class WkTJavalog20191222(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191222'


class WkTJavalog20191223(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191223'


class WkTJavalog20191224(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191224'


class WkTJavalog20191225(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191225'


class WkTJavalog20191226(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191226'


class WkTJavalog20191227(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191227'


class WkTJavalog20191228(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191228'


class WkTJavalog20191229(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191229'


class WkTJavalog20191230(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191230'


class WkTJavalog20191231(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20191231'


class WkTJavalog20200101(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200101'


class WkTJavalog20200102(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200102'


class WkTJavalog20200103(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200103'


class WkTJavalog20200104(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200104'


class WkTJavalog20200105(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200105'


class WkTJavalog20200106(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200106'


class WkTJavalog20200107(models.Model):
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    wheres = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()
    infotype = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'WK_T_JAVALOG_20200107'


class WkTLocationuserBasicnumber(models.Model):
    province_id = models.IntegerField()
    province_name = models.CharField(max_length=255)
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    county_id = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    basic_num_police = models.IntegerField()
    level = models.IntegerField()
    basic_num_edu = models.IntegerField()
    basic_num_poster = models.IntegerField()
    basic_num_organization = models.IntegerField()
    basic_num_gov = models.IntegerField()
    basic_num_disciplinary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_LOCATIONUSER_BASICNUMBER'


class WkTLocationuserCoverage(models.Model):
    month = models.CharField(max_length=255)
    province_id = models.IntegerField()
    province_name = models.CharField(max_length=255)
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    county_id = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    basicnumber_police = models.IntegerField(blank=True, null=True)
    formal_user_police = models.CharField(max_length=255, blank=True, null=True)
    test_user_police = models.CharField(max_length=255, blank=True, null=True)
    basicnumber_poster = models.IntegerField(blank=True, null=True)
    formal_user_poster = models.CharField(max_length=255, blank=True, null=True)
    test_user_poster = models.CharField(max_length=255, blank=True, null=True)
    basicnumber_edu = models.IntegerField(blank=True, null=True)
    formal_user_edu = models.CharField(max_length=255, blank=True, null=True)
    test_user_edu = models.CharField(max_length=255, blank=True, null=True)
    all_user = models.CharField(max_length=255, blank=True, null=True)
    all_formal_user = models.CharField(max_length=255, blank=True, null=True)
    all_test_user = models.CharField(max_length=255, blank=True, null=True)
    basicnumber_organization = models.IntegerField(blank=True, null=True)
    formal_user_organization = models.CharField(max_length=255, blank=True, null=True)
    test_user_organization = models.CharField(max_length=255, blank=True, null=True)
    basicnumber_gov = models.IntegerField(blank=True, null=True)
    formal_user_gov = models.CharField(max_length=255, blank=True, null=True)
    test_user_gov = models.CharField(max_length=255, blank=True, null=True)
    basicnumber_disciplinary = models.IntegerField(blank=True, null=True)
    formal_user_disciplinary = models.CharField(max_length=255, blank=True, null=True)
    test_user_disciplinary = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_LOCATIONUSER_COVERAGE'


class WkTPlatformpushed(models.Model):
    kw_id = models.AutoField(db_column='KW_ID', primary_key=True)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=32)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=32)  # Field name made lowercase.
    kv_title = models.TextField(db_column='KV_TITLE')  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT')  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_kws = models.CharField(db_column='KV_KWS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.TextField(db_column='KV_URL', blank=True, null=True)  # Field name made lowercase.
    kv_ori = models.IntegerField(db_column='KV_ORI', blank=True, null=True)  # Field name made lowercase.
    kv_filter = models.IntegerField(db_column='KV_FILTER')  # Field name made lowercase.
    ding_id = models.CharField(db_column='DING_ID', max_length=100)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME', blank=True, null=True)  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME', blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    pushtime = models.CharField(db_column='PUSHTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tags = models.TextField(db_column='TAGS', blank=True, null=True)  # Field name made lowercase.
    info_status = models.IntegerField(db_column='INFO_STATUS', blank=True, null=True)  # Field name made lowercase.
    new_ori = models.IntegerField(db_column='NEW_ORI', blank=True, null=True)  # Field name made lowercase.
    later_ding_id = models.CharField(db_column='LATER_DING_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    later_pushtime = models.CharField(db_column='LATER_PUSHTIME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    wlevel = models.IntegerField(db_column='WLEVEL', blank=True, null=True)  # Field name made lowercase.
    is_ocr = models.IntegerField(db_column='IS_OCR', blank=True, null=True)  # Field name made lowercase.
    is_oversea = models.IntegerField(db_column='IS_OVERSEA', blank=True, null=True)  # Field name made lowercase.
    retweeted_status_url = models.CharField(db_column='RETWEETED_STATUS_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    is_comment = models.IntegerField(db_column='IS_COMMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PLATFORMPUSHED'


class WkTPlatformpushedOld(models.Model):
    kw_id = models.AutoField(db_column='KW_ID', primary_key=True)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=32)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=32)  # Field name made lowercase.
    kv_title = models.TextField(db_column='KV_TITLE')  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT')  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_kws = models.CharField(db_column='KV_KWS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.TextField(db_column='KV_URL', blank=True, null=True)  # Field name made lowercase.
    kv_ori = models.IntegerField(db_column='KV_ORI', blank=True, null=True)  # Field name made lowercase.
    kv_filter = models.IntegerField(db_column='KV_FILTER')  # Field name made lowercase.
    ding_id = models.CharField(db_column='DING_ID', max_length=100)  # Field name made lowercase.
    kr_infotype = models.CharField(db_column='KR_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_state = models.CharField(db_column='KR_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_islocal = models.CharField(db_column='KR_ISLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg3 = models.CharField(db_column='ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isyj = models.IntegerField(db_column='ISYJ', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    ismyattention = models.IntegerField(db_column='ISMYATTENTION', blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.IntegerField(db_column='ISFEEDBACK', blank=True, null=True)  # Field name made lowercase.
    arg4 = models.CharField(db_column='ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arg5 = models.CharField(db_column='ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_collecttime = models.CharField(db_column='KV_COLLECTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_hot = models.IntegerField(db_column='KV_HOT', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    isusermain = models.IntegerField(db_column='ISUSERMAIN', blank=True, null=True)  # Field name made lowercase.
    ismainsimhash = models.IntegerField(db_column='ISMAINSIMHASH', blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ispic = models.IntegerField(db_column='KV_ISPIC', blank=True, null=True)  # Field name made lowercase.
    kv_isvideo = models.IntegerField(db_column='KV_ISVIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_imgurl = models.CharField(db_column='KV_IMGURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_vedeourl = models.CharField(db_column='KV_VEDEOURL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_stateonly = models.CharField(db_column='KR_STATEONLY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME', blank=True, null=True)  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME', blank=True, null=True)  # Field name made lowercase.
    hotsimhash = models.CharField(db_column='HOTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webchannel = models.CharField(db_column='KV_WEBCHANNEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_hotkeyword = models.CharField(db_column='KV_HOTKEYWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    pushtime = models.CharField(db_column='PUSHTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tags = models.TextField(db_column='TAGS', blank=True, null=True)  # Field name made lowercase.
    info_status = models.IntegerField(db_column='INFO_STATUS', blank=True, null=True)  # Field name made lowercase.
    new_ori = models.IntegerField(db_column='NEW_ORI', blank=True, null=True)  # Field name made lowercase.
    later_ding_id = models.CharField(db_column='LATER_DING_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    later_pushtime = models.CharField(db_column='LATER_PUSHTIME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    wlevel = models.IntegerField(db_column='WLEVEL', blank=True, null=True)  # Field name made lowercase.
    is_ocr = models.IntegerField(db_column='IS_OCR', blank=True, null=True)  # Field name made lowercase.
    is_oversea = models.IntegerField(db_column='IS_OVERSEA', blank=True, null=True)  # Field name made lowercase.
    retweeted_status_url = models.CharField(db_column='RETWEETED_STATUS_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PLATFORMPUSHED_old'


class WkTPlatformuser(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=32)  # Field name made lowercase.
    uniqueid = models.IntegerField(db_column='UNIQUEID', blank=True, null=True)  # Field name made lowercase.
    staff = models.CharField(db_column='STAFF', max_length=32, blank=True, null=True)  # Field name made lowercase.
    failed = models.IntegerField(db_column='FAILED', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PLATFORMUSER'


class WkTPlatformuserOld(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=32)  # Field name made lowercase.
    uniqueid = models.IntegerField(db_column='UNIQUEID', blank=True, null=True)  # Field name made lowercase.
    staff = models.CharField(db_column='STAFF', max_length=32, blank=True, null=True)  # Field name made lowercase.
    failed = models.IntegerField(db_column='FAILED', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PLATFORMUSER_old'


class WkTUseraction(models.Model):
    uid = models.IntegerField()
    action_count = models.IntegerField()
    action_date = models.IntegerField()
    saler = models.CharField(max_length=255)
    uname = models.CharField(max_length=255, blank=True, null=True)
    saler_frame = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_USERACTION'


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


class WkTUseractivity2018(models.Model):
    uid = models.IntegerField()
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
        db_table = 'WK_T_USERACTIVITY_2018'


class WkTUseractivity2020(models.Model):
    uid = models.IntegerField()
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
        db_table = 'WK_T_USERACTIVITY_2020'


class WkTUserOperationModuleCount(models.Model):
    uid = models.IntegerField()
    source = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    params = models.CharField(max_length=255, blank=True, null=True)
    action_time = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_USER_OPERATION_MODULE_COUNT'


class WkTUserSalerMap(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=255)
    status = models.IntegerField()
    genre = models.IntegerField()
    regdate = models.CharField(max_length=255)
    trysdate = models.CharField(max_length=255)
    saler = models.CharField(max_length=255)
    saler_frame = models.CharField(max_length=255, blank=True, null=True)
    saler_frame_id = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    county = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=100, blank=True, null=True)
    location_level = models.IntegerField(blank=True, null=True)
    industry = models.IntegerField(blank=True, null=True)
    maint = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_USER_SALER_MAP'


class WkTWebuserlog(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG'


class WkTWebuserlog20171229(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20171229'


class WkTWebuserlog20180131(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180131'


class WkTWebuserlog20180228(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180228'


class WkTWebuserlog20180330(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180330'


class WkTWebuserlog20180430(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180430'


class WkTWebuserlog20180531(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180531'


class WkTWebuserlog20180629(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180629'


class WkTWebuserlog20180731(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180731'


class WkTWebuserlog20180831(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180831'


class WkTWebuserlog20180928(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20180928'


class WkTWebuserlog20181031(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20181031'


class WkTWebuserlog20181130(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20181130'


class WkTWebuserlog20181231(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20181231'


class WkTWebuserlog20190101(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190101'


class WkTWebuserlog20190102(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190102'


class WkTWebuserlog20190103(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190103'


class WkTWebuserlog20190104(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190104'


class WkTWebuserlog20190105(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190105'


class WkTWebuserlog20190106(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190106'


class WkTWebuserlog20190107(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190107'


class WkTWebuserlog20190108(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190108'


class WkTWebuserlog20190109(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190109'


class WkTWebuserlog20190110(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190110'


class WkTWebuserlog20190111(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190111'


class WkTWebuserlog20190112(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190112'


class WkTWebuserlog20190113(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190113'


class WkTWebuserlog20190114(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190114'


class WkTWebuserlog20190115(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190115'


class WkTWebuserlog20190116(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190116'


class WkTWebuserlog20190117(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190117'


class WkTWebuserlog20190118(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190118'


class WkTWebuserlog20190119(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190119'


class WkTWebuserlog20190120(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190120'


class WkTWebuserlog20190121(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190121'


class WkTWebuserlog20190122(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190122'


class WkTWebuserlog20190123(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190123'


class WkTWebuserlog20190124(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190124'


class WkTWebuserlog20190125(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190125'


class WkTWebuserlog20190126(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190126'


class WkTWebuserlog20190127(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190127'


class WkTWebuserlog20190128(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190128'


class WkTWebuserlog20190129(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190129'


class WkTWebuserlog20190130(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190130'


class WkTWebuserlog20190131(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190131'


class WkTWebuserlog20190201(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190201'


class WkTWebuserlog20190202(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190202'


class WkTWebuserlog20190203(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190203'


class WkTWebuserlog20190204(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190204'


class WkTWebuserlog20190205(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190205'


class WkTWebuserlog20190206(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190206'


class WkTWebuserlog20190207(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190207'


class WkTWebuserlog20190208(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190208'


class WkTWebuserlog20190209(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190209'


class WkTWebuserlog20190210(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190210'


class WkTWebuserlog20190211(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190211'


class WkTWebuserlog20190212(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190212'


class WkTWebuserlog20190213(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190213'


class WkTWebuserlog20190214(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190214'


class WkTWebuserlog20190215(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190215'


class WkTWebuserlog20190216(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190216'


class WkTWebuserlog20190217(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190217'


class WkTWebuserlog20190218(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190218'


class WkTWebuserlog20190219(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190219'


class WkTWebuserlog20190220(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190220'


class WkTWebuserlog20190221(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190221'


class WkTWebuserlog20190222(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190222'


class WkTWebuserlog20190223(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190223'


class WkTWebuserlog20190224(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190224'


class WkTWebuserlog20190225(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190225'


class WkTWebuserlog20190226(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190226'


class WkTWebuserlog20190227(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190227'


class WkTWebuserlog20190228(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190228'


class WkTWebuserlog20190301(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190301'


class WkTWebuserlog20190302(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190302'


class WkTWebuserlog20190303(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190303'


class WkTWebuserlog20190304(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190304'


class WkTWebuserlog20190305(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190305'


class WkTWebuserlog20190306(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190306'


class WkTWebuserlog20190307(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190307'


class WkTWebuserlog20190308(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190308'


class WkTWebuserlog20190309(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190309'


class WkTWebuserlog20190310(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190310'


class WkTWebuserlog20190311(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190311'


class WkTWebuserlog20190312(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190312'


class WkTWebuserlog20190313(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190313'


class WkTWebuserlog20190314(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190314'


class WkTWebuserlog20190315(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190315'


class WkTWebuserlog20190316(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190316'


class WkTWebuserlog20190317(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190317'


class WkTWebuserlog20190318(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190318'


class WkTWebuserlog20190319(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190319'


class WkTWebuserlog20190320(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190320'


class WkTWebuserlog20190321(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190321'


class WkTWebuserlog20190322(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190322'


class WkTWebuserlog20190323(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190323'


class WkTWebuserlog20190324(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190324'


class WkTWebuserlog20190325(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190325'


class WkTWebuserlog20190326(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190326'


class WkTWebuserlog20190327(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190327'


class WkTWebuserlog20190328(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190328'


class WkTWebuserlog20190329(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190329'


class WkTWebuserlog20190330(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190330'


class WkTWebuserlog20190331(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190331'


class WkTWebuserlog20190401(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190401'


class WkTWebuserlog20190402(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190402'


class WkTWebuserlog20190403(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190403'


class WkTWebuserlog20190404(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190404'


class WkTWebuserlog20190405(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190405'


class WkTWebuserlog20190406(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190406'


class WkTWebuserlog20190407(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190407'


class WkTWebuserlog20190408(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190408'


class WkTWebuserlog20190409(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190409'


class WkTWebuserlog20190410(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190410'


class WkTWebuserlog20190411(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190411'


class WkTWebuserlog20190412(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190412'


class WkTWebuserlog20190413(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190413'


class WkTWebuserlog20190414(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190414'


class WkTWebuserlog20190415(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190415'


class WkTWebuserlog20190416(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190416'


class WkTWebuserlog20190417(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190417'


class WkTWebuserlog20190418(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190418'


class WkTWebuserlog20190419(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190419'


class WkTWebuserlog20190420(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190420'


class WkTWebuserlog20190421(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190421'


class WkTWebuserlog20190422(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190422'


class WkTWebuserlog20190423(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190423'


class WkTWebuserlog20190424(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190424'


class WkTWebuserlog20190425(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190425'


class WkTWebuserlog20190426(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190426'


class WkTWebuserlog20190427(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190427'


class WkTWebuserlog20190428(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190428'


class WkTWebuserlog20190429(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190429'


class WkTWebuserlog20190430(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190430'


class WkTWebuserlog20190501(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190501'


class WkTWebuserlog20190502(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190502'


class WkTWebuserlog20190503(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190503'


class WkTWebuserlog20190504(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190504'


class WkTWebuserlog20190505(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190505'


class WkTWebuserlog20190506(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190506'


class WkTWebuserlog20190507(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190507'


class WkTWebuserlog20190508(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190508'


class WkTWebuserlog20190509(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190509'


class WkTWebuserlog20190510(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190510'


class WkTWebuserlog20190511(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190511'


class WkTWebuserlog20190512(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190512'


class WkTWebuserlog20190513(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190513'


class WkTWebuserlog20190514(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190514'


class WkTWebuserlog20190515(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190515'


class WkTWebuserlog20190516(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190516'


class WkTWebuserlog20190517(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190517'


class WkTWebuserlog20190518(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190518'


class WkTWebuserlog20190519(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190519'


class WkTWebuserlog20190520(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190520'


class WkTWebuserlog20190521(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190521'


class WkTWebuserlog20190522(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190522'


class WkTWebuserlog20190523(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190523'


class WkTWebuserlog20190524(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190524'


class WkTWebuserlog20190525(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190525'


class WkTWebuserlog20190526(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190526'


class WkTWebuserlog20190527(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190527'


class WkTWebuserlog20190528(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190528'


class WkTWebuserlog20190529(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190529'


class WkTWebuserlog20190530(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190530'


class WkTWebuserlog20190531(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190531'


class WkTWebuserlog20190601(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190601'


class WkTWebuserlog20190602(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190602'


class WkTWebuserlog20190603(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190603'


class WkTWebuserlog20190604(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190604'


class WkTWebuserlog20190605(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190605'


class WkTWebuserlog20190606(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190606'


class WkTWebuserlog20190607(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190607'


class WkTWebuserlog20190608(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190608'


class WkTWebuserlog20190609(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190609'


class WkTWebuserlog20190610(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190610'


class WkTWebuserlog20190611(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190611'


class WkTWebuserlog20190612(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190612'


class WkTWebuserlog20190613(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190613'


class WkTWebuserlog20190614(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190614'


class WkTWebuserlog20190615(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190615'


class WkTWebuserlog20190616(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190616'


class WkTWebuserlog20190617(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190617'


class WkTWebuserlog20190618(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190618'


class WkTWebuserlog20190619(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190619'


class WkTWebuserlog20190620(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190620'


class WkTWebuserlog20190621(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190621'


class WkTWebuserlog20190622(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190622'


class WkTWebuserlog20190623(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190623'


class WkTWebuserlog20190624(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190624'


class WkTWebuserlog20190625(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190625'


class WkTWebuserlog20190626(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190626'


class WkTWebuserlog20190627(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190627'


class WkTWebuserlog20190628(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190628'


class WkTWebuserlog20190629(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190629'


class WkTWebuserlog20190630(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190630'


class WkTWebuserlog20190701(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190701'


class WkTWebuserlog20190702(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190702'


class WkTWebuserlog20190703(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190703'


class WkTWebuserlog20190704(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190704'


class WkTWebuserlog20190705(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190705'


class WkTWebuserlog20190706(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190706'


class WkTWebuserlog20190707(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190707'


class WkTWebuserlog20190708(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190708'


class WkTWebuserlog20190709(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190709'


class WkTWebuserlog20190710(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190710'


class WkTWebuserlog20190711(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190711'


class WkTWebuserlog20190712(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190712'


class WkTWebuserlog20190713(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190713'


class WkTWebuserlog20190714(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190714'


class WkTWebuserlog20190715(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190715'


class WkTWebuserlog20190716(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190716'


class WkTWebuserlog20190717(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190717'


class WkTWebuserlog20190718(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190718'


class WkTWebuserlog20190719(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190719'


class WkTWebuserlog20190720(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190720'


class WkTWebuserlog20190721(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190721'


class WkTWebuserlog20190722(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190722'


class WkTWebuserlog20190723(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190723'


class WkTWebuserlog20190724(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190724'


class WkTWebuserlog20190725(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190725'


class WkTWebuserlog20190726(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190726'


class WkTWebuserlog20190727(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190727'


class WkTWebuserlog20190728(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190728'


class WkTWebuserlog20190729(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190729'


class WkTWebuserlog20190730(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190730'


class WkTWebuserlog20190731(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190731'


class WkTWebuserlog20190801(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190801'


class WkTWebuserlog20190802(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190802'


class WkTWebuserlog20190803(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190803'


class WkTWebuserlog20190804(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190804'


class WkTWebuserlog20190805(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190805'


class WkTWebuserlog20190806(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190806'


class WkTWebuserlog20190807(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190807'


class WkTWebuserlog20190808(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190808'


class WkTWebuserlog20190809(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190809'


class WkTWebuserlog20190810(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190810'


class WkTWebuserlog20190811(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190811'


class WkTWebuserlog20190812(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190812'


class WkTWebuserlog20190813(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190813'


class WkTWebuserlog20190814(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190814'


class WkTWebuserlog20190815(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190815'


class WkTWebuserlog20190816(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190816'


class WkTWebuserlog20190817(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190817'


class WkTWebuserlog20190818(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190818'


class WkTWebuserlog20190819(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190819'


class WkTWebuserlog20190820(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190820'


class WkTWebuserlog20190821(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190821'


class WkTWebuserlog20190822(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190822'


class WkTWebuserlog20190823(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190823'


class WkTWebuserlog20190824(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190824'


class WkTWebuserlog20190825(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190825'


class WkTWebuserlog20190826(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190826'


class WkTWebuserlog20190827(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190827'


class WkTWebuserlog20190828(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190828'


class WkTWebuserlog20190829(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190829'


class WkTWebuserlog20190830(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190830'


class WkTWebuserlog20190831(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190831'


class WkTWebuserlog20190901(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190901'


class WkTWebuserlog20190902(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190902'


class WkTWebuserlog20190903(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190903'


class WkTWebuserlog20190904(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190904'


class WkTWebuserlog20190905(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190905'


class WkTWebuserlog20190906(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190906'


class WkTWebuserlog20190907(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190907'


class WkTWebuserlog20190908(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190908'


class WkTWebuserlog20190909(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190909'


class WkTWebuserlog20190910(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190910'


class WkTWebuserlog20190911(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190911'


class WkTWebuserlog20190912(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190912'


class WkTWebuserlog20190913(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190913'


class WkTWebuserlog20190914(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190914'


class WkTWebuserlog20190915(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190915'


class WkTWebuserlog20190916(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190916'


class WkTWebuserlog20190917(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190917'


class WkTWebuserlog20190918(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190918'


class WkTWebuserlog20190919(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190919'


class WkTWebuserlog20190920(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190920'


class WkTWebuserlog20190921(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190921'


class WkTWebuserlog20190922(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190922'


class WkTWebuserlog20190923(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190923'


class WkTWebuserlog20190924(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190924'


class WkTWebuserlog20190925(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190925'


class WkTWebuserlog20190926(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190926'


class WkTWebuserlog20190927(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190927'


class WkTWebuserlog20190928(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190928'


class WkTWebuserlog20190929(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190929'


class WkTWebuserlog20190930(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20190930'


class WkTWebuserlog20191001(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191001'


class WkTWebuserlog20191002(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191002'


class WkTWebuserlog20191003(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191003'


class WkTWebuserlog20191004(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191004'


class WkTWebuserlog20191005(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191005'


class WkTWebuserlog20191006(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191006'


class WkTWebuserlog20191007(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191007'


class WkTWebuserlog20191008(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191008'


class WkTWebuserlog20191009(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191009'


class WkTWebuserlog20191010(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191010'


class WkTWebuserlog20191011(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191011'


class WkTWebuserlog20191012(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191012'


class WkTWebuserlog20191013(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191013'


class WkTWebuserlog20191014(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191014'


class WkTWebuserlog20191015(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191015'


class WkTWebuserlog20191016(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191016'


class WkTWebuserlog20191017(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191017'


class WkTWebuserlog20191018(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191018'


class WkTWebuserlog20191019(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191019'


class WkTWebuserlog20191020(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191020'


class WkTWebuserlog20191021(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191021'


class WkTWebuserlog20191022(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191022'


class WkTWebuserlog20191023(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191023'


class WkTWebuserlog20191024(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191024'


class WkTWebuserlog20191025(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191025'


class WkTWebuserlog20191026(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191026'


class WkTWebuserlog20191027(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191027'


class WkTWebuserlog20191028(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191028'


class WkTWebuserlog20191029(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191029'


class WkTWebuserlog20191030(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191030'


class WkTWebuserlog20191031(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191031'


class WkTWebuserlog20191101(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191101'


class WkTWebuserlog20191102(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191102'


class WkTWebuserlog20191103(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191103'


class WkTWebuserlog20191104(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191104'


class WkTWebuserlog20191105(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191105'


class WkTWebuserlog20191106(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191106'


class WkTWebuserlog20191107(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191107'


class WkTWebuserlog20191108(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191108'


class WkTWebuserlog20191109(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191109'


class WkTWebuserlog20191110(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191110'


class WkTWebuserlog20191111(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191111'


class WkTWebuserlog20191112(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191112'


class WkTWebuserlog20191113(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191113'


class WkTWebuserlog20191114(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191114'


class WkTWebuserlog20191115(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191115'


class WkTWebuserlog20191116(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191116'


class WkTWebuserlog20191117(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191117'


class WkTWebuserlog20191118(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191118'


class WkTWebuserlog20191119(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191119'


class WkTWebuserlog20191120(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191120'


class WkTWebuserlog20191121(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191121'


class WkTWebuserlog20191122(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191122'


class WkTWebuserlog20191123(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191123'


class WkTWebuserlog20191124(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191124'


class WkTWebuserlog20191125(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191125'


class WkTWebuserlog20191126(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191126'


class WkTWebuserlog20191127(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191127'


class WkTWebuserlog20191128(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191128'


class WkTWebuserlog20191129(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191129'


class WkTWebuserlog20191130(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191130'


class WkTWebuserlog20191201(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191201'


class WkTWebuserlog20191202(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191202'


class WkTWebuserlog20191203(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191203'


class WkTWebuserlog20191204(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191204'


class WkTWebuserlog20191205(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191205'


class WkTWebuserlog20191206(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191206'


class WkTWebuserlog20191207(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191207'


class WkTWebuserlog20191208(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191208'


class WkTWebuserlog20191209(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191209'


class WkTWebuserlog20191210(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191210'


class WkTWebuserlog20191211(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191211'


class WkTWebuserlog20191212(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191212'


class WkTWebuserlog20191213(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191213'


class WkTWebuserlog20191214(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191214'


class WkTWebuserlog20191215(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191215'


class WkTWebuserlog20191216(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191216'


class WkTWebuserlog20191217(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191217'


class WkTWebuserlog20191218(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191218'


class WkTWebuserlog20191219(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191219'


class WkTWebuserlog20191220(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191220'


class WkTWebuserlog20191221(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191221'


class WkTWebuserlog20191222(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191222'


class WkTWebuserlog20191223(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191223'


class WkTWebuserlog20191224(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191224'


class WkTWebuserlog20191225(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191225'


class WkTWebuserlog20191226(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191226'


class WkTWebuserlog20191227(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191227'


class WkTWebuserlog20191228(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191228'


class WkTWebuserlog20191229(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191229'


class WkTWebuserlog20191230(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191230'


class WkTWebuserlog20191231(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20191231'


class WkTWebuserlog20200101(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200101'


class WkTWebuserlog20200102(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200102'


class WkTWebuserlog20200103(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200103'


class WkTWebuserlog20200104(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200104'


class WkTWebuserlog20200105(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200105'


class WkTWebuserlog20200106(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200106'


class WkTWebuserlog20200107(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERLOG_20200107'


class YjPhonePush(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=10)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_info = models.CharField(db_column='KS_INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ks_state = models.CharField(db_column='KS_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_flag = models.CharField(db_column='KS_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_check = models.CharField(db_column='KS_CHECK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_checkdel = models.CharField(db_column='KS_CHECKDEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_late = models.CharField(db_column='KS_LATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_aoto = models.CharField(db_column='KS_AOTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_simhash = models.CharField(db_column='KS_SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_mustkeys = models.CharField(db_column='KS_MUSTKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_shouldkeys = models.CharField(db_column='KS_SHOULDKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_eventkeys = models.CharField(db_column='KS_EVENTKEYS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_yjkid = models.CharField(db_column='KS_YJKID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_calinfo = models.CharField(db_column='KS_CALINFO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ks_usercommyjtype = models.CharField(db_column='KS_USERCOMMYJTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_userweiboyjtype = models.CharField(db_column='KS_USERWEIBOYJTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_calcommyj = models.CharField(db_column='KS_CALCOMMYJ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_calzhutiyj = models.CharField(db_column='KS_CALZHUTIYJ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_title = models.CharField(db_column='KS_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ks_ctime = models.CharField(db_column='KS_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ks_sourcetype = models.CharField(db_column='kS_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_infotype = models.CharField(db_column='KS_INFOTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_kid = models.CharField(db_column='KS_KID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3)  # Field name made lowercase.
    ks_userlocalbbstype = models.CharField(db_column='KS_USERLOCALBBSTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ks_kidallowourcetype = models.CharField(db_column='KS_KIDALLOWOURCETYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_uidallowourcetype = models.CharField(db_column='KS_UIDALLOWOURCETYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_shielddata = models.CharField(db_column='KS_SHIELDDATA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='ISREAD', blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg5 = models.CharField(db_column='KV_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    kv_dttime = models.DateTimeField(db_column='KV_DTTIME')  # Field name made lowercase.
    channel = models.IntegerField(blank=True, null=True)
    channelid = models.CharField(max_length=80, blank=True, null=True)
    macid = models.CharField(db_column='macId', max_length=80, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(max_length=255, blank=True, null=True)
    ptime = models.CharField(max_length=255, blank=True, null=True)
    isphoneback = models.IntegerField(blank=True, null=True)
    phonetype = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'YJ_PHONE_PUSH'


class ChengdeTemp(models.Model):
    account = models.CharField(max_length=255)
    ip = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chengde_temp'


class CorrectIndustry(models.Model):
    account = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    correct_industry = models.CharField(max_length=255, blank=True, null=True)
    userstatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correct_industry'


class EsLog(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=255, blank=True, null=True)
    access_param = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log'


class EsLog1317(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log1317'


class EsLog2024(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log2024'


class EsLog501(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log501'


class EsLog502(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log502'


class EsLog503(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log503'


class EsLog504(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log504'


class EsLog505(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log505'


class EsLog506(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log506'


class EsLog507(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log507'


class EsLog508(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log508'


class EsLog509(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log509'


class EsLog510(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log510'


class EsLog511(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log511'


class EsLog512(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log512'


class EsLog518(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log518'


class EsLog519(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log519'


class EsLog523(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log523'


class EsLog524(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log524'


class EsLog525(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log525'


class EsLog526(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log526'


class EsLog527(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log527'


class EsLog528(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log528'


class EsLog529(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log529'


class EsLog530(models.Model):
    uid = models.IntegerField()
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=600, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log530'


class EsLog601(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log601'


class EsLog602(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log602'


class EsLog603(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log603'


class EsLog604(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log604'


class EsLog06(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log_06'


class EsLog61014(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log_61014'


class EsLogTest(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log_test'


class EsLogWechat(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_date = models.CharField(max_length=255)
    http_referrer = models.CharField(max_length=255)
    access_route = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255)
    request_time = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    ustatus = models.IntegerField(blank=True, null=True)
    addtime = models.CharField(max_length=255, blank=True, null=True)
    referrer_param = models.CharField(max_length=600, blank=True, null=True)
    access_param = models.CharField(max_length=1000, blank=True, null=True)
    post_param = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_log_wechat'


class ExportCount(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.CharField(max_length=50, blank=True, null=True)
    trysdate = models.CharField(max_length=50, blank=True, null=True)
    ustatus = models.CharField(max_length=10, blank=True, null=True)
    sale = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=10, blank=True, null=True)
    browns_piliang = models.IntegerField(blank=True, null=True)
    browns_piliang_info_count = models.IntegerField(blank=True, null=True)
    search_piliang = models.IntegerField(blank=True, null=True)
    search_piliang_info_count = models.IntegerField(blank=True, null=True)
    warning_piliang = models.IntegerField(blank=True, null=True)
    warning_piliang_info_count = models.IntegerField(blank=True, null=True)
    browns_allexport = models.IntegerField(blank=True, null=True)
    search_allexport = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_industry = models.CharField(max_length=255, blank=True, null=True)
    eventanalysis_piliang = models.IntegerField(blank=True, null=True)
    eventanalysis_piliang_count = models.IntegerField(blank=True, null=True)
    eventanalysis_allexport = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_count'


class InsertTest(models.Model):
    num = models.IntegerField(blank=True, null=True)
    ctime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insert_test'


class JavaCopylinkLog(models.Model):
    info_uuid = models.CharField(max_length=40)
    kv_uuid = models.CharField(max_length=40)
    info_type = models.IntegerField(blank=True, null=True)
    subject_id = models.CharField(max_length=40, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    info_state = models.CharField(max_length=2, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    is_local = models.IntegerField(blank=True, null=True)
    warning_flag = models.IntegerField(blank=True, null=True)
    is_accurate = models.IntegerField(blank=True, null=True)
    forward_source = models.CharField(max_length=50, blank=True, null=True)
    forward_status_url = models.CharField(max_length=50, blank=True, null=True)
    key_word = models.CharField(max_length=50, blank=True, null=True)
    orientation = models.IntegerField(blank=True, null=True)
    is_warning = models.IntegerField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    is_attention = models.IntegerField(blank=True, null=True)
    is_feedback = models.IntegerField(blank=True, null=True)
    praise_count = models.IntegerField(blank=True, null=True)
    forward_count = models.IntegerField(blank=True, null=True)
    visit_count = models.IntegerField(blank=True, null=True)
    reply_count = models.IntegerField(blank=True, null=True)
    simhash = models.CharField(max_length=50, blank=True, null=True)
    web_name = models.CharField(max_length=50, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    source_type = models.CharField(max_length=2, blank=True, null=True)
    hot_value = models.IntegerField(blank=True, null=True)
    is_abrupt = models.IntegerField(blank=True, null=True)
    is_hot_events = models.IntegerField(blank=True, null=True)
    is_user_main = models.IntegerField(blank=True, null=True)
    is_main_simhash = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    lost_time = models.DateTimeField(blank=True, null=True)
    orien_level = models.IntegerField(blank=True, null=True)
    noise_state = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    info_url = models.CharField(max_length=600, blank=True, null=True)
    red_word = models.CharField(max_length=200, blank=True, null=True)
    author_pic = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    clloect_time = models.DateTimeField(blank=True, null=True)
    is_pic = models.IntegerField(blank=True, null=True)
    is_video = models.IntegerField(blank=True, null=True)
    img_url = models.CharField(max_length=1000, blank=True, null=True)
    vedio_url = models.CharField(max_length=1000, blank=True, null=True)
    is_match_title = models.IntegerField(blank=True, null=True)
    must_word_beeline = models.IntegerField(blank=True, null=True)
    key_words_beeline = models.IntegerField(blank=True, null=True)
    is_only_local = models.IntegerField(blank=True, null=True)
    micro_is_earlydata = models.IntegerField(blank=True, null=True)
    micro_sign_local_noise = models.IntegerField(blank=True, null=True)
    micro_topic_noise = models.IntegerField(blank=True, null=True)
    micro_at_noise = models.IntegerField(blank=True, null=True)
    current_time = models.DateTimeField(blank=True, null=True)
    web_channel = models.CharField(max_length=100, blank=True, null=True)
    hot_word = models.CharField(max_length=100, blank=True, null=True)
    domain = models.CharField(max_length=150, blank=True, null=True)
    site_id = models.CharField(max_length=50, blank=True, null=True)
    warning_info_state = models.CharField(max_length=30, blank=True, null=True)
    importance_weight = models.IntegerField(blank=True, null=True)
    extend_field = models.TextField(blank=True, null=True)  # This field type is a guess.
    input_data_type = models.IntegerField(blank=True, null=True)
    warning_info_type = models.IntegerField(blank=True, null=True)
    warning_info = models.CharField(max_length=500, blank=True, null=True)
    warning_time = models.DateTimeField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    warning_type = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    operation_userid = models.IntegerField(blank=True, null=True)
    operation_ip = models.CharField(max_length=255, blank=True, null=True)
    operation_time = models.DateTimeField(blank=True, null=True)
    operation_user_name = models.CharField(max_length=255, blank=True, null=True)
    function_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'java_copylink_log'


class LogTmp(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'log_tmp'


class Manwarning0603(models.Model):
    uname = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manwarning_0603'


class ModAccess(models.Model):
    modname = models.CharField(max_length=255, blank=True, null=True)
    access_pc = models.CharField(max_length=255, blank=True, null=True)
    access_app = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access'


class ModAccessCount(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count'


class ModAccessCount0112(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_0112'


class ModAccessCount1317(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_1317'


class ModAccessCount1819(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_1819'


class ModAccessCount2023(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_2023'


class ModAccessCount2325(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_2325'


class ModAccessCount2628(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_2628'


class ModAccessCount2930(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_2930'


class ModAccessCountL20105(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_0105'


class ModAccessCountL20608(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_0608'


class ModAccessCountL20912(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_0912'


class ModAccessCountL21317(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_1317'


class ModAccessCountL21819(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_1819'


class ModAccessCountL22023(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_2023'


class ModAccessCountL22325(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_2325'


class ModAccessCountL22628(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_2628'


class ModAccessCountL22730(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_2730'


class ModAccessCountL22730Industry(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_2730_industry'


class ModAccessCountL22930(models.Model):
    mid = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    pc_num = models.IntegerField(blank=True, null=True)
    app_num = models.IntegerField(blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    mpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_count_l2_2930'


class ModAccessL2(models.Model):
    modname = models.CharField(max_length=255, blank=True, null=True)
    access_pc = models.CharField(max_length=255, blank=True, null=True)
    access_app = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    pc_refrerr = models.CharField(max_length=255, blank=True, null=True)
    app_refrerr = models.CharField(max_length=255, blank=True, null=True)
    parameter = models.CharField(max_length=255, blank=True, null=True)
    parameter_app = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_access_l2'


class MyAttention(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    search_word = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    modname = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_attention'


class OnekeySource(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    action_date = models.CharField(max_length=255, blank=True, null=True)
    action_type = models.CharField(max_length=255, blank=True, null=True)
    action_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onekey_source'


class TsgzLog(models.Model):
    log_type = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    login_name = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    login_ip = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)
    request_param = models.TextField(blank=True, null=True)
    request_navigation = models.CharField(max_length=5, blank=True, null=True)
    cost_time = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsgz_log'


class UniversitiesInfo(models.Model):
    province = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    manage = models.CharField(max_length=255, blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universities_info'


class UserAccessSteps(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    access_mod = models.CharField(max_length=255, blank=True, null=True)
    access_time = models.CharField(max_length=255, blank=True, null=True)
    agent = models.CharField(max_length=500, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    mod1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_access_steps'


class UserBehaviorAnalysis(models.Model):
    date = models.CharField(primary_key=True, max_length=20)
    weekactive = models.TextField(blank=True, null=True)
    weekactiveall = models.TextField(blank=True, null=True)
    thisweekbackflow = models.TextField(blank=True, null=True)
    thisweekbackflowall = models.CharField(max_length=20, blank=True, null=True)
    weeknewuser = models.TextField(blank=True, null=True)
    weeknewuserall = models.CharField(max_length=20, blank=True, null=True)
    daytimeactive_pc = models.TextField(db_column='daytimeactive_PC', blank=True, null=True)  # Field name made lowercase.
    daytimeactive_mob = models.TextField(db_column='daytimeactive_MOB', blank=True, null=True)  # Field name made lowercase.
    daytimeactive_all_pc = models.TextField(db_column='daytimeactive_all_PC', blank=True, null=True)  # Field name made lowercase.
    daytimeactive_all_mob = models.TextField(db_column='daytimeactive_all_MOB', blank=True, null=True)  # Field name made lowercase.
    zsnum_all = models.IntegerField(blank=True, null=True)
    synum_all = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_behavior_analysis'


class UserOperationBehavior(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=40)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior'


class UserOperationBehavior20190329(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190329'


class UserOperationBehavior20190330(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190330'


class UserOperationBehavior20190401(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190401'


class UserOperationBehavior20190402(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190402'


class UserOperationBehavior20190403(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190403'


class UserOperationBehavior20190404(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190404'


class UserOperationBehavior20190405(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190405'


class UserOperationBehavior20190406(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190406'


class UserOperationBehavior20190407(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190407'


class UserOperationBehavior20190408(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190408'


class UserOperationBehavior20190409(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190409'


class UserOperationBehavior20190410(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190410'


class UserOperationBehavior20190411(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190411'


class UserOperationBehavior20190412(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190412'


class UserOperationBehavior20190413(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190413'


class UserOperationBehavior20190414(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190414'


class UserOperationBehavior20190415(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190415'


class UserOperationBehavior20190416(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190416'


class UserOperationBehavior20190417(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190417'


class UserOperationBehavior20190418(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190418'


class UserOperationBehavior20190419(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190419'


class UserOperationBehavior20190420(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190420'


class UserOperationBehavior20190421(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190421'


class UserOperationBehavior20190422(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190422'


class UserOperationBehavior20190423(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190423'


class UserOperationBehavior20190424(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190424'


class UserOperationBehavior20190425(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190425'


class UserOperationBehavior20190426(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190426'


class UserOperationBehavior20190427(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190427'


class UserOperationBehavior20190428(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190428'


class UserOperationBehavior20190429(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190429'


class UserOperationBehavior20190430(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190430'


class UserOperationBehavior20190501(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190501'


class UserOperationBehavior20190502(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190502'


class UserOperationBehavior20190503(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190503'


class UserOperationBehavior20190504(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190504'


class UserOperationBehavior20190505(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190505'


class UserOperationBehavior20190506(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190506'


class UserOperationBehavior20190507(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190507'


class UserOperationBehavior20190508(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190508'


class UserOperationBehavior20190509(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190509'


class UserOperationBehavior20190510(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190510'


class UserOperationBehavior20190511(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190511'


class UserOperationBehavior20190512(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190512'


class UserOperationBehavior20190513(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190513'


class UserOperationBehavior20190514(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190514'


class UserOperationBehavior20190515(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190515'


class UserOperationBehavior20190516(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190516'


class UserOperationBehavior20190517(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190517'


class UserOperationBehavior20190518(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190518'


class UserOperationBehavior20190519(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190519'


class UserOperationBehavior20190520(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190520'


class UserOperationBehavior20190521(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190521'


class UserOperationBehavior20190522(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190522'


class UserOperationBehavior20190523(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190523'


class UserOperationBehavior20190524(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190524'


class UserOperationBehavior20190525(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190525'


class UserOperationBehavior20190526(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190526'


class UserOperationBehavior20190527(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190527'


class UserOperationBehavior20190528(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190528'


class UserOperationBehavior20190529(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190529'


class UserOperationBehavior20190530(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190530'


class UserOperationBehavior20190531(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190531'


class UserOperationBehavior20190601(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190601'


class UserOperationBehavior20190602(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190602'


class UserOperationBehavior20190603(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190603'


class UserOperationBehavior20190604(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190604'


class UserOperationBehavior20190605(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190605'


class UserOperationBehavior20190606(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190606'


class UserOperationBehavior20190607(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190607'


class UserOperationBehavior20190608(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190608'


class UserOperationBehavior20190609(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190609'


class UserOperationBehavior20190610(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190610'


class UserOperationBehavior20190611(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190611'


class UserOperationBehavior20190612(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190612'


class UserOperationBehavior20190613(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190613'


class UserOperationBehavior20190614(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190614'


class UserOperationBehavior20190615(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190615'


class UserOperationBehavior20190616(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190616'


class UserOperationBehavior20190617(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190617'


class UserOperationBehavior20190618(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190618'


class UserOperationBehavior20190619(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190619'


class UserOperationBehavior20190620(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190620'


class UserOperationBehavior20190621(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190621'


class UserOperationBehavior20190622(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190622'


class UserOperationBehavior20190623(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190623'


class UserOperationBehavior20190624(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190624'


class UserOperationBehavior20190625(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190625'


class UserOperationBehavior20190626(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190626'


class UserOperationBehavior20190627(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190627'


class UserOperationBehavior20190628(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190628'


class UserOperationBehavior20190629(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190629'


class UserOperationBehavior20190630(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190630'


class UserOperationBehavior20190701(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190701'


class UserOperationBehavior20190702(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190702'


class UserOperationBehavior20190703(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190703'


class UserOperationBehavior20190704(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190704'


class UserOperationBehavior20190705(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190705'


class UserOperationBehavior20190706(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190706'


class UserOperationBehavior20190707(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190707'


class UserOperationBehavior20190708(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190708'


class UserOperationBehavior20190709(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190709'


class UserOperationBehavior20190710(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190710'


class UserOperationBehavior20190711(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190711'


class UserOperationBehavior20190712(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190712'


class UserOperationBehavior20190713(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190713'


class UserOperationBehavior20190714(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190714'


class UserOperationBehavior20190715(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190715'


class UserOperationBehavior20190716(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190716'


class UserOperationBehavior20190717(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190717'


class UserOperationBehavior20190718(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190718'


class UserOperationBehavior20190719(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190719'


class UserOperationBehavior20190720(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190720'


class UserOperationBehavior20190721(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190721'


class UserOperationBehavior20190722(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190722'


class UserOperationBehavior20190723(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190723'


class UserOperationBehavior20190724(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190724'


class UserOperationBehavior20190725(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190725'


class UserOperationBehavior20190726(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190726'


class UserOperationBehavior20190727(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190727'


class UserOperationBehavior20190728(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190728'


class UserOperationBehavior20190729(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190729'


class UserOperationBehavior20190730(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190730'


class UserOperationBehavior20190731(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190731'


class UserOperationBehavior20190801(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190801'


class UserOperationBehavior20190802(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190802'


class UserOperationBehavior20190803(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190803'


class UserOperationBehavior20190804(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190804'


class UserOperationBehavior20190805(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190805'


class UserOperationBehavior20190806(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190806'


class UserOperationBehavior20190807(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190807'


class UserOperationBehavior20190808(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190808'


class UserOperationBehavior20190809(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190809'


class UserOperationBehavior20190810(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190810'


class UserOperationBehavior20190811(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190811'


class UserOperationBehavior20190812(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190812'


class UserOperationBehavior20190813(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190813'


class UserOperationBehavior20190814(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190814'


class UserOperationBehavior20190815(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190815'


class UserOperationBehavior20190816(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190816'


class UserOperationBehavior20190817(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190817'


class UserOperationBehavior20190818(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190818'


class UserOperationBehavior20190819(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190819'


class UserOperationBehavior20190820(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190820'


class UserOperationBehavior20190821(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190821'


class UserOperationBehavior20190822(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190822'


class UserOperationBehavior20190823(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190823'


class UserOperationBehavior20190824(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190824'


class UserOperationBehavior20190825(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190825'


class UserOperationBehavior20190826(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190826'


class UserOperationBehavior20190827(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190827'


class UserOperationBehavior20190828(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190828'


class UserOperationBehavior20190829(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190829'


class UserOperationBehavior20190830(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190830'


class UserOperationBehavior20190831(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190831'


class UserOperationBehavior20190901(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190901'


class UserOperationBehavior20190902(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190902'


class UserOperationBehavior20190903(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190903'


class UserOperationBehavior20190904(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190904'


class UserOperationBehavior20190905(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190905'


class UserOperationBehavior20190906(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190906'


class UserOperationBehavior20190907(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190907'


class UserOperationBehavior20190908(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190908'


class UserOperationBehavior20190909(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190909'


class UserOperationBehavior20190910(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190910'


class UserOperationBehavior20190911(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190911'


class UserOperationBehavior20190912(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190912'


class UserOperationBehavior20190913(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190913'


class UserOperationBehavior20190914(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190914'


class UserOperationBehavior20190915(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190915'


class UserOperationBehavior20190916(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190916'


class UserOperationBehavior20190917(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190917'


class UserOperationBehavior20190918(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190918'


class UserOperationBehavior20190919(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190919'


class UserOperationBehavior20190920(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190920'


class UserOperationBehavior20190921(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190921'


class UserOperationBehavior20190922(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190922'


class UserOperationBehavior20190923(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190923'


class UserOperationBehavior20190924(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190924'


class UserOperationBehavior20190925(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190925'


class UserOperationBehavior20190926(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190926'


class UserOperationBehavior20190927(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190927'


class UserOperationBehavior20190928(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190928'


class UserOperationBehavior20190929(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190929'


class UserOperationBehavior20190930(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20190930'


class UserOperationBehavior20191001(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191001'


class UserOperationBehavior20191002(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191002'


class UserOperationBehavior20191003(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191003'


class UserOperationBehavior20191004(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191004'


class UserOperationBehavior20191005(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191005'


class UserOperationBehavior20191006(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191006'


class UserOperationBehavior20191007(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191007'


class UserOperationBehavior20191008(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191008'


class UserOperationBehavior20191009(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191009'


class UserOperationBehavior20191010(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191010'


class UserOperationBehavior20191011(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191011'


class UserOperationBehavior20191012(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191012'


class UserOperationBehavior20191013(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191013'


class UserOperationBehavior20191014(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191014'


class UserOperationBehavior20191015(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191015'


class UserOperationBehavior20191016(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191016'


class UserOperationBehavior20191017(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191017'


class UserOperationBehavior20191018(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191018'


class UserOperationBehavior20191019(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191019'


class UserOperationBehavior20191020(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191020'


class UserOperationBehavior20191021(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191021'


class UserOperationBehavior20191022(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191022'


class UserOperationBehavior20191023(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191023'


class UserOperationBehavior20191024(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191024'


class UserOperationBehavior20191025(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191025'


class UserOperationBehavior20191026(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191026'


class UserOperationBehavior20191027(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191027'


class UserOperationBehavior20191028(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191028'


class UserOperationBehavior20191029(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191029'


class UserOperationBehavior20191030(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191030'


class UserOperationBehavior20191031(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191031'


class UserOperationBehavior20191101(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191101'


class UserOperationBehavior20191102(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191102'


class UserOperationBehavior20191103(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191103'


class UserOperationBehavior20191104(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191104'


class UserOperationBehavior20191105(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191105'


class UserOperationBehavior20191106(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191106'


class UserOperationBehavior20191107(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191107'


class UserOperationBehavior20191108(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191108'


class UserOperationBehavior20191109(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191109'


class UserOperationBehavior20191110(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191110'


class UserOperationBehavior20191111(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191111'


class UserOperationBehavior20191112(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191112'


class UserOperationBehavior20191113(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191113'


class UserOperationBehavior20191114(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191114'


class UserOperationBehavior20191115(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191115'


class UserOperationBehavior20191116(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191116'


class UserOperationBehavior20191117(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191117'


class UserOperationBehavior20191118(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191118'


class UserOperationBehavior20191119(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191119'


class UserOperationBehavior20191120(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191120'


class UserOperationBehavior20191121(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191121'


class UserOperationBehavior20191122(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191122'


class UserOperationBehavior20191123(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191123'


class UserOperationBehavior20191124(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191124'


class UserOperationBehavior20191125(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191125'


class UserOperationBehavior20191126(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191126'


class UserOperationBehavior20191127(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191127'


class UserOperationBehavior20191128(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191128'


class UserOperationBehavior20191129(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191129'


class UserOperationBehavior20191130(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191130'


class UserOperationBehavior20191201(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191201'


class UserOperationBehavior20191202(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191202'


class UserOperationBehavior20191203(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191203'


class UserOperationBehavior20191204(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191204'


class UserOperationBehavior20191205(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191205'


class UserOperationBehavior20191206(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191206'


class UserOperationBehavior20191207(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191207'


class UserOperationBehavior20191208(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191208'


class UserOperationBehavior20191209(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191209'


class UserOperationBehavior20191210(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191210'


class UserOperationBehavior20191211(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191211'


class UserOperationBehavior20191212(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191212'


class UserOperationBehavior20191213(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191213'


class UserOperationBehavior20191214(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191214'


class UserOperationBehavior20191215(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191215'


class UserOperationBehavior20191216(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191216'


class UserOperationBehavior20191217(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191217'


class UserOperationBehavior20191218(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191218'


class UserOperationBehavior20191219(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191219'


class UserOperationBehavior20191220(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191220'


class UserOperationBehavior20191221(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191221'


class UserOperationBehavior20191222(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191222'


class UserOperationBehavior20191223(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191223'


class UserOperationBehavior20191224(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191224'


class UserOperationBehavior20191225(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191225'


class UserOperationBehavior20191226(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191226'


class UserOperationBehavior20191227(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191227'


class UserOperationBehavior20191228(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191228'


class UserOperationBehavior20191229(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191229'


class UserOperationBehavior20191230(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191230'


class UserOperationBehavior20191231(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20191231'


class UserOperationBehavior20200101(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200101'


class UserOperationBehavior20200102(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200102'


class UserOperationBehavior20200103(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200103'


class UserOperationBehavior20200104(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200104'


class UserOperationBehavior20200105(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200105'


class UserOperationBehavior20200106(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200106'


class UserOperationBehavior20200107(models.Model):
    user_id = models.IntegerField()
    operation_describe = models.CharField(max_length=100)
    user_state = models.SmallIntegerField()
    user_name = models.CharField(max_length=100)
    user_industry = models.SmallIntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_operation_behavior_20200107'


class Warningsetlog(models.Model):
    operator = models.CharField(max_length=255)
    acc = models.IntegerField()
    type = models.IntegerField()
    add = models.TextField(blank=True, null=True)
    del_field = models.TextField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'warningSetLog'


class WarningCount(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    wdate = models.CharField(max_length=10, blank=True, null=True)
    wcount = models.IntegerField(blank=True, null=True)
    waoto1 = models.IntegerField(blank=True, null=True)
    waoto2 = models.IntegerField(blank=True, null=True)
    waoto3 = models.IntegerField(blank=True, null=True)
    waoto4 = models.IntegerField(blank=True, null=True)
    waoto5 = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    ustatus = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warning_count'


class YqllSearchContent(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=255, blank=True, null=True)
    access_date = models.CharField(max_length=255, blank=True, null=True)
    search_word = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yqll_search_content'
