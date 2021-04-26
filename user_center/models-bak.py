# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.URLField(verbose_name="头像", max_length=255, blank=True, null=True, default="/static/img/a7.jpg")

class CalIdf(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    word = models.CharField(db_column='Word', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idfnum = models.BigIntegerField(db_column='IDFNUM', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAL_IDF'


class CalIdfdocnum(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    docnum = models.BigIntegerField(db_column='DOCNUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAL_IDFDOCNUM'


class Cityhot(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    cityname = models.CharField(db_column='CITYNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ctime = models.CharField(db_column='CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hot = models.IntegerField(db_column='HOT', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SOURCETYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    titlesimhash = models.CharField(db_column='TITLESIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    titlekeywords = models.CharField(db_column='TITLEKEYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    procince = models.CharField(db_column='PROCINCE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cite = models.CharField(db_column='CITE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='COUNTY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    titlerefhash = models.CharField(db_column='TITLEREFHASH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_isyj = models.CharField(db_column='KV_ISYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CITYHOT'


class Config(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    key = models.CharField(db_column='KEY', max_length=50)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    source_info = models.TextField(db_column='SOURCE_INFO')  # Field name made lowercase.
    target_redis_info = models.TextField(db_column='TARGET_REDIS_INFO')  # Field name made lowercase.
    thread_buffer_redis_info = models.TextField(db_column='THREAD_BUFFER_REDIS_INFO')  # Field name made lowercase.
    mysql_host = models.CharField(db_column='MYSQL_HOST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    error_redis_info = models.TextField(db_column='ERROR_REDIS_INFO')  # Field name made lowercase.
    n_thread = models.IntegerField(db_column='N_THREAD')  # Field name made lowercase.
    n_commit = models.IntegerField(db_column='N_COMMIT')  # Field name made lowercase.
    t_commit = models.IntegerField(db_column='T_COMMIT')  # Field name made lowercase.
    table_sql = models.TextField(db_column='TABLE_SQL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG'


class Crmaccountmapping(models.Model):
    msuid = models.IntegerField(db_column='msUid', primary_key=True)  # Field name made lowercase.
    msname = models.CharField(db_column='msName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.IntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
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


class Crmaccountmapping20190614(models.Model):
    msuid = models.IntegerField(db_column='msUid')  # Field name made lowercase.
    msname = models.CharField(db_column='msName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.IntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'CRMACCOUNTMAPPING_20190614'


class Crmaccountsalemapping(models.Model):
    crmuid = models.BigIntegerField(db_column='crmUid')  # Field name made lowercase.
    ownerflag = models.IntegerField(db_column='ownerFlag')  # Field name made lowercase.
    saleid = models.BigIntegerField(db_column='saleId')  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRMACCOUNTSALEMAPPING'


class Crmsalemapping(models.Model):
    crmuid = models.BigIntegerField(db_column='crmUid')  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId')  # Field name made lowercase.
    ownerflag = models.IntegerField(db_column='ownerFlag')  # Field name made lowercase.
    saleid = models.BigIntegerField(db_column='saleId')  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRMSALEMAPPING'


class Checkurlcollection(models.Model):
    jobid = models.CharField(db_column='jobId', max_length=200)  # Field name made lowercase.
    url = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    sourcetype = models.CharField(db_column='sourceType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CheckUrlCollection'


class Checkurljob(models.Model):
    jobid = models.CharField(db_column='jobId', primary_key=True, max_length=100)  # Field name made lowercase.
    jobname = models.CharField(db_column='jobName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    infoids = models.TextField(db_column='infoIds', blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    krkeywordid = models.CharField(db_column='krKeywordId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    templateid = models.CharField(db_column='templateId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shareuserid = models.CharField(db_column='shareUserId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    checktotal = models.CharField(db_column='checkTotal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    checknum = models.CharField(db_column='checkNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    invalidnum = models.CharField(db_column='invalidNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    checkstype = models.IntegerField(db_column='checkStype', blank=True, null=True)  # Field name made lowercase.
    checkstatus = models.IntegerField(db_column='checkStatus', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckUrlJob'


class Classlyproject(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=60)  # Field name made lowercase.
    projectclasslyname = models.CharField(db_column='ProjectClasslyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    classlynames = models.TextField(db_column='ClasslyNames', blank=True, null=True)  # Field name made lowercase.
    kid = models.CharField(db_column='KID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    infotype = models.CharField(db_column='INFOTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClasslyProject'


class Classlyrule(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    classlyname = models.CharField(db_column='ClasslyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classlymaintype = models.CharField(db_column='ClasslyMainType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l1 = models.CharField(db_column='L1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l2 = models.CharField(db_column='L2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l3 = models.CharField(db_column='L3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l4 = models.CharField(db_column='L4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    words = models.TextField(blank=True, null=True)
    keyssource = models.CharField(db_column='keysSource', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(max_length=50, blank=True, null=True)
    lv = models.IntegerField(db_column='LV', blank=True, null=True)  # Field name made lowercase.
    bigdatarule = models.TextField(db_column='BIGDATARULE', blank=True, null=True)  # Field name made lowercase.
    logicrule = models.TextField(db_column='LOGICRULE', blank=True, null=True)  # Field name made lowercase.
    classlynamenickname = models.CharField(db_column='ClasslyNameNickname', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClasslyRule'


class Classlyruleclassly(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    classlyname = models.CharField(db_column='Classlyname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classlyrule = models.CharField(db_column='Classlyrule', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClasslyRuleClassly'


class Domaincount(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    domain = models.CharField(db_column='DOMAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    channel = models.CharField(db_column='CHANNEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOMAINCOUNT'


class Domainweight(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    domain = models.CharField(db_column='DOMAIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    realdomain = models.CharField(db_column='REALDOMAIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    webname = models.CharField(db_column='WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOMAINWEIGHT'


class Hero(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    damage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Hero'


class Infoclassly(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classlyname = models.CharField(db_column='CLASSLYNAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_weibouid = models.CharField(db_column='KV_WEIBOUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classlywords = models.CharField(db_column='CLASSLYWORDS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_push = models.IntegerField(db_column='KV_PUSH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFOClassly'


class MsApiStatusLog(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    old_status = models.IntegerField(db_column='OLD_STATUS')  # Field name made lowercase.
    new_status = models.IntegerField(db_column='NEW_STATUS')  # Field name made lowercase.
    old_trydate = models.DateField(db_column='OLD_TRYDATE', blank=True, null=True)  # Field name made lowercase.
    new_trydate = models.DateField(db_column='NEW_TRYDATE', blank=True, null=True)  # Field name made lowercase.
    change_time = models.CharField(db_column='CHANGE_TIME', max_length=50)  # Field name made lowercase.
    change_user = models.CharField(db_column='CHANGE_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MS_API_STATUS_LOG'


class MysqlDatasourceConfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dbname = models.CharField(db_column='DBNAME', max_length=50)  # Field name made lowercase.
    mysqlinfo = models.TextField(db_column='MYSQLINFO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MYSQL_DATASOURCE_CONFIG'


class Mobilecloudcourse(models.Model):
    coursetitle = models.CharField(db_column='courseTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coursesummary = models.CharField(db_column='courseSummary', max_length=500, blank=True, null=True)  # Field name made lowercase.
    courselectuer = models.CharField(db_column='courseLectuer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    coursereleasetime = models.CharField(db_column='courseReleaseTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    coursenum = models.IntegerField(db_column='courseNum', blank=True, null=True)  # Field name made lowercase.
    coursepicurl = models.CharField(db_column='coursePicUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lectuerid = models.CharField(db_column='lectuerId', max_length=50)  # Field name made lowercase.
    onlinetime = models.DateTimeField(db_column='onlineTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileCloudCourse'


class Mobilecloudcourselectuer(models.Model):
    lectuername = models.CharField(db_column='lectuerName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lectuersummary = models.CharField(db_column='lectuerSummary', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lectuerpicurl = models.CharField(db_column='lectuerPicUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileCloudCourseLectuer'


class Mobilecloudcourseware(models.Model):
    courseid = models.IntegerField(db_column='courseId')  # Field name made lowercase.
    coursewaretitle = models.CharField(db_column='coursewareTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coursewarevideourl = models.CharField(db_column='coursewareVideoUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coursewarevideolength = models.CharField(db_column='coursewareVideoLength', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileCloudCourseware'


class Mobilecloudevent(models.Model):
    departmentid = models.CharField(db_column='departmentId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    subjectword = models.CharField(db_column='subjectWord', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    thematicname = models.CharField(db_column='thematicName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventword = models.CharField(db_column='eventWord', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileCloudEvent'


class Mobilecloudsubject(models.Model):
    departmentid = models.CharField(db_column='departmentId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    subjectword = models.CharField(db_column='subjectWord', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MobileCloudSubject'


class Newwords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='CLASSNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classpname = models.CharField(db_column='CLASSPNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEWWORDS'


class Newwordsclassly(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEWWORDSCLASSLY'


class Notwords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notword = models.TextField(db_column='NOTWORD', blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    notwordcombin = models.TextField(db_column='NOTWORDCOMBIN', blank=True, null=True)  # Field name made lowercase.
    example = models.TextField(blank=True, null=True)
    modifytime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NOTWORDS'


class Newtable(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=64)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    kr_filename = models.CharField(db_column='KR_FILENAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    kr_tmurl = models.CharField(db_column='KR_TMURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_smburl = models.CharField(db_column='KR_SMBURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_downloadtime = models.CharField(db_column='KR_DOWNLOADTIME', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewTable'


class OverseaWeb(models.Model):
    web_type_id = models.IntegerField(db_column='WEB_TYPE_ID')  # Field name made lowercase.
    web_name = models.CharField(db_column='WEB_NAME', max_length=255)  # Field name made lowercase.
    website = models.CharField(db_column='WEBSITE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OVERSEA_WEB'


class OverseaWebtype(models.Model):
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OVERSEA_WEBTYPE'


class Pnwords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    wordtype = models.CharField(db_column='WordType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pn = models.CharField(db_column='PN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    word = models.CharField(db_column='Word', max_length=30, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    doccount = models.IntegerField(db_column='DocCount', blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PNWORDS'


class Projectclassly(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    projectrules = models.TextField(db_column='ProjectRules', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectClassly'


class Reportwords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CREATEUSER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mainword = models.CharField(db_column='MAINWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='INDUSTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORTWORDS'


class Reportclassify(models.Model):
    userid = models.CharField(db_column='userId', max_length=20)  # Field name made lowercase.
    classifyname = models.CharField(db_column='classifyName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportClassify'


class Reportfileinfo(models.Model):
    userid = models.CharField(db_column='userId', max_length=30)  # Field name made lowercase.
    reportfilename = models.CharField(db_column='reportFileName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='enterTime', blank=True, null=True)  # Field name made lowercase.
    downloadurl = models.CharField(db_column='downLoadUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reporttype = models.IntegerField(db_column='reportType', blank=True, null=True)  # Field name made lowercase.
    buildtype = models.IntegerField(db_column='buildType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportFileInfo'


class Reportvariable(models.Model):
    userid = models.CharField(db_column='userId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    initname = models.CharField(db_column='initName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inittype = models.IntegerField(db_column='initType', blank=True, null=True)  # Field name made lowercase.
    initvalue = models.IntegerField(db_column='initValue', blank=True, null=True)  # Field name made lowercase.
    inittotal = models.IntegerField(db_column='initTotal', blank=True, null=True)  # Field name made lowercase.
    inittimestamp = models.BigIntegerField(db_column='initTimeStamp', blank=True, null=True)  # Field name made lowercase.
    timeinterval = models.BigIntegerField(db_column='timeInterval', blank=True, null=True)  # Field name made lowercase.
    timedifference = models.BigIntegerField(db_column='timeDifference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportVariable'
        unique_together = (('userid', 'inittype'),)


class Saledatacount(models.Model):
    saleid = models.BigIntegerField(db_column='saleId')  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=255)  # Field name made lowercase.
    createat = models.CharField(db_column='createAt', max_length=255)  # Field name made lowercase.
    todaynewopportunity = models.BigIntegerField(db_column='todayNewOpportunity')  # Field name made lowercase.
    weeknewopportunity = models.BigIntegerField(db_column='weekNewOpportunity')  # Field name made lowercase.
    allconfirmopportunity = models.BigIntegerField(db_column='allConfirmOpportunity')  # Field name made lowercase.
    allnegotiationopportunity = models.BigIntegerField(db_column='allNegotiationOpportunity')  # Field name made lowercase.
    todayleaderconfirmcontractissue = models.BigIntegerField(db_column='todayLeaderConfirmContractIssue')  # Field name made lowercase.
    todayactualcontractissue = models.BigIntegerField(db_column='todayActualContractIssue')  # Field name made lowercase.
    weekactualcontractissue = models.BigIntegerField(db_column='weekActualContractIssue')  # Field name made lowercase.
    todayleaderconfirmcontractfile = models.BigIntegerField(db_column='todayLeaderConfirmContractFile')  # Field name made lowercase.
    todayactualcontractfile = models.BigIntegerField(db_column='todayActualContractFile')  # Field name made lowercase.
    weekactualcontractfile = models.BigIntegerField(db_column='weekActualContractFile')  # Field name made lowercase.
    todaytelephone = models.BigIntegerField(db_column='todayTelephone')  # Field name made lowercase.
    todaybusinessvisit = models.BigIntegerField(db_column='todayBusinessVisit')  # Field name made lowercase.
    todayappointmentvisit = models.BigIntegerField(db_column='todayAppointmentVisit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SALEDATACOUNT'


class SolrTCollectinfo(models.Model):
    userid = models.CharField(max_length=50, blank=True, null=True)
    collectid = models.CharField(max_length=100, blank=True, null=True)
    collectname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SOLR_T_COLLECTINFO'


class SolrTCollectinfocnt(models.Model):
    userid = models.CharField(db_column='userId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cntid = models.CharField(db_column='cntId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectid = models.CharField(db_column='collectId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contentname = models.CharField(db_column='contentName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLR_T_COLLECTINFOCNT'


class SolrTExportcondition(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    field_id = models.CharField(db_column='FIELD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    valid = models.CharField(db_column='VALID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sequences = models.IntegerField(db_column='SEQUENCES', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'SOLR_T_EXPORTCONDITION'


class SolrTExportfield(models.Model):
    field_id = models.CharField(db_column='FIELD_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    field_name = models.CharField(db_column='FIELD_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    solr_id = models.CharField(db_column='SOLR_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLR_T_EXPORTFIELD'


class SubjectUnselect(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(max_length=100, blank=True, null=True)
    subids = models.CharField(max_length=512, blank=True, null=True)
    source = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SUBJECT_UNSELECT'


class Subjectrelationlable(models.Model):
    subjectid = models.CharField(db_column='subjectId', max_length=50)  # Field name made lowercase.
    lableid = models.CharField(db_column='lableId', max_length=50)  # Field name made lowercase.
    type = models.IntegerField()
    areacontain = models.CharField(db_column='areaContain', max_length=5, blank=True, null=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='areaName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SubjectRelationLable'


class Topicauthorrelation(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=70)  # Field name made lowercase.
    topicid = models.CharField(db_column='TOPICID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    authoractive = models.CharField(db_column='AUTHORACTIVE', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    authorpassive = models.CharField(db_column='AUTHORPASSIVE', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    authorwarning = models.CharField(db_column='AUTHORWARNING', max_length=3000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOPICAUTHORRELATION'


class Topicgdlines(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=110)  # Field name made lowercase.
    topicid = models.CharField(db_column='TOPICID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gdline = models.CharField(db_column='GDLINE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdsourcetypes = models.CharField(db_column='GDSOURCETYPES', max_length=60, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gdzmclassly = models.CharField(db_column='GDZMCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzmclasslywords = models.CharField(db_column='GDZMCLASSLYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdfmclassly = models.CharField(db_column='GDFMCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdfmclasslywords = models.CharField(db_column='GDFMCLASSLYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzfxx = models.CharField(db_column='GDZFXX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gdcount = models.IntegerField(db_column='GDCOUNT', blank=True, null=True)  # Field name made lowercase.
    gdcluster = models.CharField(db_column='GDCLUSTER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdtype = models.CharField(db_column='GDTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOPICGDLINES'


class Topicrdpoint(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=70)  # Field name made lowercase.
    topicid = models.CharField(db_column='TOPICID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctime = models.CharField(db_column='CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hot = models.IntegerField(db_column='HOT', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infoid = models.CharField(db_column='INFOID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    infoids = models.CharField(db_column='INFOIDS', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    isrd = models.CharField(db_column='ISRD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    istf = models.CharField(db_column='ISTF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOPICRDPOINT'


class Topictfpoint(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=70)  # Field name made lowercase.
    topicid = models.CharField(db_column='TOPICID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctime = models.CharField(db_column='CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hot = models.IntegerField(db_column='HOT', blank=True, null=True)  # Field name made lowercase.
    isrd = models.CharField(db_column='ISRD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    istf = models.CharField(db_column='ISTF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hotrand = models.FloatField(db_column='HOTRAND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOPICTFPOINT'


class Topicweiboauthorinfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    verified_level = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=30, blank=True, null=True)
    bi_followers_count = models.IntegerField(blank=True, null=True)
    userid = models.CharField(db_column='USERID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    urank = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    last_ctime = models.CharField(max_length=30, blank=True, null=True)
    verified_reason = models.CharField(max_length=100, blank=True, null=True)
    followers_count = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    avatar_large = models.CharField(max_length=50, blank=True, null=True)
    statuses_count = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    online_status = models.IntegerField(blank=True, null=True)
    allow_all_act_msg = models.IntegerField(blank=True, null=True)
    allow_all_comment = models.IntegerField(blank=True, null=True)
    geo_enabled = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    weihao = models.CharField(max_length=15, blank=True, null=True)
    screen_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.CharField(max_length=30, blank=True, null=True)
    tid = models.CharField(db_column='TID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOPICWEIBOAUTHORINFO'


class Trainclassly(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    classlyname = models.CharField(db_column='CLASSLYNAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    centerwords = models.TextField(db_column='CENTERWORDS', blank=True, null=True)  # Field name made lowercase.
    trainwords = models.TextField(db_column='TRAINWORDS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobifytime = models.CharField(db_column='MOBIFYTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRAINCLASSLY'


class Travelplantemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    saleid = models.BigIntegerField(db_column='saleId', blank=True, null=True)  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businesstime = models.DateTimeField(db_column='businessTime', blank=True, null=True)  # Field name made lowercase.
    currentstage = models.CharField(db_column='currentStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    servicetype = models.CharField(db_column='serviceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    businessobjective = models.CharField(db_column='businessObjective', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confirminfo = models.CharField(db_column='confirmInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    success = models.IntegerField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    afterstage = models.CharField(db_column='afterStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    filebacktime = models.DateTimeField(db_column='fileBackTime', blank=True, null=True)  # Field name made lowercase.
    synchro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TRAVELPLANTEMPLATE'


class Test(models.Model):
    a = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Test'


class Test199(models.Model):
    a = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Test199'


class Testdataapi(models.Model):
    a = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestDATAAPI'


class Userdatestatuscount(models.Model):
    createat = models.CharField(db_column='createAt', primary_key=True, max_length=20)  # Field name made lowercase.
    alluser = models.BigIntegerField(db_column='allUser')  # Field name made lowercase.
    trialuser = models.BigIntegerField(db_column='trialUser')  # Field name made lowercase.
    formaluser = models.BigIntegerField(db_column='formalUser')  # Field name made lowercase.
    formalandtrial = models.BigIntegerField(db_column='formalAndTrial')  # Field name made lowercase.
    stopuser = models.BigIntegerField(db_column='stopUser')  # Field name made lowercase.
    abandonuser = models.BigIntegerField(db_column='abandonUser')  # Field name made lowercase.
    newtrial = models.BigIntegerField(db_column='newTrial')  # Field name made lowercase.
    trialtoformal = models.BigIntegerField(db_column='trialToFormal')  # Field name made lowercase.
    formaltotrial = models.BigIntegerField(db_column='formalTotrial')  # Field name made lowercase.
    trialtostop = models.BigIntegerField(db_column='trialToStop')  # Field name made lowercase.
    stoptotrial = models.BigIntegerField(db_column='stopToTrial')  # Field name made lowercase.
    stoptoformal = models.BigIntegerField(db_column='stopToFormal')  # Field name made lowercase.
    formaltoabandon = models.BigIntegerField(db_column='formalToAbandon')  # Field name made lowercase.
    trialtoabandon = models.BigIntegerField(db_column='trialToAbandon')  # Field name made lowercase.
    stoptoabandon = models.BigIntegerField(db_column='stopToAbandon')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERDATESTATUSCOUNT'


class Userpushnum(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pushnum = models.IntegerField(db_column='PUSHNUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERPUSHNUM'


class Usertimelong(models.Model):
    userid = models.BigIntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    userstatus = models.CharField(db_column='userStatus', max_length=255)  # Field name made lowercase.
    alllong = models.BigIntegerField(db_column='allLong')  # Field name made lowercase.
    avglong = models.BigIntegerField(db_column='avgLong')  # Field name made lowercase.
    industry = models.CharField(max_length=255)
    crmname = models.CharField(db_column='crmName', max_length=255)  # Field name made lowercase.
    jumpurl = models.CharField(db_column='jumpUrl', max_length=255)  # Field name made lowercase.
    countdate = models.DateTimeField(db_column='countDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERTIMELONG'


class Weibocomminfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    webname = models.CharField(db_column='WEBNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=300, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ctime = models.CharField(db_column='CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collecttime = models.CharField(db_column='COLLECTTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parenturl = models.CharField(db_column='PARENTURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    replycount = models.IntegerField(db_column='REPLYCOUNT', blank=True, null=True)  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    topicid = models.CharField(db_column='TOPICID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    autoclassly = models.CharField(db_column='AUTOCLASSLY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    classlytype = models.CharField(db_column='CLASSLYTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    classlyinfo = models.CharField(db_column='CLASSLYINFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzmclassly = models.CharField(db_column='GDZMCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdfmclassly = models.CharField(db_column='GDFMCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdfmclasslyinfo = models.CharField(db_column='GDFMCLASSLYINFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzmclasslyinfo = models.CharField(db_column='GDZMCLASSLYINFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzfxx = models.CharField(db_column='GDZFXX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sheng = models.CharField(max_length=50, blank=True, null=True)
    shi = models.CharField(max_length=50, blank=True, null=True)
    xian = models.CharField(max_length=50, blank=True, null=True)
    jigou = models.CharField(max_length=100, blank=True, null=True)
    gdinfo = models.CharField(db_column='GDINFO', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=20, blank=True, null=True)
    webnamedomain = models.CharField(db_column='WEBNAMEDOMAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    webnamelever = models.CharField(db_column='WEBNAMELEVER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    verified = models.CharField(max_length=20, blank=True, null=True)
    userid = models.CharField(db_column='USERID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    screen_name = models.CharField(max_length=50, blank=True, null=True)
    kn_arg1 = models.CharField(db_column='KN_ARG1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kn_arg2 = models.CharField(db_column='KN_ARG2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kn_arg3 = models.CharField(db_column='KN_ARG3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kn_arg4 = models.CharField(db_column='KN_ARG4', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WEIBOCOMMINFO'


class WkCopySubject(models.Model):
    cid = models.IntegerField()
    content = models.TextField()
    addtime = models.CharField(max_length=100)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_COPY_SUBJECT'


class WkCustomerWarming(models.Model):
    uid = models.CharField(max_length=38)
    cid = models.CharField(max_length=38)
    time = models.CharField(max_length=100)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_CUSTOMER_WARMING'


class WkTAccessNew(models.Model):
    kr_id = models.IntegerField(db_column='KR_ID', blank=True, null=True)  # Field name made lowercase.
    kn_id = models.IntegerField(db_column='KN_ID', blank=True, null=True)  # Field name made lowercase.
    kn_level = models.IntegerField(db_column='KN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kn_pid = models.IntegerField(db_column='KN_PID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ACCESS_NEW'


class WkTAgency(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=50)  # Field name made lowercase.
    ka_pwd = models.CharField(db_column='KA_PWD', max_length=32)  # Field name made lowercase.
    ka_aid = models.IntegerField(db_column='KA_AID')  # Field name made lowercase.
    role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_AGENCY'


class WkTAgencyLoginPage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ka_id = models.IntegerField(db_column='KA_ID')  # Field name made lowercase.
    ka_domain = models.CharField(db_column='KA_DOMAIN', max_length=100)  # Field name made lowercase.
    ka_home = models.CharField(db_column='KA_HOME', max_length=100)  # Field name made lowercase.
    ka_home_hide = models.IntegerField(db_column='KA_HOME_HIDE')  # Field name made lowercase.
    ka_title = models.CharField(db_column='KA_TITLE', max_length=50)  # Field name made lowercase.
    ka_title_hide = models.IntegerField(db_column='KA_TITLE_HIDE')  # Field name made lowercase.
    ka_copy = models.CharField(db_column='KA_COPY', max_length=255)  # Field name made lowercase.
    ka_copy_hide = models.IntegerField(db_column='KA_COPY_HIDE')  # Field name made lowercase.
    ka_logo = models.CharField(db_column='KA_LOGO', max_length=255)  # Field name made lowercase.
    ka_back_big = models.CharField(db_column='KA_BACK_BIG', max_length=255)  # Field name made lowercase.
    ka_back_small = models.CharField(db_column='KA_BACK_SMALL', max_length=255)  # Field name made lowercase.
    ka_qr = models.CharField(db_column='KA_QR', max_length=255)  # Field name made lowercase.
    ka_qr_hide = models.IntegerField(db_column='KA_QR_HIDE')  # Field name made lowercase.
    ka_loginpage = models.TextField(db_column='KA_LOGINPAGE', blank=True, null=True)  # Field name made lowercase.
    ka_vern = models.CharField(db_column='KA_VERN', max_length=10)  # Field name made lowercase.
    ka_vern_hide = models.IntegerField(db_column='KA_VERN_HIDE')  # Field name made lowercase.
    ka_template_type = models.IntegerField(db_column='KA_TEMPLATE_TYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENCY_LOGIN_PAGE'


class WkTAgents(models.Model):
    ka_id = models.CharField(db_column='KA_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ka_pid = models.CharField(db_column='KA_PID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_logo = models.CharField(db_column='KA_LOGO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_addr = models.CharField(db_column='KA_ADDR', max_length=400, blank=True, null=True)  # Field name made lowercase.
    ka_record = models.CharField(db_column='KA_RECORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_email = models.CharField(db_column='KA_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_phone = models.CharField(db_column='KA_PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_qq1 = models.CharField(db_column='KA_QQ1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_qq2 = models.CharField(db_column='KA_QQ2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_qq3 = models.CharField(db_column='KA_QQ3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_time = models.CharField(db_column='KA_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ka_site = models.CharField(db_column='KA_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_intro = models.TextField(db_column='KA_INTRO', blank=True, null=True)  # Field name made lowercase.
    ka_logo2 = models.CharField(db_column='KA_LOGO2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_ico = models.CharField(db_column='KA_ICO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ka_open = models.CharField(db_column='KA_OPEN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ka_phone2 = models.CharField(db_column='KA_PHONE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_phone3 = models.CharField(db_column='KA_PHONE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_record1 = models.CharField(db_column='KA_RECORD1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_template = models.CharField(db_column='KU_TEMPLATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_contacts = models.CharField(db_column='KA_CONTACTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_status = models.IntegerField(db_column='KA_STATUS', blank=True, null=True)  # Field name made lowercase.
    ka_sales = models.CharField(db_column='KA_SALES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_ondate = models.CharField(db_column='KA_ONDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_offdate = models.CharField(db_column='KA_OFFDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_customer_number = models.IntegerField(db_column='KA_CUSTOMER_NUMBER', blank=True, null=True)  # Field name made lowercase.
    ka_mesage = models.CharField(db_column='KA_MESAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_jump_site = models.CharField(db_column='KA_JUMP_SITE', max_length=200)  # Field name made lowercase.
    ka_domain = models.CharField(db_column='KA_DOMAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oversea_binding_add = models.CharField(db_column='OVERSEA_BINDING_ADD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ka_zhxgip = models.CharField(db_column='KA_ZHXGIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ka_isfee = models.IntegerField(db_column='KA_ISFEE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENTS'


class WkTAgentuserGroup(models.Model):
    gid = models.IntegerField(db_column='GID')  # Field name made lowercase.
    uid = models.IntegerField(db_column='UID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENTUSER_GROUP'


class WkTAgentuserGroup1(models.Model):
    gid = models.IntegerField(db_column='GID')  # Field name made lowercase.
    uid = models.IntegerField(db_column='UID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENTUSER_GROUP_1'


class WkTAgentApp(models.Model):
    aid = models.IntegerField(db_column='AID')  # Field name made lowercase.
    agent_name = models.CharField(db_column='AGENT_NAME', max_length=255)  # Field name made lowercase.
    app_name = models.CharField(db_column='APP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    add_time = models.IntegerField(db_column='ADD_TIME')  # Field name made lowercase.
    last_time = models.IntegerField(db_column='LAST_TIME', blank=True, null=True)  # Field name made lowercase.
    app_key_qq = models.CharField(db_column='APP_KEY_QQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    app_id_qq = models.CharField(db_column='APP_ID_QQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    app_id_weixin = models.CharField(db_column='APP_ID_WEIXIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    app_secret_weixin = models.CharField(db_column='APP_SECRET_WEIXIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pic_info = models.TextField(db_column='PIC_INFO', blank=True, null=True)  # Field name made lowercase.
    app_platform = models.IntegerField(db_column='APP_PLATFORM', blank=True, null=True)  # Field name made lowercase.
    app_key_qq_android = models.CharField(db_column='APP_KEY_QQ_Android', max_length=255, blank=True, null=True)  # Field name made lowercase.
    app_id_qq_android = models.CharField(db_column='APP_ID_QQ_Android', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENT_APP'


class WkTAgentAppJoblog(models.Model):
    aid = models.IntegerField(db_column='AID')  # Field name made lowercase.
    time = models.IntegerField(db_column='TIME')  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    job_type = models.IntegerField(db_column='JOB_TYPE', blank=True, null=True)  # Field name made lowercase.
    job_id = models.IntegerField(db_column='JOB_ID')  # Field name made lowercase.
    time_cost = models.IntegerField(db_column='TIME_COST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENT_APP_JOBLOG'


class WkTAgentAppStatus(models.Model):
    aid = models.IntegerField(db_column='AID')  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    package_path = models.CharField(db_column='PACKAGE_PATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ios_version = models.CharField(db_column='IOS_VERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    android_version = models.CharField(db_column='ANDROID_VERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENT_APP_STATUS'


class WkTAgentGroup(models.Model):
    gid = models.AutoField(db_column='GID', primary_key=True)  # Field name made lowercase.
    aid = models.IntegerField(db_column='AID')  # Field name made lowercase.
    gname = models.CharField(db_column='GNAME', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENT_GROUP'


class WkTAgentGroup1(models.Model):
    gid = models.AutoField(db_column='GID', primary_key=True)  # Field name made lowercase.
    aid = models.IntegerField(db_column='AID')  # Field name made lowercase.
    gname = models.CharField(db_column='GNAME', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENT_GROUP_1'


class WkTAgentNew(models.Model):
    ka_id = models.CharField(db_column='KA_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ka_pid = models.CharField(db_column='KA_PID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_logo = models.CharField(db_column='KA_LOGO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_addr = models.CharField(db_column='KA_ADDR', max_length=400, blank=True, null=True)  # Field name made lowercase.
    ka_record = models.CharField(db_column='KA_RECORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_email = models.CharField(db_column='KA_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_phone = models.CharField(db_column='KA_PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_qq1 = models.CharField(db_column='KA_QQ1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_qq2 = models.CharField(db_column='KA_QQ2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_qq3 = models.CharField(db_column='KA_QQ3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_time = models.CharField(db_column='KA_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ka_site = models.CharField(db_column='KA_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_intro = models.TextField(db_column='KA_INTRO', blank=True, null=True)  # Field name made lowercase.
    ka_logo2 = models.CharField(db_column='KA_LOGO2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_ico = models.CharField(db_column='KA_ICO', max_length=40)  # Field name made lowercase.
    ka_open = models.CharField(db_column='KA_OPEN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ka_phone2 = models.CharField(db_column='KA_PHONE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_phone3 = models.CharField(db_column='KA_PHONE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_record1 = models.CharField(db_column='KA_RECORD1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_template = models.CharField(db_column='KU_TEMPLATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_contacts = models.CharField(db_column='KA_CONTACTS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_status = models.IntegerField(db_column='KA_STATUS', blank=True, null=True)  # Field name made lowercase.
    ka_sales = models.CharField(db_column='KA_SALES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_ondate = models.CharField(db_column='KA_ONDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_offdate = models.CharField(db_column='KA_OFFDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_customer_number = models.IntegerField(db_column='KA_CUSTOMER_NUMBER', blank=True, null=True)  # Field name made lowercase.
    ka_mesage = models.CharField(db_column='KA_MESAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AGENT_NEW'


class WkTAllexport(models.Model):
    ka_id = models.CharField(db_column='KA_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ka_where = models.TextField(db_column='KA_WHERE', blank=True, null=True)  # Field name made lowercase.
    ka_status = models.CharField(db_column='KA_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ka_filename = models.CharField(db_column='KA_FILENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ka_createtime = models.CharField(db_column='KA_CREATETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ka_endtime = models.CharField(db_column='KA_ENDTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ka_filetype = models.CharField(db_column='KA_FILETYPE', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ALLEXPORT'


class WkTAnnualReport(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    foreigninvestmentinfo = models.TextField(db_column='ForeignInvestmentInfo', blank=True, null=True)  # Field name made lowercase.
    enterpriseassetstatusinfo = models.TextField(db_column='EnterpriseAssetStatusInfo', blank=True, null=True)  # Field name made lowercase.
    stockholderandinvestmentinfo = models.TextField(db_column='StockholderAndInvestmentInfo', blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    buyotherequity = models.CharField(db_column='BuyOtherEquity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unifiedsocialcreditcode = models.CharField(db_column='UnifiedSocialCreditCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    websiteoronlinestore = models.CharField(db_column='WebsiteOrOnlineStore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enterprisemanagementstatus = models.CharField(db_column='EnterpriseManagementStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    membernumber = models.CharField(db_column='MemberNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stockholderequitytransfer = models.CharField(db_column='StockholderEquityTransfer', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ANNUAL_REPORT'


class WkTAppedition(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_uuid = models.CharField(db_column='KA_UUID', max_length=50)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_APPEDITION'


class WkTAppeditionZj(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_uuid = models.CharField(db_column='KA_UUID', max_length=50)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_APPEDITION_ZJ'


class WkTApply(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_email = models.CharField(db_column='KA_EMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_qq = models.CharField(db_column='KA_QQ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_mobile = models.CharField(db_column='KA_MOBILE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_company = models.CharField(db_column='KA_COMPANY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_phone = models.CharField(db_column='KA_PHONE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_message = models.CharField(db_column='KA_MESSAGE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ka_issee = models.CharField(db_column='KA_ISSEE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ka_opinion = models.CharField(db_column='KA_OPINION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_time = models.CharField(db_column='KA_TIME', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ka_seetime = models.CharField(db_column='KA_SEETIME', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ka_kuid = models.IntegerField(db_column='KA_KUID', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_APPLY'


class WkTApptvedition(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_uuid = models.CharField(db_column='KA_UUID', max_length=50)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_APPTVEDITION'


class WkTAppSite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    site_name = models.CharField(db_column='SITE_NAME', max_length=50)  # Field name made lowercase.
    site_url = models.CharField(db_column='SITE_URL', max_length=200)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_APP_SITE'


class WkTArea(models.Model):
    ka_id = models.IntegerField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_pid = models.IntegerField(db_column='KA_PID')  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ka_desc = models.CharField(db_column='KA_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_order = models.IntegerField(db_column='KA_ORDER', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AREA'


class WkTAreaKeyws(models.Model):
    kk_id = models.IntegerField(db_column='KK_ID', primary_key=True)  # Field name made lowercase.
    ka_id = models.IntegerField(db_column='KA_ID')  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kk_relation = models.CharField(db_column='KK_RELATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_not = models.CharField(db_column='KK_NOT', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kk_keywords = models.CharField(db_column='KK_KEYWORDS', max_length=800, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AREA_KEYWS'


class WkTAutopack(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=30)  # Field name made lowercase.
    ka_path = models.CharField(db_column='KA_PATH', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AUTOPACK'


class WkTAutopackDls(models.Model):
    ka_id = models.AutoField(db_column='KA_ID', primary_key=True)  # Field name made lowercase.
    ka_name = models.CharField(db_column='KA_NAME', max_length=50)  # Field name made lowercase.
    ka_pica = models.TextField(db_column='KA_PICA')  # Field name made lowercase.
    ka_picb = models.TextField(db_column='KA_PICB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_AUTOPACK_DLS'


class WkTBackendframe(models.Model):
    name = models.CharField(max_length=60)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_BACKENDFRAME'


class WkTBackendrole(models.Model):
    name = models.CharField(max_length=60)
    kr_auth = models.IntegerField(db_column='KR_AUTH', blank=True, null=True)  # Field name made lowercase.
    bvroid = models.CharField(max_length=60, blank=True, null=True)
    vroid = models.CharField(max_length=60, blank=True, null=True)
    roletype = models.IntegerField(db_column='roleType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_BACKENDROLE'


class WkTBackendBlock(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    existlist = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_BACKEND_BLOCK'


class WkTBackendRef(models.Model):
    fid = models.IntegerField()
    rid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_BACKEND_REF'


class WkTBackendRm(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_BACKEND_RM'


class WkTBar(models.Model):
    kb_id = models.AutoField(db_column='KB_ID', primary_key=True)  # Field name made lowercase.
    kb_name = models.CharField(db_column='KB_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kb_class = models.CharField(db_column='KB_CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kb_method = models.CharField(db_column='KB_METHOD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_BAR'


class WkTBarnew(models.Model):
    kb_id = models.AutoField(db_column='KB_ID', primary_key=True)  # Field name made lowercase.
    kb_name = models.CharField(db_column='KB_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kb_class = models.CharField(db_column='KB_CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kb_method = models.CharField(db_column='KB_METHOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kb_order = models.IntegerField(db_column='KB_ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_BARNEW'


class WkTBasekeytype(models.Model):
    kb_id = models.IntegerField(db_column='KB_ID', primary_key=True)  # Field name made lowercase.
    kb_pid = models.IntegerField(db_column='KB_PID', blank=True, null=True)  # Field name made lowercase.
    kb_name = models.CharField(db_column='KB_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kb_desc = models.CharField(db_column='KB_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kb_order = models.CharField(db_column='KB_ORDER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_BASEKEYTYPE'


class WkTBasekeyws(models.Model):
    kk_id = models.IntegerField(db_column='KK_ID', primary_key=True)  # Field name made lowercase.
    kb_id = models.IntegerField(db_column='KB_ID', blank=True, null=True)  # Field name made lowercase.
    kb_name = models.CharField(db_column='KB_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_BASEKEYWS'


class WkTBelongkefuNew(models.Model):
    gid = models.IntegerField()
    kefu_id = models.IntegerField()
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_BELONGKEFU_NEW'


class WkTChannelTv(models.Model):
    kc_id = models.AutoField(db_column='KC_ID', primary_key=True)  # Field name made lowercase.
    kc_pid = models.IntegerField(db_column='KC_PID')  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=200)  # Field name made lowercase.
    kc_time = models.CharField(db_column='KC_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CHANNEL_TV'


class WkTChannelUser(models.Model):
    kh_id = models.AutoField(db_column='KH_ID', primary_key=True)  # Field name made lowercase.
    kc_id = models.IntegerField(db_column='KC_ID')  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CHANNEL_USER'


class WkTChart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45)  # Field name made lowercase.
    chart_type = models.IntegerField(db_column='CHART_TYPE', blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(db_column='X', max_length=45)  # Field name made lowercase.
    y = models.CharField(db_column='Y', max_length=45)  # Field name made lowercase.
    order_by = models.CharField(db_column='ORDER_BY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    limit = models.CharField(db_column='LIMIT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ctime = models.DateTimeField(db_column='CTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CHART'


class WkTClassification(models.Model):
    kc_id = models.AutoField(db_column='KC_ID', primary_key=True)  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=50)  # Field name made lowercase.
    kc_pid = models.IntegerField(db_column='KC_PID')  # Field name made lowercase.
    kc_lableid = models.IntegerField(db_column='KC_LABLEID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CLASSIFICATION'


class WkTCommonKeyws(models.Model):
    kc_id = models.IntegerField(db_column='KC_ID', primary_key=True)  # Field name made lowercase.
    kc_type = models.CharField(db_column='KC_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_must = models.CharField(db_column='KC_MUST', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kc_should = models.CharField(db_column='KC_SHOULD', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kc_event = models.CharField(db_column='KC_EVENT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kc_not = models.CharField(db_column='KC_NOT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_COMMON_KEYWS'


class WkTCompanyChangeinfo(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    date = models.CharField(db_column='Date', max_length=500, blank=True, null=True)  # Field name made lowercase.
    contentafter = models.CharField(db_column='ContentAfter', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    contentbefore = models.CharField(db_column='ContentBefore', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_COMPANY_CHANGEINFO'


class WkTCompanyUser(models.Model):
    companyid = models.IntegerField(db_column='COMPANYID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_COMPANY_USER'
        unique_together = (('companyid', 'userid'),)


class WkTCourtannouncement(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    bltntypename = models.CharField(db_column='BltnTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    courtname = models.CharField(db_column='CourtName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dealgradename = models.CharField(db_column='DealGradeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    judgename = models.CharField(db_column='JudgeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    judgephonenumber = models.CharField(db_column='JudgePhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    receive = models.CharField(db_column='Receive', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parties = models.TextField(db_column='Parties', blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='PublishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_COURTANNOUNCEMENT'


class WkTCustomCondition(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=65)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    search_type = models.IntegerField(db_column='SEARCH_TYPE', blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='FIELD', max_length=45)  # Field name made lowercase.
    ctime = models.DateTimeField(db_column='CTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CUSTOM_CONDITION'


class WkTCustomConditionField(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=65)  # Field name made lowercase.
    field = models.CharField(db_column='FIELD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    topicfield = models.CharField(db_column='TOPICFIELD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    solrfield = models.CharField(db_column='SOLRFIELD', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CUSTOM_CONDITION_FIELD'


class WkTCustomConditionSub(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=65)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', max_length=65)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ctime = models.DateTimeField(db_column='CTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CUSTOM_CONDITION_SUB'


class WkTCustomConditionValue(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=65)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=65)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctime = models.DateTimeField(db_column='CTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_CUSTOM_CONDITION_VALUE'


class WkTDatasourcetype(models.Model):
    kd_id = models.AutoField(db_column='KD_ID', primary_key=True)  # Field name made lowercase.
    kk_datasourcetype = models.CharField(db_column='KK_DATASOURCETYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DATASOURCETYPE'


class WkTDefinedhomeExtend(models.Model):
    kd_id = models.AutoField(db_column='KD_ID', primary_key=True)  # Field name made lowercase.
    kd_type = models.CharField(db_column='KD_TYPE', max_length=40)  # Field name made lowercase.
    kd_value = models.TextField(db_column='KD_VALUE', blank=True, null=True)  # Field name made lowercase.
    kd_datatype = models.IntegerField(db_column='KD_DATATYPE')  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_pid = models.IntegerField(db_column='KU_PID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DEFINEDHOME_EXTEND'


class WkTDelete(models.Model):
    kd_uuid = models.CharField(db_column='KD_UUID', primary_key=True, max_length=32)  # Field name made lowercase.
    kd_tablename = models.CharField(db_column='KD_TABLENAME', max_length=30)  # Field name made lowercase.
    kd_column_delete = models.CharField(db_column='KD_COLUMN_DELETE', max_length=32)  # Field name made lowercase.
    kd_column_delete_value = models.CharField(db_column='KD_COLUMN_DELETE_VALUE', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DELETE'


class WkTDeleteinfoLog(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kl_type = models.CharField(db_column='KL_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kl_rubbish = models.CharField(db_column='KL_RUBBISH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_classify = models.CharField(db_column='KL_CLASSIFY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DELETEINFO_LOG'


class WkTDeleteinfoLog1(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kl_type = models.CharField(db_column='KL_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_user = models.CharField(db_column='KL_USER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=350, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kl_rubbish = models.CharField(db_column='KL_RUBBISH', max_length=2)  # Field name made lowercase.
    kl_classify = models.CharField(db_column='KL_CLASSIFY', max_length=2)  # Field name made lowercase.
    kl_return = models.CharField(db_column='KL_RETURN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_caled = models.CharField(db_column='KL_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DELETEINFO_LOG1'


class WkTDeleteinfoLog2(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kl_type = models.CharField(db_column='KL_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_user = models.CharField(db_column='KL_USER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=350, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kl_rubbish = models.CharField(db_column='KL_RUBBISH', max_length=2)  # Field name made lowercase.
    kl_classify = models.CharField(db_column='KL_CLASSIFY', max_length=2)  # Field name made lowercase.
    kl_return = models.CharField(db_column='KL_RETURN', max_length=2)  # Field name made lowercase.
    kl_caled = models.CharField(db_column='KL_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DELETEINFO_LOG2'


class WkTDeleteinfoSource(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kl_user = models.CharField(db_column='KL_USER', max_length=50)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=20)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=50)  # Field name made lowercase.
    ks_channel = models.CharField(db_column='KS_CHANNEL', max_length=50)  # Field name made lowercase.
    ks_author = models.CharField(db_column='KS_AUTHOR', max_length=50)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DELETEINFO_SOURCE'


class WkTDeleterefReason(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40)  # Field name made lowercase.
    reason = models.TextField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.
    delete_time = models.DateTimeField(db_column='DELETE_TIME')  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DELETEREF_REASON'


class WkTDept(models.Model):
    kd_id = models.IntegerField(db_column='KD_ID', primary_key=True)  # Field name made lowercase.
    kd_pid = models.IntegerField(db_column='KD_PID')  # Field name made lowercase.
    kd_name = models.CharField(db_column='KD_NAME', max_length=40)  # Field name made lowercase.
    kd_desc = models.CharField(db_column='KD_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kd_order = models.IntegerField(db_column='KD_ORDER', blank=True, null=True)  # Field name made lowercase.
    kd_type = models.CharField(db_column='KD_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DEPT'


class WkTDingdinggroup(models.Model):
    name = models.CharField(max_length=50)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_DINGDINGGROUP'


class WkTDinggroup(models.Model):
    did = models.IntegerField(db_column='Did')  # Field name made lowercase.
    dpid = models.IntegerField(db_column='Dpid')  # Field name made lowercase.
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'WK_T_DINGGROUP'


class WkTDinggroupCopy(models.Model):
    did = models.IntegerField(db_column='Did')  # Field name made lowercase.
    dpid = models.IntegerField(db_column='Dpid')  # Field name made lowercase.
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'WK_T_DINGGROUP_copy'


class WkTDinguser(models.Model):
    uname = models.CharField(max_length=255)
    gid = models.IntegerField()
    dtalkid = models.CharField(db_column='Dtalkid', max_length=255)  # Field name made lowercase.
    passwd = models.CharField(max_length=32)
    position = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'WK_T_DINGUSER'


class WkTDinguserJob(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'WK_T_DINGUSER_JOB'


class WkTDinguserNew(models.Model):
    uname = models.CharField(max_length=255)
    gid = models.IntegerField(blank=True, null=True)
    dtalkid = models.CharField(db_column='Dtalkid', max_length=50)  # Field name made lowercase.
    passwd = models.CharField(max_length=32)
    frame = models.IntegerField(blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dingframe = models.CharField(max_length=255, blank=True, null=True)
    job = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_DINGUSER_new'


class WkTDinguserNewCopy(models.Model):
    uname = models.CharField(max_length=255)
    gid = models.IntegerField(blank=True, null=True)
    dtalkid = models.CharField(db_column='Dtalkid', max_length=50)  # Field name made lowercase.
    passwd = models.CharField(max_length=32)
    frame = models.IntegerField(blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dingframe = models.CharField(max_length=255, blank=True, null=True)
    job = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_DINGUSER_new_copy'


class WkTDinguserNewCopy1(models.Model):
    uname = models.CharField(max_length=255)
    gid = models.IntegerField(blank=True, null=True)
    dtalkid = models.CharField(db_column='Dtalkid', max_length=50)  # Field name made lowercase.
    passwd = models.CharField(max_length=32)
    frame = models.IntegerField(blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dingframe = models.CharField(max_length=255, blank=True, null=True)
    job = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_DINGUSER_new_copy1'


class WkTDishonest(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    partycardnum = models.CharField(db_column='PartyCardNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businessentityname = models.CharField(db_column='BusinessEntityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    courtname = models.CharField(db_column='CourtName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gistid = models.CharField(db_column='GistId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    casecode = models.CharField(db_column='CaseCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gistunit = models.CharField(db_column='GistUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duty = models.CharField(db_column='Duty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    performance = models.CharField(db_column='Performance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disrupttypename = models.CharField(db_column='DisruptTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='PublishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_DISHONEST'


class WkTEnforcement(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    partycardnum = models.CharField(db_column='PartyCardNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    execcourtname = models.CharField(db_column='ExecCourtName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    casecreatetime = models.CharField(db_column='CaseCreateTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    casecode = models.CharField(db_column='CaseCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    execmoney = models.CharField(db_column='ExecMoney', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ENFORCEMENT'


class WkTEverydaydata(models.Model):
    kv_id = models.CharField(db_column='KV_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_type = models.CharField(db_column='KV_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_addtime = models.CharField(db_column='KV_ADDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_lostcaltime = models.CharField(db_column='KV_LOSTCALTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kv_total = models.IntegerField(db_column='KV_TOTAL', blank=True, null=True)  # Field name made lowercase.
    kv_weibo = models.IntegerField(db_column='KV_WEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_news = models.IntegerField(db_column='KV_NEWS', blank=True, null=True)  # Field name made lowercase.
    kv_forum = models.IntegerField(db_column='KV_FORUM', blank=True, null=True)  # Field name made lowercase.
    kv_blogs = models.IntegerField(db_column='KV_BLOGS', blank=True, null=True)  # Field name made lowercase.
    kv_papers = models.IntegerField(db_column='KV_PAPERS', blank=True, null=True)  # Field name made lowercase.
    kv_weixin = models.IntegerField(db_column='KV_WEIXIN', blank=True, null=True)  # Field name made lowercase.
    kv_video = models.IntegerField(db_column='KV_VIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_other = models.IntegerField(db_column='KV_OTHER', blank=True, null=True)  # Field name made lowercase.
    kv_rd = models.IntegerField(db_column='KV_RD', blank=True, null=True)  # Field name made lowercase.
    kv_abroad = models.IntegerField(db_column='KV_ABROAD', blank=True, null=True)  # Field name made lowercase.
    kv_zdweiboweb = models.CharField(db_column='KV_ZDWEIBOWEB', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_zdaera = models.CharField(db_column='KV_ZDAERA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_zdauthor = models.CharField(db_column='KV_ZDAUTHOR', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_zdwebname = models.CharField(db_column='KV_ZDWEBNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_fmtotal = models.IntegerField(db_column='KV_FMTOTAL', blank=True, null=True)  # Field name made lowercase.
    kv_fmnews = models.IntegerField(db_column='KV_FMNEWS', blank=True, null=True)  # Field name made lowercase.
    kv_fmforum = models.IntegerField(db_column='KV_FMFORUM', blank=True, null=True)  # Field name made lowercase.
    kv_fmblogs = models.IntegerField(db_column='KV_FMBLOGS', blank=True, null=True)  # Field name made lowercase.
    kv_fmpapers = models.IntegerField(db_column='KV_FMPAPERS', blank=True, null=True)  # Field name made lowercase.
    kv_fmweibo = models.IntegerField(db_column='KV_FMWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_fmweixin = models.IntegerField(db_column='KV_FMWEIXIN', blank=True, null=True)  # Field name made lowercase.
    kv_fmvideo = models.IntegerField(db_column='KV_FMVIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_fmother = models.IntegerField(db_column='KV_FMOTHER', blank=True, null=True)  # Field name made lowercase.
    kv_fmwebname = models.CharField(db_column='KV_FMWEBNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_fmabroad = models.IntegerField(db_column='KV_FMABROAD', blank=True, null=True)  # Field name made lowercase.
    kv_fmauthor = models.CharField(db_column='KV_FMAUTHOR', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_fmzdwebname = models.CharField(db_column='KV_FMZDWEBNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_zmtotal = models.IntegerField(db_column='KV_ZMTOTAL', blank=True, null=True)  # Field name made lowercase.
    kv_zmweibo = models.IntegerField(db_column='KV_ZMWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_zmweb = models.IntegerField(db_column='KV_ZMWEB', blank=True, null=True)  # Field name made lowercase.
    kv_zmnews = models.IntegerField(db_column='KV_ZMNEWS', blank=True, null=True)  # Field name made lowercase.
    kv_zmforum = models.IntegerField(db_column='KV_ZMFORUM', blank=True, null=True)  # Field name made lowercase.
    kv_zmblogs = models.IntegerField(db_column='KV_ZMBLOGS', blank=True, null=True)  # Field name made lowercase.
    kv_zmpapers = models.IntegerField(db_column='KV_ZMPAPERS', blank=True, null=True)  # Field name made lowercase.
    kv_zmweixin = models.IntegerField(db_column='KV_ZMWEIXIN', blank=True, null=True)  # Field name made lowercase.
    kv_zmvideo = models.IntegerField(db_column='KV_ZMVIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_zmother = models.IntegerField(db_column='KV_ZMOTHER', blank=True, null=True)  # Field name made lowercase.
    kv_zmwebname = models.CharField(db_column='KV_ZMWEBNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_zxtotal = models.IntegerField(db_column='KV_ZXTOTAL', blank=True, null=True)  # Field name made lowercase.
    kv_zxnews = models.IntegerField(db_column='KV_ZXNEWS', blank=True, null=True)  # Field name made lowercase.
    kv_zxforum = models.IntegerField(db_column='KV_ZXFORUM', blank=True, null=True)  # Field name made lowercase.
    kv_zxblogs = models.IntegerField(db_column='KV_ZXBLOGS', blank=True, null=True)  # Field name made lowercase.
    kv_zxpapers = models.IntegerField(db_column='KV_ZXPAPERS', blank=True, null=True)  # Field name made lowercase.
    kv_zxweibo = models.IntegerField(db_column='KV_ZXWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_zxweixin = models.IntegerField(db_column='KV_ZXWEIXIN', blank=True, null=True)  # Field name made lowercase.
    kv_zxvideo = models.IntegerField(db_column='KV_ZXVIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_zxother = models.IntegerField(db_column='KV_ZXOTHER', blank=True, null=True)  # Field name made lowercase.
    kv_zxwebname = models.CharField(db_column='KV_ZXWEBNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_zytotal = models.IntegerField(db_column='KV_ZYTOTAL', blank=True, null=True)  # Field name made lowercase.
    kv_zynews = models.IntegerField(db_column='KV_ZYNEWS', blank=True, null=True)  # Field name made lowercase.
    kv_zyforum = models.IntegerField(db_column='KV_ZYFORUM', blank=True, null=True)  # Field name made lowercase.
    kv_zyblogs = models.IntegerField(db_column='KV_ZYBLOGS', blank=True, null=True)  # Field name made lowercase.
    kv_zypapers = models.IntegerField(db_column='KV_ZYPAPERS', blank=True, null=True)  # Field name made lowercase.
    kv_zyweibo = models.IntegerField(db_column='KV_ZYWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_zyweixin = models.IntegerField(db_column='KV_ZYWEIXIN', blank=True, null=True)  # Field name made lowercase.
    kv_zyvideo = models.IntegerField(db_column='KV_ZYVIDEO', blank=True, null=True)  # Field name made lowercase.
    kv_zyother = models.IntegerField(db_column='KV_ZYOTHER', blank=True, null=True)  # Field name made lowercase.
    kv_zywebname = models.CharField(db_column='KV_ZYWEBNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kv_app = models.IntegerField(db_column='KV_APP', blank=True, null=True)  # Field name made lowercase.
    kv_zmapp = models.IntegerField(db_column='KV_ZMAPP', blank=True, null=True)  # Field name made lowercase.
    kv_fmapp = models.IntegerField(db_column='KV_FMAPP', blank=True, null=True)  # Field name made lowercase.
    kv_zxapp = models.IntegerField(db_column='KV_ZXAPP', blank=True, null=True)  # Field name made lowercase.
    kv_zyapp = models.IntegerField(db_column='KV_ZYAPP', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_zmreply = models.IntegerField(db_column='KV_ZMREPLY', blank=True, null=True)  # Field name made lowercase.
    kv_fmreply = models.IntegerField(db_column='KV_FMREPLY', blank=True, null=True)  # Field name made lowercase.
    kv_zxreply = models.IntegerField(db_column='KV_ZXREPLY', blank=True, null=True)  # Field name made lowercase.
    kv_zyreply = models.IntegerField(db_column='KV_ZYREPLY', blank=True, null=True)  # Field name made lowercase.
    kv_cweibo = models.IntegerField(db_column='KV_CWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_zmcweibo = models.IntegerField(db_column='KV_ZMCWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_fmcweibo = models.IntegerField(db_column='KV_FMCWEIBO', blank=True, null=True)  # Field name made lowercase.
    kv_zxcweibo = models.IntegerField(db_column='KV_ZXCWEIBO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_EVERYDAYDATA'


class WkTExamine(models.Model):
    ku_eid = models.AutoField(db_column='KU_EID', primary_key=True)  # Field name made lowercase.
    dtalkid = models.CharField(db_column='Dtalkid', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_EXAMINE'


class WkTExamineTrysdate(models.Model):
    ku_eid = models.AutoField(db_column='KU_EID', primary_key=True)  # Field name made lowercase.
    dtalkid = models.CharField(db_column='Dtalkid', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_EXAMINE_TRYSDATE'


class WkTFullsearchCatalog(models.Model):
    kc_id = models.AutoField(db_column='KC_ID', primary_key=True)  # Field name made lowercase.
    kc_pid = models.IntegerField(db_column='KC_PID')  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=256)  # Field name made lowercase.
    kc_searchword = models.CharField(db_column='KC_SEARCHWORD', max_length=256, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kc_create_time = models.DateTimeField(db_column='KC_CREATE_TIME')  # Field name made lowercase.
    kc_modify_time = models.DateTimeField(db_column='KC_MODIFY_TIME')  # Field name made lowercase.
    kc_order = models.IntegerField(db_column='KC_ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_FULLSEARCH_CATALOG'


class WkTHelp(models.Model):
    kh_id = models.AutoField(db_column='KH_ID', primary_key=True)  # Field name made lowercase.
    kc_id = models.IntegerField(db_column='KC_ID')  # Field name made lowercase.
    kh_question = models.TextField(db_column='KH_QUESTION')  # Field name made lowercase.
    kh_answer = models.TextField(db_column='KH_ANSWER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HELP'


class WkTHelpClass(models.Model):
    kc_id = models.AutoField(db_column='KC_ID', primary_key=True)  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=50)  # Field name made lowercase.
    kc_pic = models.CharField(db_column='KC_PIC', max_length=100)  # Field name made lowercase.
    kc_order = models.IntegerField(db_column='KC_ORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HELP_CLASS'


class WkTHljCourtUser(models.Model):
    c_id = models.CharField(db_column='C_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kt_uuid = models.CharField(db_column='KT_UUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_gs = models.CharField(db_column='C_GS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c_bm = models.CharField(db_column='C_BM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_zw = models.CharField(db_column='C_ZW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_keyword = models.CharField(db_column='C_KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_updatetime = models.CharField(db_column='C_UPDATETIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_topicname = models.CharField(db_column='C_TOPICNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HLJ_COURT_USER'


class WkTHomekeysset(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    kk_words = models.TextField(db_column='KK_WORDS')  # Field name made lowercase.
    kk_url = models.TextField(db_column='KK_URL')  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40)  # Field name made lowercase.
    kk_site = models.TextField(db_column='KK_SITE')  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HOMEKEYSSET'


class WkTHomepage(models.Model):
    kh_id = models.CharField(db_column='KH_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    kh_title = models.CharField(db_column='KH_TITLE', max_length=300)  # Field name made lowercase.
    kh_site = models.CharField(db_column='KH_SITE', max_length=50)  # Field name made lowercase.
    kh_url = models.CharField(db_column='KH_URL', max_length=200)  # Field name made lowercase.
    kh_author = models.CharField(db_column='KH_AUTHOR', max_length=25)  # Field name made lowercase.
    kh_cnt = models.TextField(db_column='KH_CNT', blank=True, null=True)  # Field name made lowercase.
    kh_orientation = models.IntegerField(db_column='KH_ORIENTATION')  # Field name made lowercase.
    kh_high = models.IntegerField(db_column='KH_HIGH')  # Field name made lowercase.
    kh_btime = models.CharField(db_column='KH_BTIME', max_length=25)  # Field name made lowercase.
    kh_etime = models.CharField(db_column='KH_ETIME', max_length=25)  # Field name made lowercase.
    kh_time = models.CharField(db_column='KH_TIME', max_length=25)  # Field name made lowercase.
    kh_word = models.CharField(db_column='KH_WORD', max_length=100)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=50)  # Field name made lowercase.
    kh_isdel = models.IntegerField(db_column='KH_ISDEL')  # Field name made lowercase.
    kh_isshudi = models.IntegerField(db_column='KH_ISSHUDI')  # Field name made lowercase.
    kh_deltime = models.CharField(db_column='KH_DELTIME', max_length=25)  # Field name made lowercase.
    kh_lasttime = models.CharField(db_column='KH_LASTTIME', max_length=25)  # Field name made lowercase.
    ku_deluser = models.CharField(db_column='KU_DELUSER', max_length=30)  # Field name made lowercase.
    kh_mainurl = models.CharField(db_column='KH_MAINURL', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HOMEPAGE'


class WkTHomesite(models.Model):
    ks_id = models.CharField(db_column='KS_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ks_site = models.CharField(db_column='KS_SITE', max_length=50)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=100)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=5)  # Field name made lowercase.
    ks_isshudi = models.IntegerField(db_column='KS_ISSHUDI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HOMESITE'


class WkTHotinfo(models.Model):
    ki_id = models.AutoField(db_column='KI_ID', primary_key=True)  # Field name made lowercase.
    ki_title = models.CharField(db_column='KI_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_title2 = models.CharField(db_column='KI_TITLE2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_source = models.CharField(db_column='KI_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ki_ordno = models.IntegerField(db_column='KI_ORDNO', blank=True, null=True)  # Field name made lowercase.
    ki_image = models.CharField(db_column='KI_IMAGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ki_type = models.CharField(db_column='KI_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_top = models.IntegerField(db_column='KI_TOP', blank=True, null=True)  # Field name made lowercase.
    ki_address = models.CharField(db_column='KI_ADDRESS', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_hits = models.IntegerField(db_column='KI_HITS', blank=True, null=True)  # Field name made lowercase.
    ki_ctime = models.CharField(db_column='KI_CTIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ki_keys = models.CharField(db_column='KI_KEYS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ki_memo = models.CharField(db_column='KI_MEMO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ki_validdate = models.CharField(db_column='KI_VALIDDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ki_show = models.CharField(db_column='KI_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_content = models.TextField(db_column='KI_CONTENT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    orientation = models.CharField(db_column='ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    simhash = models.TextField(db_column='SIMHASH', blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    classlyone = models.CharField(db_column='CLASSLYONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    classlytwo = models.CharField(db_column='CLASSLYTWO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eventone = models.CharField(db_column='EVENTONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eventtwo = models.CharField(db_column='EVENTTWO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_procince = models.CharField(db_column='KV_PROCINCE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_city = models.CharField(db_column='KV_CITY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_county = models.CharField(db_column='KV_COUNTY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_comm = models.TextField(db_column='KV_COMM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HOTINFO'


class WkTHotinfo2(models.Model):
    ki_id = models.AutoField(db_column='KI_ID', primary_key=True)  # Field name made lowercase.
    ki_title = models.CharField(db_column='KI_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_title2 = models.CharField(db_column='KI_TITLE2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_source = models.CharField(db_column='KI_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ki_ordno = models.IntegerField(db_column='KI_ORDNO', blank=True, null=True)  # Field name made lowercase.
    ki_image = models.CharField(db_column='KI_IMAGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ki_type = models.CharField(db_column='KI_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_top = models.CharField(db_column='KI_TOP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_address = models.CharField(db_column='KI_ADDRESS', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_hits = models.IntegerField(db_column='KI_HITS', blank=True, null=True)  # Field name made lowercase.
    ki_ctime = models.CharField(db_column='KI_CTIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ki_keys = models.CharField(db_column='KI_KEYS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ki_memo = models.CharField(db_column='KI_MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ki_validdate = models.CharField(db_column='KI_VALIDDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ki_show = models.CharField(db_column='KI_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_content = models.TextField(db_column='KI_CONTENT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_HOTINFO2'


class WkTId(models.Model):
    kid_key = models.CharField(db_column='KID_KEY', primary_key=True, max_length=15)  # Field name made lowercase.
    kid_value = models.IntegerField(db_column='KID_VALUE')  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ID'


class WkTIndexModule(models.Model):
    km_id = models.AutoField(db_column='KM_ID', primary_key=True)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_isold = models.IntegerField(db_column='KM_ISOLD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_INDEX_MODULE'


class WkTIndustry(models.Model):
    ki_id = models.IntegerField(db_column='KI_ID', primary_key=True)  # Field name made lowercase.
    ki_pid = models.IntegerField(db_column='KI_PID')  # Field name made lowercase.
    ki_name = models.CharField(db_column='KI_NAME', max_length=200)  # Field name made lowercase.
    ki_desc = models.CharField(db_column='KI_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_order = models.IntegerField(db_column='KI_ORDER', blank=True, null=True)  # Field name made lowercase.
    ki_userlevel = models.CharField(db_column='KI_USERLEVEL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_INDUSTRY'


class WkTIndKeyws(models.Model):
    kk_id = models.IntegerField(db_column='KK_ID', primary_key=True)  # Field name made lowercase.
    ki_id = models.IntegerField(db_column='KI_ID', blank=True, null=True)  # Field name made lowercase.
    ki_name = models.CharField(db_column='KI_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    kk_relation = models.CharField(db_column='KK_RELATION', max_length=2)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_keywords = models.TextField(db_column='KK_KEYWORDS', blank=True, null=True)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_IND_KEYWS'


class WkTInfo(models.Model):
    ki_id = models.AutoField(db_column='KI_ID', primary_key=True)  # Field name made lowercase.
    ki_title = models.CharField(db_column='KI_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_title2 = models.CharField(db_column='KI_TITLE2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ki_source = models.CharField(db_column='KI_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ki_ordno = models.IntegerField(db_column='KI_ORDNO', blank=True, null=True)  # Field name made lowercase.
    ki_image = models.CharField(db_column='KI_IMAGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ki_type = models.CharField(db_column='KI_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_top = models.CharField(db_column='KI_TOP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ki_address = models.CharField(db_column='KI_ADDRESS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ki_hits = models.IntegerField(db_column='KI_HITS', blank=True, null=True)  # Field name made lowercase.
    ki_ctime = models.CharField(db_column='KI_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ki_keys = models.CharField(db_column='KI_KEYS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ki_memo = models.CharField(db_column='KI_MEMO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ki_validdate = models.CharField(db_column='KI_VALIDDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ki_show = models.CharField(db_column='KI_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_INFO'


class WkTInfoSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=30)
    create_time = models.DateTimeField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_INFO_SOURCE'


class WkTIpinfo(models.Model):
    kpid = models.AutoField(primary_key=True)
    kpip = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    isp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_IPINFO'


class WkTJobOffers(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalurl = models.CharField(db_column='OriginalUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    worknature = models.CharField(db_column='WorkNature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='PublishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mindegrees = models.CharField(db_column='MinDegrees', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workexperience = models.CharField(db_column='WorkExperience', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numberofrequire = models.CharField(db_column='NumberOfRequire', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companydescription = models.TextField(db_column='CompanyDescription', blank=True, null=True)  # Field name made lowercase.
    jobdescription = models.TextField(db_column='JobDescription', blank=True, null=True)  # Field name made lowercase.
    salaryrange = models.CharField(db_column='SalaryRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workplace = models.CharField(db_column='WorkPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_JOB_OFFERS'


class WkTJudgment(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    ctime = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    sitename = models.CharField(db_column='siteName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    gtime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_JUDGMENT'


class WkTJudicialsale(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    courtname = models.CharField(db_column='CourtName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='PublishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referenceprice = models.CharField(db_column='ReferencePrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacts = models.CharField(db_column='Contacts', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_JUDICIALSALE'


class WkTKefupowerNew(models.Model):
    name = models.CharField(max_length=255)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_KEFUPOWER_NEW'


class WkTKeyws(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_createtime = models.CharField(db_column='KK_CREATETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_modifytime = models.CharField(db_column='KK_MODIFYTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_savedays = models.IntegerField(db_column='KK_SAVEDAYS', blank=True, null=True)  # Field name made lowercase.
    kk_noyj = models.CharField(db_column='KK_NOYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_allowsourcetype = models.CharField(db_column='KK_ALLOWSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_allowyjsourcetype = models.CharField(db_column='KK_ALLOWYJSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_datasourcetype = models.CharField(db_column='KK_DATASOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    ku_weibotime = models.CharField(db_column='KU_WEIBOTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust = models.CharField(db_column='KU_WORDMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance = models.CharField(db_column='KU_WORDDISTANCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust_length = models.CharField(db_column='KU_WORDMUST_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance_length = models.CharField(db_column='KU_WORDDISTANCE_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_matchtitle = models.CharField(db_column='KU_MATCHTITLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_onlgmust = models.CharField(db_column='KU_ONLGMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong = models.CharField(db_column='KK_TUISONG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sendtime = models.CharField(db_column='KK_SENDTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_sourcetype = models.CharField(db_column='KK_TUISONG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_orientation = models.CharField(db_column='KK_TUISONG_ORIENTATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_state = models.CharField(db_column='KK_TUISONG_STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_haverepeat = models.CharField(db_column='KK_TUISONG_HAVEREPEAT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_btime = models.CharField(db_column='KK_TUISONG_BTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_etime = models.CharField(db_column='KK_TUISONG_ETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_search = models.TextField(db_column='KK_TUISONG_SEARCH', blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_not = models.TextField(db_column='KK_TUISONG_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_sourcetype = models.CharField(db_column='KK_DINGXIANG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_domain = models.TextField(db_column='KK_DINGXIANG_DOMAIN', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_channel = models.TextField(db_column='KK_DINGXIANG_CHANNEL', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_account = models.TextField(db_column='KK_DINGXIANG_ACCOUNT', blank=True, null=True)  # Field name made lowercase.
    kk_label = models.TextField(db_column='KK_LABEL')  # Field name made lowercase.
    kk_ishigh = models.IntegerField(db_column='KK_ISHIGH')  # Field name made lowercase.
    kk_arg1 = models.CharField(db_column='KK_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg2 = models.CharField(db_column='KK_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg3 = models.CharField(db_column='KK_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg4 = models.CharField(db_column='KK_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg5 = models.CharField(db_column='KK_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_caled = models.CharField(db_column='KK_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_pid = models.CharField(db_column='KK_PID', max_length=40)  # Field name made lowercase.
    kk_companyname = models.CharField(db_column='KK_COMPANYNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_manual_warning = models.CharField(db_column='KK_MANUAL_WARNING', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS'


class WkTKeyws1(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_createtime = models.CharField(db_column='KK_CREATETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_modifytime = models.CharField(db_column='KK_MODIFYTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_savedays = models.IntegerField(db_column='KK_SAVEDAYS', blank=True, null=True)  # Field name made lowercase.
    kk_noyj = models.CharField(db_column='KK_NOYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_allowsourcetype = models.CharField(db_column='KK_ALLOWSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_allowyjsourcetype = models.CharField(db_column='KK_ALLOWYJSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_datasourcetype = models.CharField(db_column='KK_DATASOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    ku_weibotime = models.CharField(db_column='KU_WEIBOTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust = models.CharField(db_column='KU_WORDMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance = models.CharField(db_column='KU_WORDDISTANCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust_length = models.CharField(db_column='KU_WORDMUST_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance_length = models.CharField(db_column='KU_WORDDISTANCE_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_matchtitle = models.CharField(db_column='KU_MATCHTITLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_onlgmust = models.CharField(db_column='KU_ONLGMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong = models.CharField(db_column='KK_TUISONG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sendtime = models.CharField(db_column='KK_SENDTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_sourcetype = models.CharField(db_column='KK_TUISONG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_orientation = models.CharField(db_column='KK_TUISONG_ORIENTATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_state = models.CharField(db_column='KK_TUISONG_STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_haverepeat = models.CharField(db_column='KK_TUISONG_HAVEREPEAT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_btime = models.CharField(db_column='KK_TUISONG_BTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_etime = models.CharField(db_column='KK_TUISONG_ETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_search = models.TextField(db_column='KK_TUISONG_SEARCH', blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_not = models.TextField(db_column='KK_TUISONG_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_sourcetype = models.CharField(db_column='KK_DINGXIANG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_domain = models.TextField(db_column='KK_DINGXIANG_DOMAIN', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_channel = models.TextField(db_column='KK_DINGXIANG_CHANNEL', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_account = models.TextField(db_column='KK_DINGXIANG_ACCOUNT', blank=True, null=True)  # Field name made lowercase.
    kk_label = models.TextField(db_column='KK_LABEL')  # Field name made lowercase.
    kk_ishigh = models.IntegerField(db_column='KK_ISHIGH')  # Field name made lowercase.
    kk_arg1 = models.CharField(db_column='KK_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg2 = models.CharField(db_column='KK_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg3 = models.CharField(db_column='KK_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg4 = models.CharField(db_column='KK_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg5 = models.CharField(db_column='KK_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_caled = models.CharField(db_column='KK_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_pid = models.CharField(db_column='KK_PID', max_length=40)  # Field name made lowercase.
    kk_companyname = models.CharField(db_column='KK_COMPANYNAME', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS1'


class WkTKeywsBackend(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_createtime = models.CharField(db_column='KK_CREATETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_modifytime = models.CharField(db_column='KK_MODIFYTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_savedays = models.IntegerField(db_column='KK_SAVEDAYS', blank=True, null=True)  # Field name made lowercase.
    kk_noyj = models.CharField(db_column='KK_NOYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_allowsourcetype = models.CharField(db_column='KK_ALLOWSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_allowyjsourcetype = models.CharField(db_column='KK_ALLOWYJSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_datasourcetype = models.CharField(db_column='KK_DATASOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    ku_weibotime = models.CharField(db_column='KU_WEIBOTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust = models.CharField(db_column='KU_WORDMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance = models.CharField(db_column='KU_WORDDISTANCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust_length = models.CharField(db_column='KU_WORDMUST_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance_length = models.CharField(db_column='KU_WORDDISTANCE_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_matchtitle = models.CharField(db_column='KU_MATCHTITLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_onlgmust = models.CharField(db_column='KU_ONLGMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong = models.CharField(db_column='KK_TUISONG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sendtime = models.CharField(db_column='KK_SENDTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_sourcetype = models.CharField(db_column='KK_TUISONG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_orientation = models.CharField(db_column='KK_TUISONG_ORIENTATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_state = models.CharField(db_column='KK_TUISONG_STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_haverepeat = models.CharField(db_column='KK_TUISONG_HAVEREPEAT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_btime = models.CharField(db_column='KK_TUISONG_BTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_etime = models.CharField(db_column='KK_TUISONG_ETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_search = models.TextField(db_column='KK_TUISONG_SEARCH', blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_not = models.TextField(db_column='KK_TUISONG_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_sourcetype = models.CharField(db_column='KK_DINGXIANG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_domain = models.TextField(db_column='KK_DINGXIANG_DOMAIN', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_channel = models.TextField(db_column='KK_DINGXIANG_CHANNEL', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_account = models.TextField(db_column='KK_DINGXIANG_ACCOUNT', blank=True, null=True)  # Field name made lowercase.
    kk_label = models.TextField(db_column='KK_LABEL')  # Field name made lowercase.
    kk_ishigh = models.IntegerField(db_column='KK_ISHIGH')  # Field name made lowercase.
    kk_arg1 = models.CharField(db_column='KK_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg2 = models.CharField(db_column='KK_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg3 = models.CharField(db_column='KK_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg4 = models.CharField(db_column='KK_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg5 = models.CharField(db_column='KK_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_caled = models.CharField(db_column='KK_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_pid = models.CharField(db_column='KK_PID', max_length=40)  # Field name made lowercase.
    kk_companyname = models.CharField(db_column='KK_COMPANYNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_classificationid = models.IntegerField(db_column='KK_CLASSIFICATIONID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS_BACKEND'


class WkTKeywsLog(models.Model):
    kl_id = models.CharField(db_column='KL_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=40)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=200)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_lid = models.CharField(db_column='KU_LID', max_length=100)  # Field name made lowercase.
    kl_type = models.CharField(db_column='KL_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_old_must = models.TextField(db_column='KK_OLD_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_old_should = models.TextField(db_column='KK_OLD_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_old_event = models.TextField(db_column='KK_OLD_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_old_not = models.TextField(db_column='KK_OLD_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_new_must = models.TextField(db_column='KK_NEW_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_new_should = models.TextField(db_column='KK_NEW_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_new_event = models.TextField(db_column='KK_NEW_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_new_not = models.TextField(db_column='KK_NEW_NOT', blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emailsend = models.CharField(db_column='EMAILSEND', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS_LOG'


class WkTKeywsWarnset(models.Model):
    kw_id = models.AutoField(db_column='KW_ID', primary_key=True)  # Field name made lowercase.
    ks_id = models.CharField(db_column='KS_ID', max_length=50)  # Field name made lowercase.
    kw_open = models.IntegerField(db_column='KW_OPEN', blank=True, null=True)  # Field name made lowercase.
    kw_orientation = models.CharField(db_column='KW_ORIENTATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kw_removal = models.IntegerField(db_column='KW_REMOVAL', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kw_opentime = models.CharField(db_column='KW_OPENTIME', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS_WARNSET'


class WkTKeywsCopy(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_createtime = models.CharField(db_column='KK_CREATETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_modifytime = models.CharField(db_column='KK_MODIFYTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_savedays = models.IntegerField(db_column='KK_SAVEDAYS', blank=True, null=True)  # Field name made lowercase.
    kk_noyj = models.CharField(db_column='KK_NOYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_allowsourcetype = models.CharField(db_column='KK_ALLOWSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_allowyjsourcetype = models.CharField(db_column='KK_ALLOWYJSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_datasourcetype = models.CharField(db_column='KK_DATASOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    ku_weibotime = models.CharField(db_column='KU_WEIBOTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust = models.CharField(db_column='KU_WORDMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance = models.CharField(db_column='KU_WORDDISTANCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust_length = models.CharField(db_column='KU_WORDMUST_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance_length = models.CharField(db_column='KU_WORDDISTANCE_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_matchtitle = models.CharField(db_column='KU_MATCHTITLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_onlgmust = models.CharField(db_column='KU_ONLGMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong = models.CharField(db_column='KK_TUISONG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sendtime = models.CharField(db_column='KK_SENDTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_sourcetype = models.CharField(db_column='KK_TUISONG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_orientation = models.CharField(db_column='KK_TUISONG_ORIENTATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_state = models.CharField(db_column='KK_TUISONG_STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_haverepeat = models.CharField(db_column='KK_TUISONG_HAVEREPEAT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_btime = models.CharField(db_column='KK_TUISONG_BTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_etime = models.CharField(db_column='KK_TUISONG_ETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_search = models.TextField(db_column='KK_TUISONG_SEARCH', blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_not = models.TextField(db_column='KK_TUISONG_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_sourcetype = models.CharField(db_column='KK_DINGXIANG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_domain = models.TextField(db_column='KK_DINGXIANG_DOMAIN', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_channel = models.TextField(db_column='KK_DINGXIANG_CHANNEL', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_account = models.TextField(db_column='KK_DINGXIANG_ACCOUNT', blank=True, null=True)  # Field name made lowercase.
    kk_label = models.TextField(db_column='KK_LABEL')  # Field name made lowercase.
    kk_ishigh = models.IntegerField(db_column='KK_ISHIGH')  # Field name made lowercase.
    kk_arg1 = models.CharField(db_column='KK_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg2 = models.CharField(db_column='KK_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg3 = models.CharField(db_column='KK_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg4 = models.CharField(db_column='KK_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg5 = models.CharField(db_column='KK_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_caled = models.CharField(db_column='KK_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_pid = models.CharField(db_column='KK_PID', max_length=40)  # Field name made lowercase.
    kk_companyname = models.CharField(db_column='KK_COMPANYNAME', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS_copy'


class WkTKeywsCopy1(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_createtime = models.CharField(db_column='KK_CREATETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_modifytime = models.CharField(db_column='KK_MODIFYTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_savedays = models.IntegerField(db_column='KK_SAVEDAYS', blank=True, null=True)  # Field name made lowercase.
    kk_noyj = models.CharField(db_column='KK_NOYJ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_allowsourcetype = models.CharField(db_column='KK_ALLOWSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_allowyjsourcetype = models.CharField(db_column='KK_ALLOWYJSOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_datasourcetype = models.CharField(db_column='KK_DATASOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    ku_weibotime = models.CharField(db_column='KU_WEIBOTIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust = models.CharField(db_column='KU_WORDMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance = models.CharField(db_column='KU_WORDDISTANCE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_wordmust_length = models.CharField(db_column='KU_WORDMUST_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_worddistance_length = models.CharField(db_column='KU_WORDDISTANCE_LENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_matchtitle = models.CharField(db_column='KU_MATCHTITLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_onlgmust = models.CharField(db_column='KU_ONLGMUST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong = models.CharField(db_column='KK_TUISONG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sendtime = models.CharField(db_column='KK_SENDTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_sourcetype = models.CharField(db_column='KK_TUISONG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_orientation = models.CharField(db_column='KK_TUISONG_ORIENTATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_state = models.CharField(db_column='KK_TUISONG_STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_haverepeat = models.CharField(db_column='KK_TUISONG_HAVEREPEAT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_btime = models.CharField(db_column='KK_TUISONG_BTIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_etime = models.CharField(db_column='KK_TUISONG_ETIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_search = models.TextField(db_column='KK_TUISONG_SEARCH', blank=True, null=True)  # Field name made lowercase.
    kk_tuisong_not = models.TextField(db_column='KK_TUISONG_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_sourcetype = models.CharField(db_column='KK_DINGXIANG_SOURCETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_domain = models.TextField(db_column='KK_DINGXIANG_DOMAIN', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_channel = models.TextField(db_column='KK_DINGXIANG_CHANNEL', blank=True, null=True)  # Field name made lowercase.
    kk_dingxiang_account = models.TextField(db_column='KK_DINGXIANG_ACCOUNT', blank=True, null=True)  # Field name made lowercase.
    kk_label = models.TextField(db_column='KK_LABEL')  # Field name made lowercase.
    kk_ishigh = models.IntegerField(db_column='KK_ISHIGH')  # Field name made lowercase.
    kk_arg1 = models.CharField(db_column='KK_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg2 = models.CharField(db_column='KK_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg3 = models.CharField(db_column='KK_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg4 = models.CharField(db_column='KK_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_arg5 = models.CharField(db_column='KK_ARG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kk_caled = models.CharField(db_column='KK_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_pid = models.CharField(db_column='KK_PID', max_length=40)  # Field name made lowercase.
    kk_companyname = models.CharField(db_column='KK_COMPANYNAME', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_KEYWS_copy1'


class WkTManagerLog(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ku_lid = models.CharField(db_column='KU_LID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kl_modular = models.CharField(db_column='KL_MODULAR', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kl_platform = models.CharField(db_column='KL_PLATFORM', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kl_ip = models.CharField(db_column='KL_IP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kl_work = models.TextField(db_column='KL_WORK', blank=True, null=True)  # Field name made lowercase.
    kl_user = models.CharField(db_column='KL_USER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MANAGER_LOG'


class WkTMessage(models.Model):
    km_id = models.CharField(db_column='KM_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    km_con = models.CharField(db_column='KM_CON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    km_time = models.CharField(db_column='KM_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    km_image = models.CharField(db_column='KM_IMAGE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MESSAGE'


class WkTModuleinfo(models.Model):
    km_id = models.CharField(db_column='KM_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    km_mod = models.CharField(db_column='KM_MOD', max_length=400, blank=True, null=True)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    km_worktype = models.CharField(db_column='KM_WORKTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    km_pram = models.CharField(db_column='KM_PRAM', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    km_pram_ins = models.CharField(db_column='KM_PRAM_INS', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    km_type = models.CharField(db_column='KM_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MODULEINFO'


class WkTMsversion(models.Model):
    kv_id = models.AutoField(db_column='KV_ID', primary_key=True)  # Field name made lowercase.
    kv_versionname = models.CharField(db_column='KV_VERSIONNAME', max_length=255)  # Field name made lowercase.
    kv_data = models.TextField(db_column='KV_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MSVERSION'


class WkTMuser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_mid = models.IntegerField(db_column='KU_MID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MUSER'


class WkTMuserCount(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    muserid = models.IntegerField(db_column='MUSERID')  # Field name made lowercase.
    qqcount = models.IntegerField(db_column='QQCOUNT')  # Field name made lowercase.
    wechatcount = models.IntegerField(db_column='WECHATCOUNT')  # Field name made lowercase.
    msgcount = models.IntegerField(db_column='MSGCOUNT')  # Field name made lowercase.
    warningcount = models.IntegerField(db_column='WARNINGCOUNT')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MUSER_COUNT'


class WkTMyattentionclassify(models.Model):
    km_id = models.CharField(db_column='KM_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=50)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MYATTENTIONCLASSIFY'


class WkTMycollection(models.Model):
    kc_uuid = models.CharField(db_column='KC_UUID', primary_key=True, max_length=50)  # Field name made lowercase.
    ks_id = models.CharField(db_column='KS_ID', max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=20)  # Field name made lowercase.
    kc_rename = models.CharField(db_column='KC_RENAME', max_length=50)  # Field name made lowercase.
    kc_shareid = models.CharField(db_column='KC_SHAREID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kc_time = models.DateTimeField(db_column='KC_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_MYCOLLECTION'


class WkTNewbackendLog(models.Model):
    username = models.CharField(max_length=255)
    userid = models.IntegerField()
    action = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    where = models.TextField()
    user = models.CharField(max_length=255)
    obj_id = models.CharField(max_length=11)
    time = models.IntegerField()
    agent = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    inmysql = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_NEWBACKEND_LOG'


class WkTNodeNew(models.Model):
    kn_id = models.AutoField(db_column='KN_ID', primary_key=True)  # Field name made lowercase.
    kn_name = models.CharField(db_column='KN_NAME', max_length=255)  # Field name made lowercase.
    kn_title = models.CharField(db_column='KN_TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kn_status = models.IntegerField(db_column='KN_STATUS', blank=True, null=True)  # Field name made lowercase.
    kn_pid = models.IntegerField(db_column='KN_PID', blank=True, null=True)  # Field name made lowercase.
    kn_level = models.IntegerField(db_column='KN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kn_sort = models.IntegerField(db_column='KN_SORT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_NODE_NEW'


class WkTPatent(models.Model):
    companyid = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    applicant = models.CharField(db_column='Applicant', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prioritynumber = models.CharField(db_column='PriorityNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    applicantpostcode = models.CharField(db_column='ApplicantPostCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary', blank=True, null=True)  # Field name made lowercase.
    aplicationnumber = models.CharField(db_column='AplicationNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publicationdate = models.CharField(db_column='PublicationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prioritydate = models.CharField(db_column='PriorityDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aplicationdate = models.CharField(db_column='AplicationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipcclassnumber = models.CharField(db_column='IPCClassNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publicationnumber = models.CharField(db_column='PublicationNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    applicantaddress = models.CharField(db_column='ApplicantAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventor = models.CharField(db_column='Inventor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PATENT'


class WkTPhonelist(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    macid = models.CharField(db_column='MACID', max_length=70, blank=True, null=True)  # Field name made lowercase.
    usertype = models.IntegerField(db_column='USERTYPE', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='STARTTIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='ENDTIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PHONELIST'


class WkTPhonepush(models.Model):
    wk_id = models.CharField(db_column='WK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    msg_type = models.IntegerField(db_column='MSG_TYPE', blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    info_uuid = models.CharField(db_column='INFO_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    type_flag = models.IntegerField(db_column='TYPE_FLAG', blank=True, null=True)  # Field name made lowercase.
    send_state = models.IntegerField(db_column='SEND_STATE', blank=True, null=True)  # Field name made lowercase.
    file_count = models.IntegerField(db_column='FILE_COUNT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PHONEPUSH'


class WkTPhoneInfo(models.Model):
    kp_uuid = models.CharField(db_column='KP_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kp_model = models.CharField(db_column='KP_MODEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kp_token = models.CharField(db_column='KP_TOKEN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kp_version = models.CharField(db_column='KP_VERSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kp_createtime = models.CharField(db_column='KP_CREATETIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kp_ip = models.CharField(db_column='KP_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kp_province = models.CharField(db_column='KP_PROVINCE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kp_city = models.CharField(db_column='KP_CITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kp_county = models.CharField(db_column='KP_COUNTY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isp = models.CharField(db_column='ISP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kp_useragent = models.CharField(db_column='KP_USERAGENT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kp_longitude = models.CharField(db_column='KP_LONGITUDE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kp_latitude = models.CharField(db_column='KP_LATITUDE', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PHONE_INFO'


class WkTProductLog(models.Model):
    pl_id = models.AutoField(db_column='PL_ID', primary_key=True)  # Field name made lowercase.
    pl_version_number = models.CharField(db_column='PL_VERSION_NUMBER', max_length=40)  # Field name made lowercase.
    pl_type = models.IntegerField(db_column='PL_TYPE')  # Field name made lowercase.
    pl_content = models.TextField(db_column='PL_CONTENT')  # Field name made lowercase.
    pl_version_date = models.CharField(db_column='PL_VERSION_DATE', max_length=20)  # Field name made lowercase.
    pl_status = models.IntegerField(db_column='PL_STATUS')  # Field name made lowercase.
    pl_created = models.DateTimeField(db_column='PL_CREATED')  # Field name made lowercase.
    pl_updated = models.DateTimeField(db_column='PL_UPDATED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_PRODUCT_LOG'


class WkTQqkeyws(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_must = models.CharField(db_column='KK_MUST', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_should = models.CharField(db_column='KK_SHOULD', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_event = models.CharField(db_column='KK_EVENT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_time = models.CharField(db_column='KK_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_QQKEYWS'


class WkTRegisteruser(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_domain = models.CharField(db_column='KV_DOMAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_name = models.CharField(db_column='KR_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_sex = models.CharField(db_column='KR_SEX', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kr_nation = models.CharField(db_column='KR_NATION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_birthday = models.CharField(db_column='KR_BIRTHDAY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_idcard = models.CharField(db_column='KR_IDCARD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kr_address = models.CharField(db_column='KR_ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_time = models.CharField(db_column='KR_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_REGISTERUSER'


class WkTReport(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=38)  # Field name made lowercase.
    kr_title = models.CharField(db_column='KR_TITLE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kr_address = models.CharField(db_column='KR_ADDRESS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kr_time = models.CharField(db_column='KR_TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    kr_uid = models.IntegerField(db_column='KR_UID', blank=True, null=True)  # Field name made lowercase.
    kr_type = models.CharField(db_column='KR_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kt_isshared = models.CharField(db_column='KT_ISSHARED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kt_sharedtime = models.CharField(db_column='KT_SHAREDTIME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    kt_cancelsharedtime = models.CharField(db_column='KT_CANCELSHAREDTIME', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_REPORT'


class WkTReporttemplate(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    kr_backname = models.CharField(db_column='KR_BACKNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_frontname = models.CharField(db_column='KR_FRONTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kr_picture = models.CharField(db_column='KR_PICTURE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_REPORTTEMPLATE'


class WkTRole2(models.Model):
    kr_id = models.IntegerField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    kr_pid = models.IntegerField(db_column='KR_PID', blank=True, null=True)  # Field name made lowercase.
    kd_id = models.IntegerField(db_column='KD_ID', blank=True, null=True)  # Field name made lowercase.
    kr_name = models.CharField(db_column='KR_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kr_default = models.CharField(db_column='KR_DEFAULT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kr_desc = models.CharField(db_column='KR_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kr_order = models.IntegerField(db_column='KR_ORDER', blank=True, null=True)  # Field name made lowercase.
    kr_share = models.CharField(db_column='KR_SHARE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ROLE2'


class WkTRoletitle(models.Model):
    kt_id = models.IntegerField(db_column='KT_ID', blank=True, null=True)  # Field name made lowercase.
    kr_id = models.IntegerField(db_column='KR_ID', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ROLETITLE'


class WkTRoleuserNew(models.Model):
    kr_id = models.IntegerField(db_column='KR_ID')  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_create = models.TextField(db_column='KU_CREATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ROLEUSER_NEW'


class WkTRoleNew(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    kr_name = models.CharField(db_column='KR_NAME', max_length=255)  # Field name made lowercase.
    kr_status = models.IntegerField(db_column='KR_STATUS')  # Field name made lowercase.
    kr_pid = models.IntegerField(db_column='KR_PID', blank=True, null=True)  # Field name made lowercase.
    kr_auth = models.IntegerField(db_column='KR_AUTH', blank=True, null=True)  # Field name made lowercase.
    kr_admin = models.IntegerField(db_column='KR_ADMIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ROLE_NEW'


class WkTSearchword(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ks_word = models.CharField(db_column='KS_WORD', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_SEARCHWORD'


class WkTSearchCondition(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ks_condition = models.CharField(db_column='KS_CONDITION', max_length=2000)  # Field name made lowercase.
    c_time = models.DateTimeField(db_column='C_TIME', blank=True, null=True)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sc_title = models.CharField(db_column='SC_TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    version_type = models.IntegerField(db_column='VERSION_TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_SEARCH_CONDITION'
        unique_together = (('ku_id', 'kk_id', 'ks_type', 'sc_title'),)


class WkTShare(models.Model):
    ks_id = models.CharField(db_column='KS_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=50)  # Field name made lowercase.
    ks_type = models.IntegerField(db_column='KS_TYPE')  # Field name made lowercase.
    ku_shareid = models.CharField(db_column='KU_SHAREID', max_length=50)  # Field name made lowercase.
    ks_name = models.CharField(db_column='KS_NAME', max_length=50)  # Field name made lowercase.
    ks_issys = models.IntegerField(db_column='KS_ISSYS')  # Field name made lowercase.
    ks_description = models.CharField(db_column='KS_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ks_isparent = models.IntegerField(db_column='KS_ISPARENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_SHARE'


class WkTSoftwareCopyright(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    registernumber = models.CharField(db_column='RegisterNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    classnumber = models.CharField(db_column='ClassNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='PublishDate', max_length=500, blank=True, null=True)  # Field name made lowercase.
    versionnumber = models.CharField(db_column='VersionNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.CharField(db_column='RegisterDate', max_length=500, blank=True, null=True)  # Field name made lowercase.
    copyrightownername = models.CharField(db_column='CopyrightOwnerName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_SOFTWARE_COPYRIGHT'


class WkTSubjectWordLength(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ks_id = models.CharField(db_column='KS_ID', max_length=255)  # Field name made lowercase.
    ks_pid = models.CharField(db_column='KS_PID', max_length=255)  # Field name made lowercase.
    wordlength = models.IntegerField(db_column='WORDLENGTH', blank=True, null=True)  # Field name made lowercase.
    attr = models.IntegerField(db_column='ATTR', blank=True, null=True)  # Field name made lowercase.
    ctime = models.DateTimeField(db_column='CTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_SUBJECT_WORD_LENGTH'


class WkTTitle2(models.Model):
    kt_id = models.IntegerField(db_column='KT_ID', primary_key=True)  # Field name made lowercase.
    ks_id = models.IntegerField(db_column='KS_ID')  # Field name made lowercase.
    kt_name = models.CharField(db_column='KT_NAME', max_length=30)  # Field name made lowercase.
    kt_type = models.CharField(db_column='KT_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kt_pid = models.IntegerField(db_column='KT_PID')  # Field name made lowercase.
    kt_newwin = models.CharField(db_column='KT_NEWWIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kt_security = models.CharField(db_column='KT_SECURITY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    kt_ordno = models.IntegerField(db_column='KT_ORDNO', blank=True, null=True)  # Field name made lowercase.
    kt_image = models.CharField(db_column='KT_IMAGE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kt_hits = models.IntegerField(db_column='KT_HITS', blank=True, null=True)  # Field name made lowercase.
    kt_content = models.CharField(db_column='KT_CONTENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kt_memo = models.CharField(db_column='KT_MEMO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kt_node = models.CharField(db_column='KT_NODE', max_length=6)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_TITLE2'


class WkTTopickeywordcheck(models.Model):
    msuid = models.IntegerField(db_column='msUid')  # Field name made lowercase.
    topickeyword = models.CharField(db_column='topicKeyword', max_length=255)  # Field name made lowercase.
    arekeyword = models.TextField(db_column='areKeyword')  # Field name made lowercase.
    newarekeyword = models.TextField(db_column='newAreKeyword')  # Field name made lowercase.
    checkstatus = models.IntegerField(db_column='checkStatus')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_TOPICKEYWORDCHECK'


class WkTTrademark(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    recentnews = models.CharField(db_column='RecentNews', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    registrationid = models.CharField(db_column='RegistrationId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internationregistrationdate = models.CharField(db_column='InternationRegistrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categorynumber = models.CharField(db_column='CategoryNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_TRADEMARK'


class WkTUloguser(models.Model):
    kl_id = models.CharField(db_column='KL_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_ULOGUSER'


class WkTUpdatelog(models.Model):
    kl_id = models.CharField(db_column='KL_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    kl_type = models.CharField(db_column='KL_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_title = models.CharField(db_column='KL_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kl_content = models.CharField(db_column='KL_CONTENT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kl_state = models.CharField(db_column='KL_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_UPDATELOG'


class WkTUpdaterecord(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    kr_editionno = models.CharField(db_column='KR_EDITIONNO', max_length=50)  # Field name made lowercase.
    kr_url = models.CharField(db_column='KR_URL', max_length=200)  # Field name made lowercase.
    kr_plist = models.CharField(db_column='KR_PLIST', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_uuid = models.CharField(db_column='KA_UUID', max_length=50)  # Field name made lowercase.
    kr_message = models.CharField(db_column='KR_MESSAGE', max_length=200)  # Field name made lowercase.
    kr_isupdate = models.IntegerField(db_column='KR_ISUPDATE')  # Field name made lowercase.
    kr_usertype = models.CharField(db_column='KR_USERTYPE', max_length=50)  # Field name made lowercase.
    kr_userstate = models.CharField(db_column='KR_USERSTATE', max_length=50)  # Field name made lowercase.
    kr_ctime = models.DateTimeField(db_column='KR_CTIME')  # Field name made lowercase.
    kr_utime = models.DateTimeField(db_column='KR_UTIME')  # Field name made lowercase.
    kr_stime = models.DateTimeField(db_column='KR_STIME')  # Field name made lowercase.
    kr_start = models.IntegerField(db_column='KR_START')  # Field name made lowercase.
    kr_packtype = models.IntegerField(db_column='KR_PACKTYPE')  # Field name made lowercase.
    kr_gxaddress = models.CharField(db_column='KR_GXADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_fbaddress = models.CharField(db_column='KR_FBADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_pic1 = models.CharField(db_column='KR_PIC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_pic2 = models.CharField(db_column='KR_PIC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_force_ver = models.CharField(db_column='KR_FORCE_VER', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_UPDATERECORD'


class WkTUpdaterecordZj(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    kr_editionno = models.CharField(db_column='KR_EDITIONNO', max_length=50)  # Field name made lowercase.
    kr_url = models.CharField(db_column='KR_URL', max_length=200)  # Field name made lowercase.
    kr_plist = models.CharField(db_column='KR_PLIST', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_uuid = models.CharField(db_column='KA_UUID', max_length=50)  # Field name made lowercase.
    kr_message = models.CharField(db_column='KR_MESSAGE', max_length=200)  # Field name made lowercase.
    kr_isupdate = models.IntegerField(db_column='KR_ISUPDATE')  # Field name made lowercase.
    kr_usertype = models.CharField(db_column='KR_USERTYPE', max_length=50)  # Field name made lowercase.
    kr_userstate = models.CharField(db_column='KR_USERSTATE', max_length=50)  # Field name made lowercase.
    kr_ctime = models.DateTimeField(db_column='KR_CTIME')  # Field name made lowercase.
    kr_utime = models.DateTimeField(db_column='KR_UTIME')  # Field name made lowercase.
    kr_stime = models.DateTimeField(db_column='KR_STIME')  # Field name made lowercase.
    kr_start = models.IntegerField(db_column='KR_START')  # Field name made lowercase.
    kr_packtype = models.IntegerField(db_column='KR_PACKTYPE')  # Field name made lowercase.
    kr_gxaddress = models.CharField(db_column='KR_GXADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_fbaddress = models.CharField(db_column='KR_FBADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_pic1 = models.CharField(db_column='KR_PIC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_pic2 = models.CharField(db_column='KR_PIC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_force_ver = models.CharField(db_column='KR_FORCE_VER', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_UPDATERECORD_ZJ'


class WkTUpdatetvrecord(models.Model):
    kr_id = models.AutoField(db_column='KR_ID', primary_key=True)  # Field name made lowercase.
    kr_editionno = models.CharField(db_column='KR_EDITIONNO', max_length=50)  # Field name made lowercase.
    kr_url = models.CharField(db_column='KR_URL', max_length=200)  # Field name made lowercase.
    kr_plist = models.CharField(db_column='KR_PLIST', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ka_uuid = models.CharField(db_column='KA_UUID', max_length=50)  # Field name made lowercase.
    kr_message = models.CharField(db_column='KR_MESSAGE', max_length=200)  # Field name made lowercase.
    kr_isupdate = models.IntegerField(db_column='KR_ISUPDATE')  # Field name made lowercase.
    kr_usertype = models.CharField(db_column='KR_USERTYPE', max_length=50)  # Field name made lowercase.
    kr_userstate = models.CharField(db_column='KR_USERSTATE', max_length=50)  # Field name made lowercase.
    kr_ctime = models.DateTimeField(db_column='KR_CTIME')  # Field name made lowercase.
    kr_utime = models.DateTimeField(db_column='KR_UTIME')  # Field name made lowercase.
    kr_stime = models.DateTimeField(db_column='KR_STIME')  # Field name made lowercase.
    kr_start = models.IntegerField(db_column='KR_START')  # Field name made lowercase.
    kr_packtype = models.IntegerField(db_column='KR_PACKTYPE')  # Field name made lowercase.
    kr_gxaddress = models.CharField(db_column='KR_GXADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_fbaddress = models.CharField(db_column='KR_FBADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_pic1 = models.CharField(db_column='KR_PIC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_pic2 = models.CharField(db_column='KR_PIC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_force_ver = models.CharField(db_column='KR_FORCE_VER', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_UPDATETVRECORD'


class WkTUploadFile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    folderid = models.IntegerField(db_column='FOLDERID')  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=255)  # Field name made lowercase.
    alias = models.CharField(db_column='ALIAS', max_length=255)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    c_time = models.DateTimeField(db_column='C_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_UPLOAD_FILE'


class WkTUploadFolder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    folder = models.CharField(db_column='FOLDER', max_length=255)  # Field name made lowercase.
    alias = models.CharField(db_column='ALIAS', max_length=255)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    c_time = models.DateTimeField(db_column='C_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_UPLOAD_FOLDER'


class WkTUrllog(models.Model):
    ku_id = models.AutoField(db_column='KU_ID', primary_key=True)  # Field name made lowercase.
    ku_uri = models.CharField(db_column='KU_URI', max_length=256, blank=True, null=True)  # Field name made lowercase.
    ku_counts = models.CharField(db_column='KU_COUNTS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ku_userid = models.CharField(db_column='KU_USERID', max_length=256, blank=True, null=True)  # Field name made lowercase.
    ku_ip = models.CharField(db_column='KU_IP', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ku_date = models.CharField(db_column='KU_DATE', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_URLLOG'


class WkTUsearchword(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ks_word = models.CharField(db_column='KS_WORD', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_source = models.CharField(db_column='KS_SOURCE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USEARCHWORD'


class WkTUser(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID', primary_key=True)  # Field name made lowercase.
    ku_lid = models.CharField(db_column='KU_LID', unique=True, max_length=100)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_passwd = models.CharField(db_column='KU_PASSWD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_regdate = models.CharField(db_column='KU_REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_status = models.CharField(db_column='KU_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_sex = models.CharField(db_column='KU_SEX', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_birthday = models.CharField(db_column='KU_BIRTHDAY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_email = models.CharField(db_column='KU_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_phone = models.CharField(db_column='KU_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_company = models.CharField(db_column='KU_COMPANY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kd_id = models.IntegerField(db_column='KD_ID', blank=True, null=True)  # Field name made lowercase.
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


class WkTUserapi(models.Model):
    uuid = models.CharField(db_column='UUID', primary_key=True, max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50)  # Field name made lowercase.
    ku_url = models.CharField(db_column='KU_URL', max_length=50)  # Field name made lowercase.
    ku_port = models.CharField(db_column='KU_PORT', max_length=50)  # Field name made lowercase.
    ku_action = models.CharField(db_column='KU_ACTION', max_length=50)  # Field name made lowercase.
    ku_token = models.CharField(db_column='KU_TOKEN', max_length=50)  # Field name made lowercase.
    ku_isuse = models.IntegerField(db_column='KU_ISUSE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERAPI'


class WkTUserbaseinfo(models.Model):
    ku_uuid = models.AutoField(db_column='KU_UUID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_type = models.CharField(db_column='KU_TYPE', max_length=50)  # Field name made lowercase.
    ku_value = models.TextField(db_column='KU_VALUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERBASEINFO'
        unique_together = (('ku_id', 'ku_type'),)


class WkTUsercheck(models.Model):
    ku_id = models.CharField(db_column='KU_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    km_checkid = models.CharField(db_column='KM_CHECKID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    km_focustype = models.CharField(db_column='KM_FOCUSTYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERCHECK'


class WkTUserclassify(models.Model):
    kc_uuid = models.CharField(db_column='KC_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kc_time = models.CharField(db_column='KC_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kc_state = models.CharField(db_column='KC_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_sort = models.IntegerField(db_column='KC_SORT', blank=True, null=True)  # Field name made lowercase.
    kc_isold = models.IntegerField(db_column='KC_ISOLD')  # Field name made lowercase.
    kc_type = models.IntegerField(db_column='KC_TYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERCLASSIFY'


class WkTUserclassifySystem(models.Model):
    ks_id = models.AutoField(db_column='KS_ID', primary_key=True)  # Field name made lowercase.
    ku_level = models.IntegerField(db_column='KU_LEVEL', blank=True, null=True)  # Field name made lowercase.
    ks_name = models.CharField(db_column='KS_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERCLASSIFY_SYSTEM'


class WkTUsercustom(models.Model):
    kc_uuid = models.CharField(db_column='KC_UUID', primary_key=True, max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=20)  # Field name made lowercase.
    kc_name = models.CharField(db_column='KC_NAME', max_length=20)  # Field name made lowercase.
    kc_qqone = models.CharField(db_column='KC_QQONE', max_length=20)  # Field name made lowercase.
    kc_qqtwo = models.CharField(db_column='KC_QQTWO', max_length=20)  # Field name made lowercase.
    kc_company = models.CharField(db_column='KC_COMPANY', max_length=20)  # Field name made lowercase.
    kc_record = models.CharField(db_column='KC_RECORD', max_length=20)  # Field name made lowercase.
    kc_logo = models.CharField(db_column='KC_LOGO', max_length=20)  # Field name made lowercase.
    kc_ico = models.CharField(db_column='KC_ICO', max_length=20)  # Field name made lowercase.
    kc_copyright = models.CharField(db_column='KC_COPYRIGHT', max_length=100)  # Field name made lowercase.
    kc_markettel = models.CharField(db_column='KC_MARKETTEL', max_length=20)  # Field name made lowercase.
    kc_tel = models.CharField(db_column='KC_TEL', max_length=20)  # Field name made lowercase.
    kc_phone = models.CharField(db_column='KC_PHONE', max_length=20)  # Field name made lowercase.
    kc_email = models.CharField(db_column='KC_EMAIL', max_length=50)  # Field name made lowercase.
    kc_url = models.CharField(db_column='KC_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERCUSTOM'


class WkTUserfeedback(models.Model):
    ku_fbid = models.AutoField(db_column='KU_FBID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
    time = models.IntegerField(db_column='TIME')  # Field name made lowercase.
    who = models.CharField(db_column='WHO', max_length=50)  # Field name made lowercase.
    types = models.IntegerField(db_column='TYPES')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERFEEDBACK'


class WkTUserfieldattribute(models.Model):
    km_id = models.AutoField(db_column='KM_ID', primary_key=True)  # Field name made lowercase.
    km_fieldattributename = models.CharField(db_column='KM_FIELDATTRIBUTENAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERFIELDATTRIBUTE'


class WkTUserindexModule(models.Model):
    kp_id = models.CharField(db_column='KP_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kp_alias = models.CharField(db_column='KP_ALIAS', max_length=20)  # Field name made lowercase.
    kp_order = models.IntegerField(db_column='KP_ORDER')  # Field name made lowercase.
    kp_position = models.IntegerField(db_column='KP_POSITION')  # Field name made lowercase.
    kp_condition = models.TextField(db_column='KP_CONDITION', blank=True, null=True)  # Field name made lowercase.
    km_id = models.IntegerField(db_column='KM_ID')  # Field name made lowercase.
    kp_type = models.CharField(db_column='KP_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kp_isold = models.IntegerField(db_column='KP_ISOLD')  # Field name made lowercase.
    km_status = models.CharField(db_column='KM_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    km_pid = models.CharField(db_column='KM_PID', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERINDEX_MODULE'


class WkTUsermail(models.Model):
    km_uuid = models.CharField(db_column='KM_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    km_email = models.CharField(db_column='KM_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    km_time = models.CharField(db_column='KM_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERMAIL'


class WkTUsermailExport(models.Model):
    km_uuid = models.CharField(db_column='KM_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    km_email = models.CharField(db_column='KM_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    km_time = models.CharField(db_column='KM_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    km_selected = models.CharField(db_column='KM_SELECTED', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERMAIL_EXPORT'


class WkTUsermodule(models.Model):
    km_id = models.AutoField(db_column='KM_ID', primary_key=True)  # Field name made lowercase.
    km_usermodulename = models.CharField(db_column='KM_USERMODULENAME', max_length=50)  # Field name made lowercase.
    km_order = models.IntegerField(db_column='KM_ORDER')  # Field name made lowercase.
    km_type = models.IntegerField(db_column='KM_TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERMODULE'


class WkTUsermoduledetails(models.Model):
    km_id = models.CharField(db_column='KM_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    km_moduleid = models.CharField(db_column='KM_MODULEID', max_length=50)  # Field name made lowercase.
    km_attribute = models.TextField(db_column='KM_ATTRIBUTE', blank=True, null=True)  # Field name made lowercase.
    km_order = models.IntegerField(db_column='KM_ORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERMODULEDETAILS'


class WkTUsermodulefieldtype(models.Model):
    km_id = models.AutoField(db_column='KM_ID', primary_key=True)  # Field name made lowercase.
    km_fieldtypename = models.CharField(db_column='KM_FIELDTYPENAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERMODULEFIELDTYPE'


class WkTUsermodulerelation(models.Model):
    km_id = models.CharField(db_column='KM_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    km_moduleid = models.CharField(db_column='KM_MODULEID', max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40)  # Field name made lowercase.
    km_index = models.IntegerField(db_column='KM_INDEX')  # Field name made lowercase.
    km_templateid = models.CharField(db_column='KM_TEMPLATEID', max_length=50)  # Field name made lowercase.
    km_attribute = models.TextField(db_column='KM_ATTRIBUTE', blank=True, null=True)  # Field name made lowercase.
    km_order = models.IntegerField(db_column='KM_ORDER')  # Field name made lowercase.
    km_style = models.IntegerField(db_column='KM_STYLE', blank=True, null=True)  # Field name made lowercase.
    km_isyj = models.IntegerField(db_column='KM_ISYJ', blank=True, null=True)  # Field name made lowercase.
    km_chartstyle = models.CharField(db_column='KM_CHARTSTYLE', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERMODULERELATION'


class WkTUsernav(models.Model):
    ku_uuid = models.CharField(db_column='KU_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50)  # Field name made lowercase.
    km_id = models.CharField(db_column='KM_ID', max_length=40)  # Field name made lowercase.
    ku_type = models.IntegerField(db_column='KU_TYPE')  # Field name made lowercase.
    ku_order = models.IntegerField(db_column='KU_ORDER')  # Field name made lowercase.
    ku_status = models.IntegerField(db_column='KU_STATUS')  # Field name made lowercase.
    ku_rename = models.CharField(db_column='KU_RENAME', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERNAV'


class WkTUserole2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kr_id = models.IntegerField(db_column='KR_ID')  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USEROLE2'


class WkTUserpsw(models.Model):
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.
    login_time = models.CharField(db_column='LOGIN_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=400, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERPSW'


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
    ku_report_condition = models.CharField(db_column='KU_REPORT_CONDITION', max_length=2000, blank=True, null=True)  # Field name made lowercase.
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


class WkTUsersource(models.Model):
    ks_uuid = models.CharField(db_column='KS_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ks_name = models.CharField(db_column='KS_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERSOURCE'


class WkTUsertemplate(models.Model):
    kt_id = models.CharField(db_column='KT_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    kt_templatename = models.CharField(db_column='KT_TEMPLATENAME', max_length=50)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40)  # Field name made lowercase.
    kt_ctime = models.CharField(db_column='KT_CTIME', max_length=50)  # Field name made lowercase.
    kt_type = models.IntegerField(db_column='KT_TYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERTEMPLATE'


class WkTUserweb(models.Model):
    kw_id = models.CharField(db_column='KW_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    kw_webname = models.CharField(db_column='KW_WEBNAME', max_length=50)  # Field name made lowercase.
    kw_weburl = models.CharField(db_column='KW_WEBURL', max_length=100)  # Field name made lowercase.
    kw_webtype = models.IntegerField(db_column='KW_WEBTYPE')  # Field name made lowercase.
    kw_webimportant = models.IntegerField(db_column='KW_WEBIMPORTANT')  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERWEB'


class WkTUserwxtemplate(models.Model):
    ku_uuid = models.AutoField(db_column='KU_UUID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', unique=True)  # Field name made lowercase.
    ku_value = models.TextField(db_column='KU_VALUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USERWXTEMPLATE'


class WkTUserApplicationLog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    application_name = models.TextField(db_column='APPLICATION_NAME')  # Field name made lowercase.
    macid = models.CharField(db_column='MACID', max_length=100)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    phone_version = models.CharField(db_column='PHONE_VERSION', max_length=100)  # Field name made lowercase.
    device = models.CharField(db_column='DEVICE', max_length=100)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_APPLICATION_LOG'


class WkTUserArea(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ka_id = models.IntegerField(db_column='KA_ID')  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_AREA'


class WkTUserAreaNew(models.Model):
    ku_id = models.IntegerField(unique=True)
    province_id = models.CharField(max_length=40, blank=True, null=True)
    city_id = models.CharField(max_length=40, blank=True, null=True)
    county_id = models.CharField(max_length=40, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_USER_AREA_NEW'


class WkTUserAreaNew1(models.Model):
    ku_id = models.IntegerField()
    province_id = models.CharField(max_length=40, blank=True, null=True)
    city_id = models.CharField(max_length=40, blank=True, null=True)
    county_id = models.CharField(max_length=40, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_USER_AREA_NEW1'


class WkTUserDept(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kd_id = models.IntegerField(db_column='KD_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_DEPT'


class WkTUserInd(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ki_id = models.IntegerField(db_column='KI_ID', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_IND'


class WkTUserLocalyjkeyws(models.Model):
    kk_id = models.AutoField(db_column='KK_ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kk_name = models.TextField(db_column='KK_NAME', blank=True, null=True)  # Field name made lowercase.
    kk_relation = models.CharField(db_column='KK_RELATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_not = models.TextField(db_column='KK_NOT', blank=True, null=True)  # Field name made lowercase.
    kk_keywords = models.TextField(db_column='KK_KEYWORDS', blank=True, null=True)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_must = models.TextField(db_column='KK_MUST', blank=True, null=True)  # Field name made lowercase.
    kk_should = models.TextField(db_column='KK_SHOULD', blank=True, null=True)  # Field name made lowercase.
    kk_event = models.TextField(db_column='KK_EVENT', blank=True, null=True)  # Field name made lowercase.
    kk_time = models.CharField(db_column='KK_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_keywstype = models.CharField(db_column='KK_KEYWSTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_LOCALYJKEYWS'


class WkTUserLoginLog(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ku_lid = models.CharField(db_column='KU_LID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kl_ip = models.CharField(db_column='KL_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kl_work = models.CharField(db_column='KL_WORK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kl_modular = models.CharField(db_column='KL_MODULAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kl_platform = models.CharField(db_column='KL_PLATFORM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kl_user = models.CharField(db_column='KL_USER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kl_useragent = models.CharField(db_column='KL_USERAGENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arg2 = models.CharField(db_column='ARG2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='is_Synchronized', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_status = models.CharField(db_column='KU_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_LOGIN_LOG'


class WkTUserRemarks(models.Model):
    msuid = models.IntegerField(db_column='msUid')  # Field name made lowercase.
    oldstatus = models.CharField(db_column='oldStatus', max_length=2)  # Field name made lowercase.
    newstatus = models.CharField(db_column='newStatus', max_length=2)  # Field name made lowercase.
    remarkcontent = models.TextField(db_column='remarkContent')  # Field name made lowercase.
    remarkfile = models.CharField(db_column='remarkFile', max_length=255)  # Field name made lowercase.
    dingtalkid = models.CharField(db_column='dingTalkId', max_length=100)  # Field name made lowercase.
    dingtalkname = models.CharField(db_column='dingTalkName', max_length=100)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_REMARKS'


class WkTUserStatusLog(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    ku_status = models.CharField(db_column='KU_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kl_id = models.CharField(db_column='KL_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kl_time = models.CharField(db_column='KL_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_old_status = models.CharField(db_column='KU_OLD_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_STATUS_LOG'


class WkTUserYjkeyws(models.Model):
    kk_id = models.IntegerField(db_column='KK_ID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kk_relation = models.CharField(db_column='KK_RELATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_not = models.CharField(db_column='KK_NOT', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kk_keywords = models.CharField(db_column='KK_KEYWORDS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_must = models.CharField(db_column='KK_MUST', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_should = models.CharField(db_column='KK_SHOULD', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_event = models.CharField(db_column='KK_EVENT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_time = models.CharField(db_column='KK_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_keywstype = models.CharField(db_column='KK_KEYWSTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_USER_YJKEYWS'


class WkTValidationInfo(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.TextField(db_column='KV_TITLE', blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.TextField(db_column='KV_URL', blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.BigIntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.BigIntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.BigIntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.BigIntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.BigIntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_templet = models.CharField(db_column='KV_TEMPLET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_sna_flag = models.CharField(db_column='KV_SNA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_index_flag = models.CharField(db_column='KV_INDEX_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.BigIntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kv_insert_time = models.CharField(db_column='KV_INSERT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_qc_time = models.CharField(db_column='KV_QC_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dy_time = models.CharField(db_column='KV_DY_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_zf_time = models.CharField(db_column='KV_ZF_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dk_time = models.CharField(db_column='KV_DK_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_titlesimhash = models.CharField(db_column='KV_TITLESIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_titlekeywords = models.TextField(db_column='KV_TITLEKEYWORDS', blank=True, null=True)  # Field name made lowercase.
    kv_insideforwardstatus = models.IntegerField(db_column='KV_INSIDEFORWARDSTATUS', blank=True, null=True)  # Field name made lowercase.
    kv_insideforwardcount = models.IntegerField(db_column='KV_INSIDEFORWARDCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_contentsimhash = models.CharField(db_column='KV_CONTENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_contentkeywords = models.CharField(db_column='KV_CONTENTKEYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_titlerefhash = models.TextField(db_column='KV_TITLEREFHASH', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.
    kv_procince = models.CharField(db_column='KV_PROCINCE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_cite = models.CharField(db_column='KV_CITE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_county = models.CharField(db_column='KV_COUNTY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_fansnum = models.IntegerField(db_column='KV_FANSNUM', blank=True, null=True)  # Field name made lowercase.
    kv_area = models.CharField(db_column='KV_AREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_messagenum = models.IntegerField(db_column='KV_MESSAGENUM', blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_isyj = models.CharField(db_column='KV_ISYJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    firsttime = models.CharField(db_column='firstTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstweb = models.CharField(db_column='firstWeb', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isfeedback = models.CharField(max_length=255, blank=True, null=True)
    ismyattention = models.CharField(max_length=255, blank=True, null=True)
    isread = models.CharField(max_length=255, blank=True, null=True)
    isyj = models.CharField(max_length=255, blank=True, null=True)
    kkid = models.CharField(max_length=255, blank=True, null=True)
    krinfotype = models.CharField(db_column='krInfotype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    krkeywordid = models.CharField(db_column='krKeywordid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    krstate = models.CharField(db_column='krState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ksinfo = models.CharField(db_column='ksInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kstype = models.CharField(db_column='ksType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ksuuid = models.CharField(db_column='ksUuid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kvcontent = models.CharField(db_column='kvContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kvhot = models.CharField(db_column='kvHot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    importancescore = models.CharField(db_column='importanceScore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kvarg1 = models.CharField(db_column='kvArg1', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_INFO'


class WkTValidationInfocnt(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_INFOCNT'


class WkTValidationInfocnt20160614(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_INFOCNT_20160614'


class WkTValidationInfocnt20160615(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_INFOCNT_20160615'


class WkTValidationInfo20160614(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
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
    kv_procince = models.CharField(db_column='KV_PROCINCE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_cite = models.CharField(db_column='KV_CITE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_county = models.CharField(db_column='KV_COUNTY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_fansnum = models.IntegerField(db_column='KV_FANSNUM', blank=True, null=True)  # Field name made lowercase.
    kv_area = models.CharField(db_column='KV_AREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_messagenum = models.IntegerField(db_column='KV_MESSAGENUM', blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_isyj = models.CharField(db_column='KV_ISYJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_INFO_20160614'


class WkTValidationInfo20160615(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
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
    kv_procince = models.CharField(db_column='KV_PROCINCE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_cite = models.CharField(db_column='KV_CITE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_county = models.CharField(db_column='KV_COUNTY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    kv_fansnum = models.IntegerField(db_column='KV_FANSNUM', blank=True, null=True)  # Field name made lowercase.
    kv_area = models.CharField(db_column='KV_AREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_wbauthorpic = models.CharField(db_column='KV_WBAUTHORPIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_messagenum = models.IntegerField(db_column='KV_MESSAGENUM', blank=True, null=True)  # Field name made lowercase.
    kv_arg1 = models.CharField(db_column='KV_ARG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg2 = models.CharField(db_column='KV_ARG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg3 = models.CharField(db_column='KV_ARG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_arg4 = models.CharField(db_column='KV_ARG4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_siteid = models.CharField(db_column='KV_SITEID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    losttime = models.CharField(db_column='LOSTTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entityarea = models.CharField(db_column='ENTITYAREA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitypeople = models.CharField(db_column='ENTITYPEOPLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitymethanism = models.CharField(db_column='ENTITYMETHANISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_isyj = models.CharField(db_column='KV_ISYJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    noisestatus = models.CharField(db_column='NOISESTATUS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kv_classlyone = models.CharField(db_column='KV_CLASSLYONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlytwo = models.CharField(db_column='KV_CLASSLYTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlythree = models.CharField(db_column='KV_CLASSLYTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfone = models.CharField(db_column='KV_CLASSLYZFONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzftwo = models.CharField(db_column='KV_CLASSLYZFTWO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_classlyzfthree = models.CharField(db_column='KV_CLASSLYZFTHREE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_INFO_20160615'


class WkTValidationLocationrefHxs(models.Model):
    kl_uuid = models.CharField(db_column='KL_UUID', max_length=40)  # Field name made lowercase.
    kr_uuid = models.CharField(db_column='KR_UUID', max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID', blank=True, null=True)  # Field name made lowercase.
    kr_provinceid = models.CharField(db_column='KR_PROVINCEID', max_length=40)  # Field name made lowercase.
    kr_cityid = models.CharField(db_column='KR_CITYID', max_length=40)  # Field name made lowercase.
    kr_countyid = models.CharField(db_column='KR_COUNTYID', max_length=40)  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20)  # Field name made lowercase.
    kv_dtctime = models.DateTimeField(db_column='KV_DTCTIME')  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=50)  # Field name made lowercase.
    arg1 = models.CharField(db_column='ARG1', max_length=50)  # Field name made lowercase.
    town = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_LOCATIONREF_HXS'


class WkTValidationYjinfo(models.Model):
    ky_uuid = models.CharField(db_column='KY_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.TextField(db_column='KV_TITLE', blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.TextField(db_column='KV_URL', blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.BigIntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.BigIntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.BigIntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.BigIntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.BigIntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_templet = models.CharField(db_column='KV_TEMPLET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_sna_flag = models.CharField(db_column='KV_SNA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_index_flag = models.CharField(db_column='KV_INDEX_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.BigIntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kv_insert_time = models.CharField(db_column='KV_INSERT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_qc_time = models.CharField(db_column='KV_QC_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dy_time = models.CharField(db_column='KV_DY_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_zf_time = models.CharField(db_column='KV_ZF_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_dk_time = models.CharField(db_column='KV_DK_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_titlesimhash = models.CharField(db_column='KV_TITLESIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_titlekeywords = models.TextField(db_column='KV_TITLEKEYWORDS', blank=True, null=True)  # Field name made lowercase.
    kv_insideforwardstatus = models.IntegerField(db_column='KV_INSIDEFORWARDSTATUS', blank=True, null=True)  # Field name made lowercase.
    kv_insideforwardcount = models.IntegerField(db_column='KV_INSIDEFORWARDCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_contentsimhash = models.CharField(db_column='KV_CONTENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_contentkeywords = models.CharField(db_column='KV_CONTENTKEYWORDS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_titlerefhash = models.TextField(db_column='KV_TITLEREFHASH', blank=True, null=True)  # Field name made lowercase.
    kv_istf = models.IntegerField(db_column='KV_ISTF', blank=True, null=True)  # Field name made lowercase.
    kv_isrd = models.IntegerField(db_column='KV_ISRD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_YJINFO'


class WkTValidationYjinfocnt(models.Model):
    ky_uuid = models.CharField(db_column='KY_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VALIDATION_YJINFOCNT'


class WkTVersionupgradeLog(models.Model):
    username = models.CharField(max_length=50)
    userid = models.CharField(max_length=20)
    action = models.CharField(max_length=50)
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'WK_T_VERSIONUPGRADE_LOG'


class WkTVersionPatch(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    version_no = models.CharField(db_column='VERSION_NO', max_length=20)  # Field name made lowercase.
    patch_no = models.CharField(db_column='PATCH_NO', max_length=20)  # Field name made lowercase.
    patch_path = models.CharField(db_column='PATCH_PATH', max_length=200)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=1)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VERSION_PATCH'


class WkTVideo(models.Model):
    kv_uuid = models.CharField(db_column='KV_UUID', primary_key=True, max_length=64)  # Field name made lowercase.
    kv_filename = models.CharField(db_column='KV_FILENAME', max_length=255)  # Field name made lowercase.
    kv_tmurl = models.CharField(db_column='KV_TMURL', max_length=255)  # Field name made lowercase.
    kv_smburl = models.CharField(db_column='KV_SMBURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kv_downtime = models.CharField(db_column='KV_DOWNTIME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    kv_lastdownkuid = models.CharField(db_column='KV_LASTDOWNKUID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    kv_counts = models.IntegerField(db_column='KV_COUNTS', blank=True, null=True)  # Field name made lowercase.
    kv_remark = models.CharField(db_column='KV_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VIDEO'


class WkTVideorecord(models.Model):
    kr_uuid = models.CharField(db_column='KR_UUID', primary_key=True, max_length=64)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    kr_filename = models.CharField(db_column='KR_FILENAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    kr_tmurl = models.CharField(db_column='KR_TMURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_smburl = models.CharField(db_column='KR_SMBURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kr_downloadtime = models.CharField(db_column='KR_DOWNLOADTIME', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_VIDEORECORD'


class WkTWarnaccDinguser(models.Model):
    warnacc = models.IntegerField()
    dingid = models.CharField(max_length=32, blank=True, null=True)
    time = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_WARNACC_DINGUSER'


class WkTWarnaccUser(models.Model):
    warnacc = models.IntegerField()
    uid = models.IntegerField()
    type = models.IntegerField()
    oldyj = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_WARNACC_USER'


class WkTWarnspecialAlldinguser(models.Model):
    kw_id = models.AutoField(db_column='KW_ID', primary_key=True)  # Field name made lowercase.
    kw_dname = models.CharField(db_column='KW_DNAME', max_length=50)  # Field name made lowercase.
    kw_dingid = models.CharField(db_column='KW_DINGID', max_length=40)  # Field name made lowercase.
    kw_dgroup = models.CharField(db_column='KW_DGROUP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kw_position = models.CharField(db_column='KW_POSITION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kw_mobile = models.CharField(db_column='KW_MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WARNSPECIAL_ALLDINGUSER'


class WkTWarnspecialDinguser(models.Model):
    kw_id = models.AutoField(db_column='KW_ID', primary_key=True)  # Field name made lowercase.
    ks_id = models.CharField(db_column='KS_ID', max_length=40)  # Field name made lowercase.
    kw_dingid = models.CharField(db_column='KW_DINGID', max_length=40)  # Field name made lowercase.
    warn_acc = models.IntegerField(db_column='WARN_ACC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WARNSPECIAL_DINGUSER'


class WkTWarnspecialUser(models.Model):
    kw_id = models.AutoField(db_column='KW_ID', primary_key=True)  # Field name made lowercase.
    ks_id = models.CharField(db_column='KS_ID', max_length=50)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kw_type = models.IntegerField(db_column='KW_TYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WARNSPECIAL_USER'


class WkTWebsite(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='SITENAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    siteurl = models.CharField(db_column='SITEURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    kv_type = models.CharField(db_column='KV_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WEBSITE'


class WkTWebuserbacklog(models.Model):
    username = models.CharField(max_length=50)
    userid = models.IntegerField()
    action = models.CharField(max_length=50)
    type = models.IntegerField()
    wheres = models.TextField()
    param = models.TextField()
    users = models.CharField(max_length=50)
    uid = models.IntegerField()
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_T_WEBUSERBACKLOG'


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


class WkTWorkcopyright(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    registernumber = models.CharField(db_column='RegisterNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.CharField(db_column='RegisterDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    copyrightownername = models.CharField(db_column='CopyrightOwnerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    finishdate = models.CharField(db_column='FinishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='PublishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    releasedate = models.CharField(db_column='ReleaseDate', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WORKCOPYRIGHT'


class WkTWtfk(models.Model):
    kw_uuid = models.CharField(db_column='KW_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kw_time = models.CharField(db_column='KW_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kw_type = models.CharField(db_column='KW_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kw_opinion = models.CharField(db_column='KW_OPINION', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kv_id = models.CharField(db_column='KV_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kv_title = models.CharField(db_column='KV_TITLE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kv_source = models.CharField(db_column='KV_SOURCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kv_time = models.CharField(db_column='KV_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.IntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.IntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.IntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_abstract = models.CharField(db_column='KV_ABSTRACT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    kv_site = models.CharField(db_column='KV_SITE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kv_templet = models.CharField(db_column='KV_TEMPLET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kv_orientation = models.CharField(db_column='KV_ORIENTATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kv_flag = models.CharField(db_column='KV_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_sna_flag = models.CharField(db_column='KV_SNA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_index_flag = models.CharField(db_column='KV_INDEX_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_orien_level = models.IntegerField(db_column='KV_ORIEN_LEVEL', blank=True, null=True)  # Field name made lowercase.
    kv_insert_time = models.CharField(db_column='KV_INSERT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='is_Synchronized', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WTFK'


class WkTWtfkCnt(models.Model):
    kw_uuid = models.CharField(db_column='KW_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kv_ctime = models.CharField(db_column='KV_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='is_Synchronized', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WTFK_CNT'


class WkTWxkeyws(models.Model):
    kk_id = models.CharField(db_column='KK_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400)  # Field name made lowercase.
    kk_must = models.CharField(db_column='KK_MUST', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_should = models.CharField(db_column='KK_SHOULD', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_event = models.CharField(db_column='KK_EVENT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_time = models.CharField(db_column='KK_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_sort = models.IntegerField(db_column='KK_SORT', blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_WXKEYWS'


class WkTYqjb1(models.Model):
    ky_uuid = models.CharField(db_column='KY_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ky_title = models.CharField(db_column='KY_TITLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    kuid = models.CharField(db_column='KUID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ky_time = models.CharField(db_column='KY_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_YQJB1'


class WkTYqmsonlyuser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    t_uid = models.CharField(db_column='T_UID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    u_name = models.CharField(db_column='U_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    macid = models.CharField(db_column='MACID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PHONETYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    channeltype = models.CharField(db_column='CHANNELTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='USERTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    channelid = models.CharField(db_column='CHANNELID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pushuid = models.CharField(db_column='PUSHUID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    communicationid = models.CharField(db_column='COMMUNICATIONID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_YQMSONLYUSER'


class WkTYqmsywpushnews(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t_uid = models.CharField(db_column='T_UID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    macid = models.CharField(db_column='MACID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_YQMSYWPUSHNEWS'


class WkTYqmsywuser(models.Model):
    user_id = models.CharField(db_column='ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    t_uid = models.CharField(db_column='T_UID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    macid = models.CharField(db_column='MACID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_YQMSYWUSER'


class WkTYsDomain(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    sponsorname = models.CharField(db_column='SponsorName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    urllist = models.CharField(db_column='UrlList', max_length=500, blank=True, null=True)  # Field name made lowercase.
    websitename = models.CharField(db_column='WebSiteName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    possibledelete = models.CharField(db_column='PossibleDelete', max_length=500, blank=True, null=True)  # Field name made lowercase.
    recordnumber = models.CharField(db_column='RecordNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.
    checkdate = models.CharField(db_column='CheckDate', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sponsorproperty = models.CharField(db_column='SponsorProperty', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_YS_DOMAIN'


class WkTYtjUser(models.Model):
    ku_id = models.IntegerField(db_column='KU_ID', primary_key=True)  # Field name made lowercase.
    ku_lid = models.CharField(db_column='KU_LID', unique=True, max_length=100)  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ku_passwd = models.CharField(db_column='KU_PASSWD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_regdate = models.CharField(db_column='KU_REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_status = models.CharField(db_column='KU_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ku_sex = models.CharField(db_column='KU_SEX', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ku_birthday = models.CharField(db_column='KU_BIRTHDAY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ku_email = models.CharField(db_column='KU_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_phone = models.CharField(db_column='KU_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ku_company = models.CharField(db_column='KU_COMPANY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kd_id = models.IntegerField(db_column='KD_ID', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'WK_T_YTJ_USER'


class WkTYtjUserbaseinfo(models.Model):
    ku_uuid = models.AutoField(db_column='KU_UUID', primary_key=True)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_type = models.CharField(db_column='KU_TYPE', max_length=50)  # Field name made lowercase.
    ku_value = models.TextField(db_column='KU_VALUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WK_T_YTJ_USERBASEINFO'
        unique_together = (('ku_id', 'ku_type'),)


class WkTYtjUserservice(models.Model):
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
    ku_report_condition = models.CharField(db_column='KU_REPORT_CONDITION', max_length=2000, blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'WK_T_YTJ_USERSERVICE'


class WkTYtjUserAreaNew(models.Model):
    ku_id = models.IntegerField(unique=True)
    province_id = models.CharField(max_length=40, blank=True, null=True)
    city_id = models.CharField(max_length=40, blank=True, null=True)
    county_id = models.CharField(max_length=40, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WK_T_YTJ_USER_AREA_NEW'


class WkUserWarming(models.Model):
    uid = models.CharField(max_length=38)
    name = models.CharField(max_length=40)
    warningtimetype = models.CharField(db_column='warningTimeType', max_length=100)  # Field name made lowercase.
    isopenwarning = models.IntegerField(db_column='isOpenWarning')  # Field name made lowercase.
    warningendtime = models.CharField(db_column='warningEndTime', max_length=32)  # Field name made lowercase.
    type = models.IntegerField()
    firstopen = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'WK_USER_WARMING'


class WtKSubrelation(models.Model):
    ks_id = models.CharField(db_column='KS_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ks_pid = models.CharField(db_column='KS_PID', max_length=50)  # Field name made lowercase.
    ks_sid = models.CharField(db_column='KS_SID', max_length=50)  # Field name made lowercase.
    ks_ctime = models.CharField(db_column='KS_CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=10)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    is_parent = models.CharField(db_column='IS_PARENT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ks_index = models.IntegerField(db_column='KS_INDEX', blank=True, null=True)  # Field name made lowercase.
    kc_index = models.IntegerField(db_column='KC_INDEX', blank=True, null=True)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ks_share = models.IntegerField(db_column='KS_SHARE', blank=True, null=True)  # Field name made lowercase.
    ks_attrbute = models.IntegerField(db_column='KS_ATTRBUTE', blank=True, null=True)  # Field name made lowercase.
    ks_havesonsub = models.IntegerField(db_column='KS_HAVESONSUB', blank=True, null=True)  # Field name made lowercase.
    ks_istop = models.IntegerField(db_column='KS_ISTOP', blank=True, null=True)  # Field name made lowercase.
    ks_onlymatchsub = models.CharField(db_column='KS_ONLYMATCHSUB', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_isshared = models.CharField(db_column='KS_ISSHARED', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_containsub = models.CharField(db_column='KS_CONTAINSUB', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_iscollection = models.CharField(db_column='KS_ISCOLLECTION', max_length=4, blank=True, null=True)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_is_sync = models.CharField(db_column='KS_IS_SYNC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_ref_subject_id = models.CharField(db_column='KS_REF_SUBJECT_ID', max_length=100)  # Field name made lowercase.
    ks_filter_domain = models.TextField(db_column='KS_FILTER_DOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ks_filter_region = models.TextField(db_column='KS_FILTER_REGION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ks_is_open_precise_region = models.IntegerField(db_column='KS_IS_OPEN_PRECISE_REGION')  # Field name made lowercase.
    ismodify = models.CharField(db_column='ISMODIFY', max_length=2)  # Field name made lowercase.
    ks_only_match_precise = models.IntegerField(db_column='KS_ONLY_MATCH_PRECISE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WT_K_SUBRELATION'


class WtKSubrelationBackend(models.Model):
    ks_id = models.CharField(db_column='KS_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ks_pid = models.CharField(db_column='KS_PID', max_length=50)  # Field name made lowercase.
    ks_sid = models.CharField(db_column='KS_SID', max_length=50)  # Field name made lowercase.
    ks_ctime = models.CharField(db_column='KS_CTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=10)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    is_parent = models.CharField(db_column='IS_PARENT', max_length=2)  # Field name made lowercase.
    kc_uuid = models.CharField(db_column='KC_UUID', max_length=40)  # Field name made lowercase.
    ks_index = models.IntegerField(db_column='KS_INDEX')  # Field name made lowercase.
    kc_index = models.IntegerField(db_column='KC_INDEX')  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=2)  # Field name made lowercase.
    ks_share = models.IntegerField(db_column='KS_SHARE')  # Field name made lowercase.
    ks_attrbute = models.IntegerField(db_column='KS_ATTRBUTE')  # Field name made lowercase.
    ks_havesonsub = models.IntegerField(db_column='KS_HAVESONSUB')  # Field name made lowercase.
    ks_istop = models.IntegerField(db_column='KS_ISTOP')  # Field name made lowercase.
    ks_onlymatchsub = models.CharField(db_column='KS_ONLYMATCHSUB', max_length=45)  # Field name made lowercase.
    ks_isshared = models.CharField(db_column='KS_ISSHARED', max_length=45)  # Field name made lowercase.
    ks_containsub = models.CharField(db_column='KS_CONTAINSUB', max_length=45)  # Field name made lowercase.
    ks_iscollection = models.CharField(db_column='KS_ISCOLLECTION', max_length=4, blank=True, null=True)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_is_sync = models.CharField(db_column='KS_IS_SYNC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ks_classificationid = models.IntegerField(db_column='KS_CLASSIFICATIONID', blank=True, null=True)  # Field name made lowercase.
    ks_is_open_precise_region = models.IntegerField(db_column='KS_IS_OPEN_PRECISE_REGION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WT_K_SUBRELATION_BACKEND'


class Yjclusteruser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    titles = models.CharField(db_column='TITLES', max_length=500, blank=True, null=True)  # Field name made lowercase.
    simhash = models.CharField(db_column='SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parentsimhash = models.CharField(db_column='PARENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    simhashs = models.CharField(db_column='SIMHASHS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zfxx = models.IntegerField(db_column='ZFXX', blank=True, null=True)  # Field name made lowercase.
    titlewords = models.CharField(db_column='TITLEWORDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YJCLUSTERUSER'


class YqzbTCkey(models.Model):
    kk_uuid = models.CharField(db_column='KK_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kt_uuid = models.CharField(db_column='KT_UUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kk_ctime = models.CharField(db_column='KK_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kk_state = models.CharField(db_column='KK_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kk_not = models.CharField(db_column='KK_NOT', max_length=400)  # Field name made lowercase.
    kk_type = models.CharField(db_column='KK_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kk_caled = models.CharField(db_column='KK_CALED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_CKEY'


class YqzbTEngineInfo(models.Model):
    uuid = models.CharField(db_column='UUID', primary_key=True, max_length=140)  # Field name made lowercase.
    kt_uuid = models.CharField(db_column='KT_UUID', max_length=40)  # Field name made lowercase.
    kn_type = models.CharField(db_column='KN_TYPE', max_length=2)  # Field name made lowercase.
    kn_title = models.CharField(db_column='KN_TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kn_source = models.CharField(db_column='KN_SOURCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kn_url = models.CharField(db_column='KN_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kn_time = models.CharField(db_column='KN_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kn_ctime = models.CharField(db_column='KN_CTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kn_repeatcount = models.IntegerField(db_column='KN_REPEATCOUNT', blank=True, null=True)  # Field name made lowercase.
    kn_abstract = models.CharField(db_column='KN_ABSTRACT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kv_visitcount = models.IntegerField(db_column='KV_VISITCOUNT', blank=True, null=True)  # Field name made lowercase.
    kv_reply = models.IntegerField(db_column='KV_REPLY', blank=True, null=True)  # Field name made lowercase.
    kv_collection = models.IntegerField(db_column='KV_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    kv_transport = models.IntegerField(db_column='KV_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    kv_repeat = models.IntegerField(db_column='KV_REPEAT', blank=True, null=True)  # Field name made lowercase.
    kv_state = models.CharField(db_column='KV_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kn_site = models.CharField(db_column='KN_SITE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kn_orientation = models.CharField(db_column='KN_ORIENTATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kn_author = models.CharField(db_column='KN_AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kn_topicuid = models.CharField(db_column='KN_TOPICUID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kn_inputtype = models.CharField(db_column='KN_INPUTTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kn_orien_level = models.CharField(db_column='KN_ORIEN_LEVEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kn_fanscount = models.IntegerField(db_column='KN_FANSCOUNT', blank=True, null=True)  # Field name made lowercase.
    kn_content = models.CharField(db_column='KN_CONTENT', max_length=3500, blank=True, null=True)  # Field name made lowercase.
    kn_jingwai = models.CharField(db_column='KN_JINGWAI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kn_titleseg = models.CharField(db_column='KN_TITLESEG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kn_topicwords = models.CharField(db_column='KN_TOPICWORDS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    kn_zyinfo = models.CharField(db_column='KN_ZYINFO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kt_weibouid = models.CharField(db_column='KT_WEIBOUID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kn_arg = models.CharField(db_column='KN_ARG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    configid = models.CharField(db_column='ConfigID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    autoclassly = models.CharField(db_column='AUTOCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    classlytype = models.CharField(db_column='CLASSLYTYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    classlyinfo = models.CharField(db_column='CLASSLYINFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzmclassly = models.CharField(db_column='GDZMCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdfmclassly = models.CharField(db_column='GDFMCLASSLY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdfmclasslyinfo = models.CharField(db_column='GDFMCLASSLYINFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzmclasslyinfo = models.CharField(db_column='GDZMCLASSLYINFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gdzfxx = models.CharField(db_column='GDZFXX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sheng = models.CharField(max_length=50, blank=True, null=True)
    shi = models.CharField(max_length=50, blank=True, null=True)
    xian = models.CharField(max_length=50, blank=True, null=True)
    jigou = models.CharField(max_length=100, blank=True, null=True)
    gdinfo = models.CharField(db_column='GDINFO', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=20, blank=True, null=True)
    webnamedomain = models.CharField(db_column='WEBNAMEDOMAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    webnamelever = models.CharField(db_column='WEBNAMELEVER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    verified = models.CharField(max_length=20, blank=True, null=True)
    userid = models.CharField(db_column='USERID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    screen_name = models.CharField(max_length=50, blank=True, null=True)
    kn_arg1 = models.CharField(db_column='KN_ARG1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kn_arg2 = models.CharField(db_column='KN_ARG2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kn_arg3 = models.CharField(db_column='KN_ARG3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kn_arg4 = models.CharField(db_column='KN_ARG4', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_ENGINE_INFO'


class YqzbTQq(models.Model):
    kq_uuid = models.CharField(db_column='KQ_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kq_qqno = models.CharField(db_column='KQ_QQNO', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kq_psw = models.CharField(db_column='KQ_PSW', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kq_summary = models.CharField(db_column='KQ_SUMMARY', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    kq_time = models.CharField(db_column='KQ_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_QQ'


class YqzbTQqmes(models.Model):
    km_uuid = models.CharField(db_column='KM_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    kq_no = models.CharField(db_column='KQ_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kq_name = models.CharField(db_column='KQ_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_qqnum = models.CharField(db_column='KM_QQNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_postnum = models.CharField(db_column='KM_POSTNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_time = models.CharField(db_column='KM_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    km_content = models.TextField(db_column='KM_CONTENT', blank=True, null=True)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    km_state = models.CharField(db_column='KM_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    km_isdelete = models.IntegerField(db_column='KM_ISDELETE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_QQMES'


class YqzbTSyncLog(models.Model):
    ks_id = models.CharField(db_column='KS_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    ks_type = models.CharField(db_column='KS_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ks_tablename = models.CharField(db_column='KS_TABLENAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ks_time = models.CharField(db_column='KS_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ks_time_used = models.CharField(db_column='KS_TIME_USED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ks_description = models.CharField(db_column='KS_DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_SYNC_LOG'


class YqzbTTopic(models.Model):
    kt_uuid = models.CharField(db_column='KT_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    kt_name = models.CharField(db_column='KT_NAME', max_length=400)  # Field name made lowercase.
    kt_summary = models.CharField(db_column='KT_SUMMARY', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kt_begin = models.CharField(db_column='KT_BEGIN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    kt_end = models.CharField(db_column='KT_END', max_length=14, blank=True, null=True)  # Field name made lowercase.
    kt_interval = models.IntegerField(db_column='KT_INTERVAL', blank=True, null=True)  # Field name made lowercase.
    kt_status = models.CharField(db_column='KT_STATUS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    kk_name = models.CharField(db_column='KK_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kt_time = models.CharField(db_column='KT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kt_expression = models.CharField(db_column='KT_EXPRESSION', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kt_not = models.CharField(db_column='KT_NOT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    kk_closetime = models.CharField(db_column='KK_CLOSETIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kt_is_logic = models.CharField(db_column='KT_IS_LOGIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kt_isnew = models.IntegerField(db_column='KT_ISNEW', blank=True, null=True)  # Field name made lowercase.
    kt_isshared = models.IntegerField(db_column='KT_ISSHARED', blank=True, null=True)  # Field name made lowercase.
    kt_sharedtime = models.CharField(db_column='KT_SHAREDTIME', max_length=32)  # Field name made lowercase.
    kt_cancelsharedtime = models.CharField(db_column='KT_CANCELSHAREDTIME', max_length=32)  # Field name made lowercase.
    kt_isdelete = models.IntegerField(db_column='KT_ISDELETE')  # Field name made lowercase.
    snapshoturl = models.CharField(db_column='snapshotUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    appsnapshoturl = models.CharField(db_column='appSnapshotUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    faceimgurl = models.CharField(db_column='faceImgUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_set_home = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'YQZB_T_TOPIC'


class YqzbTTopicModuleSummary(models.Model):
    event_id = models.CharField(max_length=64)
    module_id = models.IntegerField()
    summary = models.CharField(max_length=500, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'YQZB_T_TOPIC_MODULE_SUMMARY'
        unique_together = (('event_id', 'module_id'),)


class YqzbTWeixin(models.Model):
    kw_uuid = models.CharField(db_column='KW_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=100)  # Field name made lowercase.
    kw_wxno = models.CharField(db_column='KW_WXNO', max_length=200)  # Field name made lowercase.
    kw_nickname = models.CharField(db_column='KW_NICKNAME', max_length=200)  # Field name made lowercase.
    kw_psw = models.CharField(db_column='KW_PSW', max_length=200)  # Field name made lowercase.
    kw_summary = models.CharField(db_column='KW_SUMMARY', max_length=200)  # Field name made lowercase.
    kw_time = models.CharField(db_column='KW_TIME', max_length=20)  # Field name made lowercase.
    oracle_mysql_uuid = models.CharField(db_column='ORACLE_MYSQL_UUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_synchronized = models.CharField(db_column='IS_SYNCHRONIZED', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_WEIXIN'


class YqzbTWxmsg(models.Model):
    km_uuid = models.CharField(db_column='KM_UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    km_wxno = models.CharField(db_column='KM_WXNO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_name = models.CharField(db_column='KM_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_wxnum = models.CharField(db_column='KM_WXNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_nickname = models.CharField(db_column='KM_NICKNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_time = models.CharField(db_column='KM_TIME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    km_postnum = models.CharField(db_column='KM_POSTNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    km_content = models.TextField(db_column='KM_CONTENT', blank=True, null=True)  # Field name made lowercase.
    kk_id = models.CharField(db_column='KK_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ku_id = models.CharField(db_column='KU_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    km_state = models.CharField(db_column='KM_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    km_isdelete = models.IntegerField(db_column='KM_ISDELETE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_WXMSG'


class YqzbTYjxx(models.Model):
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
    kv_content = models.TextField(db_column='KV_CONTENT', blank=True, null=True)  # Field name made lowercase.
    ks_url = models.CharField(db_column='KS_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YQZB_T_YJXX'


class Ytjcrmaccountmapping(models.Model):
    msuid = models.IntegerField(db_column='msUid', primary_key=True)  # Field name made lowercase.
    msname = models.CharField(db_column='msName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.IntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'YTJCRMACCOUNTMAPPING'


class Zycluster(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    titles = models.CharField(db_column='TITLES', max_length=500, blank=True, null=True)  # Field name made lowercase.
    simhash = models.CharField(db_column='SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parentsimhash = models.CharField(db_column='PARENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    simhashs = models.CharField(db_column='SIMHASHS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zfxx = models.IntegerField(db_column='ZFXX', blank=True, null=True)  # Field name made lowercase.
    titlewords = models.CharField(db_column='TITLEWORDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZYCLUSTER'


class Zyclusteruser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    titles = models.CharField(db_column='TITLES', max_length=500, blank=True, null=True)  # Field name made lowercase.
    simhash = models.CharField(db_column='SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parentsimhash = models.CharField(db_column='PARENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    simhashs = models.CharField(db_column='SIMHASHS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zfxx = models.IntegerField(db_column='ZFXX', blank=True, null=True)  # Field name made lowercase.
    titlewords = models.CharField(db_column='TITLEWORDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZYCLUSTERUSER'


class Zywhiteuser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    titles = models.CharField(db_column='TITLES', max_length=500, blank=True, null=True)  # Field name made lowercase.
    simhash = models.CharField(db_column='SIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parentsimhash = models.CharField(db_column='PARENTSIMHASH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    simhashs = models.CharField(db_column='SIMHASHS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zfxx = models.IntegerField(db_column='ZFXX', blank=True, null=True)  # Field name made lowercase.
    titlewords = models.CharField(db_column='TITLEWORDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZYWHITEUSER'


class Zywords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    wordtype = models.CharField(db_column='WordType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pn = models.CharField(db_column='PN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    word = models.CharField(db_column='Word', max_length=30, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    doccount = models.IntegerField(db_column='DocCount', blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='ADDTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZYWORDS'


class Aaa(models.Model):
    timeline = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aaa'


class AppImportData(models.Model):
    appwords = models.CharField(max_length=500, blank=True, null=True)
    apppictures = models.CharField(max_length=300, blank=True, null=True)
    appvoices = models.CharField(max_length=300, blank=True, null=True)
    appuserid = models.CharField(max_length=50, blank=True, null=True)
    inputdate = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    edition = models.CharField(max_length=30, blank=True, null=True)
    valid = models.CharField(max_length=5, blank=True, null=True)
    appusername = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_import_data'


class AppUsageStatistics(models.Model):
    package_name = models.CharField(max_length=500, blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=45, blank=True, null=True)
    userid = models.CharField(max_length=45, blank=True, null=True)
    device_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_usage_statistics'
        unique_together = (('package_name', 'date'),)


class Artificialearlywarning(models.Model):
    id = models.BigAutoField(primary_key=True)
    crmuid = models.CharField(db_column='crmUid', max_length=32)  # Field name made lowercase.
    startdate = models.CharField(db_column='startDate', max_length=100)  # Field name made lowercase.
    enddate = models.CharField(db_column='endDate', max_length=100)  # Field name made lowercase.
    trytype = models.CharField(db_column='tryType', max_length=255)  # Field name made lowercase.
    pushperson = models.CharField(db_column='pushPerson', max_length=100)  # Field name made lowercase.
    buytype = models.CharField(db_column='buyType', max_length=255)  # Field name made lowercase.
    pushtime = models.CharField(db_column='pushTime', max_length=255)  # Field name made lowercase.
    feedback = models.TextField()
    accountname = models.CharField(db_column='accountName', max_length=100)  # Field name made lowercase.
    remarks = models.TextField()

    class Meta:
        managed = False
        db_table = 'artificialEarlyWarning'


class DatacountAccurateCondition(models.Model):
    edate = models.IntegerField()
    euser = models.CharField(max_length=255, blank=True, null=True)
    kv_titlematch = models.CharField(db_column='KV_TITLEMATCH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_mustwordminindex = models.IntegerField(db_column='KV_MUSTWORDMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_keywordsminindex = models.IntegerField(db_column='KV_KEYWORDSMININDEX', blank=True, null=True)  # Field name made lowercase.
    kv_onlylocal = models.CharField(db_column='KV_ONLYLOCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_weiboovertime = models.CharField(db_column='KV_WEIBOOVERTIME', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_weibosignlocalnoise = models.CharField(db_column='KV_WEIBOSIGNLOCALNOISE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_weibotopicnoise = models.CharField(db_column='KV_WEIBOTOPICNOISE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kv_weiboatnoise = models.CharField(db_column='KV_WEIBOATNOISE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    count_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datacount_accurate_condition'


class Datestatus(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    curdate = models.CharField(unique=True, max_length=8)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'datestatus'


class FgCourt(models.Model):
    fg_id = models.CharField(primary_key=True, max_length=50)
    fg_fy = models.CharField(max_length=50, blank=True, null=True)
    fg_bm = models.CharField(max_length=30, blank=True, null=True)
    fg_name = models.CharField(max_length=20)
    fg_zw = models.CharField(max_length=30, blank=True, null=True)
    fg_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fg_court'


class HomepageHeadlinesInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cover = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    poster = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(unique=True, max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    news_id = models.CharField(max_length=50, blank=True, null=True)
    content_abstract = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homepage_headlines_info'


class LawProtect(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'law_protect'


class MobileLibrary(models.Model):
    id = models.BigAutoField(primary_key=True)
    mobile = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mobile_library'


class MsAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    sso_account_id = models.IntegerField()
    account = models.CharField(max_length=200)
    password = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    wechat = models.CharField(max_length=200, blank=True, null=True)
    template = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    identity = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    product_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ms_account'


class MsEventKeywordsGroup(models.Model):
    subjectid = models.CharField(db_column='subjectId', max_length=45)  # Field name made lowercase.
    classifyid = models.IntegerField(db_column='classifyId')  # Field name made lowercase.
    classifypid = models.IntegerField(db_column='classifyPid')  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=45)  # Field name made lowercase.
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_event_keywords_group'


class MsEventKeywordsGroupSubjectRelation(models.Model):
    subjectid = models.CharField(db_column='subjectId', max_length=45)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=45)  # Field name made lowercase.
    isselectall = models.IntegerField(db_column='isSelectAll')  # Field name made lowercase.
    keywords = models.CharField(db_column='keyWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    addedtime = models.DateTimeField(db_column='addedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ms_event_keywords_group_subject_relation'


class MsIndustryCategory(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=45)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_industry_category'


class MsNavigation(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=45, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_navigation'


class MsOutbox(models.Model):
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    username = models.CharField(max_length=45, blank=True, null=True)
    hostname = models.CharField(max_length=45, blank=True, null=True)
    agent_id = models.CharField(max_length=45, blank=True, null=True)
    userid = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ms_outbox'


class MsShareInfo(models.Model):
    userid = models.IntegerField()
    url = models.CharField(max_length=500)
    type = models.IntegerField()
    pid = models.CharField(max_length=45)
    time = models.DateTimeField(blank=True, null=True)
    snapshot_url = models.CharField(max_length=500, blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ms_share_info'


class MsSourceType(models.Model):
    sourcename = models.CharField(db_column='sourceName', max_length=45)  # Field name made lowercase.
    sourcecode = models.CharField(db_column='sourceCode', max_length=45)  # Field name made lowercase.
    sourceindex = models.IntegerField(db_column='sourceIndex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ms_source_type'


class MsSubject(models.Model):
    subject_id = models.CharField(primary_key=True, max_length=32)
    pid = models.CharField(max_length=32, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    subject_name = models.CharField(max_length=45, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    shared = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    subject_type = models.IntegerField(blank=True, null=True)
    subject_state = models.IntegerField(blank=True, null=True)
    region_word = models.TextField(blank=True, null=True)
    entity_word = models.TextField(blank=True, null=True)
    event_word = models.TextField(blank=True, null=True)
    expression = models.TextField(blank=True, null=True)
    negative_word = models.TextField(blank=True, null=True)
    ambiguous_word = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    push = models.IntegerField(blank=True, null=True)
    data_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    region_word_pos = models.IntegerField(blank=True, null=True)
    word_distance = models.IntegerField(blank=True, null=True)
    push_media = models.TextField(blank=True, null=True)  # This field type is a guess.
    push_attitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    push_word = models.TextField(blank=True, null=True)
    push_negative_word = models.TextField(blank=True, null=True)
    directional_media = models.TextField(blank=True, null=True)  # This field type is a guess.
    directional_domain = models.TextField(blank=True, null=True)  # This field type is a guess.
    directional_channel = models.TextField(blank=True, null=True)  # This field type is a guess.
    directional_author = models.TextField(blank=True, null=True)  # This field type is a guess.
    logic = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_subject'


class MsUserNavigation(models.Model):
    navigation_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=45, blank=True, null=True)
    index = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_user_navigation'


class MsYqscreenUser(models.Model):
    cname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    genre = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    industry = models.IntegerField(blank=True, null=True)
    did = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    county = models.IntegerField(blank=True, null=True)
    screen_num = models.IntegerField(blank=True, null=True)
    online_num = models.IntegerField(blank=True, null=True)
    msid = models.IntegerField(blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)
    endtime = models.CharField(max_length=8, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_yqscreen_user'


class Newtable(models.Model):
    name_id = models.IntegerField(blank=True, null=True)
    nane = models.CharField(max_length=50, blank=True, null=True)
    hash = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newTable'


class Num(models.Model):
    i = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'num'


class OfficalAdvertise(models.Model):
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    num = models.IntegerField()
    place = models.CharField(max_length=255)
    time = models.IntegerField()
    duty = models.TextField()
    describe = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'offical_advertise'


class OfficalNews(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    time = models.IntegerField()
    abstract = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'offical_news'


class OfficalNewsContent(models.Model):
    nid = models.IntegerField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'offical_news_content'


class OverseaSwitchChangeLog(models.Model):
    uid = models.IntegerField()
    type = models.IntegerField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=60)
    staff = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oversea_switch_change_log'


class PreservationEvidenceApply(models.Model):
    uid = models.IntegerField()
    apply_time = models.DateTimeField()
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    service_type = models.IntegerField()
    apply_type = models.IntegerField()
    third_status = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preservation_evidence_apply'


class PreservationEvidenceApplyRecord(models.Model):
    uid = models.IntegerField()
    pea_id = models.IntegerField()
    type = models.IntegerField()
    staff = models.CharField(max_length=32)
    remark = models.CharField(max_length=255, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preservation_evidence_apply_record'


class PreservationEvidenceRecord(models.Model):
    ev_id = models.AutoField(primary_key=True)
    ku_id = models.IntegerField()
    uuid = models.CharField(max_length=55, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    evidence_id = models.CharField(max_length=20, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preservation_evidence_record'


class RegionCount(models.Model):
    region_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'region_count'


class RemindDownloadApp(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    saleid = models.BigIntegerField(db_column='saleId', blank=True, null=True)  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dingid = models.CharField(db_column='dingId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msuid = models.BigIntegerField(db_column='msUid', blank=True, null=True)  # Field name made lowercase.
    msname = models.CharField(db_column='msName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remindstatus = models.BigIntegerField(db_column='remindStatus', blank=True, null=True)  # Field name made lowercase.
    remindtime = models.CharField(db_column='remindTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remind_download_app'


class ReportStyle(models.Model):
    color = models.CharField(max_length=45, blank=True, null=True)
    font_size = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    bold = models.IntegerField(blank=True, null=True)
    inclined = models.IntegerField(blank=True, null=True)
    align = models.IntegerField(blank=True, null=True)
    row_spacing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_style'


class ReportTemplate(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    templatename = models.CharField(db_column='templateName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    template = models.TextField(blank=True, null=True)  # This field type is a guess.
    templateimg = models.TextField(db_column='templateImg', blank=True, null=True)  # Field name made lowercase.
    templatetype = models.IntegerField(db_column='templateType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report_template'


class ReportTextComponent(models.Model):
    text = models.TextField()
    templateid = models.IntegerField()
    style = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'report_text_component'


class SyncMonitor(models.Model):
    name = models.CharField(unique=True, max_length=10)
    value = models.BigIntegerField()
    utime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sync_monitor'


class SysDept(models.Model):
    dept_id = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    dept_name = models.CharField(max_length=100, blank=True, null=True)
    saas_id = models.CharField(max_length=50, blank=True, null=True)
    sso_id = models.IntegerField(blank=True, null=True)
    flag = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dept'


class SysDeptRel(models.Model):
    dept_id = models.PositiveIntegerField(primary_key=True)
    saas_id = models.PositiveIntegerField()
    sso_id = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dept_rel'


class SysModule(models.Model):
    module_id = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField()
    module_name = models.CharField(max_length=50)
    module_url = models.CharField(max_length=200, blank=True, null=True)
    flag = models.PositiveIntegerField()
    order_no = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_module'


class SysRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)
    role_desc = models.CharField(max_length=255, blank=True, null=True)
    flag = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleModule(models.Model):
    role_id = models.PositiveIntegerField()
    module_id = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role_module'


class SysUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    dept_id = models.PositiveIntegerField()
    dept_name = models.CharField(max_length=100, blank=True, null=True)
    flag = models.PositiveIntegerField()
    sso_id = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserConfig(models.Model):
    logname = models.CharField(db_column='logName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pasd = models.CharField(max_length=100, blank=True, null=True)
    repasd = models.CharField(max_length=100, blank=True, null=True)
    xiaoshou = models.CharField(max_length=100, blank=True, null=True)
    classpid = models.CharField(max_length=100, blank=True, null=True)
    kusex = models.CharField(max_length=100, blank=True, null=True)
    keywordnum = models.CharField(max_length=100, blank=True, null=True)
    f_time = models.CharField(db_column='F_TIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apiip = models.CharField(max_length=100, blank=True, null=True)
    redisip = models.CharField(max_length=100, blank=True, null=True)
    userstates = models.CharField(db_column='userStates', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zsname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_config'


class SysUserRole(models.Model):
    user_id = models.PositiveIntegerField()
    role_id = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class SystemTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    tasktype = models.IntegerField(db_column='taskType', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    remindtime = models.CharField(db_column='remindTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    saleid = models.BigIntegerField(db_column='saleId', blank=True, null=True)  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dingid = models.CharField(db_column='dingId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msuid = models.BigIntegerField(db_column='msUid', blank=True, null=True)  # Field name made lowercase.
    msname = models.CharField(db_column='msName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.BigIntegerField(db_column='opportunityId', blank=True, null=True)  # Field name made lowercase.
    opportunityname = models.CharField(db_column='opportunityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmuid = models.BigIntegerField(db_column='crmUid', blank=True, null=True)  # Field name made lowercase.
    crmname = models.CharField(db_column='crmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crmmobile = models.CharField(db_column='crmMobile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat = models.CharField(db_column='weChat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taskstatus = models.IntegerField(db_column='taskStatus', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system_task'


class TC3P0Test(models.Model):
    a = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_c3p0_test'


class TestContent(models.Model):
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_content'


class Testweiwen(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testweiwen'


class Topic(models.Model):
    topic_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topic'


class UserFilterKeyword(models.Model):
    user_id = models.IntegerField()
    topic_id = models.CharField(max_length=40, blank=True, null=True)
    module_id = models.IntegerField()
    filter_keyword = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_filter_keyword'


class Userdatacount(models.Model):
    username = models.CharField(max_length=255)
    uid = models.IntegerField()
    count_date = models.CharField(max_length=255)
    all_data_count = models.IntegerField()
    redis_data_count = models.IntegerField()
    accurate_data_count = models.IntegerField()
    ustats = models.IntegerField()
    utype = models.IntegerField()
    udata = models.CharField(max_length=255)
    negative_data_count = models.IntegerField()
    normal_data_count = models.IntegerField()
    all_ctdata_count = models.IntegerField()
    all_yjdata_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userdatacount'


class UsersetChangeIllustrate(models.Model):
    msid = models.IntegerField()
    uname = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField()
    old = models.CharField(max_length=255, blank=True, null=True)
    new = models.CharField(max_length=255, blank=True, null=True)
    illustrate = models.CharField(max_length=255, blank=True, null=True)
    staff = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userset_change_illustrate'


class Warningstatuslog(models.Model):
    uid = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    oldstatus = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    staff = models.CharField(max_length=255, blank=True, null=True)
    endtime = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warningStatusLog'


class Warningtimesetting(models.Model):
    warningid = models.BigAutoField(db_column='warningId', primary_key=True)  # Field name made lowercase.
    msuid = models.BigIntegerField(db_column='msUid')  # Field name made lowercase.
    warningtimetype = models.CharField(db_column='warningTimeType', max_length=100)  # Field name made lowercase.
    isopenwarning = models.IntegerField(db_column='isOpenWarning')  # Field name made lowercase.
    allday = models.IntegerField(db_column='allDay')  # Field name made lowercase.
    weekdaytimestart = models.CharField(db_column='weekdayTimeStart', max_length=50)  # Field name made lowercase.
    weekdaytimeend = models.CharField(db_column='weekdayTimeEnd', max_length=50)  # Field name made lowercase.
    weekendtimestart = models.CharField(db_column='weekendTimeStart', max_length=50)  # Field name made lowercase.
    weekendtimeend = models.CharField(db_column='weekendTimeEnd', max_length=50)  # Field name made lowercase.
    warningremark = models.CharField(db_column='warningRemark', max_length=255)  # Field name made lowercase.
    warningendtime = models.CharField(db_column='warningEndTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warningTimeSetting'


class Warningtimesettingsystem(models.Model):
    syswarningid = models.BigAutoField(db_column='syswarningId', primary_key=True)  # Field name made lowercase.
    msuid = models.BigIntegerField(db_column='msUid')  # Field name made lowercase.
    type = models.IntegerField()
    weekdaytime = models.CharField(db_column='weekdayTime', max_length=100)  # Field name made lowercase.
    weekendtime = models.CharField(db_column='weekendTime', max_length=100)  # Field name made lowercase.
    warningendtime = models.CharField(db_column='warningEndTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    kkid = models.CharField(max_length=50, blank=True, null=True)
    warningremark = models.CharField(db_column='warningRemark', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warningTimeSettingSystem'


class WarningServiceApplication(models.Model):
    uid = models.IntegerField()
    who = models.CharField(max_length=32)
    tel = models.CharField(max_length=15)
    applytime = models.CharField(max_length=14)
    endtime = models.CharField(max_length=8)
    servicetype = models.IntegerField()
    examinetype = models.IntegerField()
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warning_service_application'


class WarningServiceApplicationLog(models.Model):
    uid = models.IntegerField()
    target = models.IntegerField()
    type = models.CharField(max_length=10)
    dingid = models.CharField(max_length=32)
    explain = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'warning_service_application_log'


class WebMessage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    mname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    tid = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    extends = models.TextField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_message'


class WeixinCorpid(models.Model):
    id = models.BigAutoField(primary_key=True)
    corpid = models.CharField(max_length=100)
    secrect = models.CharField(max_length=100)
    admin_name = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    max_users = models.IntegerField()
    status = models.IntegerField()
    ctime = models.DateTimeField()
    utime = models.DateTimeField()
    available = models.CharField(max_length=2, blank=True, null=True)
    ka_id = models.IntegerField(blank=True, null=True)
    ka_path = models.CharField(max_length=200, blank=True, null=True)
    ka_open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weixin_corpid'


class WeixinPush(models.Model):
    id = models.BigAutoField(primary_key=True)
    ku_id = models.IntegerField(db_column='KU_ID')  # Field name made lowercase.
    ku_name = models.CharField(db_column='KU_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    push_id = models.CharField(db_column='PUSH_ID', max_length=20)  # Field name made lowercase.
    wx_id = models.CharField(db_column='WX_ID', max_length=20)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    errmsg = models.CharField(max_length=200, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    corp_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'weixin_push'


class WeixinpushExamined(models.Model):
    msid = models.IntegerField()
    kv_sourcetype = models.CharField(db_column='KV_SOURCETYPE', max_length=4)  # Field name made lowercase.
    kv_keyword = models.CharField(db_column='KV_KEYWORD', max_length=255)  # Field name made lowercase.
    is_ocr = models.IntegerField(db_column='IS_OCR')  # Field name made lowercase.
    kr_keywordid = models.CharField(db_column='KR_KEYWORDID', max_length=50)  # Field name made lowercase.
    kv_title = models.TextField(db_column='KV_TITLE')  # Field name made lowercase.
    kr_ctime = models.CharField(db_column='KR_CTIME', max_length=20)  # Field name made lowercase.
    orientation = models.IntegerField(db_column='ORIENTATION')  # Field name made lowercase.
    is_oversea = models.IntegerField(db_column='IS_OVERSEA')  # Field name made lowercase.
    importance_weight = models.IntegerField(db_column='IMPORTANCE_WEIGHT')  # Field name made lowercase.
    kv_abstract = models.TextField(db_column='KV_ABSTRACT')  # Field name made lowercase.
    kv_simhash = models.CharField(db_column='KV_SIMHASH', max_length=50)  # Field name made lowercase.
    kv_url = models.CharField(db_column='KV_URL', max_length=255)  # Field name made lowercase.
    kv_uuid = models.CharField(db_column='KV_UUID', max_length=50)  # Field name made lowercase.
    kv_author = models.CharField(db_column='KV_AUTHOR', max_length=100)  # Field name made lowercase.
    tags = models.CharField(db_column='TAGS', max_length=255)  # Field name made lowercase.
    kv_webname = models.CharField(db_column='KV_WEBNAME', max_length=50)  # Field name made lowercase.
    kr_gtime = models.CharField(db_column='KR_GTIME', max_length=20)  # Field name made lowercase.
    retweeted_status_url = models.CharField(db_column='RETWEETED_STATUS_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    staff = models.CharField(max_length=50)
    examine_time = models.CharField(max_length=14)
    type = models.IntegerField()
    push_time = models.CharField(max_length=30, blank=True, null=True)
    wechat_group = models.CharField(max_length=255, blank=True, null=True)
    wechat_group_success = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weixinpush_examined'


class WeixinpushGroup(models.Model):
    staff = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(max_length=50, blank=True, null=True)
    msid = models.IntegerField(blank=True, null=True)
    accid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weixinpush_group'


class WeixinpushMsid(models.Model):
    staff = models.CharField(max_length=50)
    msid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weixinpush_msid'


class WeixinpushMuban(models.Model):
    gid = models.IntegerField()
    model = models.TextField()

    class Meta:
        managed = False
        db_table = 'weixinpush_muban'


class WeixinpushStaff(models.Model):
    staff = models.CharField(max_length=32)
    acc = models.CharField(max_length=50)
    accid = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weixinpush_staff'


class Word2Vecwords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wordline = models.TextField(db_column='WORDLINE', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'word2vecWords'


class ZhsqCompany(models.Model):
    companyid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    status = models.IntegerField()
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zhsq_company'


class ZhsqCompanyBaseinfo(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    unifiedsocialcreditcode = models.CharField(db_column='UnifiedSocialCreditCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registeredcapital = models.CharField(db_column='RegisteredCapital', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businessdatestart = models.CharField(db_column='BusinessDateStart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    managers = models.CharField(db_column='Managers', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businessdateend = models.CharField(db_column='BusinessDateEnd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registerstatus = models.CharField(db_column='RegisterStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofapproval = models.CharField(db_column='DateOfApproval', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationauthority = models.CharField(db_column='RegistrationAuthority', max_length=255, blank=True, null=True)  # Field name made lowercase.
    revokedate = models.CharField(db_column='RevokeDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businesspremises = models.CharField(db_column='BusinessPremises', max_length=255, blank=True, null=True)  # Field name made lowercase.
    compositionform = models.CharField(db_column='CompositionForm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.CharField(db_column='RegisterDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    investor = models.CharField(db_column='Investor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    legalrepresentative = models.CharField(db_column='LegalRepresentative', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businessscope = models.TextField(db_column='BusinessScope', blank=True, null=True)  # Field name made lowercase.
    branchinfo = models.TextField(db_column='BranchInfo', blank=True, null=True)  # Field name made lowercase.
    keypersoninfo = models.TextField(db_column='KeyPersonInfo', blank=True, null=True)  # Field name made lowercase.
    stockholderinfo = models.TextField(db_column='StockholderInfo', blank=True, null=True)  # Field name made lowercase.
    logourl = models.CharField(db_column='LogoUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WebSite', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    telphone = models.CharField(db_column='Telphone', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhsq_company_baseinfo'
