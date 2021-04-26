import datetime
import hashlib
import json
import random
import re
import uuid

import pymysql
import requests
from django.conf import settings
from django.http import request

from customer.service.redis_operation import RedisBase
from customer.service.serviceUtil import req_post, strstr
from customer.utils import insertsql_factory



from public.utils import parse_kwargs_for_pymysql



class CreateNewCust():
    def __init__(self,cookie):
        self.cookie = cookie
        self.ip = ""
        self.upMap = {}
        self.add = {}         #用户表
        self.userData = {}    #修改用户表
        self.dyData = {}      #地域表
        self.serviceData = {} #服务表
        self.userfl = ""      #账号分类


        self.tvremind = False


        self.jwkeywsdel_step2 = "http://192.168.185.97:8080/Redis!addRedisByUserid.do"

    #保存WK_T_USER



    #人工预警时间设置


    #创建个人服务表信息
    def createserviceData(self, getPostInfo):
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        theNewid = getPostInfo.get('cid')
        userfl = getPostInfo.get('classify')

        self.serviceData['KU_ID'] = theNewid
        classpid = getPostInfo.get('classpid')  # 添加用户行业分类  子分类
        classid = getPostInfo.get('classid')  # 添加用户行业分类  父分类
        classification = classid if classid else classpid
        # /*快速创建判断 政府不开地域 其他开启地域*/
        if classpid == '1' and getPostInfo.get('areaSet'):
            getPostInfo['areaSet'] = '0'
        elif classpid != '1' and getPostInfo.get('areaSet'):
            getPostInfo['areaSet'] = '1'

        if classification:
            self.serviceData['KU_INDUSTRY'] = classification
        else:
            self.serviceData['KU_INDUSTRY'] = '0'

        self.serviceData['KU_MAINT'] = getPostInfo.get('xiaoshou')  # 商务
        self.serviceData['KU_VERSION'] = getPostInfo.get('userLeve') if getPostInfo.get('userLeve') else 'B1'  # 版本选择
        self.serviceData['KU_KEYWORDNUM'] = getPostInfo.get('keywordnum') if getPostInfo.get(
            'keywordnum') else '300'  # 关键词数量
        self.serviceData['KU_USERGENRE'] = userfl  # 部门
        self.serviceData['KU_USERSTATUS'] = getPostInfo.get('userStates') if getPostInfo.get(
            'userStates') else 1  # 用户服务状态： 0-正常 1-试用 2-停止试用
        self.serviceData['KU_OAID'] = getPostInfo.get('oaId') if getPostInfo.get('oaId') else 0  # OAID
        tryDate = getPostInfo.get('F_TIME') if getPostInfo.get('F_TIME') else (
                    datetime.datetime.now() + datetime.timedelta(days=30)).strftime(
            "%Y-%m-%d")  # 试用截止日期：KU_TRYSDATE 默认30天
        if tryDate:
            self.serviceData['KU_TRYSDATE'] = tryDate
        self.serviceData['KU_T_PHONECOUNT'] = getPostInfo.get('phonenum') if getPostInfo.get(
            'phonenum') else '5'  # 允许登录的手机个数
        saveDays = getPostInfo.get('saveDays') if getPostInfo('saveDays') else '7'
        if getPostInfo.get('classify') in (1, 2):  # 员工和测试帐号数据保存天数固定两天
            saveDays = 2
        self.serviceData['KU_SAVEDAYS'] = saveDays  # 用户数据保留天数
        self.serviceData['KU_KWSDAYMAXDATA'] = getPostInfo.get('maxdata') if getPostInfo.get(
            'maxdata') else 100000  # 专题最大数据量/条
        self.serviceData['KU_USERDAYMAXDATA'] = getPostInfo.get('daydata') if getPostInfo.get(
            'daydata') else 200000  # 用户每天数据量/条
        self.serviceData['KU_QQ'] = getPostInfo.get('qqNum') if getPostInfo.get('qqNum') else '0'  # qq号绑定数量/条
        self.serviceData['KU_WEIXINCHECK'] = getPostInfo.get('weiXin') if getPostInfo.get('weiXin') else '0'  # 微信群监控是否开启
        self.serviceData['KU_WEIXINNUMCOUNT'] = getPostInfo.get('weiXnum') if getPostInfo.get('weiXnum') else '0'  # 微信号绑定数量
        self.serviceData['KU_WEIXINGROUPCOUNT'] = getPostInfo.get('weiPack')
        self.serviceData['KU_QQCOUNT'] = getPostInfo.get('qqPack')
        self.serviceData['KU_WORDCOUNT'] = getPostInfo.get('wordCount')
        self.serviceData['KU_TOPICCOUNT'] = getPostInfo.get('textfield') if getPostInfo.get('textfield') else '3'  # 话题挖掘个数
        topicrefresh = getPostInfo.get('topicrefresh')  # 话题挖掘刷新按钮
        # if topicrefresh == '1':
        #     serviceData['KU_TOPICREFRESH'] = '1'
        # else:
        #     serviceData['KU_TOPICREFRESH'] = '0'
        self.serviceData['KU_OPENHIGHSET'] = getPostInfo.get('openHighSet') if getPostInfo.get(
            'openHighSet') else '0'  # 是否开启高级设置
        self.serviceData['KU_SIZE'] = getPostInfo.get('openHighSet') if getPostInfo.get('openHighSet') else '10'  # 专题默认显示条数
        self.serviceData['KU_SHOWABS'] = getPostInfo.get('showAbs') if getPostInfo.get('showAbs') else '0'  # 专题默认是否显示摘要
        if self.add.get('KU_SEX') == '4':
            self.serviceData['KU_SETABSTRACT'] = '1'
            self.serviceData['KU_JINGZHUN'] = '1'
            self.serviceData['KU_SHOWALLSUB'] = '2'
            self.serviceData['KU_ZFWORDS'] = '1'
        else:
            self.serviceData['KU_SETABSTRACT'] = getPostInfo.get('setAbstract') if getPostInfo.get(
                'setAbstract') else '1'  # 用户是否使用自定义摘要1是    0否
            self.serviceData['KU_JINGZHUN'] = getPostInfo.get('jingZhun') if getPostInfo.get('jingZhun') else '1'
            self.serviceData['KU_SHOWALLSUB'] = getPostInfo.get('noiseAllsub') if getPostInfo.get('noiseAllsub') else '1'
            self.serviceData['KU_ZFWORDS'] = getPostInfo.get('zfwords') if getPostInfo.get('zfwords') else '1'
        self.serviceData['KU_HOMEQUERY'] = getPostInfo.get('indexAbst') if getPostInfo.get(
            'indexAbst') else '0'  # 是否开启主页巡查 1是  0否
        self.serviceData['KU_FINANCE'] = getPostInfo.get('finance') if getPostInfo.get(
            'finance') else '1'  # 是否开启金融专题搜索 1是  0否
        self.serviceData['KU_CAR'] = getPostInfo.get('carSour') if getPostInfo.get('carSour') else '1'  # 是否开启汽车专题搜索 1是  0否
        self.serviceData['KU_TRAVEL'] = getPostInfo.get('Tourism') if getPostInfo.get(
            'Tourism') else '1'  # 是否开启旅游专题搜索 1是  0否
        self.serviceData['KU_ISTIBETAN'] = getPostInfo.get('zwmw')  # 是否开启臧维蒙文搜索 1是  0否
        self.serviceData['KU_ISFORLANGUAGE'] = getPostInfo.get('waiwen')  # 是否开启外文搜索 1是  0否
        self.serviceData['KU_COMMZT'] = getPostInfo.get('commZt') if getPostInfo.get('commZt') else '1'  # 是否推送专题 1是  0否
        self.serviceData['KU_REPEAT'] = getPostInfo.get('remova') if getPostInfo.get('remova') else '1'  # 是否默认去重信息 0去重  1不去重
        self.serviceData['KU_ZAOYIN'] = getPostInfo.get('noise') if getPostInfo.get('noise') else '1'  # 是否开启噪音过滤 1是  0否
        self.serviceData['KU_SPECIALSPACING'] = getPostInfo.get('zhuantijianju') if getPostInfo.get(
            'zhuantijianju') else '1'  # 是否开启专题间距 1开启 0不开启
        self.serviceData['KU_T_SHOWALL'] = getPostInfo.get('showAll')
        self.serviceData['KU_INSERTINFO'] = getPostInfo.get('insertInfo') if getPostInfo.get(
            'insertInfo') else '1'  # 展示人工添加专题信息功能： 1展示  0不展示
        self.serviceData['KU_SINGLE'] = getPostInfo.get('single') if getPostInfo.get(
            'single') else '0'  # 用户词设置是否允许单字： 1允许  0不允许
        self.serviceData['KU_AREASET'] = getPostInfo.get('areaSet') if getPostInfo.get(
            'areaSet') else '1'  # 客户是否允许设置地域词： 1允许  0不允许
        self.serviceData['KU_ALLEXPORT'] = getPostInfo.get('allexport') if getPostInfo.get(
            'allexport') else '1'  # 客户是否允许全部导出： 1允许  0不允许
        self.serviceData['KU_WEIXIN'] = getPostInfo.get('weixinbang') if getPostInfo.get(
            'weixinbang') else '1'  # 客户是否允许开通微信绑定： 1允许  0不允许
        self.serviceData['KU_SHOWSOURCE'] = getPostInfo.get('showSource') if getPostInfo.get(
            'showSource') else '1'  # 客户专题是否允许自定义来源查询： 1允许  0不允许
        self.serviceData['KU_ORDERTIME'] = getPostInfo.get('orderTime') if getPostInfo.get(
            'orderTime') else '0'  # 舆情浏览信息按时间排序： 0发布时间    1采集时间
        self.serviceData['KU_ORDERZTTJ'] = getPostInfo.get('ztDesc') if getPostInfo.get(
            'ztDesc') else '0'  # 首页专题统计排序： 0从大到小    1专题设置
        self.serviceData['KU_SOURCETYPE'] = getPostInfo.get('sourceType') if getPostInfo.get(
            'sourceType') else '0'  # 专题浏览默认显示来源类型：0全部01新闻02论坛03博客04微博05平媒06微信07视频
        self.serviceData['KU_ZQRUBBISH'] = getPostInfo.get('zqRubbish') if getPostInfo.get(
            'zqRubbish') else '1'  # 是否开启早期垃圾过滤
        self.serviceData['KU_XTZAOYIN'] = getPostInfo.get('xtZaoyin') if getPostInfo.get('xtZaoyin') else '0'  # 是否关闭系统噪音
        self.serviceData['KU_XTZHENGFU'] = getPostInfo.get('xtzhengfu') if getPostInfo.get(
            'xtzhengfu') else '1'  # 是否关闭系统正负面 1开启 0关闭
        self.serviceData['KU_YJTIME'] = getPostInfo.get('yjTime') if getPostInfo.get('yjTime') else '1'  # 是否关闭预警时间限制
        self.serviceData['KU_BBSVIEW'] = getPostInfo.get('bbsView') if getPostInfo.get('bbsView') else '1'  # 展示地域论坛功能
        self.serviceData['KU_BBSALLINFO'] = getPostInfo.get('bbsAllInfo') if getPostInfo.get(
            'bbsAllInfo') else '1'  # 客户是否允许地域论坛入全部信息
        self.serviceData['KU_BIGV'] = getPostInfo.get('bigV')  # 大V评论开关
        self.serviceData['KU_WEIBOCOMMENT'] = getPostInfo.get('wbpl')  # 微博评论开关
        self.serviceData['KU_HTRECOLLECT'] = getPostInfo.get('htrecollect')  # 话题回采开关
        self.serviceData['KU_LOCALBBSYJ'] = getPostInfo.get('localBbsYj') if getPostInfo.get(
            'localBbsYj') else '1'  # 地域论坛预警：0发送  1不发送
        self.serviceData['KU_COMMYJ'] = getPostInfo.get('commYj') if getPostInfo.get(
            'commYj') else '0'  # 是否发送公共预警：2全部  0负面 1全部不发
        self.serviceData['KU_WEIBOYJ'] = getPostInfo.get('weiBoYj') if getPostInfo.get(
            'weiBoYj') else '1'  # 微博主体预警：0全部  1负面 2全部不发
        self.serviceData['KU_YJWORDCOUNT'] = getPostInfo.get('yJWordCount') if getPostInfo.get(
            'yJWordCount') else '50'  # 预警关键词个数

        overtime1 = int(getPostInfo.get('overTime1')) if getPostInfo.get('overTime1') else 0
        overtime2 = int(getPostInfo.get('overTime2')) if getPostInfo.get('overTime2') else 0
        overtime = (overtime1 * 3600) + (overtime2 * 60)
        self.serviceData['KU_OVERTIME'] = overtime if overtime else (72 * 3600)
        self.serviceData['KU_ISLOCATIONREF'] = getPostInfo.get('Regional') if getPostInfo.get(
            'Regional') else '0'  # 是否开启地域数据
        self.serviceData['KU_DAYREPORT'] = getPostInfo.get('dayReport') if getPostInfo.get(
            'dayReport') else '1'  # 是否生成日报：1是  0否
        self.serviceData['KU_SETREPORT'] = getPostInfo.get('setReport') if getPostInfo.get(
            'setReport') else '1'  # 是否定制日报：1是  0否
        self.serviceData['KU_SHOWREPORT'] = getPostInfo.get('showReport') if getPostInfo.get(
            'showReport') else ''  # 前台展示供用户定制的日报模板： 凝瑞模板   KU_SHOWREPORT
        if getPostInfo.get('weixinPushReport'):
            self.serviceData['KU_ISWXPUSH'] = getPostInfo.get('weixinPushReport')
        self.serviceData['KU_REPORTTITLE'] = getPostInfo.get('reportTitle') if getPostInfo.get(
            'reportTitle') else '0'  # 是否自定义日报标题：1是  0否
        self.serviceData['KU_DAYREPORTTIME'] = getPostInfo.get('dayReportTime') if getPostInfo.get(
            'dayReportTime') else '0'  # 日报生成时间
        self.serviceData['KU_SENDREPORT'] = getPostInfo.get('sendReport') if getPostInfo.get(
            'sendReport') else '0'  # 是否发送日报邮件
        self.serviceData['KU_CHANGEVERSION'] = '2'  # 设置KU_CHANGEVERSION字段为
        self.serviceData['KU_TEMPLATETYPE'] = getPostInfo.get('templateType') if getPostInfo.get('templateType') else '0'

        # ====================================电视监控start=============================================
        tvmonitor = getPostInfo.get('ispen', '')  # 是否开启电视监控
        limittvgjc = getPostInfo.get('gjcnum', '')  # 关键词个数 1-500
        limitdlnum = getPostInfo.get('downloadnum', '')  # 下载个数  1-5000
        tvchannel = getPostInfo.get('tvchannel', [])  # 电视频道
        tvchannel = list(set(tvchannel))
        mailopen = getPostInfo.get('mailopen')  # 是否开启邮件开关 1开 0关
        tvtrysdate = getPostInfo.get('tvexpire')  # 电视监控到期日期

        if tvmonitor == '1' and limittvgjc != '' and tvchannel != '' and (not tvchannel):
            self.serviceData['KU_TVISOPEN'] = '1'
            if int(limittvgjc) > 2 and getPostInfo['xiaoshou'] != 'YDY':
                self.serviceData['KU_TVKEYWSNUM'] = '2'
            else:
                self.serviceData['KU_TVKEYWSNUM'] = limittvgjc

            if int(limitdlnum) > 2 and getPostInfo['xiaoshou'] != 'YDY':
                self.serviceData['KU_TVDOWNLOADNUM'] = '2'
                self.serviceData['KU_TVLASTDOWNLOADNUM'] = '2'
            else:
                self.serviceData['KU_TVDOWNLOADNUM'] = limitdlnum
                self.serviceData['KU_TVLASTDOWNLOADNUM'] = limitdlnum
            if len(tvchannel) > 20 and getPostInfo['xiaoshou'] != 'YDY':
                self.tvremind = True
                tvchannel = tvchannel[:20]  # 限定20个

            tup = tuple()
            for c in tvchannel:
                t_in = (c, theNewid)  # (频道id ,用户id)
                tup += (t_in,)

            if not tup:
                # WK_T_CHANNEL_USER表
                sql = '''
                        INSERT INTO WK_T_CHANNEL_USER (KC_ID, KU_ID) VALUES
                        (%s,%s)
                    '''
                cursor.executemany(sql, tup)
                conn.commit()

            baseinfo = (
                (theNewid, 'KU_TVTRYSDATE', tvtrysdate),
                (theNewid, 'KU_TVMAILSWITCH', mailopen)
            )
            # WK_T_USERBASEINFO表
            sql = '''
                    INSERT INTO WK_T_USERBASEINFO (KU_ID, KU_TYPE, KU_VALUE) VALUES
                        (%s,%s,%s)
                '''
            cursor.executemany(sql, baseinfo)
            conn.commit()

            if mailopen == '1':  # 开启邮箱推送设置推送数据起始时间
                # WK_T_USERBASEINFO表
                sql = '''
                        INSERT INTO WK_T_USERBASEINFO (KU_ID, KU_TYPE, KU_VALUE) VALUES
                        ({},'{}','{}')
                    '''.format(theNewid, 'KB_TVPUSHMAILTIME', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                cursor.execute(sql)
                conn.commit()

        for k, v in self.serviceData.items():
            self.serviceData[k] = "" if v == None else v

        if getPostInfo['openExpert'] == 'expert':  # 修复专家添加时没有频道导致开始失败问题
            self.serviceData['KU_TVISOPEN'] = getPostInfo.get('isopen')
            self.serviceData['KU_TVKEYWSNUM'] = getPostInfo.get('gjcnum')
            self.serviceData['KU_TVLASTDOWNLOADNUM'] = getPostInfo.get('downloadnum')
        # ===================================电视监控end===============================================================

        # 是否开启小视频
        self.serviceData['KU_OPENSMALLVIDEO'] = getPostInfo.get('openSmallVideo') if getPostInfo.get(
            'openSmallVideo') else '1'
        # 开通事件境外数据
        self.serviceData['open_topic_overseas'] = getPostInfo.get('openjwdata') if getPostInfo.get('openjwdata') else '0'

        # TAG备注字段
        if getPostInfo.get('tag'):
            self.serviceData['TAG'] = getPostInfo.get('tag')
        if '_tsgz' in getPostInfo.get('logName'):
            self.serviceData['KU_USERGENRE'] = '8'
            self.serviceData['KU_SALE'] = '缪杨'

        # WK_T_USERSERVICE表 插入
        insertsql = insertsql_factory('WK_T_USERSERVICE', self.serviceData)
        cursor.execute(insertsql, self.serviceData)
        conn.commit()

    #添加用户信息
    def adduserinfo(self, getPostInfo):
        # 此函数需要连的数据库
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)


        theNewid = getPostInfo.get('cid')
        userfl = getPostInfo.get('classify')

        muban = getPostInfo.get('muban')  # 用户选择的模板
        # 如果账号分类不是模板账号，在userbaseinfo表中保存一个该用户继承的模板ID
        if userfl != '7':
            savemuban = {
                "KU_ID": theNewid,
                "KU_TYPE": 'KU_MUBANUSERID',
                "KU_VALUE": muban if muban else '0'
            }
            # 添加WK_T_USERBASEINFO表
            insertsql = insertsql_factory('WK_T_USERBASEINFO', savemuban)
            cursor.execute(insertsql, savemuban)
            conn.commit()
        warndata_delay_time = getPostInfo.get('warndata_delay_time')  # 容忍预警数据延迟时间
        warndata_delay_time = '' if warndata_delay_time == '0' or warndata_delay_time == None else warndata_delay_time

        # 添加WK_T_USERBASEINFO表
        savedelaytime = {
            "KU_ID": theNewid,
            "KU_TYPE": 'warndata_delay_time',
            "KU_VALUE": warndata_delay_time
        }
        insertsql = insertsql_factory('WK_T_USERBASEINFO', savedelaytime)
        cursor.execute(insertsql, savedelaytime)
        conn.commit()

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

        userinfoarr = dict((str(k), v) for k, v in USERBASEINFO.items() if v)
        userinfodata = ",".join(userinfoarr)
        infodatas = {
            "KU_ID": theNewid,
            "KU_TYPE": 'dataType',
            "KU_VALUE": userinfodata
        }
        insertsql = insertsql_factory('WK_T_USERBASEINFO', infodatas)
        cursor.execute(insertsql, infodatas)
        conn.commit()

    # 新建完成后需要执行的
    def endAfter(self, getPostInfo):
        result = {
            "msg": "",
            "code": 200,
            "data": None
        }

        #此函数需要连的数据库
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)



        theNewid = getPostInfo.get('cid')
        muban = getPostInfo.get('muban')
        userfl = getPostInfo.get('classify')
        uid = getPostInfo.get('KU_ID')             #操作人


        upstatus = 'http://192.168.185.123:8080'
        userStates = getPostInfo.get('userStates') if getPostInfo.get('userStates') else '1'
        if userStates == '0' or userStates == '1':
            url = upstatus + '/Redis!loadDataLimit.do'  # 用户信息数量限制同步接口
        else:
            url = upstatus + '/Redis!deleteDataLimit.do'  # 用户信息数量限制删除接口
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

        # 用户选择了模板
        if int(muban) > 0:
            tongbumuban = "http://192.168.185.97:8080" + "/UserDefinedHome/saveAddDefinedHomeClone.do"
            copymuban = {
                'userid': theNewid,
                'extendid': muban
            }
            requests.post(url=tongbumuban, data=json.dumps(copymuban))
        if userfl == '5':
            # 账号id入预警账号缓存
            redis_server = RedisBase('', 12)  # 这里不知道 服务器和库
            redis_server.sadd('artificial_warning_user', theNewid)

            # 发布消息
            redis_server = RedisBase('192.168.16.154', 5)
            redis_server.publish('configStatus', '1')

            # 2020-1-17 新逻辑 是预警账号 id添加到新redis
            redis_server = RedisBase('', 11)  # 这里不知道 服务器
            redis_server.hset('sourceAccountList', theNewid, getPostInfo.get('logName'))

            # 添加到push_server库ap_ms
            add_apms = {
                "id": theNewid,
                "username": getPostInfo.get('logName'),
                'valid': '1',
                'ms_group': '2'
            }
            sql = insertsql_factory('ap_ms', add_apms)
            conn.select_db('push_server')
            cursor.execute(sql)
            conn.commit()

        #操作记录
        data = {
            'username': getPostInfo.get('KU_LID'),
            'userid':getPostInfo.get('KU_ID'),
            'action': '新建秘书账号',
            'type': '1',
            'user': getPostInfo.get('logName'),
            'where': dict(
                self.add.items() + self.upMap.items() + self.userData.items() + self.serviceData.items() + self.dyData.items()),
            'id': theNewid,
            'agent': request.HttpHeaders.get('User-Agent'),
            'ip': request.HttpRequest().META.get('HTTP_X_FORWARDED_FOR') if request.HttpRequest().META.get('HTTP_X_FORWARDED_FOR') else request.HttpRequest().META.get('REMOTE_ADDR')
        }
        redis_server = RedisBase('192.168.16.154', 5)  # 这里不知道 服务器
        redis_server.lpush('adminuserlog', json.dumps(data))

        if self.tvremind:
            result['msg'] = '频道设置过多，已自动截取前20个保存！'
            result['code'] = 201
            result['data'] = json.dumps(self.tvremind)
            return result

        #没用数据
        set = {
            "userid": theNewid,
            "sso_account_id": getPostInfo.get("ssoAccountId", ""),
            "account": getPostInfo.get("logName", ""),
            "password": hashlib.md5(getPostInfo['pasd'].encode(encoding='UTF-8')).hexdigest().upper(),
            "name": getPostInfo.get("zsname"),
            "phone": getPostInfo.get("userphone"),
            "email": getPostInfo.get("uemail"),
            "state": 1,
            "ctime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        # sql = insertsql_factory('ms_account', set)
        # cursor.execute(sql, set)
        # conn.commit()

        #?????
        statuid = {
            "userid": theNewid
        }
        r = req_post(self.jwkeywsdel_step2, statuid)


        ispl = strstr(getPostInfo.get("tag"), "批量")

        if (not getPostInfo.get('tag')) or len(ispl) < 1:
            #zpp 新建用户 消息订阅 -- alpha
            redis_server = RedisBase('192.168.16.154', 5)
            redis_server.publish('configStatus', '1')

        #保存用户选择的专题模板
        areaid = ''
        if getPostInfo.get('city_id'):
            areaid = getPostInfo.get('city_id')
        elif getPostInfo.get('province_id'):
            areaid = getPostInfo.get('province_id')

        if getPostInfo.get('newksid') and areaid and theNewid:
            compysecialtemplate = self.save_Selected_Special_Template(getPostInfo.get('newksid'), areaid, theNewid, uid)   # 第一次失败 再次创建
            if not compysecialtemplate:
                compysecialtemplate = self.save_Selected_Special_Template(getPostInfo.get('newksid'), areaid, theNewid, # 第二次 存入redis
                                                                          uid)
                if not compysecialtemplate:
                    redis_server = RedisBase('192.168.185.28', 1)
                    redis_server.hset('createspecial', theNewid, getPostInfo.get('newksid') + '/' + areaid)

        #账号类型:添加代理商 政府用户 无客户地域 需保存锁定地域
        if getPostInfo.get('agent') and getPostInfo.get('kusex') == '1' and getPostInfo.get('province_id'):
            add = {
                'KU_ID': theNewid,
                'KU_TYPE': 'region_lock_word',
                'KU_VALUE': getPostInfo.get('region_lock_word')
            }
            sql = insertsql_factory('WK_T_USERBASEINFO',add)
            conn.select_db('yqms2')
            cursor.execute(sql, add)
            conn.commit()

        #企业用户 开通境外数据 需填写境外锁定词
        if getPostInfo.get('kusex') == '4' and getPostInfo.get('openjw') == '1':
            add = {
                'KU_ID': theNewid,
                'KU_TYPE': 'oversea_lock_word',
                'KU_VALUE': getPostInfo.get('oversea_lock_word')
            }
            sql = insertsql_factory('WK_T_USERBASEINFO', add)
            conn.select_db('yqms2')
            cursor.execute(sql, add)
            conn.commit()

        #新建4.0秘书
        if userfl in ['0','1','2','3','5','7'] and int(getPostInfo.get('agent')) <1 :
            add1 = {
                'KU_ID': theNewid,
                'KU_TYPE': 'ms_version',
                'KU_VALUE': '4.0'
            }
            add2 = {
                'KU_ID': theNewid,
                'KU_TYPE': 'ms_version_date',
                'KU_VALUE': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            sql1 = insertsql_factory('WK_T_USERBASEINFO', add1)
            sql2 = insertsql_factory('WK_T_USERBASEINFO', add2)
            conn.select_db('yqms2')
            cursor.execute(sql1, add1)
            cursor.execute(sql2, add2)
            conn.commit()

    #enAfter 函数里调用的   保存秘书所选专题模板
    def save_Selected_Special_Template(self, template_id, areaid, id, uid):
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        #所在地域
        template_id_lst = template_id.split(',')
        conn.select_db('yqht')
        sql = '''
            SELECT province, city, county FROM b_locationinfo WHERE uuid='{}'
        '''.format(areaid)
        cursor.execute(sql)
        res_area = cursor.fetchone()
        if res_area['county']:
            area = res_area['country']
        elif res_area['city']:
            area = res_area['city']
        else:
            area = res_area['province']


        #用户数据来源
        sql = '''
            SELECT U.KU_COMPANY as abroad,U.KU_SEARCH as search,S.KU_FINANCE as jinrong,
            S.KU_CAR as car,S.KU_TRAVEL as lvyou,S.KU_ISTIBETAN as minzu,
            S.KU_ISFORLANGUAGE as waiwen,S.KU_INDUSTRY FROM WK_T_USER U,WK_T_USERSERVICE S WHERE
            U.KU_ID = '{}' AND U.KU_ID=S.KU_ID
        '''.format(id)
        conn.select_db('yqms2')
        cursor.execute(sql)
        res = cursor.fetchone()

        selected = set()
        if res['aborad']:
            selected.add('3')
        if res['search']:
            selected.add('8')
        if res['jinrong']:
            selected.add('9')
        if res['car']:
            selected.add('10')
        if res['lvyou']:
            selected.add('11')
        #全部要判断的来源 境外3  搜索8  金融9  汽车10  旅游11
        all = {'3', '8', '9', '10', '11'}
        remove = all - selected

        #WT_K_SUBRELATION_BACKEND表数据
        sql = '''
            SELECT * FROM WT_K_SUBRELATION_BACKEND WHERE KS_ID IN (%s)
        ''' % (','.join([ "'" + t +"'" for t in template_id_lst]))
        conn.select_db('yqms2')
        cursor.execute(sql)
        subrel = cursor.fetchall()

        # WK_T_KEYWS_BACKEND表数据
        kkid = []
        for s in subrel:
            s["KU_ID"] = uid
            s["KK_TYPE"] = '01'            # 专题类型 默认01
            del s["KS_CLASSIFICATIONID"]   #模板特有字段 不要
            kkid.append(str("'" + s["KS_SID"] + "'"))

        sql = '''
            SELECT * FROM WK_T_KEYWS_BACKEND WHERE KK_ID IN (%s)
        ''' % (','.join(kkid))
        cursor.execute(sql)
        keyws = cursor.fetchall()


        for k in keyws:
            k['KU_ID'] = uid
            temp = k['KK_DATASOURCETYPE'].split(',')
            temp = set(temp)
            k['KK_DATASOURCETYPE'] = ','.join(temp - remove) #除去不需要的数据来源
            k['KK_MUST'] = area
            #替换表达式中的地域
            k['KK_LABEL'] = re.sub(r"\#\$\%(.*?)\#\$\%", "(" + area + ")" , k['KK_LABEL'])
            k['KK_TYPE'] = '01'
            del k['KK_CLASSIFICATIONID']  #模板特有字段 不要

            old = k['KK_ID']
            new = str(uuid.uuid4()) + str(datetime.datetime.now().timestamp()) + str(random.randint(0, 9999999))
            new = hashlib.md5(new.encode(encoding='UTF-8')).hexdigest().upper()
            k["KU_ID"] = id
            k["KK_ID"] = new
            for s in subrel:
                if s["KS_SID"] == old:
                    s['KS_SID'] = new
                s["KU_ID"] = id
                s["KS_ID"] = new
                s["KS_PID"] = '0'  #无上下级关系

        conn.begin()
        sql = insertsql_factory('WK_T_KEYWS', keyws)
        step1 = cursor.execute(sql)
        if not step1:
            conn.rollback()
            cursor.close()
            conn.close()
            return False

        sql = insertsql_factory('WT_K_SUBRELATION', keyws)
        step2 = cursor.execute(sql)
        if not step2:
            conn.rollback()
            cursor.close()
            conn.close()
            return False
        # 进行词同步
        diaoyong = {
            "userid": id
        }
        r = req_post(self.jwkeywsdel_step2, diaoyong)
        if r.get('result') != '1':
            conn.rollback()
            cursor.close()
            conn.close()
            return False

        conn.commit()

        # 写日志
        sql = '''
            SELECT * FROM WT_K_SUBRELATION_BACKEND WHERE KS_ID IN (%s)
        ''' % (','.join(["'" + t + "'" for t in template_id_lst]))
        cursor.execute(sql)
        res = cursor.fetchall()
        writelog = ""
        for r in res:
            writelog += str(r) + ','
        writelog = writelog.strip(',')
        who = self.cookie
        #写日志
        return True























