import re

import pymysql

from customer.service.GetJumpData import getconnect

'''
* 创建用户库
* @param $ip 用户库所在的ip
* @param $uid 用户ID
'''

def ipcreate(ip, uid):
    result = {"code": 200, "msg": ""}

    ipInfo = getconnect(ip, uid)
    #ipInfo ----> "mysql://fuser:kmyln08y6xa5@mysql24-ref-1.istarshine.net.cn:3306/U" + uid
    pattern = r'mysql://(.*):(.*)@(.*)/'
    r = re.match(pattern, ipInfo)
    musername = r.group(1)
    password = r.group(2)
    connip = r.group(3)
    host = connip.split(':')[0]
    port = int(connip.split(":")[1])
    try:
        db_name = 'U{}'.format(str(uid))
        connect = pymysql.connect(host=host,port=port, user=musername, password=password)
        if connect:
            cur = connect.cursor(pymysql.cursors.DictCursor)
            query_sql = '''
                CREATE DATABASE {}
            '''.format(db_name)
            cur.execute(query_sql)
            connect.commit()
            connect.select_db(db_name)
            query_sql = '''
                set names utf8
            '''
            cur.execute(query_sql)
            create_sql = '''
                CREATE TABLE `YQZB_T_ENGINE_INFO` (
                    `UUID` VARCHAR(140) NOT NULL,
                    `KT_UUID` VARCHAR(40) NOT NULL,
                    `KN_TYPE` CHAR(2) NOT NULL,
                    `KN_TITLE` CHAR(150) NULL DEFAULT NULL,
                    `KN_SOURCE` CHAR(50) NULL DEFAULT NULL,
                    `KN_URL` VARCHAR(270) NULL DEFAULT NULL,
                    `KN_TIME` CHAR(20) NULL DEFAULT NULL,
                    `KN_CTIME` CHAR(20) NULL DEFAULT NULL,
                    `KN_REPEATCOUNT` INT(4) NULL DEFAULT NULL,
                    `KN_ABSTRACT` VARCHAR(200) NULL DEFAULT NULL,
                    `KV_VISITCOUNT` INT(4) NULL DEFAULT NULL,
                    `KV_REPLY` INT(4) NULL DEFAULT NULL,
                    `KV_COLLECTION` INT(4) NULL DEFAULT NULL,
                    `KV_TRANSPORT` INT(4) NULL DEFAULT NULL,
                    `KV_REPEAT` INT(4) NULL DEFAULT NULL,
                    `KV_STATE` VARCHAR(2) NULL DEFAULT NULL,
                    `KN_SITE` CHAR(50) NULL DEFAULT NULL,
                    `KN_ORIENTATION` CHAR(2) NULL DEFAULT NULL,
                    `KN_AUTHOR` VARCHAR(50) NULL DEFAULT NULL,
                    `KN_TOPICUID` VARCHAR(40) NULL DEFAULT NULL,
                    `KN_INPUTTYPE` VARCHAR(2) NULL DEFAULT NULL,
                    `KN_ORIEN_LEVEL` VARCHAR(2) NULL DEFAULT NULL,
                    `KN_FANSCOUNT` INT(9) NULL DEFAULT NULL,
                    `KN_CONTENT` VARCHAR(3500) NULL DEFAULT NULL,
                    `KN_JINGWAI` VARCHAR(2) NULL DEFAULT NULL,
                    `KN_TITLESEG` VARCHAR(200) NULL DEFAULT NULL,
                    `KN_TOPICWORDS` VARCHAR(60) NULL DEFAULT NULL,
                    `KN_ZYINFO` VARCHAR(50) NULL DEFAULT NULL,
                    `KT_WEIBOUID` VARCHAR(30) NULL DEFAULT NULL,
                    `KN_ARG` VARCHAR(50) NULL DEFAULT NULL,
                    `ConfigID` VARCHAR(50) NULL,
                    `AUTOCLASSLY` VARCHAR(200) NULL,
                    `CLASSLYTYPE` VARCHAR(5) NULL,
                    `CLASSLYINFO` VARCHAR(200) NULL,
                    `GDZMCLASSLY` VARCHAR(200) NULL,
                    `GDFMCLASSLY` VARCHAR(200) NULL,
                    `GDFMCLASSLYINFO` VARCHAR(200) NULL,
                    `GDZMCLASSLYINFO` VARCHAR(200) NULL,
                    `GDZFXX` VARCHAR(10) NULL,
                    `sheng` VARCHAR(50) NULL,
                    `shi` VARCHAR(50) NULL,
                    `xian` VARCHAR(50) NULL,
                    `jigou` VARCHAR(100) NULL,
                    `GDINFO` VARCHAR(300) NULL,
                    `gender` VARCHAR(20) NULL,
                    `WEBNAMEDOMAIN` VARCHAR(50) NULL,
                    `WEBNAMELEVER` VARCHAR(10) NULL,
                    `location` VARCHAR(20) NULL,
                    `verified` VARCHAR(20) NULL,
                    `USERID` VARCHAR(50) NULL,
                    `screen_name` VARCHAR(50) NULL,
                    `KN_ARG1` VARCHAR(100) NULL,
                    `KN_ARG2` VARCHAR(100) NULL,
                    `KN_ARG3` VARCHAR(100) NULL,
                    `KN_ARG4` VARCHAR(100) NULL,
                    `KV_DTCTIME` DATETIME NOT NULL DEFAULT '1970-01-01',
                    `KV_DTTIME` DATETIME NOT NULL DEFAULT '1970-01-01',
                    PRIMARY KEY (`UUID`),
                    UNIQUE INDEX `UUID` (`UUID`) USING BTREE,
                    INDEX `KT_UUID` (`KT_UUID`) USING BTREE,
                    INDEX `TOPICUID` (`KN_TOPICUID`) USING BTREE,
                    INDEX `URL` (`KN_URL`) USING BTREE,
                    INDEX `CTIME` (`KN_CTIME`) USING BTREE,
                    INDEX `SITE` (`KN_SITE`) USING BTREE,
                    INDEX `ORIENTATION` (`KN_ORIENTATION`) USING BTREE,
                    INDEX `KN_TIME` (`KN_TIME`) USING BTREE,
                    INDEX `INDEX_KV_DTCTIME` (`KV_DTCTIME`),
                    INDEX `INDEX_KV_DTTIME` (`KV_DTTIME`)
                    )
                    COLLATE='utf8_general_ci'
                    ENGINE=InnoDB
            
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return  result

            create_sql = '''
                CREATE TABLE `WK_T_VALIDATION_INFO` (
                  `KV_UUID` varchar(40) NOT NULL,
                  `KV_SOURCETYPE` varchar(2) DEFAULT NULL,
                  `KV_TITLE` varchar(150) DEFAULT NULL,
                  `KV_SOURCE` varchar(50) DEFAULT NULL,
                  `KV_URL` varchar(270) DEFAULT NULL,
                  `KV_TIME` varchar(20) DEFAULT NULL,
                  `KV_CTIME` varchar(20) DEFAULT NULL,
                  `KV_VISITCOUNT` int(4) DEFAULT NULL,
                  `KV_REPLY` int(4) DEFAULT NULL,
                  `KV_COLLECTION` int(4) DEFAULT NULL,
                  `KV_TRANSPORT` int(4) DEFAULT NULL,
                  `KV_REPEAT` int(4) DEFAULT NULL,
                  `KV_ABSTRACT` varchar(200) DEFAULT NULL,
                  `KV_ORIENTATION` varchar(3) DEFAULT NULL,
                  `KV_FLAG` varchar(1) DEFAULT NULL,
                  `KV_SITE` varchar(50) DEFAULT NULL,
                  `KV_TEMPLET` varchar(10) DEFAULT NULL,
                  `KV_STATE` varchar(1) DEFAULT NULL,
                  `KV_SNA_FLAG` varchar(1) DEFAULT NULL,
                  `KV_INDEX_FLAG` varchar(1) DEFAULT NULL,
                  `KV_ORIEN_LEVEL` int(2) DEFAULT NULL,
                  `KV_INSERT_TIME` varchar(20) DEFAULT NULL,
                  `KV_TITLESIMHASH` varchar(50) DEFAULT NULL,
                  `KV_TITLEKEYWORDS` varchar(200) DEFAULT NULL,
                  `KV_INSIDEFORWARDSTATUS` int(4) DEFAULT NULL,
                  `KV_INSIDEFORWARDCOUNT` int(4) DEFAULT NULL,
                  `KV_CONTENTSIMHASH` varchar(50) DEFAULT NULL,
                  `KV_CONTENTKEYWORDS` varchar(200) DEFAULT NULL,
                  `KV_TITLEREFHASH` varchar(200) DEFAULT NULL,
                  `KV_ISTF` int(2) DEFAULT NULL,
                  `KV_ISRD` int(2) DEFAULT NULL,
                  `KV_PROCINCE` varchar(80) DEFAULT NULL,
                  `KV_CITE` varchar(80) DEFAULT NULL,
                  `KV_COUNTY` varchar(80) DEFAULT NULL,
                  `KV_FANSNUM` int(7) DEFAULT NULL,
                  `KV_WBAUTHORPIC` varchar(200) DEFAULT NULL,
                  `KV_MESSAGENUM` int(5) DEFAULT NULL,
                  `KV_ARG3` varchar(50) DEFAULT NULL,
                  `KV_AUTHOR` varchar(50) DEFAULT NULL,
                  `KV_SITEID` varchar(50) DEFAULT NULL,
                  `LOSTTIME` varchar(20) DEFAULT NULL,
                  `ENTITYAREA` varchar(200) DEFAULT NULL,
                  `ENTITYPEOPLE` varchar(200) DEFAULT NULL,
                  `ENTITYMETHANISM` varchar(200) DEFAULT NULL,
                  `NOISESTATUS` varchar(5) DEFAULT NULL,
                  `KV_DTCTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
                  `KV_DTTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
                  PRIMARY KEY (`KV_UUID`),
                  KEY `INDEX_CTIME` (`KV_CTIME`) USING BTREE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
            
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                CREATE TABLE `WK_T_VALIDATION_INFOCNT` (
                    `KV_UUID` varchar(40) NOT NULL,
                    `KV_CTIME` varchar(20) DEFAULT NULL,
                    `KV_CONTENT` mediumtext,`LOSTTIME` varchar(20) DEFAULT NULL,
                    `KV_DTCTIME` DATETIME NOT NULL DEFAULT "1970-01-01",
                    `KV_DTTIME` DATETIME NOT NULL DEFAULT "1970-01-01",
                    `KV_CONTENT_XML` longtext,
                    PRIMARY KEY (`KV_UUID`),
                    UNIQUE
                    KEY `PK_VALIDATION_CNT` (`KV_UUID`) USING BTREE,
                    KEY `INDEX_CTIME` (`KV_CTIME`) USING BTREE,
                    KEY `INDEX_LOSTTIME` (`LOSTTIME`) USING BTREE,
                    KEY `INDEX_KV_DTCTIME` (`KV_DTCTIME`),
                    KEY `INDEX_KV_DTTIME` (`KV_DTTIME`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4   
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                CREATE TABLE `WK_T_VALIDATION_REF` (
			  `KR_UUID` varchar(40) NOT NULL DEFAULT '',
			  `KV_UUID` varchar(40) DEFAULT NULL,
			  `KR_INFOTYPE` varchar(2) DEFAULT NULL,
			  `KR_KEYWORDID` varchar(40) DEFAULT NULL,
			  `KR_UID` int(5) DEFAULT NULL,
			  `KR_STATE` varchar(2) DEFAULT NULL,
			  `KR_CTIME` varchar(20) DEFAULT NULL,
			  `KR_GTIME` varchar(20) DEFAULT NULL,
			  `KR_ISLOCAL` varchar(1) DEFAULT NULL,
			  `KV_FLAG` varchar(1) DEFAULT NULL,
			  `ARG1` varchar(50) DEFAULT NULL,
			  `ARG2` varchar(50) DEFAULT NULL,
			  `ARG3` varchar(50) DEFAULT NULL,
			  `KEYWORD` varchar(200) DEFAULT NULL,
			  `ORIENTATION` varchar(2) DEFAULT NULL,
			  `ISYJ` int(2) DEFAULT NULL,
			  `ISREAD` int(2) DEFAULT NULL,
			  `ISMYATTENTION` int(2) DEFAULT NULL,
			  `ISFEEDBACK` int(2) DEFAULT NULL,
			  `ARG4` varchar(50) DEFAULT NULL,
			  `ARG5` varchar(50) DEFAULT NULL,
			  `KV_VISITCOUNT` int(2) DEFAULT NULL,
			  `KV_REPLY` int(2) DEFAULT NULL,
			  `KV_SIMHASH` varchar(50) DEFAULT NULL,
			  `KV_WEBNAME` varchar(50) DEFAULT NULL,
			  `KV_COLLECTTIME` varchar(20) DEFAULT NULL,
			  `KV_SOURCETYPE` varchar(2) DEFAULT NULL,
			  `KV_HOT` int(2) DEFAULT NULL,
			  `KV_ISTF` int(2) DEFAULT NULL,
			  `KV_ISRD` int(2) DEFAULT NULL,
			  `ISUSERMAIN` int(2) DEFAULT NULL,
			  `ISMAINSIMHASH` int(2) DEFAULT NULL,
			  `KV_TITLE` varchar(200) DEFAULT NULL,
			  `LOSTTIME` varchar(10) DEFAULT NULL,
			  `KV_ORIEN_LEVEL` int(2) DEFAULT NULL,
			  `NOISESTATUS` varchar(100) DEFAULT NULL,
			  `KV_ABSTRACT` varchar(500) DEFAULT NULL,
			  `KV_URL` varchar(270) DEFAULT NULL,
			  `KV_KEYWORD` varchar(200) DEFAULT NULL,
			  `KV_WBAUTHORPIC` varchar(200) DEFAULT NULL,
			  `KV_AUTHOR` varchar(50) DEFAULT NULL,
			  `KV_ISPIC` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否有图片 0没有 1有',
			  `KV_ISVIDEO` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否有视频 0 没有 1 有',
			  `KV_IMGURL` varchar(1000) DEFAULT NULL,
			  `KV_VEDEOURL` varchar(1000) DEFAULT NULL,
			  `KV_TITLEMATCH` varchar(2) NOT NULL DEFAULT '',
			  `KV_MUSTWORDMININDEX` int(11) NOT NULL DEFAULT '0',
			  `KV_KEYWORDSMININDEX` int(11) NOT NULL DEFAULT '0',
			  `KV_ONLYLOCAL` varchar(2) NOT NULL DEFAULT '',
			  `KV_WEIBOOVERTIME` varchar(2) NOT NULL DEFAULT '',
			  `KV_WEIBOSIGNLOCALNOISE` varchar(2) NOT NULL DEFAULT '',
			  `KV_WEIBOTOPICNOISE` varchar(2) NOT NULL DEFAULT '',
			  `KV_WEIBOATNOISE` varchar(2) NOT NULL DEFAULT '',
			  `KV_DTCTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_DTTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_WEBCHANNEL` varchar(100) DEFAULT NULL COMMENT '频道名称',
			  `KV_HOTKEYWORD` varchar(100) DEFAULT NULL COMMENT '主题词',
			  `KV_DOMAIN` varchar(150) DEFAULT NULL COMMENT '域名',
			  `KV_SITEID` varchar(50) DEFAULT NULL COMMENT '配置ID',
			  `KV_INFORMATIONSTATE` varchar(30) NOT NULL DEFAULT '0' COMMENT '平台预警信息状态',
			  `IMPORTANCE_WEIGHT` int(11) NOT NULL DEFAULT '0' COMMENT '重要度',
			  `KV_EXTEND_FIELD` json DEFAULT NULL COMMENT '扩展JSON字段',
			  `KV_INPUTDATATYPE` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:系统录入 2：手动录入',
			  `isDelete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '原帖是否删除 0:未删除，1:已删除',
			  `ts_tag` varchar(20) NOT NULL DEFAULT '' COMMENT '态势感知涉事类型tag',
			  `media_type` tinyint NOT NULL DEFAULT 0 COMMENT '媒体分类',
			  `is_comment` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否评论，0：非评论 1：评论',
			  `delete_time` varchar(20) NOT NULL DEFAULT '' COMMENT '删除时间',
			  `defender` varchar(20) NOT NULL DEFAULT '' COMMENT '维护人',
			  `location_code` int(10)  DEFAULT 0 COMMENT '信息地域id',
			  `media_source_type` tinyint(4) DEFAULT '99' COMMENT '新媒体类型默认99为了与3.0统一特殊处理',
			  `media_subord_type` tinyint(4) DEFAULT '99' COMMENT '下级媒体类型默认99为了与3.0统一特殊处理',
			  `info_source_range` tinyint(4) DEFAULT '1' COMMENT '默认本市 信源范围',
			  `url_md5` varchar(32) DEFAULT '' COMMENT '文章链接md5',
			  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '入库时间',
			  `author_id` varchar(32) DEFAULT '' COMMENT '作者id',
			  `media_level` tinyint(4) NOT NULL DEFAULT 0 COMMENT '媒体级别  中央: 1、省级: 2、地方: 3、国外: 4、其他 :5',
			  `media_nature` tinyint(4) NOT NULL DEFAULT 0 COMMENT '媒体性质  党媒: 1、官媒: 2、商媒: 3、自媒: 4',
			  PRIMARY KEY (`KR_UUID`),
			  KEY `index_ORIENTATION` (`ORIENTATION`) USING BTREE,
			  KEY `INDEX_KV_UUID` (`KV_UUID`) USING BTREE,
			  KEY `INDEX_KR_CTIME` (`KR_CTIME`) USING BTREE,
			  KEY `INDEX_SIMHASH` (`KV_SIMHASH`) USING BTREE,
			  KEY `INDEX_WEBNAME` (`KV_WEBNAME`) USING BTREE,
			  KEY `INDEX_SOURCETYPE` (`KV_SOURCETYPE`) USING BTREE,
			  KEY `KV_COLLECTTIME` (`KV_COLLECTTIME`),
			  KEY `KV_URL` (`KV_URL`),
			  KEY `INDEX_IMPORTANCE_WEIGHT` (`IMPORTANCE_WEIGHT`),
			  KEY `IDX_UID_KWID_CT` (`KR_UID`,`KR_KEYWORDID`,`KR_CTIME`),
			  KEY `IDX_KWID_ST` (`KR_KEYWORDID`,`KR_STATE`),
			  KEY `index_ctime_location` (`location_code`,`KR_CTIME`) USING BTREE,
			  INDEX `index_url_md5` (`url_md5`) USING BTREE
			) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                CREATE TABLE `YQZB_T_QQMES` (
                  `KM_UUID` VARCHAR(40) NOT NULL DEFAULT '',
                  `KQ_NO` VARCHAR(100) NULL DEFAULT NULL,
                  `KQ_NAME` VARCHAR(100) NULL DEFAULT NULL,
                  `KM_QQNUM` VARCHAR(100) NULL DEFAULT NULL,
                  `KM_NAME` VARCHAR(100) NULL DEFAULT NULL,
                  `KM_TIME` VARCHAR(40) NULL DEFAULT NULL,
                  `KM_CONTENT` VARCHAR(2000) NULL DEFAULT NULL,
                  `KK_ID` VARCHAR(40) NULL DEFAULT NULL,
                  `KU_ID` VARCHAR(40) NULL DEFAULT NULL,
                  `KM_STATE` VARCHAR(2) NULL DEFAULT NULL,
                  `KM_POSTNUM` VARCHAR(100) NULL DEFAULT NULL COMMENT '发信息者QQ',
                  `KM_ISDELETE` TINYINT(4) NOT NULL DEFAULT '1',
                  PRIMARY KEY (`KM_UUID`),
                  UNIQUE INDEX `KM_UUID` (`KM_UUID`) USING BTREE,
                  INDEX `KK_ID` (`KK_ID`) USING BTREE,
                  INDEX `KU_ID` (`KU_ID`) USING BTREE,
                  INDEX `KQ_NO` (`KQ_NO`) USING BTREE,
                  INDEX `KM_QQNUM` (`KM_QQNUM`) USING BTREE,
                  INDEX `KM_TIME` (`KM_TIME`) USING BTREE,
                  INDEX `KM_CONTENT` (`KM_CONTENT`(255)) USING BTREE,
                  INDEX `KM_NAME` (`KM_NAME`) USING BTREE
                )
                COLLATE='utf8_general_ci'
                ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                        DROP DATABASE {}
                    '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                CREATE TABLE `WK_T_YQJB_INFO` (
			`KM_UUID` varchar(40) NOT NULL DEFAULT '',
			`KY_UUID` varchar(40) DEFAULT NULL,
			`KV_SOURCETYPE` varchar(2) DEFAULT NULL,
			`KV_ID` varchar(30) DEFAULT NULL,
			`KV_TITLE` varchar(300) DEFAULT NULL,
			`KV_SOURCE` varchar(200) DEFAULT NULL,
			`KV_URL` varchar(600) DEFAULT NULL,
			`KV_TIME` varchar(20) DEFAULT NULL,
			`KV_CTIME` varchar(20) DEFAULT NULL,
			`KV_VISITCOUNT` int(11) DEFAULT NULL,
			`KV_REPLY` int(11) DEFAULT NULL,
			`KV_COLLECTION` int(11) DEFAULT NULL,
			`KV_TRANSPORT` int(11) DEFAULT NULL,
			`KV_REPEAT` int(11) DEFAULT NULL,
			`KV_ABSTRACT` varchar(500) DEFAULT NULL,
			`KV_ORIENTATION` varchar(3) DEFAULT NULL,
			`KV_FLAG` varchar(1) DEFAULT NULL,
			`KV_SITE` varchar(100) DEFAULT NULL,
			`KV_TEMPLET` varchar(50) DEFAULT NULL,
			`KV_STATE` varchar(1) DEFAULT NULL,
			`KV_SNA_FLAG` varchar(1) DEFAULT NULL,
			`KV_INDEX_FLAG` varchar(1) DEFAULT NULL,
			`KV_ORIEN_LEVEL` int(11) DEFAULT NULL,
			`KV_INSERT_TIME` varchar(20) DEFAULT NULL,
			`KV_UUID` varchar(40) DEFAULT NULL,
			`CLOSECJ` varchar(1) DEFAULT '0',
			`ORACLE_MYSQL_UUID` varchar(32) DEFAULT NULL,
			`IS_SYNCHRONIZED` char(1) DEFAULT NULL,
            `TOPIC_ID` varchar(40) NOT NULL DEFAULT '' COMMENT '专题或话题id',
            `KV_TYPE` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1：专题id 2：事件分析id',
            `isDelete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '原帖是否删除 0:未删除，1:已删除',
			PRIMARY KEY (`KM_UUID`),
			INDEX `KM_UUID` (`KM_UUID`) USING BTREE,
			INDEX `ORACLE_MYSQL_UUID` (`ORACLE_MYSQL_UUID`) USING BTREE,
			INDEX `IS_SYNCHRONIZED` (`IS_SYNCHRONIZED`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                    DROP DATABASE {}
                                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result
            create_sql = '''
            CREATE TABLE `WK_T_YQJB_INFOCNT` (
			`KM_UUID` VARCHAR(40) NOT NULL DEFAULT '',
			`KV_CTIME` VARCHAR(20) NULL DEFAULT NULL,
			`KV_CONTENT` MEDIUMTEXT NULL,
			`ORACLE_MYSQL_UUID` VARCHAR(32) NULL DEFAULT NULL,
			`IS_SYNCHRONIZED` CHAR(1) NULL DEFAULT NULL,
			PRIMARY KEY (`KM_UUID`),
			INDEX `KM_UUID` (`KM_UUID`) USING BTREE,
			INDEX `ORACLE_MYSQL_UUID` (`ORACLE_MYSQL_UUID`) USING BTREE,
			INDEX `IS_SYNCHRONIZED` (`IS_SYNCHRONIZED`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                                DROP DATABASE {}
                                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                        CREATE TABLE `WK_T_REPORT` (
			`KR_UUID` varchar(38) NOT NULL,
			`KR_TITLE` varchar(500) DEFAULT NULL,
			`KR_ADDRESS` varchar(1000) DEFAULT NULL,
			`KR_TIME` varchar(14) DEFAULT NULL,
			`KR_UID` int(10) DEFAULT NULL,
			`KR_TYPE` varchar(2) DEFAULT NULL,
			`KR_EMAIL` tinyint(4) NOT NULL DEFAULT '1' COMMENT '是否已发邮件 1否 0是',
			PRIMARY KEY (`KR_UUID`),
			INDEX `KR_UID` (`KR_UID`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
                        '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_EVERYDAYDATA` (
			`KV_ID` varchar(50) NOT NULL DEFAULT '',
			`KU_ID` varchar(50) DEFAULT NULL,
			`KV_TYPE` varchar(50) DEFAULT NULL,
			`KK_NAME` varchar(100) DEFAULT NULL,
			`KU_NAME` varchar(100) DEFAULT NULL,
			`KV_TIME` varchar(50) DEFAULT NULL,
			`KV_ADDTIME` varchar(50) DEFAULT NULL,
			`KV_LOSTCALTIME` varchar(30) DEFAULT NULL,
			`KV_TOTAL` int(11) DEFAULT NULL,
			`KV_WEIBO` int(11) DEFAULT NULL,
			`KV_NEWS` int(11) DEFAULT NULL,
			`KV_FORUM` int(11) DEFAULT NULL,
			`KV_BLOGS` int(11) DEFAULT NULL,
			`KV_PAPERS` int(11) DEFAULT NULL,
			`KV_WEIXIN` int(11) DEFAULT NULL,
			`KV_VIDEO` int(11) DEFAULT NULL,
			`KV_OTHER` int(11) DEFAULT NULL,
			`KV_RD` int(11) DEFAULT NULL,
			`KV_ABROAD` int(11) DEFAULT NULL,
			`KV_ZDWEIBOWEB` varchar(500) DEFAULT NULL,
			`KV_ZDAERA` varchar(500) DEFAULT NULL,
			`KV_ZDAUTHOR` varchar(500) DEFAULT NULL,
			`KV_ZDWEBNAME` varchar(500) DEFAULT NULL,
			`KV_FMTOTAL` int(11) DEFAULT NULL,
			`KV_FMNEWS` int(11) DEFAULT NULL,
			`KV_FMFORUM` int(11) DEFAULT NULL,
			`KV_FMBLOGS` int(11) DEFAULT NULL,
			`KV_FMPAPERS` int(11) DEFAULT NULL,
			`KV_FMWEIBO` int(11) DEFAULT NULL,
			`KV_FMWEIXIN` int(11) DEFAULT NULL,
			`KV_FMVIDEO` int(11) DEFAULT NULL,
			`KV_FMOTHER` int(11) DEFAULT NULL,
			`KV_FMWEBNAME` varchar(500) DEFAULT NULL,
			`KV_FMABROAD` int(11) DEFAULT NULL,
			`KV_FMAUTHOR` varchar(500) DEFAULT NULL,
			`KV_FMZDWEBNAME` varchar(500) DEFAULT NULL,
			`KV_ZMTOTAL` int(11) DEFAULT NULL,
			`KV_ZMWEIBO` int(11) DEFAULT NULL,
			`KV_ZMWEB` int(11) DEFAULT NULL,
			`KV_ZMNEWS` int(11) DEFAULT NULL,
			`KV_ZMFORUM` int(11) DEFAULT NULL,
			`KV_ZMBLOGS` int(11) DEFAULT NULL,
			`KV_ZMPAPERS` int(11) DEFAULT NULL,
			`KV_ZMWEIXIN` int(11) DEFAULT NULL,
			`KV_ZMVIDEO` int(11) DEFAULT NULL,
			`KV_ZMOTHER` int(11) DEFAULT NULL,
			`KV_ZMWEBNAME` varchar(500) DEFAULT NULL,
			`KV_ZXTOTAL` int(11) DEFAULT NULL,
			`KV_ZXNEWS` int(11) DEFAULT NULL,
			`KV_ZXFORUM` int(11) DEFAULT NULL,
			`KV_ZXBLOGS` int(11) DEFAULT NULL,
			`KV_ZXPAPERS` int(11) DEFAULT NULL,
			`KV_ZXWEIBO` int(11) DEFAULT NULL,
			`KV_ZXWEIXIN` int(11) DEFAULT NULL,
			`KV_ZXVIDEO` int(11) DEFAULT NULL,
			`KV_ZXOTHER` int(11) DEFAULT NULL,
			`KV_ZXWEBNAME` varchar(500) DEFAULT NULL,
			`KV_ZYTOTAL` int(11) DEFAULT NULL,
			`KV_ZYNEWS` int(11) DEFAULT NULL,
			`KV_ZYFORUM` int(11) DEFAULT NULL,
			`KV_ZYBLOGS` int(11) DEFAULT NULL,
			`KV_ZYPAPERS` int(11) DEFAULT NULL,
			`KV_ZYWEIBO` int(11) DEFAULT NULL,
			`KV_ZYWEIXIN` int(11) DEFAULT NULL,
			`KV_ZYVIDEO` int(11) DEFAULT NULL,
			`KV_ZYOTHER` int(11) DEFAULT NULL,
			`KV_ZYWEBNAME` varchar(500) DEFAULT NULL,
			`KV_APP` int(11) DEFAULT NULL,
			`KV_ZMAPP` int(11) DEFAULT NULL,
			`KV_FMAPP` int(11) DEFAULT NULL,
			`KV_ZXAPP` int(11) DEFAULT NULL,
			`KV_ZYAPP` int(11) DEFAULT NULL,
			`KV_REPLY` int(11) DEFAULT NULL,
			`KV_ZMREPLY` int(11) DEFAULT NULL,
			`KV_FMREPLY` int(11) DEFAULT NULL,
			`KV_ZXREPLY` int(11) DEFAULT NULL,
			`KV_ZYREPLY` int(11) DEFAULT NULL,
			`KV_CWEIBO` int(11) DEFAULT NULL,
			`KV_ZMCWEIBO` int(11) DEFAULT NULL,
			`KV_FMCWEIBO` int(11) DEFAULT NULL,
			`KV_ZXCWEIBO` int(11) DEFAULT NULL,
			PRIMARY KEY (`KV_ID`),
			INDEX `INDEX_KVID` (`KV_ID`) USING BTREE,
			INDEX `INDEX_KUID` (`KU_ID`) USING BTREE,
			INDEX `INDEX_TYPE` (`KV_TYPE`) USING BTREE,
			INDEX `INDEX_DATE` (`KV_TIME`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                CREATE TABLE `WK_T_USER_LOG` (
			`KL_UUID` varchar(40) NOT NULL DEFAULT '',
			`KU_ID` int(10) DEFAULT NULL,
			`KU_LID` varchar(400) DEFAULT NULL,
			`KL_TIME` varchar(40) DEFAULT NULL,
			`KL_IP` varchar(40) DEFAULT NULL,
			`KL_WORK` varchar(4000) DEFAULT NULL,
			`KL_MODULAR` varchar(400) DEFAULT NULL,
			`KL_PLATFORM` varchar(400) DEFAULT NULL,
			`KL_USER` varchar(200) DEFAULT NULL,
			`ARG1` varchar(400) DEFAULT NULL,
			`ARG2` varchar(400) DEFAULT NULL,
			`ORACLE_MYSQL_UUID` varchar(32) DEFAULT NULL,
			`is_Synchronized` char(1) DEFAULT NULL,
			PRIMARY KEY (`KL_UUID`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `YQZB_T_YJXX` (
			  `KS_UUID` varchar(40) NOT NULL,
			  `KV_UUID` varchar(40) NOT NULL,
			  `KU_ID` varchar(10) NOT NULL,
			  `KS_TYPE` varchar(2) DEFAULT NULL,
			  `KS_INFO` varchar(200) DEFAULT NULL,
			  `KS_TIME` varchar(14) DEFAULT NULL,
			  `KS_STATE` varchar(2) DEFAULT NULL,
			  `KS_FLAG` varchar(2) DEFAULT NULL,
			  `KS_CHECK` varchar(2) DEFAULT NULL,
			  `KS_CHECKDEL` varchar(2) DEFAULT NULL,
			  `KS_LATE` varchar(2) DEFAULT NULL,
			  `KS_AOTO` varchar(2) DEFAULT NULL,
			  `KS_SIMHASH` varchar(50) DEFAULT NULL,
			  `KS_TITLE` varchar(150) DEFAULT NULL,
			  `KS_CTIME` varchar(20) DEFAULT NULL,
			  `kS_SOURCETYPE` varchar(2) DEFAULT NULL,
			  `KS_INFOTYPE` varchar(2) DEFAULT NULL,
			  `KS_KID` varchar(40) DEFAULT NULL,
			  `KV_ABSTRACT` text,
			  `ISREAD` int(2) DEFAULT '0',
			  `KV_WEBNAME` varchar(50) DEFAULT NULL,
			  `KV_ARG1` varchar(50) DEFAULT NULL,
			  `KV_ARG2` varchar(50) DEFAULT NULL,
			  `KV_ARG3` varchar(50) DEFAULT NULL,
			  `KV_ARG4` varchar(50) DEFAULT NULL,
			  `KV_ARG5` varchar(50) DEFAULT NULL,
			  `KS_URL` varchar(270) DEFAULT NULL,
			  `KV_CONTENT` mediumtext,
			  `KV_ORIENTATION` varchar(3) NOT NULL DEFAULT '',
			  `KV_DTCTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_DTTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `warning_level` INT(2) NOT NULL DEFAULT '0' COMMENT '预警级别 0一般 1中等 2严重 3高危',
			  `proposal` VARCHAR(500) NOT NULL DEFAULT '' COMMENT '研判建议',
			  `tags` json DEFAULT NULL COMMENT '事件标签',
			  `is_oversea` INT(2) NOT NULL DEFAULT '0' COMMENT '是否境外 0否 1是',
			  `main_part` VARCHAR(500) NOT NULL DEFAULT '' COMMENT '涉事主体',
			  `isDelete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '原帖是否删除 0:未删除，1:已删除',
			  `module_type` INT NULL DEFAULT 1 COMMENT '预警信息来源：1 专题，2搜索，3 事件，4 其他',
			  `EXTEND_FIELD` json DEFAULT NULL COMMENT '地域信息扩展JSON字段',
			  `location_code` int(10) DEFAULT 0 COMMENT '信息地域id',
			  `is_comment` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否评论，0：非评论 1：评论',
			  `media_source_type` tinyint(4) DEFAULT '99' COMMENT '新媒体类型默认99为了与3.0统一特殊处理',
			  `media_subord_type` tinyint(4) DEFAULT '99' COMMENT '下级媒体类型默认99为了与3.0统一特殊处理',
			  `info_source_range` tinyint(4) DEFAULT '1' COMMENT '默认本市 信源范围',
			  `url_md5` varchar(32) DEFAULT '' COMMENT '文章链接md5',
			  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '入库时间',
			  `author_id` varchar(32) DEFAULT '' COMMENT '作者id',
			  `author_auth_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '作者认证类型：1普通 2橙v 3蓝v',
			  `weibo_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '博文类型，1原创2仅转发3转发并回复4评论，目前只有微博数据有博文类型',
			  `industry_tag_v1` varchar(50) default '' not null comment '行业一级标签',
			  `industry_tag_v2` varchar(50) default '' not null comment '行业二级标签',
			  PRIMARY KEY (`KS_UUID`),
			  KEY `KVUUID` (`KV_UUID`) USING BTREE,
			  KEY `CHECKDEL` (`KS_CHECKDEL`) USING BTREE,
			  KEY `TYPE` (`KS_TYPE`) USING BTREE,
			  KEY `CTIME` (`KS_CTIME`) USING BTREE,
			  KEY `TIME` (`KS_TIME`) USING BTREE,
			  KEY `KU_ID` (`KU_ID`,`KS_TIME`) USING BTREE,
			  KEY `KS_KID` (`KS_KID`) USING BTREE,
			  KEY `ISREAD` (`ISREAD`) USING BTREE,
			  KEY `IDX_ST_TIME` (`KS_STATE`,`KS_TIME`),
			  KEY `index_ctime_location` (`location_code`,`KS_TIME`) USING BTREE,
			  INDEX `index_url_md5` (`url_md5`) USING BTREE
			) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                        DROP DATABASE {}
                                    '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_MYATTENTION_INFO` (
			`KM_UUID` VARCHAR(40) NOT NULL DEFAULT '',
			`KU_ID` VARCHAR(50) NULL DEFAULT NULL,
			`KV_SOURCETYPE` VARCHAR(2) NULL DEFAULT NULL,
			`KV_ID` VARCHAR(30) NULL DEFAULT NULL,
			`KV_TITLE` VARCHAR(300) NULL DEFAULT NULL,
			`KV_SOURCE` VARCHAR(200) NULL DEFAULT NULL,
			`KV_URL` VARCHAR(600) NULL DEFAULT NULL,
			`KV_TIME` VARCHAR(20) NULL DEFAULT NULL,
			`KV_CTIME` VARCHAR(20) NULL DEFAULT NULL,
			`KV_VISITCOUNT` INT(11) NULL DEFAULT NULL,
			`KV_REPLY` INT(11) NULL DEFAULT NULL,
			`KV_COLLECTION` INT(11) NULL DEFAULT NULL,
			`KV_TRANSPORT` INT(11) NULL DEFAULT NULL,
			`KV_REPEAT` INT(11) NULL DEFAULT NULL,
			`KV_ABSTRACT` VARCHAR(500) NULL DEFAULT NULL,
			`KV_ORIENTATION` VARCHAR(3) NULL DEFAULT NULL,
			`KV_FLAG` VARCHAR(1) NULL DEFAULT NULL,
			`KV_SITE` VARCHAR(100) NULL DEFAULT NULL,
			`KV_TEMPLET` VARCHAR(50) NULL DEFAULT NULL,
			`KV_STATE` VARCHAR(1) NULL DEFAULT NULL,
			`KV_SNA_FLAG` VARCHAR(1) NULL DEFAULT NULL,
			`KV_INDEX_FLAG` VARCHAR(1) NULL DEFAULT NULL,
			`KV_ORIEN_LEVEL` INT(11) NULL DEFAULT NULL,
			`KV_INSERT_TIME` VARCHAR(20) NULL DEFAULT NULL,
			`KV_UUID` VARCHAR(40) NULL DEFAULT NULL,
			`KV_KEYWORD` VARCHAR(200) NULL DEFAULT NULL COMMENT '关键词',
			`CLOSECJ` VARCHAR(1) NULL DEFAULT '0',
			`ORACLE_MYSQL_UUID` VARCHAR(32) NULL DEFAULT NULL,
			`IS_SYNCHRONIZED` CHAR(1) NULL DEFAULT NULL,
			`KM_ID` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '信息分类ID',
			`TOPIC_ID` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '专题或话题ID',
			`KV_TYPE` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1：专题id 2：事件分析id',
			`isDelete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '原帖是否删除 0:未删除，1:已删除',
			`media_source_type` tinyint(4) DEFAULT '99' COMMENT '新媒体类型默认99为了与3.0统一特殊处理',
			`media_subord_type` tinyint(4) DEFAULT '99' COMMENT '下级媒体类型默认99为了与3.0统一特殊处理',
			`info_source_range` tinyint(4) DEFAULT '1' COMMENT '默认本市 信源范围',
			`author_id` varchar(32) DEFAULT '' COMMENT '作者id',
			PRIMARY KEY (`KM_UUID`),
			INDEX `KM_UUID` (`KM_UUID`) USING BTREE,
			INDEX `ORACLE_MYSQL_UUID` (`ORACLE_MYSQL_UUID`) USING BTREE,
			INDEX `IS_SYNCHRONIZED` (`IS_SYNCHRONIZED`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                                    DROP DATABASE {}
                                                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_MYATTENTION_INFOCNT` (
			`KM_UUID` VARCHAR(40) NOT NULL DEFAULT '',
			`KV_CTIME` VARCHAR(20) NULL DEFAULT NULL,
			`KV_CONTENT` MEDIUMTEXT NULL,
			`ORACLE_MYSQL_UUID` VARCHAR(32) NULL DEFAULT NULL,
			`IS_SYNCHRONIZED` CHAR(1) NULL DEFAULT NULL,
			PRIMARY KEY (`KM_UUID`),
			INDEX `KM_UUID` (`KM_UUID`) USING BTREE,
			INDEX `ORACLE_MYSQL_UUID` (`ORACLE_MYSQL_UUID`) USING BTREE,
			INDEX `IS_SYNCHRONIZED` (`IS_SYNCHRONIZED`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                        CREATE TABLE `USERPUSHNUM` (
			`ID` VARCHAR(50) NOT NULL DEFAULT '',
			`DATE` VARCHAR(50) NULL DEFAULT NULL,
			`USERID` VARCHAR(50) NULL DEFAULT NULL,
			`PUSHNUM` INT(11) NULL DEFAULT NULL,
			PRIMARY KEY (`ID`),
			INDEX `DATE` (`DATE`),
			INDEX `USERID` (`USERID`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                                    CREATE TABLE `WK_T_USER_LOGIN_LOG` (
			`KL_UUID` VARCHAR(40) NOT NULL DEFAULT '',
			`KU_ID` INT(10) NULL DEFAULT NULL,
			`KU_LID` VARCHAR(20) NULL DEFAULT NULL,
			`KL_TIME` VARCHAR(20) NULL DEFAULT NULL,
			`KL_IP` VARCHAR(20) NULL DEFAULT NULL,
			`KL_WORK` VARCHAR(255) NULL DEFAULT NULL,
			`KL_MODULAR` VARCHAR(255) NULL DEFAULT NULL,
			`KL_PLATFORM` VARCHAR(255) NULL DEFAULT NULL,
			`KL_USER` VARCHAR(200) NULL DEFAULT NULL,
			`KL_USERAGENT` VARCHAR(255) NULL DEFAULT NULL,
			`ARG2` VARCHAR(255) NULL DEFAULT NULL,
			`ORACLE_MYSQL_UUID` VARCHAR(32) NULL DEFAULT NULL,
			`is_Synchronized` CHAR(1) NULL DEFAULT NULL,
			PRIMARY KEY (`KL_UUID`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `TOPICWEIBOAUTHORINFO` (
			`ID` VARCHAR(50) NOT NULL DEFAULT '',
			`verified_level` INT(11) NULL DEFAULT NULL,
			`domain` VARCHAR(30) NULL DEFAULT NULL,
			`bi_followers_count` INT(11) NULL DEFAULT NULL,
			`USERID` VARCHAR(30) NULL DEFAULT NULL,
			`urank` INT(11) NULL DEFAULT NULL,
			`city` VARCHAR(30) NULL DEFAULT NULL,
			`verified` INT(11) NULL DEFAULT NULL,
			`last_ctime` VARCHAR(30) NULL DEFAULT NULL,
			`verified_reason` VARCHAR(100) NULL DEFAULT NULL,
			`followers_count` VARCHAR(30) NULL DEFAULT NULL,
			`location` VARCHAR(30) NULL DEFAULT NULL,
			`province` VARCHAR(30) NULL DEFAULT NULL,
			`avatar_large` VARCHAR(50) NULL DEFAULT NULL,
			`statuses_count` INT(11) NULL DEFAULT NULL,
			`description` VARCHAR(500) NULL DEFAULT NULL,
			`friends_count` INT(11) NULL DEFAULT NULL,
			`online_status` INT(11) NULL DEFAULT NULL,
			`allow_all_act_msg` INT(11) NULL DEFAULT NULL,
			`allow_all_comment` INT(11) NULL DEFAULT NULL,
			`geo_enabled` INT(11) NULL DEFAULT NULL,
			`name` VARCHAR(30) NULL DEFAULT NULL,
			`weihao` VARCHAR(15) NULL DEFAULT NULL,
			`screen_name` VARCHAR(20) NULL DEFAULT NULL,
			`gender` VARCHAR(5) NULL DEFAULT NULL,
			`created_at` VARCHAR(30) NULL DEFAULT NULL,
			`TID` VARCHAR(50) NULL DEFAULT NULL,
			PRIMARY KEY (`ID`),
			INDEX `TID` (`TID`),
			INDEX `location` (`location`),
			INDEX `USERID` (`USERID`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                        DROP DATABASE {}
                    '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `TOPICGDLINES` (
			`ID` VARCHAR(110) NOT NULL DEFAULT '',
			`TOPICID` VARCHAR(50) NULL DEFAULT NULL,
			`GDLINE` VARCHAR(200) NULL DEFAULT NULL,
			`GDSOURCETYPES` VARCHAR(60) NULL DEFAULT NULL,
			`ADDTIME` VARCHAR(50) NULL DEFAULT NULL,
			`GDZMCLASSLY` VARCHAR(200) NULL DEFAULT NULL,
			`GDZMCLASSLYWORDS` VARCHAR(200) NULL DEFAULT NULL,
			`GDFMCLASSLY` VARCHAR(200) NULL DEFAULT NULL,
			`GDFMCLASSLYWORDS` VARCHAR(200) NULL DEFAULT NULL,
			`GDZFXX` VARCHAR(10) NULL DEFAULT NULL,
			`GDCOUNT` INT(11) NULL DEFAULT NULL,
			`GDCLUSTER` VARCHAR(200) NULL DEFAULT NULL,
			`GDTYPE` VARCHAR(10) NULL DEFAULT NULL,
			PRIMARY KEY (`ID`),
			INDEX `TOPICID` (`TOPICID`),
			INDEX `GDLINE` (`GDLINE`),
			INDEX `GDTYPE` (`GDTYPE`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                        DROP DATABASE {}
                    '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
                CREATE TABLE `TOPICAUTHORRELATION` (
			`ID` VARCHAR(70) NOT NULL,
			`TOPICID` VARCHAR(50) NULL DEFAULT NULL,
			`AUTHOR` VARCHAR(50) NULL DEFAULT NULL,
			`AUTHORACTIVE` VARCHAR(3000) NULL DEFAULT NULL,
			`AUTHORPASSIVE` VARCHAR(3000) NULL DEFAULT NULL,
			`ADDTIME` VARCHAR(50) NULL DEFAULT NULL,
			`AUTHORWARNING` VARCHAR(3000) NULL DEFAULT NULL,
			`RELATIONTYPE` INT(4) NOT NULL DEFAULT '0' COMMENT '关系类型 1.转发关系2.@关系3.被关注且转发4.评论关系',
            PRIMARY KEY (`ID`),
            INDEX `IDX_RELATIONTYPE` (`RELATIONTYPE`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_DELETEINFO_LOG` (
			  `KL_UUID` VARCHAR(40) NOT NULL,
			  `KL_TYPE` VARCHAR(2) NULL DEFAULT NULL,
			  `KL_USER` VARCHAR(40) NULL DEFAULT NULL,
			  `KL_TIME` VARCHAR(20) NULL DEFAULT NULL,
			  `KV_TITLE` VARCHAR(200) NULL DEFAULT NULL,
			  `KV_URL` VARCHAR(270) NULL DEFAULT NULL,
			  `KV_CTIME` VARCHAR(20) NULL DEFAULT NULL,
			  `KV_SITE` VARCHAR(50) NULL DEFAULT NULL,
			  `KV_AUTHOR` VARCHAR(50) NULL DEFAULT NULL,
			  `KV_CONTENT` TEXT NULL,
			  `KU_ID` INT(10) NULL DEFAULT NULL,
			  `KL_RUBBISH` VARCHAR(2) NOT NULL DEFAULT '0',
			  `KL_CLASSIFY` VARCHAR(2) NOT NULL DEFAULT '0',
			  PRIMARY KEY (`KL_UUID`),
			  INDEX `KL_UUID` (`KL_UUID`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `YQZB_T_WXMSG` (
			`KM_UUID` varchar(40) NOT NULL DEFAULT '' COMMENT '唯一id',
			`KM_WXNO` varchar(100) DEFAULT NULL COMMENT '微信群号',
			`KM_NAME` varchar(100) DEFAULT NULL COMMENT '微信群名',
			`KM_WXNUM` varchar(100) DEFAULT NULL COMMENT '微信账号',
			`KM_NICKNAME` varchar(100) DEFAULT NULL COMMENT '发布人昵称',
			`KM_TIME` varchar(40) DEFAULT NULL COMMENT '发布时间',
			`KM_CONTENT` text COMMENT '发布内容',
			`KK_ID` varchar(40) DEFAULT NULL COMMENT '微信专题id',
			`KU_ID` varchar(40) DEFAULT NULL COMMENT '用户ID',
			`KM_STATE` varchar(2) DEFAULT NULL,
			`KM_ISDELETE` tinyint(4) NOT NULL DEFAULT '1' COMMENT '是否删除 1 存在  0删除',
			`KM_POSTNUM` varchar(100) DEFAULT NULL COMMENT '发帖人微信号',
			PRIMARY KEY (`KM_UUID`),
			UNIQUE INDEX `KM_UUID` (`KM_UUID`) USING BTREE,
			INDEX `KK_ID` (`KK_ID`) USING BTREE,
			INDEX `KU_ID` (`KU_ID`) USING BTREE,
			INDEX `KQ_NO` (`KM_WXNO`) USING BTREE,
			INDEX `KM_QQNUM` (`KM_WXNUM`) USING BTREE,
			INDEX `KM_TIME` (`KM_TIME`) USING BTREE,
			INDEX `KM_NAME` (`KM_NICKNAME`) USING BTREE
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                            DROP DATABASE {}
                        '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_VALIDATION_LOCATIONREF` (
			  `KL_UUID` varchar(40) NOT NULL DEFAULT '' COMMENT 'UUID',
			  `KR_UUID` varchar(40) NOT NULL DEFAULT '' COMMENT 'REF_UUID',
			  `KV_UUID` varchar(40) NOT NULL DEFAULT '' COMMENT '信息uuid',
			  `KK_ID` varchar(40) NOT NULL DEFAULT '' COMMENT '专题ID',
			  `KU_ID` int(5) DEFAULT NULL COMMENT '用户ID',
			  `KR_PROVINCEID` varchar(40) NOT NULL DEFAULT '' COMMENT '省域ID',
			  `KR_CITYID` varchar(40) NOT NULL DEFAULT '' COMMENT '市域ID',
			  `KR_COUNTYID` varchar(40) NOT NULL DEFAULT '' COMMENT '区县ID',
			  `KR_CTIME` varchar(20) NOT NULL DEFAULT '' COMMENT '发布时间',
			  `KV_DTCTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT '发布时间',
			  `KEYWORD` varchar(50) NOT NULL DEFAULT '' COMMENT '匹配关键词',
			  `ARG1` varchar(50) NOT NULL DEFAULT '' COMMENT '备用字段',
			  `town` varchar(200) NOT NULL DEFAULT '' COMMENT '村镇',
			  PRIMARY KEY (`KL_UUID`),
			  KEY `INDEX_KR_CTIME` (`KR_CTIME`) USING BTREE
			) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_MYATTENTIONCLASSIFY` (
			`KM_ID` VARCHAR(50) NOT NULL DEFAULT '',
			`KM_NAME` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '分类名称',
			`KU_ID` INT(10) NOT NULL DEFAULT '0' COMMENT '用户ID',
			`KM_PID` VARCHAR(50) NOT NULL DEFAULT '0' COMMENT '分类父id',
			PRIMARY KEY (`KM_ID`)
			)
            COMMENT='我的关注分类表'
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WEIBOCOMMINFO` (
			`ID` VARCHAR(100) NOT NULL,
			`WEBNAME` VARCHAR(20) NULL DEFAULT NULL,
			`CONTENT` VARCHAR(300) NULL DEFAULT NULL,
			`TITLE` VARCHAR(150) NULL DEFAULT NULL,
			`CTIME` VARCHAR(50) NULL DEFAULT NULL,
			`COLLECTTIME` VARCHAR(50) NULL DEFAULT NULL,
			`AUTHOR` VARCHAR(30) NULL DEFAULT NULL,
			`URL` VARCHAR(270) NULL DEFAULT NULL,
			`PARENTURL` VARCHAR(270) NULL DEFAULT NULL,
			`REPLYCOUNT` INT(11) NULL DEFAULT NULL,
			`VISITCOUNT` INT(11) NULL DEFAULT NULL,
			`TOPICID` VARCHAR(50) NULL DEFAULT NULL,
			`AUTOCLASSLY` VARCHAR(20) NULL DEFAULT NULL,
			`CLASSLYTYPE` VARCHAR(5) NULL DEFAULT NULL,
			`CLASSLYINFO` VARCHAR(200) NULL DEFAULT NULL,
			`GDZMCLASSLY` VARCHAR(200) NULL DEFAULT NULL,
			`GDFMCLASSLY` VARCHAR(200) NULL DEFAULT NULL,
			`GDFMCLASSLYINFO` VARCHAR(200) NULL DEFAULT NULL,
			`GDZMCLASSLYINFO` VARCHAR(200) NULL DEFAULT NULL,
			`GDZFXX` VARCHAR(10) NULL DEFAULT NULL,
			`sheng` VARCHAR(50) NULL DEFAULT NULL,
			`shi` VARCHAR(50) NULL DEFAULT NULL,
			`xian` VARCHAR(50) NULL DEFAULT NULL,
			`jigou` VARCHAR(100) NULL DEFAULT NULL,
			`GDINFO` VARCHAR(300) NULL DEFAULT NULL,
			`gender` VARCHAR(20) NULL DEFAULT NULL,
			`WEBNAMEDOMAIN` VARCHAR(50) NULL DEFAULT NULL,
			`WEBNAMELEVER` VARCHAR(10) NULL DEFAULT NULL,
			`location` VARCHAR(20) NULL DEFAULT NULL,
			`verified` VARCHAR(20) NULL DEFAULT NULL,
			`USERID` VARCHAR(50) NULL DEFAULT NULL,
			`screen_name` VARCHAR(50) NULL DEFAULT NULL,
			`KN_ARG1` VARCHAR(100) NULL DEFAULT NULL,
			`KN_ARG2` VARCHAR(100) NULL DEFAULT NULL,
			`KN_ARG3` VARCHAR(100) NULL DEFAULT NULL,
			`KN_ARG4` VARCHAR(100) NULL DEFAULT NULL,
			PRIMARY KEY (`ID`),
			INDEX `AUTHOR` (`AUTHOR`),
			INDEX `PARENTURL` (`PARENTURL`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_LABEL` (
			`KL_UUID` VARCHAR(50) NOT NULL COMMENT '主键id',
			`KL_NAME` VARCHAR(255) NULL DEFAULT '' COMMENT '标签名称',
			`KL_CTIME` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '添加时间',
			PRIMARY KEY (`KL_UUID`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `MYATTENTION_T_LABEL` (
			`KS_UUID` VARCHAR(50) NOT NULL COMMENT '主键id',
			`KV_UUID` VARCHAR(50) NOT NULL COMMENT '信息id' COLLATE 'utf8_bin',
			`KL_UUID` VARCHAR(50) NOT NULL COMMENT '标签id',
			INDEX `KV_UUID` (`KV_UUID`),
			INDEX `KL_UUID` (`KL_UUID`)
			)
			COLLATE='utf8_general_ci'
			ENGINE=InnoDB
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                        DROP DATABASE {}
                    '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_MYREPORT` (
			`KM_UUID` varchar(50) NOT NULL,
			`KM_NAME` varchar(50) NOT NULL DEFAULT '' COMMENT '报告名称',
			`KM_FILENAME` varchar(50) NOT NULL DEFAULT '' COMMENT '文件名称',
			`KM_CTIME` varchar(20) NOT NULL DEFAULT '' COMMENT '上传时间',
			PRIMARY KEY (`KM_UUID`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='我的报告'
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            #首页自定义表 add by ztf 2017-05-17
            create_sql = '''
            CREATE TABLE `WK_T_DEFINEDHOME` (
			`KD_ID` int(10) NOT NULL AUTO_INCREMENT,
			`KD_TYPE` varchar(40) NOT NULL COMMENT '类型',
			`KD_VALUE` mediumtext COMMENT '属性',
			`KD_DATATYPE` int(10) NOT NULL DEFAULT '1' COMMENT '1：头部数据，2：尾部数据',
			PRIMARY KEY (`KD_ID`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                                DROP DATABASE {}
                            '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            #信息和地域关联表 add by zxj 2017-12-20
            create_sql = '''
            CREATE TABLE `WK_T_INFO_REGION` (
			`KV_UUID` varchar(32) NOT NULL  COMMENT '信息ID',
			`REGION_ID` int(11) NOT NULL  COMMENT '地域ID',
            `KR_CTIME` varchar(20) DEFAULT NULL COMMENT '发布时间',
			PRIMARY KEY (`KV_UUID`,`REGION_ID`),
            INDEX `INDEX_KR_CTIME` (`KR_CTIME`) USING BTREE
			) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `slave_warning` (
				`id` INT NOT NULL AUTO_INCREMENT COMMENT '主键',
				`time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP COMMENT '预警时间',
				`kv_uuid` VARCHAR(45) NULL COMMENT '信息ID',
				`ks_id` VARCHAR(45) NULL COMMENT '专题ID',
				`type` VARCHAR(45) NULL COMMENT '预警类型',
				PRIMARY KEY (`id`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT = '预警信息从表，存储匹配但未预警的信息'
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `AllReportData` (
				`infoUuid` varchar(50) NOT NULL COMMENT '主键id',
				`title` varchar(300) DEFAULT NULL COMMENT '标题',
				`summary` TEXT DEFAULT NULL COMMENT '摘要',
				`content` longtext COMMENT '正文',
				`contentXml` longtext COMMENT 'html详情内容',
				`webName` varchar(50) DEFAULT NULL COMMENT '来源网站',
				`sourceType` varchar(10) DEFAULT NULL COMMENT '媒体类型',
				`author` varchar(50) DEFAULT NULL COMMENT '作者',
				`infoUrl` varchar(500) DEFAULT NULL COMMENT '信息Url',
				`orientation` varchar(5) DEFAULT NULL COMMENT '倾向性',
				`publishTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '发布时间',
				`keyWord` varchar(100) DEFAULT NULL COMMENT '关键词',
				`isWarning` int(2) DEFAULT NULL COMMENT '是否预警',
				`isAttention` int(2) DEFAULT NULL COMMENT '是否关注',
				`isRead` int(2) DEFAULT NULL COMMENT '是否已读',
				`visitCount` int(11) DEFAULT NULL COMMENT '信息访问数',
				`replyCount` int(11) DEFAULT NULL COMMENT '信息评论数',
				`infoSimhash` varchar(50) DEFAULT NULL COMMENT '信息simhash值',
				`authorPic` varchar(200) DEFAULT NULL COMMENT '作者头像url',
				`domain` varchar(50) DEFAULT NULL COMMENT '域名',
				`imgUrl` varchar(1000) DEFAULT NULL COMMENT '信息图片url',
				`vedioUrl` varchar(1000) DEFAULT NULL COMMENT '信息视频url',
				`importanceWeight` int(11) DEFAULT NULL COMMENT '重要度',
				`extendField` json DEFAULT NULL COMMENT '扩展字段',
				`enterTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入报时间',
				`classifyId` int(11) DEFAULT '0' COMMENT '分类ID',
				`isExport` varchar(5) DEFAULT '0' COMMENT '是否生成过简报 1-生成过 0-未生成过',
				`isDelete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '原帖是否删除 0:未删除，1:已删除',
				`media_source_type` tinyint(4) DEFAULT '99' COMMENT '新媒体类型默认99为了与3.0统一特殊处理',
				`media_subord_type` tinyint(4) DEFAULT '99' COMMENT '下级媒体类型默认99为了与3.0统一特殊处理',
				`info_source_range` tinyint(4) DEFAULT '1' COMMENT '默认本市 信源范围',
				`author_id` varchar(32) DEFAULT '' COMMENT '作者id',
				PRIMARY KEY (`infoUuid`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_VIDEO_INFO` (
			  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
			  `info_id` varchar(32) NOT NULL COMMENT '信息ID',
			  `original_link` varchar(300) DEFAULT NULL COMMENT '原链接',
			  `info_source` int(11) NOT NULL COMMENT '信息来源',
			  `info_content` text NOT NULL COMMENT '原视频内容',
			  `comment_content` text COMMENT '评论内容，当前信息为评论信息时，此字段有值',
			  `keyword` varchar(300) NOT NULL COMMENT '关键词',
			  `is_read` int(11) NOT NULL DEFAULT '0' COMMENT '是否已读 0未读 1已读',
			  `is_warning` int(11) NOT NULL DEFAULT '0' COMMENT '是否预警 0未预警 1 预警',
			  `orientation` int(11) NOT NULL COMMENT '倾向性 1 正面 2负面 3 中性',
			  `subject_id` varchar(32) NOT NULL COMMENT '专题ID',
			  `cover_image_link` varchar(300) DEFAULT NULL COMMENT '封面图片链接',
			  `url` varchar(300) NOT NULL COMMENT '视频或评论链接',
			  `is_comment_data` int(11) NOT NULL DEFAULT '0' COMMENT '是否是评论数据 0否 1是',
			  `frequency_of_play` int(11) DEFAULT '0' COMMENT '播放次数',
			  `number_of_points` int(11) DEFAULT '0' COMMENT '点赞次数',
			  `release_time` datetime NOT NULL COMMENT '发布时间',
			  `acquisition_time` datetime NOT NULL COMMENT '采集时间',
			  `insert_time` datetime NOT NULL COMMENT '插入时间',
			  `author` varchar(50) NOT NULL COMMENT '作者',
			  `author_key` varchar(50) NOT NULL DEFAULT '' COMMENT '作者key，用于查找作者详细信息',
			  `author_head_link` varchar(300) DEFAULT NULL COMMENT '作者头像链接',
			  `author_fans_count` int(11) DEFAULT '0' COMMENT '作者粉丝数',
			  `author_number_of_works` int(11) DEFAULT '0' COMMENT '作者作品数',
			  `simhash` varchar(32) DEFAULT NULL,
			  `is_delete` int(11) NOT NULL DEFAULT '0' COMMENT '是否删除0未删除 1已删除',
			  PRIMARY KEY (`id`),
			  KEY `INDEX_RELEASE_TIME` (`release_time`) USING BTREE,
			  KEY `INDEX_SIMHASH` (`simhash`) USING BTREE,
			  KEY `INDEX_INSERT_TIME` (`insert_time`) USING BTREE
			) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `origin` (
			  `id` int(11) NOT NULL AUTO_INCREMENT,
			  `url` varchar(1024) CHARACTER SET utf8 DEFAULT '' COMMENT '原文链接',
			  `content` mediumtext COMMENT '原文内容',
			  `author` varchar(255) DEFAULT '' COMMENT '原文作者',
			  `author_avatar_url` varchar(1024) DEFAULT '' COMMENT '原文作者头像',
			  `attitude` int(11) DEFAULT '3' COMMENT '原文倾向性 默认中性',
			  `publish_time` timestamp(3) NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '原文发布时间',
			  `author_auth_type` int(11) DEFAULT '1' COMMENT '原文作者认证类型',
			  PRIMARY KEY (`id`),
			  UNIQUE KEY `Index_url` (`url`) USING BTREE
			) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='信息原文'
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `info_delete_log` (
			  `KR_UUID` varchar(40)  NOT NULL DEFAULT '',
			  `KV_UUID` varchar(40)  DEFAULT NULL,
			  `KR_INFOTYPE` varchar(2)  DEFAULT NULL,
			  `KR_KEYWORDID` varchar(40)  DEFAULT NULL,
			  `KR_UID` int(5) DEFAULT NULL,
			  `KR_STATE` varchar(2)  DEFAULT NULL,
			  `KR_CTIME` varchar(20)  DEFAULT NULL,
			  `KR_ISLOCAL` varchar(1)  DEFAULT NULL,
			  `KV_FLAG` varchar(1)  DEFAULT NULL,
			  `ARG1` varchar(50)  DEFAULT NULL,
			  `ARG2` varchar(50)  DEFAULT NULL,
			  `ARG3` varchar(50)  DEFAULT NULL,
			  `KEYWORD` varchar(200)  DEFAULT NULL,
			  `ORIENTATION` varchar(2)  DEFAULT NULL,
			  `ISYJ` int(2) DEFAULT NULL,
			  `ISREAD` int(2) DEFAULT NULL,
			  `ISMYATTENTION` int(2) DEFAULT NULL,
			  `ISFEEDBACK` int(2) DEFAULT NULL,
			  `ARG4` varchar(50)  DEFAULT NULL,
			  `ARG5` varchar(50)  DEFAULT NULL,
			  `KV_VISITCOUNT` int(2) DEFAULT NULL,
			  `KV_REPLY` int(2) DEFAULT NULL,
			  `KV_SIMHASH` varchar(50)  DEFAULT NULL,
			  `KV_WEBNAME` varchar(50)  DEFAULT NULL,
			  `KV_COLLECTTIME` varchar(20)  DEFAULT NULL,
			  `KV_SOURCETYPE` varchar(2)  DEFAULT NULL,
			  `KV_HOT` int(2) DEFAULT NULL,
			  `KV_ISTF` int(2) DEFAULT NULL,
			  `KV_ISRD` int(2) DEFAULT NULL,
			  `ISUSERMAIN` int(2) DEFAULT NULL,
			  `ISMAINSIMHASH` int(2) DEFAULT NULL,
			  `KV_TITLE` varchar(200)  DEFAULT NULL,
			  `LOSTTIME` varchar(10)  DEFAULT NULL,
			  `KV_ORIEN_LEVEL` int(2) DEFAULT NULL,
			  `NOISESTATUS` varchar(100)  DEFAULT NULL,
			  `KV_ABSTRACT` varchar(500)  DEFAULT NULL,
			  `KV_URL` varchar(270)  DEFAULT '' NOT NULL,
			  `KV_KEYWORD` varchar(200)  DEFAULT NULL,
			  `KV_WBAUTHORPIC` varchar(200)  DEFAULT NULL,
			  `KV_AUTHOR` varchar(50)  DEFAULT NULL,
			  `KR_GTIME` varchar(20)  DEFAULT NULL,
			  `KV_ISPIC` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否有图片 0没有 1有',
			  `KV_ISVIDEO` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否有视频 0 没有 1 有',
			  `KV_IMGURL` varchar(1000)  DEFAULT NULL,
			  `KV_VEDEOURL` varchar(1000)  DEFAULT NULL,
			  `KV_TITLEMATCH` varchar(2)  NOT NULL DEFAULT '',
			  `KV_MUSTWORDMININDEX` int(11) NOT NULL DEFAULT '0',
			  `KV_KEYWORDSMININDEX` int(11) NOT NULL DEFAULT '0',
			  `KV_ONLYLOCAL` varchar(2)  NOT NULL DEFAULT '',
			  `KV_WEIBOOVERTIME` varchar(2)  NOT NULL DEFAULT '',
			  `KV_WEIBOSIGNLOCALNOISE` varchar(2)  NOT NULL DEFAULT '',
			  `KV_WEIBOTOPICNOISE` varchar(2)  NOT NULL DEFAULT '',
			  `KV_WEIBOATNOISE` varchar(2)  NOT NULL DEFAULT '',
			  `KV_DTCTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_DTTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_WEBCHANNEL` varchar(100)  DEFAULT NULL COMMENT '频道名称',
			  `KV_HOTKEYWORD` varchar(100)  DEFAULT NULL COMMENT '主题词',
			  `KV_DOMAIN` varchar(150)  DEFAULT NULL COMMENT '域名',
			  `KV_SITEID` varchar(50)  DEFAULT NULL COMMENT '配置ID',
			  `KV_INFORMATIONSTATE` varchar(30)  DEFAULT '0' COMMENT '平台预警信息状态',
			  `ENTITYAREA` varchar(200)  NOT NULL DEFAULT '' COMMENT '地域',
			  `ENTITYPEOPLE` varchar(200)  NOT NULL DEFAULT '' COMMENT '人名',
			  `ENTITYMETHANISM` varchar(200)  NOT NULL DEFAULT '' COMMENT '机构',
			  `IMPORTANCE_WEIGHT` int(11) NOT NULL DEFAULT '0' COMMENT '重要度',
			  `KV_EXTEND_FIELD` json DEFAULT NULL COMMENT '扩展JSON字段',
			  `KV_INPUTDATATYPE` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:系统录入 2：手动录入',
			  `isDelete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '原帖是否删除，0:未删除，1:已删除',
			  `ts_tag` varchar(20)  NOT NULL DEFAULT '' COMMENT '态势感知涉事类型tag',
			  `media_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '媒体分类',
			  `is_comment` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否评论，0：非评论 1：评论',
			  `delete_time` varchar(20)  NOT NULL DEFAULT '' COMMENT '删除时间',
			  `defender` varchar(20)  NOT NULL DEFAULT '' COMMENT '维护人',
			  `media_source_type` tinyint(4) DEFAULT '99' COMMENT '新媒体类型默认99为了与3.0统一特殊处理',
			  `media_subord_type` tinyint(4) DEFAULT '99' COMMENT '下级媒体类型默认99为了与3.0统一特殊处理',
			  `info_source_range` tinyint(4) DEFAULT '1' COMMENT '默认本市 信源范围',
			  `url_md5` varchar(32)  DEFAULT '' COMMENT '文章链接md5',
			  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '入库时间',
			  `author_id` varchar(32)  DEFAULT '' COMMENT '作者id',
			  `location_code` int(10) DEFAULT '0' COMMENT '新闻地域id',
			  PRIMARY KEY (`KR_UUID`),
			  KEY `KV_URL` (`KV_URL`) USING BTREE
			) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='删除信息日志表'
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `author` (
			  `id` int(11) NOT NULL AUTO_INCREMENT,
			  `author_id` varchar(32) DEFAULT '' COMMENT '作者id',
			  `author_type` tinyint(4) DEFAULT '99' COMMENT '作者类型--微博 贴吧 。。。。',
			  `auth_type` int(11) DEFAULT '1' COMMENT '作者认证类型',
			  `avatar_url` varchar(1024) DEFAULT '' COMMENT '作者头像url',
			  `nickname` varchar(255) DEFAULT '' COMMENT '作者昵称',
			  `sex` tinyint(2) DEFAULT '0' COMMENT '作者性别',
			  `region` varchar(255) DEFAULT '' COMMENT '作者地域',
			  `fans_count` int(11) DEFAULT '0' COMMENT '作者粉丝数',
			  `works_num` int(11) DEFAULT '0' COMMENT '作者作品数',
			  `create_time` timestamp(3) NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '作者入库时间',
			  PRIMARY KEY (`id`),
			  UNIQUE KEY `index_id` (`author_id`) USING BTREE,
			  KEY `index_author` (`author_id`,`auth_type`)
			) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `TS_T_VALIDATION_REF`  (
			  `KR_UUID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_UUID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KR_INFOTYPE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KR_KEYWORDID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KR_UID` int(5) NULL DEFAULT NULL,
			  `KR_STATE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KR_CTIME` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KR_GTIME` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KR_ISLOCAL` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_FLAG` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `ARG1` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `ARG2` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `ARG3` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KEYWORD` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `ORIENTATION` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `ISYJ` int(2) NULL DEFAULT NULL,
			  `ISREAD` int(2) NULL DEFAULT NULL,
			  `ISMYATTENTION` int(2) NULL DEFAULT NULL,
			  `ISFEEDBACK` int(2) NULL DEFAULT NULL,
			  `ARG4` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `ARG5` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_VISITCOUNT` int(2) NULL DEFAULT NULL,
			  `KV_REPLY` int(2) NULL DEFAULT NULL,
			  `KV_SIMHASH` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_WEBNAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_COLLECTTIME` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_SOURCETYPE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_HOT` int(2) NULL DEFAULT NULL,
			  `KV_ISTF` int(2) NULL DEFAULT NULL,
			  `KV_ISRD` int(2) NULL DEFAULT NULL,
			  `ISUSERMAIN` int(2) NULL DEFAULT NULL,
			  `ISMAINSIMHASH` int(2) NULL DEFAULT NULL,
			  `KV_TITLE` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `LOSTTIME` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_ORIEN_LEVEL` int(2) NULL DEFAULT NULL,
			  `NOISESTATUS` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_ABSTRACT` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_URL` varchar(270) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_KEYWORD` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_WBAUTHORPIC` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_AUTHOR` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_ISPIC` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否有图片 0没有 1有',
			  `KV_ISVIDEO` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否有视频 0 没有 1 有',
			  `KV_IMGURL` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_VEDEOURL` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
			  `KV_TITLEMATCH` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_MUSTWORDMININDEX` int(11) NOT NULL DEFAULT 0,
			  `KV_KEYWORDSMININDEX` int(11) NOT NULL DEFAULT 0,
			  `KV_ONLYLOCAL` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_WEIBOOVERTIME` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_WEIBOSIGNLOCALNOISE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_WEIBOTOPICNOISE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_WEIBOATNOISE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
			  `KV_DTCTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_DTTIME` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
			  `KV_WEBCHANNEL` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '频道名称',
			  `KV_HOTKEYWORD` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '主题词',
			  `KV_DOMAIN` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '域名',
			  `KV_SITEID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配置ID',
			  `KV_INFORMATIONSTATE` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '0' COMMENT '平台预警信息状态',
			  `IMPORTANCE_WEIGHT` int(11) NOT NULL DEFAULT 0 COMMENT '重要度',
			  `KV_EXTEND_FIELD` json DEFAULT NULL COMMENT '扩展JSON字段',
			  `KV_INPUTDATATYPE` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1:系统录入 2：手动录入',
			  `isDelete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '原帖是否删除 0:未删除，1:已删除',
			  `ts_tag` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '态势感知涉事类型tag',
			  `media_type` tinyint(4) NOT NULL DEFAULT 0 COMMENT '媒体分类',
			  `is_comment` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否评论，0：非评论 1：评论',
			  `delete_time` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '删除时间',
			  `defender` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '维护人',
			  `location_code` int(10) NULL DEFAULT 0 COMMENT '信息地域id',
			  `media_source_type` tinyint(4) NULL DEFAULT 99 COMMENT '新媒体类型默认99为了与3.0统一特殊处理',
			  `media_subord_type` tinyint(4) NULL DEFAULT 99 COMMENT '下级媒体类型默认99为了与3.0统一特殊处理',
			  `info_source_range` tinyint(4) NULL DEFAULT 1 COMMENT '默认本市 信源范围',
			  `url_md5` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '文章链接md5',
			  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '入库时间',
			  `author_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '作者id',
			  `TS_EXTEND_FIELD` json DEFAULT NULL COMMENT '态势专用扩展JSON字段',
			  PRIMARY KEY (`KR_UUID`) USING BTREE,
			  INDEX `index_ORIENTATION`(`ORIENTATION`) USING BTREE,
			  INDEX `INDEX_KV_UUID`(`KV_UUID`) USING BTREE,
			  INDEX `INDEX_KR_CTIME`(`KR_CTIME`) USING BTREE,
			  INDEX `INDEX_SIMHASH`(`KV_SIMHASH`) USING BTREE,
			  INDEX `INDEX_SOURCETYPE`(`KV_SOURCETYPE`) USING BTREE,
			  INDEX `KV_COLLECTTIME`(`KV_COLLECTTIME`) USING BTREE,
			  INDEX `KV_URL`(`KV_URL`) USING BTREE,
			  INDEX `INDEX_IMPORTANCE_WEIGHT`(`IMPORTANCE_WEIGHT`) USING BTREE,
			  INDEX `IDX_UID_KWID_CT`(`KR_UID`, `KR_KEYWORDID`, `KR_CTIME`) USING BTREE
			) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            create_sql = '''
            CREATE TABLE `WK_T_VALIDATION_NEW_REF`  (
			  `KR_UUID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主键，随机32位uuid',
			  `KV_UUID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '信息uuid，对应data数据中的uuid',
			  `KR_KEYWORDID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '专题id，信息所属的专题id',
			  `KR_STATE` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '噪音过滤',
			  `KR_CTIME` varchar(20) NOT NULL DEFAULT '' COMMENT '发布时间',
			  `KR_ISLOCAL` tinyint(4) NOT NULL DEFAULT 0 COMMENT '信息来源，0境内 1境外 2外媒，默认为境内',
			  `ORIENTATION` tinyint(4) NOT NULL DEFAULT 3 COMMENT '倾向性，1正面2负面3中性，默认为中性',
			  `ISREAD` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否已读，0未读1已读，默认为未读',
			  `KV_SIMHASH` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT 'simhash，信息hash值用于计算相似信息',
			  `create_time` varchar(20) NOT NULL DEFAULT '' COMMENT '入库时间',
			  `isDelete` tinyint(4) NOT NULL DEFAULT 0 COMMENT '原帖是否删除，0未删除1已删除',
			  `is_comment` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否评论，0非评论1评论',
			  `media_source_type` tinyint(4) NOT NULL DEFAULT 99 COMMENT '4.0媒体类型，默认99兼容3.0',
			  `media_subord_type` tinyint(4) NOT NULL DEFAULT 99 COMMENT '小视频类型，默认99',
			  `IMPORTANCE_WEIGHT` smallint(6) NOT NULL DEFAULT 0 COMMENT '重要度，默认为0',
			  `info_source_range` tinyint(4) NOT NULL DEFAULT 1 COMMENT '信源范围，1本市2本省3省外',
			  `url_md5` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '信息url的md5值，用于去重使用',
			  `ARG1` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否精准，流式中0为非精准1为精准，秘书中 0精准 1非精准',
			  `KV_HOTKEYWORD` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主体词，用于检测统计分析热词模块',
			  `KV_WEBNAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '网站名称',
			  `KV_AUTHOR` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '信息作者',
			  `weibo_type` tinyint(4) NOT NULL DEFAULT 0 COMMENT '博文类型，1原创2仅转发3转发并回复4评论，目前只有微博数据有博文类型',
			  `isOcr` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否图片识别数据，0不是 1是',
			  `author_auth_type` tinyint(4) NOT NULL DEFAULT 1 COMMENT '作者认证类型，1 普通用户2 橙V 3蓝V',
			  `KV_TITLEMATCH` tinyint(4) NOT NULL DEFAULT 0 COMMENT '精准筛选 0 匹配全部 1 匹配标题',
			  `KV_MUSTWORDMININDEX` smallint(5) UNSIGNED NOT NULL DEFAULT 0 COMMENT '地域词首次出现位置',
			  `KV_KEYWORDSMININDEX` smallint(5) UNSIGNED NOT NULL DEFAULT 0 COMMENT '词距范围',
			  `KV_ONLYLOCAL` tinyint(4) NOT NULL DEFAULT 0 COMMENT '唯一地域 0 关闭 1 开启',
			  `KV_WEIBOOVERTIME` tinyint(4) NOT NULL DEFAULT 0 COMMENT '微博时间过滤 0 否  1 是',
			  `KV_WEIBOSIGNLOCALNOISE` tinyint(4) NOT NULL DEFAULT 0 COMMENT '忽略微博位置中的关键词 0 否 1 是',
			  `KV_WEIBOTOPICNOISE` tinyint(4) NOT NULL DEFAULT 0 COMMENT '忽略微博话题中的关键词 0 否 1 是',
			  `KV_WEIBOATNOISE` tinyint(4) NOT NULL DEFAULT 0 COMMENT '忽略微博话题中的关键词 0 否 1 是',
			  `language_type` tinyint(4) NOT NULL DEFAULT 0 COMMENT '语种类型 1 中文 2 外文',
			  `KV_INPUTDATATYPE` tinyint(4) NOT NULL DEFAULT 1 COMMENT '录入类型 1 系统录入 2手动录入',
			  `media_type` tinyint NOT NULL DEFAULT 0 COMMENT '媒体分类，1: 中央媒体 2:地方媒体 3:商业媒体 4: 海外媒体',
			  `industry_tag_v1` varchar(50) NOT NULL DEFAULT '' COMMENT '行业一级标签',
			  `industry_tag_v2` varchar(50) NOT NULL DEFAULT '' COMMENT '行业二级标签',
			  PRIMARY KEY (`KR_UUID`) USING BTREE,
			  INDEX `INDEX_KR_CTIME`(`KR_CTIME`) USING BTREE,
			  INDEX `INDEX_SIMHASH`(`KV_SIMHASH`) USING BTREE,
			  INDEX `INDEX_MEDIA_SOURCE_TYPE`(`media_source_type`) USING BTREE,
			  INDEX `INDEX_KV_URL_MD5`(`url_md5`) USING BTREE,
			  INDEX `INDEX_CREATE_TIME`(`create_time`) USING BTREE,
			  INDEX `INDEX_KEYWORD_CTIME`(`KR_KEYWORDID`, `KR_CTIME`) USING BTREE,
			  INDEX `INDEX_WEBNAME`(`KV_WEBNAME`) USING BTREE,
			  INDEX `INDEX_IMPORTANCE_WEIGHT`(`IMPORTANCE_WEIGHT`) USING BTREE,
			  INDEX `INDEX_IS_OCR`(`isOcr`) USING BTREE,
			  INDEX `INDEX_WEIBO_TYPE`(`weibo_type`) USING BTREE,
			  INDEX `INDEX_LANGUAGE_TYPE`(`language_type`) USING BTREE,
			  INDEX `INDEX_HOTKEYWORD`(`KV_HOTKEYWORD`) USING BTREE,
			  INDEX `INDEX_AUTHOR`(`KV_AUTHOR`) USING BTREE
			) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '查询统计子表' ROW_FORMAT = Dynamic
            '''
            rs = cur.execute(create_sql)
            if not rs:
                drop_sql = '''
                    DROP DATABASE {}
                '''.format(db_name)
                cur.execute(drop_sql)
                connect.commit()
                result['code'] = 201
                result['msg'] = 'err'
                return result

            connect.commit()
            result['ip'] = ip
            return result
        else:
            result['code'] = 201
            result['msg'] = 'err'
            return result
    except:
        result['code'] = 201
        result['msg'] = 'err'
        return result


