import redis
from public.utils import get_conn

from .base import *  # NOQA

DEBUG = False

MODE = 'beta'

NEW_SUPPORT_HOST = "http://support20-beta.istarshine.com"
OLD_SUPPORT_HOST = "http://support.istarshine.com"

DATABASES["default"]['NAME'] = 'xgyypt_beta'
DATABASES["crminfo_33"]['NAME'] = 'crm_info_beta'

# 对接卢达上传微信群二维码的接口
WECHAT_QR_CODE_UPLOAD_API = "http://push-admin-beta.istarshine.com/api/common/wechat/group"


#微信群消息推送
WECHAT_GROUP_MESSAGE_PUSH_LIST = "yqms_warning_push_beta"

#钉钉H5应用参数-beta:
# APP_KEY = "ding3x5t5idhnf2u3v5o"
APP_KEY = "dingjxm73egkeiihqvnv"
# APP_SECRET = "DstSSn-Y7K5Np3tF8WxL3rkySDu5GMO_aGhqZ9ZmX0JzLyVQx02yswBFdP9jaCTD"
APP_SECRET = "aDBHMujzlOlQvymtjW_2ARowkzv-iqCVCyJowU0iG1vMay7mHGPnm3lbRdORy7DS"

# 清除访问限制redis信息
MS_REDIS = redis.StrictRedis(
    host='192.168.185.85',
    port=6379,
    db=14,
    decode_responses=True  # 设置为True返回的数据格式就是str类型
)


# 舆情秘书mysql数据库，连接数据库并获取游标
conn_info = dict(host='192.168.30.2', user='fbeta', passwd='9yacto9659d', db='yqms2')     #beta


# 舆情秘书域名
domain_yqms = 'yqms-beta-g3'


# 星光后台域名
domain_support = 'support-beta'

# 环境
environment = 'beta'
