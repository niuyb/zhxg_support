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
    add = {}           #?????????
    userData = {}      #???????????????
    dyData = {}        #?????????
    serviceData = {}   #?????????

    if getPostInfo.get('specify_ip'):
        ip = getPostInfo.get('specify_ip')

    userfl = getPostInfo.get('classify')  #????????????
    classifyIP = {
        '6': "192.168.30.4",
        '3':"192.168.30.5"
    }
    ip = classifyIP.get(str(userfl))
    addUserUrl = "http://192.168.185.97:8080"  #??????????????????????????????IP
    if not ip:
        url = addUserUrl + '/Userdb!saveAddUserdb.do?userid=29461'
        r = requests.get(url=url)
        ipTrue = check_ip(r.text)
        if not ipTrue:
            returnMessage['msg'] = '???????????????????????????????????????'
            returnMessage['status'] = 201
            return returnMessage


    if not getPostInfo["logName"]:
        returnMessage['msg'] = '??????????????????????????????????????????'
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
        returnMessage['msg'] = '??????????????????'
        returnMessage['status'] = 201
        return returnMessage

    if not getPostInfo['zsname']:
        returnMessage['msg'] = '??????????????????????????????????????????'
        returnMessage['status'] = 201
        return returnMessage


    add['KU_ID'] = theNewid
    add['KU_LID'] = getPostInfo['logName']   #?????????
    add['KU_NAME'] = getPostInfo['zsname']    #????????????
    add['KU_LEVEL'] = getPostInfo['userbm']
    add['KU_PASSWD'] = hashlib.md5(getPostInfo['pasd'].encode(encoding='UTF-8')).hexdigest().upper()
    add['KU_PHONE'] = getPostInfo['userphone']   #??????
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
        returnMessage['msg'] = '??????????????????????????????????????????'
        returnMessage['status'] = 201
        return returnMessage

    #????????????????????????????????????????????????????????????
    uip = ipcreate(ip, theNewid)
    if not check_ip(uip):
        returnMessage['msg'] = '?????????????????????,????????????????????????'
        returnMessage['status'] = 201
        return returnMessage

    getSetId('set')          #WK_T_ID id +1
    inserUserindex(add['KU_SEX'], theNewid)     #??????WK_T_USERINDEX_MODULE??????
    contractdata = {
        'KU_ID': theNewid,
        'KU_TYPE': 'KB_CONTRACTDATE',
        'KU_VALUE': datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    }
    sql = insertsql_factory('WK_T_USERBASEINFO', contractdata)
    cursor.execute(sql, contractdata)
    conn_33.commit()
    #???????????????id
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
    add = {}           #?????????
    userData = {}      #???????????????
    dyData = {}        #?????????
    serviceData = {}   #?????????

    #????????????????????????????????????????????????
    if getPostInfo.get('ALLOW_LOG_YQMS'):
        saveAllow = {
            'KU_ID': theNewid,
            'KU_TYPE': 'ALLOW_LOG_YQMS',
            'KU_VALUE': getPostInfo.get('ALLOW_LOG_YQMS')
        }
        sql = insertsql_factory('WK_T_USERBASEINFO', saveAllow)
        cursor.execute(sql, saveAllow)
        conn_33.commit()

    #**------------------UP-----?????????----userData------start-------------------------**
    userData['KD_ID'] = getPostInfo.get('agent')    #???????????????  KD_ID
    userData['KU_DBNAME'] = uip                     #?????????
    userData['KU_ANSWER'] = getPostInfo.get('qqOpen') if getPostInfo.get('qqOpen') else '0'      #qq?????????????????????
    userData['KU_SEARCH'] = getPostInfo.get('abssorc') if getPostInfo.get('abssorc') else '1'   #??????????????????????????????1???0???
    if getPostInfo.get('openExpert') != 'expert':             #???????????????
        userData['KU_TEMPLATE'] = 'comold'                    #??????????????????
    yqmsSynchroUpdate('WK_T_USER', 'KU_ID', theNewid, userData)

    #**------------------UP-----?????????----userData------end--------------------------**


    #* 2019/08/09 ???????????????????????????????????? *
    if getPostInfo.get('agent') == '7347':
        specialagentjudge = {
            'KU_ID': theNewid,
            'KU_TYPE': 'IS_NEW_HOMEPAGE',
            'KU_VALUE': '0'
        }
        sql = insertsql_factory('WK_T_USERBASEINFO', specialagentjudge)
        cursor.execute(sql, specialagentjudge)
        conn_33.commit()


    #**----------------insert------????????????-----dyData------strst--------------------**\
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

    #**----------------insert------????????????-----dyData-------end----------------------**



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
            #??????
            yqmsSynchroUpdate('YTJCRMACCOUNTMAPPING', 'msUid',theNewid, data)
        else:
            error_log = '{}?????????{}-{},?????????{}-{} ????????????\n'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                getPostInfo.get('crmUid'),
                getPostInfo.get('crmName'),
                theNewid,
                getPostInfo.get('logName')
            )
            message_type = 3
            destination = '/var/tmp/xiaoshouyiFalse{}.log'.format(datetime.datetime.now().strftime('_%Y_%m_%d'))
            pass



    #????????????????????????
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

        #??????warningTimeSetting???
        insertsql = insertsql_factory('warningTimeSetting', warningTimeSetting)
        cursor.execute(insertsql, warningTimeSetting)
        conn_33.commit()

        #??????????????????
        where_open_log = {
            'uid' : theNewid,
            'status': getPostInfo.get('isOpenWarning'),
            'oldstatus': '',
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'staff': "",
            'endtime': getPostInfo.get('stoptime')
        }
        if int(getPostInfo.get('isOpenWarning')) > 0:
            #??????warningStatusLog???
            insertsql = insertsql_factory('warningStatusLog', where_open_log)
            cursor.execute(insertsql, where_open_log)
            conn_33.commit()


        # ????????????????????????
    if getPostInfo.get('ypmodular'):
        ypmodular = {
            "KU_ID": theNewid,
            "KU_TYPE": 'MS_YPMODULAR',
            "KU_VALUE": getPostInfo.get('ypmodular')
        }
        insertsql = insertsql_factory('WK_T_USERBASEINFO', ypmodular)
        cursor.execute(insertsql, ypmodular)
        conn_33.commit()


    #**--------???????????????????????????----------serviceData-----start-----------------------**
    serviceData['KU_ID'] = theNewid
    classpid = getPostInfo.get('classpid')             #????????????????????????  ?????????
    classid = getPostInfo.get('classid')               #????????????????????????  ?????????
    classification = classid if classid else classpid
    #/*?????????????????? ?????????????????? ??????????????????*/
    if classpid == '1' and getPostInfo.get('areaSet'):
        getPostInfo['areaSet'] = '0'
    elif classpid != '1' and getPostInfo.get('areaSet'):
        getPostInfo['areaSet'] = '1'

    if classification:
        serviceData['KU_INDUSTRY'] = classification
    else:
        serviceData['KU_INDUSTRY'] = '0'

    serviceData['KU_MAINT'] = getPostInfo.get('xiaoshou') #??????
    serviceData['KU_VERSION'] = getPostInfo.get('userLeve') if getPostInfo.get('userLeve') else 'B1' # ????????????
    serviceData['KU_KEYWORDNUM'] = getPostInfo.get('keywordnum') if getPostInfo.get('keywordnum') else '300' #???????????????
    serviceData['KU_USERGENRE'] = userfl        #??????
    serviceData['KU_USERSTATUS'] = getPostInfo.get('userStates') if getPostInfo.get('userStates') else 1   #????????????????????? 0-?????? 1-?????? 2-????????????
    serviceData['KU_OAID'] = getPostInfo.get('oaId') if getPostInfo.get('oaId') else 0    #OAID
    tryDate = getPostInfo.get('F_TIME') if getPostInfo.get('F_TIME') else (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")   #?????????????????????KU_TRYSDATE ??????30???
    if tryDate:
        serviceData['KU_TRYSDATE'] = tryDate
    serviceData['KU_T_PHONECOUNT'] = getPostInfo.get('phonenum') if getPostInfo.get('phonenum') else '5'   #???????????????????????????
    saveDays = getPostInfo.get('saveDays') if getPostInfo('saveDays') else '7'
    if getPostInfo.get('classify') in (1, 2):                #???????????????????????????????????????????????????
        saveDays = 2
    serviceData['KU_SAVEDAYS'] = saveDays        # ????????????????????????
    serviceData['KU_KWSDAYMAXDATA'] = getPostInfo.get('maxdata') if getPostInfo.get('maxdata') else 100000       #?????????????????????/???
    serviceData['KU_USERDAYMAXDATA'] = getPostInfo.get('daydata') if getPostInfo.get('daydata') else 200000     #?????????????????????/???
    serviceData['KU_QQ'] = getPostInfo.get('qqNum') if getPostInfo.get('qqNum') else '0'                      #qq???????????????/???
    serviceData['KU_WEIXINCHECK'] = getPostInfo.get('weiXin') if getPostInfo.get('weiXin') else '0'           #???????????????????????????
    serviceData['KU_WEIXINNUMCOUNT'] = getPostInfo.get('weiXnum') if getPostInfo.get('weiXnum') else '0'        #?????????????????????
    serviceData['KU_WEIXINGROUPCOUNT'] = getPostInfo.get('weiPack')
    serviceData['KU_QQCOUNT'] = getPostInfo.get('qqPack')
    serviceData['KU_WORDCOUNT'] = getPostInfo.get('wordCount')
    serviceData['KU_TOPICCOUNT'] = getPostInfo.get('textfield') if getPostInfo.get('textfield') else '3'       #??????????????????
    topicrefresh = getPostInfo.get('topicrefresh')             #????????????????????????
    # if topicrefresh == '1':
    #     serviceData['KU_TOPICREFRESH'] = '1'
    # else:
    #     serviceData['KU_TOPICREFRESH'] = '0'
    serviceData['KU_OPENHIGHSET'] = getPostInfo.get('openHighSet') if getPostInfo.get('openHighSet') else '0'  #????????????????????????
    serviceData['KU_SIZE'] = getPostInfo.get('openHighSet') if getPostInfo.get('openHighSet') else '10'       #????????????????????????
    serviceData['KU_SHOWABS'] = getPostInfo.get('showAbs') if getPostInfo.get('showAbs') else '0'            #??????????????????????????????
    if add.get('KU_SEX') == '4':
        serviceData['KU_SETABSTRACT'] = '1'
        serviceData['KU_JINGZHUN'] = '1'
        serviceData['KU_SHOWALLSUB'] = '2'
        serviceData['KU_ZFWORDS'] = '1'
    else:
        serviceData['KU_SETABSTRACT'] = getPostInfo.get('setAbstract') if getPostInfo.get('setAbstract') else '1'   #?????????????????????????????????1???    0???
        serviceData['KU_JINGZHUN'] = getPostInfo.get('jingZhun') if getPostInfo.get('jingZhun') else '1'
        serviceData['KU_SHOWALLSUB'] = getPostInfo.get('noiseAllsub') if getPostInfo.get('noiseAllsub') else '1'
        serviceData['KU_ZFWORDS'] = getPostInfo.get('zfwords')  if getPostInfo.get('zfwords') else '1'
    serviceData['KU_HOMEQUERY'] = getPostInfo.get('indexAbst') if getPostInfo.get('indexAbst') else '0'         #???????????????????????? 1???  0???
    serviceData['KU_FINANCE'] = getPostInfo.get('finance') if getPostInfo.get('finance') else '1'               #?????????????????????????????? 1???  0???
    serviceData['KU_CAR'] = getPostInfo.get('carSour') if getPostInfo.get('carSour') else '1'                   #?????????????????????????????? 1???  0???
    serviceData['KU_TRAVEL'] = getPostInfo.get('Tourism') if getPostInfo.get('Tourism') else '1'                #?????????????????????????????? 1???  0???
    serviceData['KU_ISTIBETAN'] = getPostInfo.get('zwmw')  #?????????????????????????????? 1???  0???
    serviceData['KU_ISFORLANGUAGE'] = getPostInfo.get('waiwen') #???????????????????????? 1???  0???
    serviceData['KU_COMMZT'] = getPostInfo.get('commZt') if getPostInfo.get('commZt') else '1'                  #?????????????????? 1???  0???
    serviceData['KU_REPEAT'] = getPostInfo.get('remova') if getPostInfo.get('remova') else '1'                  #???????????????????????? 0??????  1?????????
    serviceData['KU_ZAOYIN'] = getPostInfo.get('noise') if getPostInfo.get('noise') else '1'                    #???????????????????????? 1???  0???
    serviceData['KU_SPECIALSPACING'] = getPostInfo.get('zhuantijianju') if getPostInfo.get('zhuantijianju') else '1'     #???????????????????????? 1?????? 0?????????
    serviceData['KU_T_SHOWALL'] = getPostInfo.get('showAll')
    serviceData['KU_INSERTINFO'] = getPostInfo.get('insertInfo') if getPostInfo.get('insertInfo') else '1'        #??????????????????????????????????????? 1??????  0?????????
    serviceData['KU_SINGLE'] = getPostInfo.get('single') if getPostInfo.get('single') else '0'             #???????????????????????????????????? 1??????  0?????????
    serviceData['KU_AREASET'] = getPostInfo.get('areaSet') if getPostInfo.get('areaSet') else '1'        #???????????????????????????????????? 1??????  0?????????
    serviceData['KU_ALLEXPORT'] = getPostInfo.get('allexport') if getPostInfo.get('allexport') else '1' #????????????????????????????????? 1??????  0?????????
    serviceData['KU_WEIXIN'] = getPostInfo.get('weixinbang') if getPostInfo.get('weixinbang') else '1'   #??????????????????????????????????????? 1??????  0?????????
    serviceData['KU_SHOWSOURCE'] = getPostInfo.get('showSource') if getPostInfo.get('showSource') else '1'  #???????????????????????????????????????????????? 1??????  0?????????
    serviceData['KU_ORDERTIME'] = getPostInfo.get('orderTime') if getPostInfo.get('orderTime') else '0'     #???????????????????????????????????? 0????????????    1????????????
    serviceData['KU_ORDERZTTJ'] = getPostInfo.get('ztDesc') if getPostInfo.get('ztDesc') else '0'           #??????????????????????????? 0????????????    1????????????
    serviceData['KU_SOURCETYPE'] = getPostInfo.get('sourceType') if getPostInfo.get('sourceType') else '0'  #???????????????????????????????????????0??????01??????02??????03??????04??????05??????06??????07??????
    serviceData['KU_ZQRUBBISH'] = getPostInfo.get('zqRubbish') if getPostInfo.get('zqRubbish') else '1'     #??????????????????????????????
    serviceData['KU_XTZAOYIN'] = getPostInfo.get('xtZaoyin') if getPostInfo.get('xtZaoyin') else '0'        #????????????????????????
    serviceData['KU_XTZHENGFU'] = getPostInfo.get('xtzhengfu') if getPostInfo.get('xtzhengfu') else '1'     #??????????????????????????? 1?????? 0??????
    serviceData['KU_YJTIME'] = getPostInfo.get('yjTime') if getPostInfo.get('yjTime') else '1'              #??????????????????????????????
    serviceData['KU_BBSVIEW'] = getPostInfo.get('bbsView') if getPostInfo.get('bbsView') else '1'           #????????????????????????
    serviceData['KU_BBSALLINFO'] = getPostInfo.get('bbsAllInfo') if getPostInfo.get('bbsAllInfo') else '1'  #?????????????????????????????????????????????
    serviceData['KU_BIGV'] = getPostInfo.get('bigV')           #???V????????????
    serviceData['KU_WEIBOCOMMENT'] = getPostInfo.get('wbpl')    #??????????????????
    serviceData['KU_HTRECOLLECT'] = getPostInfo.get('htrecollect')   #??????????????????
    serviceData['KU_LOCALBBSYJ'] = getPostInfo.get('localBbsYj') if getPostInfo.get('localBbsYj') else '1'     #?????????????????????0??????  1?????????
    serviceData['KU_COMMYJ'] = getPostInfo.get('commYj') if getPostInfo.get('commYj') else '0'                 #???????????????????????????2??????  0?????? 1????????????
    serviceData['KU_WEIBOYJ'] = getPostInfo.get('weiBoYj') if getPostInfo.get('weiBoYj') else '1'              #?????????????????????0??????  1?????? 2????????????
    serviceData['KU_YJWORDCOUNT'] = getPostInfo.get('yJWordCount') if getPostInfo.get('yJWordCount') else '50' #?????????????????????

    overtime1 = int(getPostInfo.get('overTime1')) if getPostInfo.get('overTime1') else 0
    overtime2 = int(getPostInfo.get('overTime2')) if getPostInfo.get('overTime2') else 0
    overtime = (overtime1 * 3600) + (overtime2 * 60)
    serviceData['KU_OVERTIME'] = overtime if overtime else (72*3600)
    serviceData['KU_ISLOCATIONREF'] = getPostInfo.get('Regional') if getPostInfo.get('Regional') else '0'        #????????????????????????
    serviceData['KU_DAYREPORT'] = getPostInfo.get('dayReport') if getPostInfo.get('dayReport') else '1'          #?????????????????????1???  0???
    serviceData['KU_SETREPORT'] = getPostInfo.get('setReport') if getPostInfo.get('setReport') else '1'          #?????????????????????1???  0???
    serviceData['KU_SHOWREPORT'] = getPostInfo.get('showReport') if getPostInfo.get('showReport') else ''        #????????????????????????????????????????????? ????????????   KU_SHOWREPORT
    if getPostInfo.get('weixinPushReport'):
        serviceData['KU_ISWXPUSH'] = getPostInfo.get('weixinPushReport')
    serviceData['KU_REPORTTITLE'] = getPostInfo.get('reportTitle') if getPostInfo.get('reportTitle') else '0'           #??????????????????????????????1???  0???
    serviceData['KU_DAYREPORTTIME'] = getPostInfo.get('dayReportTime') if getPostInfo.get('dayReportTime') else '0'     #??????????????????
    serviceData['KU_SENDREPORT'] = getPostInfo.get('sendReport') if getPostInfo.get('sendReport') else '0'              #????????????????????????
    serviceData['KU_CHANGEVERSION'] = '2'                           #??????KU_CHANGEVERSION?????????
    serviceData['KU_TEMPLATETYPE'] = getPostInfo.get('templateType') if getPostInfo.get('templateType') else '0'



    #====================================????????????start=============================================
    tvmonitor = getPostInfo.get('ispen', '')     #????????????????????????
    limittvgjc = getPostInfo.get('gjcnum', '')      #??????????????? 1-500
    limitdlnum = getPostInfo.get('downloadnum', '')   #????????????  1-5000
    tvchannel = getPostInfo.get('tvchannel', [])    #????????????
    tvchannel = list(set(tvchannel))
    mailopen = getPostInfo.get('mailopen')        #???????????????????????? 1??? 0???
    tvtrysdate = getPostInfo.get('tvexpire')      #????????????????????????

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
            tvchannel = tvchannel[:20]     #??????20???

        tup = tuple()
        for c in tvchannel:
            t_in = (c, theNewid)         #(??????id ,??????id)
            tup += (t_in,)

        if not tup:
            #WK_T_CHANNEL_USER???
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
        #WK_T_USERBASEINFO???
        sql = '''
            INSERT INTO WK_T_USERBASEINFO (KU_ID, KU_TYPE, KU_VALUE) VALUES
                (%s,%s,%s)
        '''
        cursor.executemany(sql, baseinfo)
        conn_33.commit()

        if mailopen == '1':                  #????????????????????????????????????????????????
            #WK_T_USERBASEINFO???
            sql = '''
                INSERT INTO WK_T_USERBASEINFO (KU_ID, KU_TYPE, KU_VALUE) VALUES
                ({},'{}','{}')
            '''.format(theNewid, 'KB_TVPUSHMAILTIME' , datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            cursor.execute(sql)
            conn_33.commit()

    for k,v in serviceData.items():
        serviceData[k] = "" if v == None else v

    if getPostInfo['openExpert'] == 'expert': #?????????????????????????????????????????????????????????
        serviceData['KU_TVISOPEN'] = getPostInfo.get('isopen')
        serviceData['KU_TVKEYWSNUM'] = getPostInfo.get('gjcnum')
        serviceData['KU_TVLASTDOWNLOADNUM'] = getPostInfo.get('downloadnum')
    #===================================????????????end===============================================================

    #?????????????????????
    serviceData['KU_OPENSMALLVIDEO'] = getPostInfo.get('openSmallVideo') if getPostInfo.get('openSmallVideo') else '1'
    #????????????????????????
    serviceData['open_topic_overseas'] = getPostInfo.get('openjwdata') if getPostInfo.get('openjwdata') else '0'

    #TAG????????????
    if getPostInfo.get('tag'):
        serviceData['TAG'] = getPostInfo.get('tag')
    if '_tsgz' in getPostInfo.get('logName'):
        serviceData['KU_USERGENRE'] = '8'
        serviceData['KU_SALE'] = '??????'

    #WK_T_USERSERVICE??? ??????
    insertsql = insertsql_factory('WK_T_USERSERVICE', serviceData)
    cursor.execute(insertsql, serviceData)
    conn_33.commit()


    #**---------HY-------WK_T_USERBASEINFO-------??????????????????------start-------------**
    muban = getPostInfo.get('muban')        #?????????????????????
    #??????????????????????????????????????????userbaseinfo??????????????????????????????????????????ID
    if userfl != '7':
        savemuban = {
            "KU_ID": theNewid,
            "KU_TYPE": 'KU_MUBANUSERID',
            "KU_VALUE": muban if muban else '0'
        }
        #??????WK_T_USERBASEINFO???
        insertsql = insertsql_factory('WK_T_USERBASEINFO', savemuban)
        cursor.execute(insertsql, savemuban)
        conn_33.commit()
    warndata_delay_time = getPostInfo.get('warndata_delay_time')   #??????????????????????????????
    warndata_delay_time = '' if warndata_delay_time == '0' or warndata_delay_time == None else warndata_delay_time

    #??????WK_T_USERBASEINFO???
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

    #---------------------------??????????????????????????????----------------------------------
    upstatus = 'http://192.168.185.123:8080'
    userStates = getPostInfo.get('userStates') if getPostInfo.get('userStates') else '1'
    if userStates == '0' or userStates == '1':
        url = upstatus + '/Redis!loadDataLimit.do' #????????????????????????????????????
    else:
        url = upstatus + '/Redis!deleteDataLimit.do'  #????????????????????????????????????
    statuid = {
        "userid": theNewid
    }
    r = requests.get(url=url, params=statuid)

    # / *???????????????2017
    # ???10???23???
    # ???????????????redis??????uid
    # ?????????????????????????????????---lc * /
    # // $haoran1 = C('waringUrl'); // ??????????????????
    # ????????????alpha
    # // self::request_by_curl($haoran1, $statuid);
    redis_server = RedisBase('192.168.185.28', 12)
    redis_server.hset('needWaringId', theNewid, theNewid)

    #?????????????????????
    if int(muban) > 0:
        tongbumuban = "http://192.168.185.97:8080" + "/UserDefinedHome/saveAddDefinedHomeClone.do"
        copymuban = {
            'userid': theNewid,
            'extendid': muban
        }
        requests.post(url=tongbumuban, data = json.dumps(copymuban))
    if userfl == '5':
        #??????id?????????????????????
        redis_server = RedisBase('', 12)  #??????????????? ???????????????
        redis_server.sadd('artificial_warning_user', theNewid)

        #????????????
        redis_server = RedisBase('192.168.16.154', 5)
        redis_server.publish('configStatus', '1')

        #2020-1-17 ????????? ??????????????? id????????????redis
        redis_server = RedisBase('', 11)   #??????????????? ?????????
        redis_server.hset('sourceAccountList', theNewid, getPostInfo.get('logName'))

        #?????????push_server???ap_ms
        add_apms = {
            "id": theNewid,
            "username": getPostInfo.get('logName'),
            'valid': '1',
            'ms_group': '2'
        }
        insertsql_factory('ap_ms', add_apms)





    #????????????
    username = getPostInfo.get('KU_LID')
    uid = getPostInfo.get('KU_ID')
    action = "??????????????????"
    type = '1'
    user = getPostInfo.get('logName')








