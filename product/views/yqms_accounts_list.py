import json
import logging
import datetime
from django.http import HttpResponse, JsonResponse
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required


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


"""获取账号列表"""
# @permission_required("product.accounts_manage.view", login_url=JSON_403)
def yqms_accounts_list_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="账号管理-舆情秘书账号列表api", action="查询", message=message)

    conn, cur = get_conn(**conn_info)
    conn2, cur2 = get_conn(host='192.168.185.33', user='root', passwd='1CzoOCywfJ*h', db='contract')
    conn_log, cur_log = get_conn(host='192.168.18.68', user='loguser', passwd='f693b823', db='log')

    data_infos = []

    all = request.GET.get("all")


    if str(all) == '1':
        limit = ' limit 0,300'
    else:
        limit = ''



    sql_yqms = """ SELECT u.KU_LID,u.KU_ID,s.KU_USERSTATUS,u.KU_NAME,s.KU_SALE,s.KU_MAINT,s.KU_SAVEDAYS,u.KU_REGDATE,s.KU_TRYSDATE,u.KU_LTIME,u.KU_PASSWD,u.KU_DBNAME,u.KU_TEMPLATE,s.KU_CHANGEVERSION,s.KU_INDUSTRY,s.KU_USERGENRE,c.crmUid,c.opportunityId,c.crmName,c.province 
                FROM WK_T_USER u LEFT JOIN WK_T_USERSERVICE s ON u.KU_ID=s.KU_ID LEFT JOIN CRMACCOUNTMAPPING c ON u.KU_ID=c.msUid 
                WHERE ( u.KU_ID=s.KU_ID ) AND ( s.KU_USERSTATUS IN ('0','1','2','-1') ) AND ( s.KU_API_STATUS IN ('0','1','2') )  
                ORDER BY u.KU_REGDATE DESC """ + limit
    cur.execute(sql_yqms)
    all_infos = cur.fetchall()

    """关于商机信息的查询并封装成字典"""
    # 去重查询所有的opportunityId，用于查询商机的条件
    sql_yqms_oppId = """ SELECT DISTINCT opportunityId FROM CRMACCOUNTMAPPING """
    cur.execute(sql_yqms_oppId)
    opp_ids = cur.fetchall()
    # 查询商机、销售确认、结单日期（条件为：所有CRMACCOUNTMAPPING表存在的商机id对应的信息）
    sql_yqms2 = """ SELECT id,opportunityName,dbcSelect26,closeDate FROM opportunity WHERE id IN %s """
    cur2.execute(sql_yqms2, [(opp_ids)])
    all_infos2 = cur2.fetchall()
    #遍历商机的查询结果，封装成字典：key为id
    dic2 = {}
    for infosTwo in all_infos2:
        opportunity_id = infosTwo[0]
        dic2[opportunity_id] = infosTwo

    """关于秘书4.0版本的查询并封装成字典"""
    sql_yqms_version4 = """ SELECT KU_ID,KU_VALUE FROM WK_T_USERBASEINFO WHERE KU_TYPE = 'ms_version' """
    cur.execute(sql_yqms_version4)
    ms_version_infos = cur.fetchall()
    # 遍历查询结果，封装成字典：key为KU_ID
    dic3 = {}
    for infos in ms_version_infos:
        user_id = infos[0]
        dic3[user_id] = infos

    """关于登录天数的查询并封装成字典"""
    sql_log = """ SELECT uid, COUNT(uid) as times FROM `WK_T_USERACTIVITY` WHERE activity_self > 0 AND date >= %s GROUP BY uid """
    days_ago_7 = (datetime.date.today() - datetime.timedelta(days=6)).strftime("%Y%m%d")
    days_ago_30 = (datetime.date.today() - datetime.timedelta(days=29)).strftime("%Y%m%d")
    cur_log.execute(sql_log, days_ago_7)
    active_infos_7 = cur_log.fetchall()
    cur_log.execute(sql_log, days_ago_30)
    active_infos_30 = cur_log.fetchall()
    # 遍历查询结果，封装成字典：key为uid
    dic_active_7 = {}
    for infos in active_infos_7:
        user_id = infos[0]
        dic_active_7[user_id] = infos
    dic_active_30 = {}
    for infos in active_infos_30:
        user_id = infos[0]
        dic_active_30[user_id] = infos


    for infos in all_infos:
        opp_id = infos[17]       # 商机id
        opportunity_name = None
        saler_confirm = None
        close_date = None
        if opp_id != None:
            if opp_id in dic2.keys():
                infos2 = dic2[opp_id]
                opportunity_name = infos2[1]
                saler_confirm = infos2[2]
                close_date = infos2[3]

        if saler_confirm == '1':
            saler_confirm = '承诺'
        elif saler_confirm == '2':
            saler_confirm = '争取'
        elif saler_confirm == '4':
            saler_confirm = '跟进'
        else:
            saler_confirm = ''

        if close_date != None:
            close_date = close_date[0:10]


        regdate=infos[7]
        login_date = infos[9]
        account_status = infos[2]
        account_type = infos[15]
        if regdate != None:
            regdate = infos[7][0:4]+"-"+infos[7][4:6]+"-"+infos[7][6:8]

        if login_date != None:
            login_date = infos[9][0:4] + "-" + infos[9][4:6] + "-" + infos[9][6:8]

        if account_status == '0':
            account_status_str = '正式'
        elif account_status == '1':
            account_status_str = '试用'
        elif account_status == '2':
            account_status_str = '停用'
        elif account_status == '-1':
            account_status_str = '弃用'
        else:
            account_status_str = '其他'

        if account_type == 0:
            account_type_str = '用户'
        elif account_type == 1:
            account_type_str = '员工'
        elif account_type == 2:
            account_type_str = '测试'
        elif account_type == 3:
            account_type_str = '系统用户'
        elif account_type == 4:
            account_type_str = '代理商'
        elif account_type == 5:
            account_type_str = '预警用户'
        elif account_type == 6:
            account_type_str = '项目用户'
        elif account_type == 7:
            account_type_str = '模版用户'
        elif account_type == 8:
            account_type_str = '态势感知创建秘书'
        else:
            account_type_str = '其他'


        """
        秘书版本:wk_T_userservice   KU_CHANGEVERSION   0->2.4  2->3.0
                wk_t_userbaseinfo   ku_type = ms_version   ku_value = 4.0
        """
        user_id = infos[1]
        if user_id in dic3.keys():
            ms_version_userbaseinfo = dic3[user_id][1]  # WK_T_USERBASEINFO表中只保存版本为4.0的账号的版本信息，所以当user_id存在时，返回查询结果，不存在时值为空
        else:
            ms_version_userbaseinfo = ''
        ms_version_userservice = infos[13]
        if ms_version_userbaseinfo == '4.0':
            ms_version = '秘书4.0'
        elif ms_version_userservice == 2:
            ms_version = '秘书3.0'
        elif ms_version_userservice == 0:
            ms_version = '秘书2.4'
        else:
            ms_version = ''

        """账号是否活跃：近7天登录天数>=3天，或近30天登录天数>=12天的账号为活跃账号"""
        if user_id in dic_active_7.keys():
            login_days_7 = dic_active_7[user_id][1]
        else:
            login_days_7 = None
        if user_id in dic_active_30.keys():
            login_days_30 = dic_active_30[user_id][1]
        else:
            login_days_30 = None
        if_active = '不活跃'
        if login_days_7 and login_days_30:
            if (login_days_7 >= 3) or (login_days_30 >= 12):
                if_active = '活跃'
        elif login_days_30:
            if login_days_30 >= 12:
                if_active = '活跃'


        info_dict = {
            "account_name": infos[0],
            "customer_name": infos[18],
            "account_status": account_status_str,
            "account_type": account_type_str,
            "regdate": regdate,
            "due_date": infos[8],
            "last_login_date": login_date,
            "save_days": infos[6],
            "customer_province": infos[19],
            "saler": infos[4],
            "maintainer": infos[5],
            "user_id": infos[1],
            "password": infos[10],
            "opportunity_name": opportunity_name,
            "saler_confirm": saler_confirm,
            "close_date": close_date,
            "ms_version": ms_version,
            "domain_yqms": domain_yqms,
            "domain_support": domain_support,
            "if_active": if_active,
            "login_days_7": login_days_7,
            "login_days_30": login_days_30,
            # "saler_department": infos[0],
        }
        data_infos.append(info_dict)

    total = len(data_infos)
    page = 1
    result = {'data': {"data": data_infos, "page": page, "num": total, "total": total}, 'code': 1, 'error': '测试'}
    cur.close()
    conn.close()
    cur2.close()
    conn2.close()
    cur_log.close()
    conn_log.close()
    return JsonResponse(result)


# 清除访问限制接口
def reset_access_frequencylock(request):
    uid = request.GET.get("uid")
    r = MS_REDIS
    list = r.keys()
    for key in list:
        if ((uid+"_") in key) and (("_"+uid) not in key) and ((uid+"_black") not in key):
            # print('----------------------------------'+key)
            r.delete(key)
            # print('----------------------------------')
    result = {'message': "清除成功！"}
    return JsonResponse(result)


# 清除手机个数接口
def clear_phone(request):
    uid = request.GET.get("uid")
    # 连接数据库并获取游标
    conn, cur = get_conn(**conn_info)

    sql = """ DELETE FROM WK_T_YQMSONLYUSER WHERE T_UID = %s """
    # 执行sql
    cur.execute(sql, [(uid)])
    # 提交修改，不提交相当于没有执行上一句sql
    conn.commit()
    cur.close()
    conn.close()
    result = {'message': "清除成功！"}
    return JsonResponse(result)

