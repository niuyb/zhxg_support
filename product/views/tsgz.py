import json
import logging
import datetime
from django.http import HttpResponse, JsonResponse
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required
import pymysql
from django.shortcuts import render
from user_center.models import UserLog
from django.conf import settings
from support.settings import *
from public.utils import get_conn





JSON_403 = settings.JSON_403
logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

domain_yqms = domain_yqms
domain_support = domain_support

def tsgz_list(request):
    user_type = {0:'用户', 1:'员工', 2:'测试', 3:'系统用户', 4:'代理商用户', 5:'预警用户', 6:'项目用户', 7:'模板用户'}

    sql = """ SELECT a.id,a.password,R.crmName as cname,a.login_name as name,left(a.create_time,10) as regtime,a.exp_time as endtime,a.user_status,a.user_type as genre,a.type,B.KC_NAME as industry,C.KU_SAVEDAYS as savedays,C.KU_SALE as sale,C.KU_MAINT as maint,D.KU_LEVEL as bumen,e.province,f.city,g.county,R.crmUid FROM tsgz.tsgz_user a LEFT JOIN WK_T_CLASSIFICATION B ON B.KC_ID =a.industry LEFT JOIN WK_T_USERSERVICE C ON C.KU_ID=a.relate_id LEFT JOIN WK_T_USER D ON D.KU_ID=a.relate_id LEFT JOIN yqht.b_locationinfo e on e.uuid=a.province LEFT JOIN yqht.b_locationinfo f on f.uuid=a.city LEFT JOIN yqht.b_locationinfo g on g.uuid=a.county LEFT JOIN CRMACCOUNTMAPPING R ON R.msUid=D.KU_ID WHERE ( a.user_status IN ('0','1','2','-1') ) ORDER BY a.create_time DESC limit 10"""


    conn = pymysql.connect(**conn_info)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    all_infos = cursor.fetchall()
    cursor.close()
    conn.close()
    for val in all_infos:
        val['area'] = ''
        if val['province']:
            val['area'] = val['province'] + ' '
        if val['city']:
            val['area'] = val['area'] + val['city'] + ' '
        if val['county']:
            val['area'] = val['area'] + val['county'] + ' '
        del val['province']
        del val['city']
        del val['county']
        val['genre'] = user_type[val['genre']]


    print(all_infos)
    return render(request, "product/tsgz.html", locals())




def tsgz_list_api(request):
    result = []
    return JsonResponse(result)