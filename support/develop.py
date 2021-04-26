import redis
from public.utils import get_conn

from .base import *  # NOQA

DEBUG = True

MODE = "develop"

import socket

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)

NEW_SUPPORT_HOST = "http://" + myaddr + ":8000"
OLD_SUPPORT_HOST = "http://support.istarshine.com"

DATABASES["log_120"]['HOST'] = '192.168.18.68'
DATABASES["default"]['NAME'] = 'xgyypt_develop'
DATABASES["crminfo_33"]['NAME'] = 'crm_info_beta'


# DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'yqms2',
    #     'USER': 'tom',
    #     'PASSWORD': 'tom123',
    #     'HOST': 'localhost',
    #     'PORT':3306,
    #     'OPTIONS':{'isolation_level':None}
    # },
    # 'support_mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'yqms2',
    #     'USER': 'tom',
    #     'PASSWORD': 'tom123',
    #     'HOST': 'localhost',
    #     'PORT':3306,
    #     'OPTIONS':{'isolation_level':None}
    # },
    # 'account_mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'yqms2',
    #     'USER': 'tom',
    #     'PASSWORD': 'tom123',
    #     'HOST': 'localhost',
    #     'PORT':3306,
    #     'OPTIONS':{'isolation_level':None}
    # },
# }

# DATABASE_APPS_MAPPING = {
#         # example:
#         #'app_label':'database_name',
#         'user_center': 'default',
#         'mslist': 'db01',
#         'account': 'db02',
#         'admin': 'default',
#         'auth': 'default',
#         'contenttypes': 'default',
#         'sessions': 'default',
# }

# 清除访问限制redis信息
MS_REDIS = redis.StrictRedis(
    host='192.168.185.85',
    port=6379,
    db=14,
    decode_responses=True  # 设置为True返回的数据格式就是str类型
)





# 舆情秘书mysql数据库，连接数据库并获取游标
conn_info = dict(host='192.168.30.2', user='fbeta', passwd='9yacto9659d', db='yqms2')     #beta
# conn_info = dict(host='192.168.16.199', user='fuser', passwd='97yu1r221pxeyt3', db='yqms2')     #线上


# 舆情秘书域名
domain_yqms = 'yqms-beta-g3'      #beta
# domain_yqms = 'yqms'        #线上


# 星光后台域名
domain_support = 'support-beta'       #beta
# domain_support = 'support'      #线上

# 环境
environment = 'develop'
# environment = 'product'

