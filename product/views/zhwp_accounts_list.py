import json
import pandas as pd
import logging
import pymysql

from django.http import HttpResponse, JsonResponse
from mandala.auth import get_user_model

from support.settings import *

from public.utils import parse_kwargs_for_pymysql
from django.conf import settings
from datetime import datetime, date,timedelta
import time, datetime
from sqlalchemy import create_engine
import pandas as pd
JSON_403 = settings.JSON_403
logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

domain_yqms = domain_yqms
domain_support = domain_support
#获取网评列表
# @app.route('/product/zhwp_accounts_list_api', methods=['GET'])
def zhwp_accounts_list_api(request):

    # message = json.dumps(dict(request.GET))
    if request.GET.get('pageNo'):
        pageNo = int(request.GET.get('pageNo'))
    else:
        pageNo = 1
    if request.GET.get('pageSize'):
        pageSize = int(request.GET.get('pageSize'))
    else:
        pageSize = 10
    start = (pageNo-1)*pageSize
    # 获取当前时间
    now = int(time.time())  # 1533952277
    timeArray = time.localtime(now)
    nowotherStyleTime = time.strftime("%Y-%m-%d 23:59:59", timeArray)
    nowtimeArray = time.strptime(nowotherStyleTime, "%Y-%m-%d %H:%M:%S")
    nowtimeStamp = int(time.mktime(nowtimeArray))
    sql_yqms = "SELECT sys.id,sys.parent_id,sys.org_name,sys.status,sys.created_time,ext.expire_time,ext.org_type,ext.root_status,ext.customerType,sysuser.login_name,sysuser.id as sysuserid " \
               "FROM sys_organization as sys " \
               "left join sys_organization_ext as ext on sys.id=ext.id " \
               "left join sys_user as sysuser on sysuser.org_id = sys.id " \
               "WHERE sys.ssoid IS NULL AND left(sys.created_time,10) < {} GROUP BY sys.org_name ORDER BY sys.created_time DESC".format(nowtimeStamp)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["zhwp_new"])
    conn_33 = pymysql.connect(**kws)
    cursor = conn_33.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_yqms)
    info = cursor.fetchall()
    total = len(info)


    sql_yqms = "SELECT sys.id,sys.parent_id,sys.org_name,sys.status,sys.created_time,ext.expire_time,ext.org_type,ext.root_status,ext.customerType,sysuser.login_name,sysuser.id as sysuserid " \
               "FROM sys_organization as sys " \
               "left join sys_organization_ext as ext on sys.id=ext.id " \
               "left join sys_user as sysuser on sysuser.org_id = sys.id " \
               "WHERE sys.ssoid IS NULL AND left(sys.created_time,10) < {} GROUP BY sys.org_name ORDER BY sys.created_time DESC  LIMIT {} OFFSET {}".format(nowtimeStamp,pageSize,start)
    # print('++++++++++++++++++++++++++++++++++++++++')
    # print(sql_yqms)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["zhwp_new"])
    conn_33 = pymysql.connect(**kws)
    cursor = conn_33.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_yqms)
    items = cursor.fetchall()

    # 机构状态集合
    statusMapping = {1:'正常',0:'停用'}
    # 机构类型集合
    typeMapping = {1:'正式',0:'试用'}
    # 根节点状态集合
    rootStatusMapping = {1:'启用',0:'停用'}
    # customerType集合
    customerTypeMapping ={0:'用户',1:'员工',2:'测试',3:'测试',4:'代理商用户',6:'项目用户'}
    # 组合列表数据
    for value in items:
        wpid = value['id']
        sql = "select * from CRMWPMAPPING where wpId = '{}'".format(wpid)
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        crminfo = cursor.fetchall()
        # print('-----------**'*22)
        # print(crminfo)yqms_log_overview_api

        if not crminfo:
            # value.update({'crmId':'--'})
            value['crmId'] = '--'
            value['crmName'] = '--'
            value['oppName'] = '--'
        else:
            # value.update({'crmId': crminfo[0]['crmId']})
            value['crmId'] =  crminfo[0]['crmId']
            value['crmName'] = crminfo[0]['crmName']
            value['oppName'] = crminfo[0]['oppName']
            # 获取商务信息
            oppid = crminfo[0]['oppId']
            salesql = "select * from CRMSALEMAPPING  where ownerFlag=2 and  opportunityId = '{}'".format(oppid)
            kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
            conn = pymysql.connect(**kws)
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(salesql)
            saleInfo = cursor.fetchall()
            value['saleName'] = saleInfo[0]['saleName']

        nowtime = str(value['created_time'])
        nowtime = nowtime[0:-3]
        timeStamp = int(nowtime)
        timeArray = time.localtime(timeStamp)
        value['created_time'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        if value['expire_time']:

            exptime = value['expire_time']
            timeArray = time.strptime(exptime, "%Y-%m-%d %H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            nowtimestamp = int(time.time())
            if timeStamp < nowtimestamp:
                value['org_type'] = '停用'
            else:
                org_type = value['org_type']
                value['org_type'] = typeMapping[org_type] if typeMapping[org_type] != '' else org_type
            value['expire_time'] = time.strftime("%Y-%m-%d", timeArray)

        else:
            value['expire_time'] = ''

        root_status = value['root_status']
        if root_status:
            value['root_status'] = rootStatusMapping[root_status]
        customerType = value['customerType']
        if customerType:
            value['customerType'] = customerTypeMapping[customerType]
        status = value['status']
        if status:
            value['status'] = statusMapping[status]
        # 获取七天登陆次数
        sixDayAgo = (datetime.datetime.now() - datetime.timedelta(days=6))
        sixtimeStamp = int(time.mktime(sixDayAgo.timetuple()))
        count_sql="SELECT COUNT(id) as num FROM `sys_log` " \
                  "WHERE ( left(created_time,10) > '{}' ) AND ( `org_id` = '{}' ) AND ( `operate_type` = '0' ) " \
                  "GROUP BY from_unixtime(LEFT (created_time, 10),'%Y-%m-%d') ".format(sixtimeStamp,value['id'])
        kws = parse_kwargs_for_pymysql(settings.DATABASES["zhwp_new"])
        conn_wpcount = pymysql.connect(**kws)
        cursor = conn_wpcount.cursor(pymysql.cursors.DictCursor)
        cursor.execute(count_sql)
        logincount = cursor.fetchall()
        value['weeknum'] = len(logincount)
        # print('-----------**' * 22)
        # print(logincount)
        # # for val in logincount:
        # #     # print('-----------**' * 22)
        # #     # print(val['num'])
        # #     value['weeknum'] = val['num']
        # 获取用户信息
        sys_user = "SELECT * FROM `sys_user` WHERE ( `org_id` = '{}' ) ORDER BY created_time DESC LIMIT 1  ".format(value['id'])
        kws = parse_kwargs_for_pymysql(settings.DATABASES["zhwp_new"])
        conn_sys_user = pymysql.connect(**kws)
        cursor = conn_sys_user.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sys_user)
        sys_user_info = cursor.fetchall()
        if len(sys_user_info)>0:
            value['account'] = sys_user_info[0]['login_name']
            value['login_name'] = sys_user_info[0]['login_name']
            value['orgid'] = sys_user_info[0]['org_id']
            value['userid'] = sys_user_info[0]['id']
            value['pwd'] = sys_user_info[0]['login_pwd']

    # print('-----------**' * 22)
    # print(items)
    result = {'data': {"data": items, "page": pageNo, "num": pageSize, "total": total}, 'code': 1, 'error': '测试'}


    return JsonResponse(result,safe=False)
def zhwp_accounts_list_count(request):
    # 获取当前时间
    now = int(time.time())  # 1533952277
    timeArray = time.localtime(now)
    nowotherStyleTime = time.strftime("%Y-%m-%d 23:59:59", timeArray)
    nowtimeArray = time.strptime(nowotherStyleTime, "%Y-%m-%d %H:%M:%S")
    nowtimeStamp = int(time.mktime(nowtimeArray))
    sql_yqms = "SELECT sys.id,sys.parent_id,sys.org_name,sys.status,sys.created_time,ext.expire_time,ext.org_type,ext.root_status,ext.customerType,sysuser.login_name,sysuser.id as sysuserid " \
               "FROM sys_organization as sys " \
               "left join sys_organization_ext as ext on sys.id=ext.id " \
               "left join sys_user as sysuser on sysuser.org_id = sys.id " \
               "WHERE sys.ssoid IS NULL AND left(sys.created_time,10) < {} GROUP BY sys.org_name ORDER BY sys.created_time DESC".format(nowtimeStamp)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["zhwp_new"])
    conn_33 = pymysql.connect(**kws)
    cursor = conn_33.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_yqms)
    info = cursor.fetchall()
    total = len(info)
    return JsonResponse(total,safe=False)




def getLoginBase(request):
    # wpid = request.GET.get('id')
    wpid = '2547402231023616'
    # userid = request.GET.get('userid')
    sql_crm = "SELECT crmId,crmName,oppId,oppName FROM CRMWPMAPPING WHERE wpId='{}'".format(wpid)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    conn_33 = pymysql.connect(**kws)
    cursor = conn_33.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_crm)
    info = cursor.fetchall()

    return JsonResponse(info, safe=False)