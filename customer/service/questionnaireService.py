#md5加密
import base64

import pymysql

from customer.models import SurverySubject
from public.utils import parse_kwargs_for_pymysql
from django.conf import settings


def encryption(str):
    queuuid = base64.b64encode(str.encode("utf8"))
    # queuuid = uuid.uuid3(uuid.NAMESPACE_DNS,str)
    queuuid = queuuid.decode("utf8")
    return queuuid

#解密
def deciphering(pwd):
    account_id = base64.b64decode(pwd)
    account_id = account_id.decode("utf8")
    return account_id





#特殊行业id 对应
industry_id_mapping = {
    36: 73,     #高校
    6: 8,       #检察院
    7: 9,       #交通局
    17: 19,     #政府办
    4: 6,       #纪检委
    34: 66,      #市场监督管理局
    72: 72,
    74: 74,
    67: 67,
    76: 76
}
industry_id_33 = [6, 73, 74, 67, 66, 76, 8, 72, 19, 9]


#他们的subject同步到系统表
def sync_subject(industry_id):
    sql = "select id, subject_name, describtion, is_must, region_tag_type from system_recommend_subject where industry_id= '{}' and (describtion != null or describtion != '' or catalog_id != 0)".format(
        industry_id)

    if settings.MODE == 'develop' or settings.MODE == 'beta':
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
    else:
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    conn = pymysql.connect(**kws)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    oppinfo = cursor.fetchall()

    SurverySubject.objects.filter(industry_id=industry_id).delete()

    lst = []
    for o in oppinfo:
        ss = SurverySubject()
        ss.catalog_id = o["id"]
        ss.type = "2"
        ss.catalogname = o["subject_name"]
        ss.tip = o["describtion"]
        ss.question_id = 2
        ss.industry_id = industry_id
        ss.is_default = o["is_must"]
        ss.region_tag_type = o["region_tag_type"]
        # ss.save()
        lst.append(ss)

    SurverySubject.objects.bulk_create(lst)