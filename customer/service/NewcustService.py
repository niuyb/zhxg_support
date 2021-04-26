import datetime
import hashlib
import json

import pymysql
import requests
from django.conf import settings

from customer.models import Account
from customer.service.BuildDB import ipcreate
from customer.service.GetCloudccDataModel import updateAccountData
from customer.service.NewcustService_b import CreateNewCust
from customer.service.UserIndexData import inserUserindex
from customer.service.UserModel import yqmsSynchroUpdate
from customer.service.redis_operation import RedisBase
from customer.utils import insertsql_factory, check_ip
from public.utils import parse_kwargs_for_pymysql
from django.conf import settings


if settings.MODE == 'develop' or settings.MODE == 'beta':
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
else:
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
conn = pymysql.connect(**kws)
cursor = conn.cursor(pymysql.cursors.DictCursor)

def getSetId(type=''):
    if type == 'get':
        pass
    if type == 'set':
        sql = '''
            UPDATE WK_T_ID SET KID_KEY = KID_KEY + 1 WHERE KID_KEY = 'UserID'
        '''
        cursor.execute(sql)
        conn.commit()
    if type == 'ret':
        sql = '''
            UPDATE WK_T_ID SET KID_KEY = KID_KEY - 1 WHERE KID_KEY = 'UserID'
        '''
        cursor.execute(sql)
        conn.commit()
    sql = '''
        SELECT * FROM WK_T_ID WHERE KID_KEY = 'UserID'
    '''
    cursor.execute(sql)
    items = cursor.fetchone()
    id = items['KID_VALUE']
    cursor.close()
    conn.close()
    return id

def newInternal(getPostInfo):
    id = getSetId('get')
    getPostInfo["cid"] = id + 1
    getMesse = ExecutionCreate(getPostInfo)
    return getMesse

def ExecutionCreate(getPostInfo, cookie):
    cnc = CreateNewCust(cookie)

    if getPostInfo.get('specify_ip'):
        cnc.ip = getPostInfo.get('specify_ip')
    cnc.userfl = getPostInfo.get('classify')

    classifyIP = {
        '6': "192.168.30.4",
        '3': "192.168.30.5"
    }
    cnc.ip = classifyIP.get(str(cnc.userfl))


def ExecutionCreate_bak(getPostInfo):
    theNewid = getPostInfo.get('cid')
    returnMessage = {'msg':'', 'status': 200, 'data': ''}

    ip = ""
    add = {}           #用户表
    userData = {}      #修改用户表
    dyData = {}        #地域表
    serviceData = {}   #服务表

    if getPostInfo.get('specify_ip'):
        ip = getPostInfo.get('specify_ip')

    userfl = getPostInfo.get('classify')  #账号分类
    classifyIP = {
        '6': "192.168.30.4",
        '3':"192.168.30.5"
    }
    ip = classifyIP.get(str(userfl))
    addUserUrl = "http://192.168.185.97:8080"  #生产环境新建调用返回IP
    if not ip:
        url = addUserUrl + '/Userdb!saveAddUserdb.do?userid=29461'
        r = requests.get(url=url)
        ipTrue = check_ip(r.text)
        if not ipTrue:
            returnMessage['msg'] = '数据连接错误，请稍后再试！'
            returnMessage['status'] = 201
            return returnMessage


    if not getPostInfo["logName"]:
        returnMessage['msg'] = '用户名不能为空，请稍后再试！'
        returnMessage['status'] = 201
        return returnMessage

    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
    conn_33 = pymysql.connect(**kws)
    cursor = conn_33.cursor(pymysql.cursors.DictCursor)

    sql = '''
            SELECT * FROM WK_T_ID WHERE KU_LID = '{}'
        '''.format(getPostInfo['logName'])
    cursor.execute(sql)
    user = cursor.fetchone()

    if user:
        returnMessage['msg'] = '用户名重复！'
        returnMessage['status'] = 201
        return returnMessage

    if not getPostInfo['zsname']:
        returnMessage['msg'] = '真实姓名不能为空，请稍后再试'
        returnMessage['status'] = 201
        return returnMessage


    add['KU_ID'] = theNewid
    add['KU_LID'] = getPostInfo['logName']   #用户名
    add['KU_NAME'] = getPostInfo['zsname']    #真实姓名
    add['KU_LEVEL'] = getPostInfo['userbm']
    add['KU_PASSWD'] = hashlib.md5(getPostInfo['pasd'].encode(encoding='UTF-8')).hexdigest().upper()
    add['KU_PHONE'] = getPostInfo['userphone']   #电话
    add['KU_COMPANY'] = getPostInfo['openjw'] if getPostInfo['openjw'] else '0'
    add['KU_EMAIL'] = getPostInfo['uemail'] if len(getPostInfo['uemail'])>5 else ''
    add['KU_SEX'] = getPostInfo['kusex'] if getPostInfo['kusex'] else '1'
    add['KU_BIRTHDAY'] = getPostInfo['useryear'] if getPostInfo['useryear'] else ''
    add['KU_TEMPLATE'] = 'comold'
    add['KU_REGDATE '] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    insert_sql = '''
        INSERT INTO WK_T_USER (KU_ID,KU_LID,KU_NAME,KU_LEVEL,KU_PASSWD,KU_PHONE,KU_COMPANY,KU_EMAIL,KU_SEX,KU_BIRTHDAY,KU_TEMPLATE,KU_REGDATE) VALUES 
        ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
    '''.format(
        getPostInfo['cid'],
        theNewid,
        getPostInfo['logName'],
        getPostInfo['zsname'],
        getPostInfo['userbm'],
        hashlib.md5(getPostInfo['pasd'].encode(encoding='UTF-8')).hexdigest().upper(),
        getPostInfo['userphone'],
        getPostInfo['openjw'] if getPostInfo['openjw'] else '0',
        getPostInfo['uemail'] if len(getPostInfo['uemail'])>5 else '',
        getPostInfo['kusex'] if getPostInfo['kusex'] else '1',
        getPostInfo['useryear'] if getPostInfo['useryear'] else '',
        'comold',
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    cursor.execute(insert_sql)
    conn_33.commit()
    select_sql = '''
        SELECT id FROM WK_T_ID WHERE KU_ID = '{}'
    '''.format(getPostInfo['cid'])
    cursor.execute(select_sql)
    users = cursor.fetchall()
    if not users:
        returnMessage['msg'] = '用户基本信息写入用户表失败！'
        returnMessage['status'] = 201
        return returnMessage

    #用户基本信息创建完成后创建个人库和个人表
    uip = ipcreate(ip, theNewid)
    if not check_ip(uip):
        returnMessage['msg'] = '用户库连接失败,请重新创建用户！'
        returnMessage['status'] = 201
        return returnMessage

    getSetId('set')          #WK_T_ID id +1
    inserUserindex(add['KU_SEX'], theNewid)     #创建WK_T_USERINDEX_MODULE信息
    contractdata = {
        'KU_ID': theNewid,
        'KU_TYPE': 'KB_CONTRACTDATE',
        'KU_VALUE': datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    }
    sql = insertsql_factory('WK_T_USERBASEINFO', contractdata)
    cursor.execute(sql, contractdata)
    conn_33.commit()
    #第三方账号id
    if getPostInfo.get('thirdId'):
        addthirdid = {
            'KU_ID': theNewid,
            'KU_TYPE': 'KU_THIRDID',
            'KU_VALUE': getPostInfo.get('thirdId')
        }
        sql = insertsql_factory('WK_T_USERBASEINFO', addthirdid)
        cursor.execute(sql, addthirdid)
        conn_33.commit()

    addintodb = {
        'KU_ID': theNewid,
        'KU_TYPE': 'KB_NEWTOPIC',
        'KU_VALUE': '1'
    }
    sql = insertsql_factory('WK_T_USERBASEINFO', addintodb)
    cursor.execute(sql, addintodb)
    conn_33.commit()




    cursor.close()
    conn_33.close()








def tvmonitor(getPostInfo):
    userfl = str(3)

    theNewid = getPostInfo.get('cid')

    #yqms2
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
    conn_33 = pymysql.connect(**kws)
    cursor = conn_33.cursor(pymysql.cursors.DictCursor)
    #yqht
    kws_yght = parse_kwargs_for_pymysql(settings.DATABASES["yqht_32"])
    conn_yght = pymysql.connect(**kws_yght)
    cursor_yght = conn_yght.cursor(pymysql.cursors.DictCursor)


    ip = ""
    add = {}           #用户表
    userData = {}      #修改用户表
    dyData = {}        #地域表
    serviceData = {}   #服务表

    #针对项目用户是否允许登陆平台秘书
    if getPostInfo.get('ALLOW_LOG_YQMS'):
        saveAllow = {
            'KU_ID': theNewid,
            'KU_TYPE': 'ALLOW_LOG_YQMS',
            'KU_VALUE': getPostInfo.get('ALLOW_LOG_YQMS')
        }
        sql = insertsql_factory('WK_T_USERBASEINFO', saveAllow)
        cursor.execute(sql, saveAllow)
        conn_33.commit()

    #**------------------UP-----用户表----userData------start-------------------------**
    userData['KD_ID'] = getPostInfo.get('agent')    #添加代理商  KD_ID
    userData['KU_DBNAME'] = uip                     #绑定库
    userData['KU_ANSWER'] = getPostInfo.get('qqOpen') if getPostInfo.get('qqOpen') else '0'      #qq群监控是否开启
    userData['KU_SEARCH'] = getPostInfo.get('abssorc') if getPostInfo.get('abssorc') else '1'   #是否开启专题搜索类型1是0否
    if getPostInfo.get('openExpert') != 'expert':             #不是专家版
        userData['KU_TEMPLATE'] = 'comold'                    #首页导航控制
    yqmsSynchroUpdate('WK_T_USER', 'KU_ID', theNewid, userData)

    #**------------------UP-----用户表----userData------end--------------------------**


    #* 2019/08/09 代理商为南方舆情特殊判断 *
    if getPostInfo.get('agent') == '7347':
        specialagentjudge = {
            'KU_ID': theNewid,
            'KU_TYPE': 'IS_NEW_HOMEPAGE',
            'KU_VALUE': '0'
        }
        sql = insertsql_factory('WK_T_USERBASEINFO', specialagentjudge)
        cursor.execute(sql, specialagentjudge)
        conn_33.commit()


    #**----------------insert------用户地域-----dyData------strst--------------------**\
    dyData['ku_id'] = theNewid
    if getPostInfo.get('province_id'):
        dyData['province_id'] = getPostInfo.get('province_id')
    if getPostInfo.get('city_id'):
        dyData['city_id'] = getPostInfo.get('city_id')
    if getPostInfo.get('county_id'):
        dyData['county_id'] = getPostInfo.get('county_id')
    dyData['level'] = len(dict((k,v) for k,v in dyData if v)) -1
    sql = insertsql_factory('WK_T_USER_AREA_NEW', dyData)
    cursor.execute(sql, dyData)
    conn_33.commit()

    #**----------------insert------用户地域-----dyData-------end----------------------**



    ssdiyu = {}
    if getPostInfo.get('ssdiyu'):
        sql = '''
            SELECT uuid FROM b_locationinfo WHERE province = '{}' AND level = 1
        '''.format(getPostInfo.get('ssdiyu'))
        cursor_yght.execute(sql)
        province = cursor_yght.fetchone()
        provinceId = province.get('uuid')
    else:
        provinceId = 0
    if getPostInfo.get('ss_city'):
        sql = '''
            SELECT uuid FROM b_locationinfo WHERE city = '{}' AND level = 2
        '''.format(getPostInfo.get('ss_city'))
        cursor_yght.execute(sql)
        city = cursor_yght.fetchone()
        cityId = city.get('uuid')
    else:
        cityId = 0
    if getPostInfo.get('ss_county'):
        sql = '''
                    SELECT uuid FROM b_locationinfo WHERE county = '{}' AND level = 3
                '''.format(getPostInfo.get('ss_county'))
        cursor_yght.execute(sql)
        county = cursor_yght.fetchone()
        countyId = county.get('uuid')
    else:
        countyId = 0

    sql = '''
        SELECT * FROM YTJCRMACCOUNTMAPPING WHERE msUid = {}
    '''.format(theNewid)
    cursor.execute(sql)
    synchro = cursor.fetchone()
    if synchro:
        ssdiyuUpdate = {}
        ssdiyuUpdate['userGenre'] = userfl
        ssdiyuUpdate['userStatus'] = getPostInfo.get('userStates') if getPostInfo.get('userStates') else 1
        ssdiyuUpdate['status'] = '1'
        ssdiyuUpdate['msName'] = getPostInfo.get('logName')
        ssdiyuUpdate['crmUid'] = getPostInfo.get('crmUid')
        ssdiyuUpdate['crmName'] = getPostInfo.get('crmName');
        ssdiyuUpdate['opportunityId'] = getPostInfo.get('opportunityId')
        ssdiyuUpdate['opportunityName'] = getPostInfo.get('opportunityName')
        ssdiyuUpdate['province'] = getPostInfo.get('ssdiyu')
        ssdiyuUpdate['city'] = getPostInfo.get('ss_city')
        ssdiyuUpdate['county'] = getPostInfo.get('ss_county')
        ssdiyuUpdate['province_id'] = provinceId;
        ssdiyuUpdate['city_id'] = cityId
        ssdiyuUpdate['county_id'] = countyId
        ssdiyuUpdate['trysDate'] = getPostInfo.get('F_TIME')
        yqmsSynchroUpdate('YTJCRMACCOUNTMAPPING', 'msUid',theNewid, ssdiyuUpdate)
    else:
        ssdiyu['msUid'] = theNewid
        ssdiyu['msName'] = getPostInfo['logName']
        ssdiyu['crmUid'] = getPostInfo['crmUid']
        ssdiyu['crmName'] = getPostInfo['crmName']
        ssdiyu['opportunityId'] = getPostInfo['opportunityId']
        ssdiyu['opportunityName'] = getPostInfo['opportunityName']
        ssdiyu['userGenre'] = userfl
        ssdiyu['userStatus'] = getPostInfo.get('userStates') if  getPostInfo.get('userStates') else 1
        ssdiyu['status'] = '1'
        ssdiyu['province'] = getPostInfo.get('ssdiyu')
        ssdiyu['city'] = getPostInfo.get('ss_city')
        ssdiyu['county'] = getPostInfo.get('ss_county')
        ssdiyu['province_id'] = provinceId
        ssdiyu['city_id'] = cityId
        ssdiyu['county_id'] = countyId
        ssdiyu['regDate'] = add.get('KU_REGDATE')
        ssdiyu['trysDate'] = getPostInfo.get('F_TIME')
        ssdiyu['createTime'] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        sql = insertsql_factory('YTJCRMACCOUNTMAPPING', ssdiyu)
        cursor.execute(sql, ssdiyu)
        conn_33.commit()


    if getPostInfo.get('crmUid'):
        account = Account.objects.filter(id=getPostInfo.get('crmUid')).first()
        new_account_id = account.new_account_id
        cloudccdata = 'https://support.istarshine.com/DataCount/single_user_activity_count?uid={}'.format(theNewid)
        accountInfo = updateAccountData(new_account_id, 'back_url', cloudccdata)
        if accountInfo:
            data = {
                "callback": '1'
            }
            #更新
            yqmsSynchroUpdate('YTJCRMACCOUNTMAPPING', 'msUid',theNewid, data)
        else:
            error_log = '{}客户：{}-{},账号：{}-{} 回写失败\n'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                getPostInfo.get('crmUid'),
                getPostInfo.get('crmName'),
                theNewid,
                getPostInfo.get('logName')
            )
            message_type = 3
            destination = '/var/tmp/xiaoshouyiFalse{}.log'.format(datetime.datetime.now().strftime('_%Y_%m_%d'))
            pass



    #人工预警时间设置
    if getPostInfo.get('isOpenWarning'):
        warningTimeSetting = {}
        warningTimeSetting['msUid'] = theNewid
        warningTimeSetting['warningTimeType'] = getPostInfo.get('warningTimeType') if getPostInfo.get('warningTimeType') else '5*8'
        warningTimeSetting['isOpenWarning'] = getPostInfo.get('isOpenWarning')
        warningTimeSetting['status'] = getPostInfo.get('warnstatus')
        allday = int(getPostInfo.get('allDay')) if getPostInfo.get('allDay') else 0
        if allday != 1:
            warningTimeSetting['weekdayTimeStart'] = getPostInfo.get('weekdayTimeStart') if getPostInfo.get('weekdayTimeStart') else '8:30'
            warningTimeSetting['weekdayTimeEnd'] = getPostInfo.get('weekdayTimeEnd') if getPostInfo.get('weekdayTimeEnd') else '17:30'
            warningTimeSetting['weekendTimeStart'] = getPostInfo.get('weekendTimeStart')
            warningTimeSetting['weekendTimeEnd'] = getPostInfo.get('weekendTimeEnd')
            warningTimeSetting['allDay'] = '0'
        else:
            warningTimeSetting['weekdayTimeStart'] = ''
            warningTimeSetting['weekdayTimeEnd'] = ''
            warningTimeSetting['weekendTimeStart'] = ''
            warningTimeSetting['weekendTimeEnd'] = ''
            warningTimeSetting['allDay'] = '1'
        stoptime = getPostInfo.get('stoptime')
        # stoptime = getPostInfo.get('warnstoptime')  #2020-01-01
        if stoptime:
            warningTimeSetting['warningEndTime'] = datetime.datetime.strptime(stoptime, '%Y-%m-%d').strftime('%Y%m%d')

        #插入warningTimeSetting表
        insertsql = insertsql_factory('warningTimeSetting', warningTimeSetting)
        cursor.execute(insertsql, warningTimeSetting)
        conn_33.commit()

        #记录开启日志
        where_open_log = {
            'uid' : theNewid,
            'status': getPostInfo.get('isOpenWarning'),
            'oldstatus': '',
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'staff': "",
            'endtime': getPostInfo.get('stoptime')
        }
        if int(getPostInfo.get('isOpenWarning')) > 0:
            #插入warningStatusLog表
            insertsql = insertsql_factory('warningStatusLog', where_open_log)
            cursor.execute(insertsql, where_open_log)
            conn_33.commit()


        # 秘书研判模块开关
    if getPostInfo.get('ypmodular'):
        ypmodular = {
            "KU_ID": theNewid,
            "KU_TYPE": 'MS_YPMODULAR',
            "KU_VALUE": getPostInfo.get('ypmodular')
        }
        insertsql = insertsql_factory('WK_T_USERBASEINFO', ypmodular)
        cursor.execute(insertsql, ypmodular)
        conn_33.commit()


    #**--------创建个人服务表信息----------serviceData-----start-----------------------**
    serviceData['KU_ID'] = theNewid
    classpid = getPostInfo.get('classpid')             #添加用户行业分类  子分类
    classid = getPostInfo.get('classid')               #添加用户行业分类  父分类
    classification = classid if classid else classpid
    #/*快速创建判断 政府不开地域 其他开启地域*/
    if classpid == '1' and getPostInfo.get('areaSet'):
        getPostInfo['areaSet'] = '0'
    elif classpid != '1' and getPostInfo.get('areaSet'):
        getPostInfo['areaSet'] = '1'

    if classification:
        serviceData['KU_INDUSTRY'] = classification
    else:
        serviceData['KU_INDUSTRY'] = '0'

    serviceData['KU_MAINT'] = getPostInfo.get('xiaoshou') #商务
    serviceData['KU_VERSION'] = getPostInfo.get('userLeve') if getPostInfo.get('userLeve') else 'B1' # 版本选择
    serviceData['KU_KEYWORDNUM'] = getPostInfo.get('keywordnum') if getPostInfo.get('keywordnum') else '300' #关键词数量
    serviceData['KU_USERGENRE'] = userfl        #部门
    serviceData['KU_USERSTATUS'] = getPostInfo.get('userStates') if getPostInfo.get('userStates') else 1   #用户服务状态： 0-正常 1-试用 2-停止试用
    serviceData['KU_OAID'] = getPostInfo.get('oaId') if getPostInfo.get('oaId') else 0    #OAID
    tryDate = getPostInfo.get('F_TIME') if getPostInfo.get('F_TIME') else (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")   #试用截止日期：KU_TRYSDATE 默认30天
    if tryDate:
        serviceData['KU_TRYSDATE'] = tryDate
    serviceData['KU_T_PHONECOUNT'] = getPostInfo.get('phonenum') if getPostInfo.get('phonenum') else '5'   #允许登录的手机个数
    saveDays = getPostInfo.get('saveDays') if getPostInfo('saveDays') else '7'
    if getPostInfo.get('classify') in (1, 2):                #员工和测试帐号数据保存天数固定两天
        saveDays = 2
    serviceData['KU_SAVEDAYS'] = saveDays        # 用户数据保留天数
    serviceData['KU_KWSDAYMAXDATA'] = getPostInfo.get('maxdata') if getPostInfo.get('maxdata') else 100000       #专题最大数据量/条
    serviceData['KU_USERDAYMAXDATA'] = getPostInfo.get('daydata') if getPostInfo.get('daydata') else 200000     #用户每天数据量/条
    serviceData['KU_QQ'] = getPostInfo.get('qqNum') if getPostInfo.get('qqNum') else '0'                      #qq号绑定数量/条
    serviceData['KU_WEIXINCHECK'] = getPostInfo.get('weiXin') if getPostInfo.get('weiXin') else '0'           #微信群监控是否开启
    serviceData['KU_WEIXINNUMCOUNT'] = getPostInfo.get('weiXnum') if getPostInfo.get('weiXnum') else '0'        #微信号绑定数量
    serviceData['KU_WEIXINGROUPCOUNT'] = getPostInfo.get('weiPack')
    serviceData['KU_QQCOUNT'] = getPostInfo.get('qqPack')
    serviceData['KU_WORDCOUNT'] = getPostInfo.get('wordCount')
    serviceData['KU_TOPICCOUNT'] = getPostInfo.get('textfield') if getPostInfo.get('textfield') else '3'       #话题挖掘个数
    topicrefresh = getPostInfo.get('topicrefresh')             #话题挖掘刷新按钮
    # if topicrefresh == '1':
    #     serviceData['KU_TOPICREFRESH'] = '1'
    # else:
    #     serviceData['KU_TOPICREFRESH'] = '0'
    serviceData['KU_OPENHIGHSET'] = getPostInfo.get('openHighSet') if getPostInfo.get('openHighSet') else '0'  #是否开启高级设置
    serviceData['KU_SIZE'] = getPostInfo.get('openHighSet') if getPostInfo.get('openHighSet') else '10'       #专题默认显示条数
    serviceData['KU_SHOWABS'] = getPostInfo.get('showAbs') if getPostInfo.get('showAbs') else '0'            #专题默认是否显示摘要
    if add.get('KU_SEX') == '4':
        serviceData['KU_SETABSTRACT'] = '1'
        serviceData['KU_JINGZHUN'] = '1'
        serviceData['KU_SHOWALLSUB'] = '2'
        serviceData['KU_ZFWORDS'] = '1'
    else:
        serviceData['KU_SETABSTRACT'] = getPostInfo.get('setAbstract') if getPostInfo.get('setAbstract') else '1'   #用户是否使用自定义摘要1是    0否
        serviceData['KU_JINGZHUN'] = getPostInfo.get('jingZhun') if getPostInfo.get('jingZhun') else '1'
        serviceData['KU_SHOWALLSUB'] = getPostInfo.get('noiseAllsub') if getPostInfo.get('noiseAllsub') else '1'
        serviceData['KU_ZFWORDS'] = getPostInfo.get('zfwords')  if getPostInfo.get('zfwords') else '1'
    serviceData['KU_HOMEQUERY'] = getPostInfo.get('indexAbst') if getPostInfo.get('indexAbst') else '0'         #是否开启主页巡查 1是  0否
    serviceData['KU_FINANCE'] = getPostInfo.get('finance') if getPostInfo.get('finance') else '1'               #是否开启金融专题搜索 1是  0否
    serviceData['KU_CAR'] = getPostInfo.get('carSour') if getPostInfo.get('carSour') else '1'                   #是否开启汽车专题搜索 1是  0否
    serviceData['KU_TRAVEL'] = getPostInfo.get('Tourism') if getPostInfo.get('Tourism') else '1'                #是否开启旅游专题搜索 1是  0否
    serviceData['KU_ISTIBETAN'] = getPostInfo.get('zwmw')  #是否开启臧维蒙文搜索 1是  0否
    serviceData['KU_ISFORLANGUAGE'] = getPostInfo.get('waiwen') #是否开启外文搜索 1是  0否
    serviceData['KU_COMMZT'] = getPostInfo.get('commZt') if getPostInfo.get('commZt') else '1'                  #是否推送专题 1是  0否
    serviceData['KU_REPEAT'] = getPostInfo.get('remova') if getPostInfo.get('remova') else '1'                  #是否默认去重信息 0去重  1不去重
    serviceData['KU_ZAOYIN'] = getPostInfo.get('noise') if getPostInfo.get('noise') else '1'                    #是否开启噪音过滤 1是  0否
    serviceData['KU_SPECIALSPACING'] = getPostInfo.get('zhuantijianju') if getPostInfo.get('zhuantijianju') else '1'     #是否开启专题间距 1开启 0不开启
    serviceData['KU_T_SHOWALL'] = getPostInfo.get('showAll')
    serviceData['KU_INSERTINFO'] = getPostInfo.get('insertInfo') if getPostInfo.get('insertInfo') else '1'        #展示人工添加专题信息功能： 1展示  0不展示
    serviceData['KU_SINGLE'] = getPostInfo.get('single') if getPostInfo.get('single') else '0'             #用户词设置是否允许单字： 1允许  0不允许
    serviceData['KU_AREASET'] = getPostInfo.get('areaSet') if getPostInfo.get('areaSet') else '1'        #客户是否允许设置地域词： 1允许  0不允许
    serviceData['KU_ALLEXPORT'] = getPostInfo.get('allexport') if getPostInfo.get('allexport') else '1' #客户是否允许全部导出： 1允许  0不允许
    serviceData['KU_WEIXIN'] = getPostInfo.get('weixinbang') if getPostInfo.get('weixinbang') else '1'   #客户是否允许开通微信绑定： 1允许  0不允许
    serviceData['KU_SHOWSOURCE'] = getPostInfo.get('showSource') if getPostInfo.get('showSource') else '1'  #客户专题是否允许自定义来源查询： 1允许  0不允许
    serviceData['KU_ORDERTIME'] = getPostInfo.get('orderTime') if getPostInfo.get('orderTime') else '0'     #舆情浏览信息按时间排序： 0发布时间    1采集时间
    serviceData['KU_ORDERZTTJ'] = getPostInfo.get('ztDesc') if getPostInfo.get('ztDesc') else '0'           #首页专题统计排序： 0从大到小    1专题设置
    serviceData['KU_SOURCETYPE'] = getPostInfo.get('sourceType') if getPostInfo.get('sourceType') else '0'  #专题浏览默认显示来源类型：0全部01新闻02论坛03博客04微博05平媒06微信07视频
    serviceData['KU_ZQRUBBISH'] = getPostInfo.get('zqRubbish') if getPostInfo.get('zqRubbish') else '1'     #是否开启早期垃圾过滤
    serviceData['KU_XTZAOYIN'] = getPostInfo.get('xtZaoyin') if getPostInfo.get('xtZaoyin') else '0'        #是否关闭系统噪音
    serviceData['KU_XTZHENGFU'] = getPostInfo.get('xtzhengfu') if getPostInfo.get('xtzhengfu') else '1'     #是否关闭系统正负面 1开启 0关闭
    serviceData['KU_YJTIME'] = getPostInfo.get('yjTime') if getPostInfo.get('yjTime') else '1'              #是否关闭预警时间限制
    serviceData['KU_BBSVIEW'] = getPostInfo.get('bbsView') if getPostInfo.get('bbsView') else '1'           #展示地域论坛功能
    serviceData['KU_BBSALLINFO'] = getPostInfo.get('bbsAllInfo') if getPostInfo.get('bbsAllInfo') else '1'  #客户是否允许地域论坛入全部信息
    serviceData['KU_BIGV'] = getPostInfo.get('bigV')           #大V评论开关
    serviceData['KU_WEIBOCOMMENT'] = getPostInfo.get('wbpl')    #微博评论开关
    serviceData['KU_HTRECOLLECT'] = getPostInfo.get('htrecollect')   #话题回采开关
    serviceData['KU_LOCALBBSYJ'] = getPostInfo.get('localBbsYj') if getPostInfo.get('localBbsYj') else '1'     #地域论坛预警：0发送  1不发送
    serviceData['KU_COMMYJ'] = getPostInfo.get('commYj') if getPostInfo.get('commYj') else '0'                 #是否发送公共预警：2全部  0负面 1全部不发
    serviceData['KU_WEIBOYJ'] = getPostInfo.get('weiBoYj') if getPostInfo.get('weiBoYj') else '1'              #微博主体预警：0全部  1负面 2全部不发
    serviceData['KU_YJWORDCOUNT'] = getPostInfo.get('yJWordCount') if getPostInfo.get('yJWordCount') else '50' #预警关键词个数

    overtime1 = int(getPostInfo.get('overTime1')) if getPostInfo.get('overTime1') else 0
    overtime2 = int(getPostInfo.get('overTime2')) if getPostInfo.get('overTime2') else 0
    overtime = (overtime1 * 3600) + (overtime2 * 60)
    serviceData['KU_OVERTIME'] = overtime if overtime else (72*3600)
    serviceData['KU_ISLOCATIONREF'] = getPostInfo.get('Regional') if getPostInfo.get('Regional') else '0'        #是否开启地域数据
    serviceData['KU_DAYREPORT'] = getPostInfo.get('dayReport') if getPostInfo.get('dayReport') else '1'          #是否生成日报：1是  0否
    serviceData['KU_SETREPORT'] = getPostInfo.get('setReport') if getPostInfo.get('setReport') else '1'          #是否定制日报：1是  0否
    serviceData['KU_SHOWREPORT'] = getPostInfo.get('showReport') if getPostInfo.get('showReport') else ''        #前台展示供用户定制的日报模板： 凝瑞模板   KU_SHOWREPORT
    if getPostInfo.get('weixinPushReport'):
        serviceData['KU_ISWXPUSH'] = getPostInfo.get('weixinPushReport')
    serviceData['KU_REPORTTITLE'] = getPostInfo.get('reportTitle') if getPostInfo.get('reportTitle') else '0'           #是否自定义日报标题：1是  0否
    serviceData['KU_DAYREPORTTIME'] = getPostInfo.get('dayReportTime') if getPostInfo.get('dayReportTime') else '0'     #日报生成时间
    serviceData['KU_SENDREPORT'] = getPostInfo.get('sendReport') if getPostInfo.get('sendReport') else '0'              #是否发送日报邮件
    serviceData['KU_CHANGEVERSION'] = '2'                           #设置KU_CHANGEVERSION字段为
    serviceData['KU_TEMPLATETYPE'] = getPostInfo.get('templateType') if getPostInfo.get('templateType') else '0'



    #====================================电视监控start=============================================
    tvmonitor = getPostInfo.get('ispen', '')     #是否开启电视监控
    limittvgjc = getPostInfo.get('gjcnum', '')      #关键词个数 1-500
    limitdlnum = getPostInfo.get('downloadnum', '')   #下载个数  1-5000
    tvchannel = getPostInfo.get('tvchannel', [])    #电视频道
    tvchannel = list(set(tvchannel))
    mailopen = getPostInfo.get('mailopen')        #是否开启邮件开关 1开 0关
    tvtrysdate = getPostInfo.get('tvexpire')      #电视监控到期日期

    if tvmonitor == '1' and limittvgjc != '' and tvchannel != '' and (not tvchannel):
        serviceData['KU_TVISOPEN'] = '1'
        if int(limittvgjc) > 2 and getPostInfo['xiaoshou'] != 'YDY':
            serviceData['KU_TVKEYWSNUM'] = '2'
        else:
            serviceData['KU_TVKEYWSNUM'] = limittvgjc

        if int(limitdlnum) > 2 and getPostInfo['xiaoshou'] !='YDY':
            serviceData['KU_TVDOWNLOADNUM'] = '2'
            serviceData['KU_TVLASTDOWNLOADNUM'] = '2'
        else:
            serviceData['KU_TVDOWNLOADNUM'] = limitdlnum
            serviceData['KU_TVLASTDOWNLOADNUM'] = limitdlnum
        if len(tvchannel) > 20 and getPostInfo['xiaoshou'] != 'YDY':
            tvremind = True
            tvchannel = tvchannel[:20]     #限定20个

        tup = tuple()
        for c in tvchannel:
            t_in = (c, theNewid)         #(频道id ,用户id)
            tup += (t_in,)

        if not tup:
            #WK_T_CHANNEL_USER表
            sql = '''
                INSERT INTO WK_T_CHANNEL_USER (KC_ID, KU_ID) VALUES
                (%s,%s)
            '''
            cursor.executemany(sql, tup)
            conn_33.commit()

        baseinfo = (
            (theNewid,'KU_TVTRYSDATE',tvtrysdate),
            (theNewid, 'KU_TVMAILSWITCH', mailopen)
        )
        #WK_T_USERBASEINFO表
        sql = '''
            INSERT INTO WK_T_USERBASEINFO (KU_ID, KU_TYPE, KU_VALUE) VALUES
                (%s,%s,%s)
        '''
        cursor.executemany(sql, baseinfo)
        conn_33.commit()

        if mailopen == '1':                  #开启邮箱推送设置推送数据起始时间
            #WK_T_USERBASEINFO表
            sql = '''
                INSERT INTO WK_T_USERBASEINFO (KU_ID, KU_TYPE, KU_VALUE) VALUES
                ({},'{}','{}')
            '''.format(theNewid, 'KB_TVPUSHMAILTIME' , datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            cursor.execute(sql)
            conn_33.commit()

    for k,v in serviceData.items():
        serviceData[k] = "" if v == None else v

    if getPostInfo['openExpert'] == 'expert': #修复专家添加时没有频道导致开始失败问题
        serviceData['KU_TVISOPEN'] = getPostInfo.get('isopen')
        serviceData['KU_TVKEYWSNUM'] = getPostInfo.get('gjcnum')
        serviceData['KU_TVLASTDOWNLOADNUM'] = getPostInfo.get('downloadnum')
    #===================================电视监控end===============================================================

    #是否开启小视频
    serviceData['KU_OPENSMALLVIDEO'] = getPostInfo.get('openSmallVideo') if getPostInfo.get('openSmallVideo') else '1'
    #开通事件境外数据
    serviceData['open_topic_overseas'] = getPostInfo.get('openjwdata') if getPostInfo.get('openjwdata') else '0'

    #TAG备注字段
    if getPostInfo.get('tag'):
        serviceData['TAG'] = getPostInfo.get('tag')
    if '_tsgz' in getPostInfo.get('logName'):
        serviceData['KU_USERGENRE'] = '8'
        serviceData['KU_SALE'] = '缪杨'

    #WK_T_USERSERVICE表 插入
    insertsql = insertsql_factory('WK_T_USERSERVICE', serviceData)
    cursor.execute(insertsql, serviceData)
    conn_33.commit()


    #**---------HY-------WK_T_USERBASEINFO-------添加用户信息------start-------------**
    muban = getPostInfo.get('muban')        #用户选择的模板
    #如果账号分类不是模板账号，在userbaseinfo表中保存一个该用户继承的模板ID
    if userfl != '7':
        savemuban = {
            "KU_ID": theNewid,
            "KU_TYPE": 'KU_MUBANUSERID',
            "KU_VALUE": muban if muban else '0'
        }
        #添加WK_T_USERBASEINFO表
        insertsql = insertsql_factory('WK_T_USERBASEINFO', savemuban)
        cursor.execute(insertsql, savemuban)
        conn_33.commit()
    warndata_delay_time = getPostInfo.get('warndata_delay_time')   #容忍预警数据延迟时间
    warndata_delay_time = '' if warndata_delay_time == '0' or warndata_delay_time == None else warndata_delay_time

    #添加WK_T_USERBASEINFO表
    savedelaytime = {
        "KU_ID": theNewid,
        "KU_TYPE": 'warndata_delay_time',
        "KU_VALUE": warndata_delay_time
    }
    insertsql = insertsql_factory('WK_T_USERBASEINFO', savedelaytime)
    cursor.execute(insertsql, savedelaytime)
    conn_33.commit()

    USERBASEINFO = {}
    if getPostInfo['kusex'] == '1':
        USERBASEINFO[0] = getPostInfo['interinfo'] if getPostInfo.get('interinfo') else '1'
        USERBASEINFO[2] = getPostInfo['seaweb'] if getPostInfo.get('seaweb') else '4'
        USERBASEINFO[9] = getPostInfo['questions'] if getPostInfo.get('questions') else '15'
        USERBASEINFO[13] = getPostInfo['Picture'] if getPostInfo.get('Picture') else '20'
        USERBASEINFO[15] = getPostInfo['video'] if getPostInfo.get('video') else '21,22'
        USERBASEINFO[11] = getPostInfo['foreign'] if getPostInfo.get('foreign') else '17'
        USERBASEINFO[10] = getPostInfo['Tibetan'] if getPostInfo.get('Tibetan') else '16'
        USERBASEINFO[1] = getPostInfo['oversea'] if getPostInfo.get('oversea') else ''
        USERBASEINFO[14] = getPostInfo['watch'] if getPostInfo.get('watch') else ''
    elif getPostInfo['kusex'] == '4':
        USERBASEINFO[0] = getPostInfo['interinfo'] if getPostInfo.get('interinfo') else '1'
        USERBASEINFO[2] = getPostInfo['seaweb'] if getPostInfo.get('seaweb') else '4'
        USERBASEINFO[4] = getPostInfo['finance'] if getPostInfo.get('finance') else '9'
        USERBASEINFO[5] = getPostInfo['car'] if getPostInfo.get('car') else '10'
        USERBASEINFO[6] = getPostInfo['tour'] if getPostInfo.get('tour') else '11'
        USERBASEINFO[7] = getPostInfo['policy'] if getPostInfo.get('policy') else '13'
        USERBASEINFO[8] = getPostInfo['bids'] if getPostInfo.get('bids') else '14'
        USERBASEINFO[9] = getPostInfo['questions'] if getPostInfo.get('questions') else '15'
        USERBASEINFO[10] = getPostInfo['Tibetan'] if getPostInfo.get('Tibetan') else '16'
        USERBASEINFO[11] = getPostInfo['foreign'] if getPostInfo.get('foreign') else '17'
        USERBASEINFO[13] = getPostInfo['Picture'] if getPostInfo.get('Picture') else '20'
        USERBASEINFO[15] = getPostInfo['video'] if getPostInfo.get('video') else '21,22'
        USERBASEINFO[1] = getPostInfo['oversea'] if getPostInfo.get('oversea') else ''
        USERBASEINFO[14] = getPostInfo['watch'] if getPostInfo.get('watch') else ''
        USERBASEINFO[16] = getPostInfo['hangyeqita'] if getPostInfo.get('hangyeqita') else '2'
    else:
        USERBASEINFO[0] = getPostInfo['interinfo'] if getPostInfo.get('interinfo') else ''
        USERBASEINFO[1] = getPostInfo['oversea'] if getPostInfo.get('oversea') else ''
        USERBASEINFO[2] = getPostInfo['seaweb'] if getPostInfo.get('seaweb') else ''
        USERBASEINFO[3] = getPostInfo['search'] if getPostInfo.get('search') else ''
        USERBASEINFO[4] = getPostInfo['finance'] if getPostInfo.get('finance') else ''
        USERBASEINFO[5] = getPostInfo['car'] if getPostInfo.get('car') else ''
        USERBASEINFO[6] = getPostInfo['tour'] if getPostInfo.get('tour') else ''
        USERBASEINFO[7] = getPostInfo['policy'] if getPostInfo.get('policy') else ''
        USERBASEINFO[8] = getPostInfo['bids'] if getPostInfo.get('bids') else ''
        USERBASEINFO[9] = getPostInfo['questions'] if getPostInfo.get('questions') else ''
        USERBASEINFO[10] = getPostInfo['Tibetan'] if getPostInfo.get('Tibetan') else ''
        USERBASEINFO[11] = getPostInfo['foreign'] if getPostInfo.get('foreign') else ''
        USERBASEINFO[12] = getPostInfo['Roaming'] if getPostInfo.get('Roaming') else ''
        USERBASEINFO[13] = getPostInfo['Picture'] if getPostInfo.get('Picture') else ''
        USERBASEINFO[14] = getPostInfo['watch'] if getPostInfo.get('watch') else ''
        USERBASEINFO[15] = getPostInfo['video'] if getPostInfo.get('video') else ''
        USERBASEINFO[16] = getPostInfo['hangyeqita'] if getPostInfo.get('hangyeqita') else ''

    userinfoarr = dict((str(k), v) for k,v in USERBASEINFO.items() if v)
    userinfodata = ",".join(userinfoarr)
    infodatas = {
        "KU_ID": theNewid,
        "KU_TYPE": 'dataType',
        "KU_VALUE": userinfodata
    }
    insertsql = insertsql_factory('WK_T_USERBASEINFO', infodatas)
    cursor.execute(insertsql, infodatas)
    conn_33.commit()

    #---------------------------新建完成后需要执行的----------------------------------
    upstatus = 'http://192.168.185.123:8080'
    userStates = getPostInfo.get('userStates') if getPostInfo.get('userStates') else '1'
    if userStates == '0' or userStates == '1':
        url = upstatus + '/Redis!loadDataLimit.do' #用户信息数量限制同步接口
    else:
        url = upstatus + '/Redis!deleteDataLimit.do'  #用户信息数量限制删除接口
    statuid = {
        "userid": theNewid
    }
    r = requests.get(url=url, params=statuid)

    # / *注释时间：2017
    # 年10月23日
    # 原因：新增redis存入uid
    # 定时调用预警同步任务，---lc * /
    # // $haoran1 = C('waringUrl'); // 调用郝然接口
    # 目前只有alpha
    # // self::request_by_curl($haoran1, $statuid);
    redis_server = RedisBase('192.168.185.28', 12)
    redis_server.hset('needWaringId', theNewid, theNewid)

    #用户选择了模板
    if int(muban) > 0:
        tongbumuban = "http://192.168.185.97:8080" + "/UserDefinedHome/saveAddDefinedHomeClone.do"
        copymuban = {
            'userid': theNewid,
            'extendid': muban
        }
        requests.post(url=tongbumuban, data = json.dumps(copymuban))
    if userfl == '5':
        #账号id入预警账号缓存
        redis_server = RedisBase('', 12)  #这里不知道 服务器和库
        redis_server.sadd('artificial_warning_user', theNewid)

        #发布消息
        redis_server = RedisBase('192.168.16.154', 5)
        redis_server.publish('configStatus', '1')

        #2020-1-17 新逻辑 是预警账号 id添加到新redis
        redis_server = RedisBase('', 11)   #这里不知道 服务器
        redis_server.hset('sourceAccountList', theNewid, getPostInfo.get('logName'))

        #添加到push_server库ap_ms
        add_apms = {
            "id": theNewid,
            "username": getPostInfo.get('logName'),
            'valid': '1',
            'ms_group': '2'
        }
        insertsql_factory('ap_ms', add_apms)





    #操作记录
    username = getPostInfo.get('KU_LID')
    uid = getPostInfo.get('KU_ID')
    action = "新建秘书账号"
    type = '1'
    user = getPostInfo.get('logName')








