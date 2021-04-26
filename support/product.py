import redis
from public.utils import get_conn

from .base import *  # NOQA

DEBUG = False

MODE = 'product'

NEW_SUPPORT_HOST = "http://support20.istarshine.com"
OLD_SUPPORT_HOST = "http://support.istarshine.com"


# 对接卢达上传微信群二维码的接口
WECHAT_QR_CODE_UPLOAD_API = "http://push-admin.istarshine.com/api/common/wechat/group"

# 上传微信群二维码时，将结果保存到redis
WECHAT_QR_CODE_BINDING_RESULT_HASH = "wechat_qr_code_binding_result_hash"
WECHAT_QR_CODE_TASK_CUSTOMER_HASH = "wechat_qr_code_task_customer_hash"

#微信群消息推送
WECHAT_GROUP_MESSAGE_PUSH_LIST = "yqms_warning_push_prod"

#钉钉H5应用参数-product:
APP_KEY = "dinge9ewltitjuaw2gfe"
APP_SECRET = "TPejIBoEy2x1vBNAYqS40vd097Ty4QkxqkkEqn1ch1T_fZK2XFy1zQXMOUgeOQdt"

# 清除访问限制redis信息
MS_REDIS = redis.StrictRedis(
    host='192.168.16.154',
    port=6379,
    db=14,
    decode_responses=True  # 设置为True返回的数据格式就是str类型
)


# 舆情秘书mysql数据库，连接数据库并获取游标
conn_info = dict(host='192.168.16.199', user='fuser', passwd='97yu1r221pxeyt3', db='yqms2')     #线上


# 舆情秘书域名
domain_yqms = 'yqms'


# 星光后台域名
domain_support = 'support'

# 环境
environment = 'product'
