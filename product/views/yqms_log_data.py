import json
import logging
import datetime
import requests
from django.http import HttpResponse, JsonResponse, FileResponse
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required
from product.script import export_mslog

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

"""舆情秘书-操作日志-操作日历，数据接口"""


@permission_required("product.accounts_manage.view", login_url=JSON_403)
def yqms_log_calendar_api(request):
    message = json.dumps(dict(request.POST))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                           model="舆情秘书-操作日志-日历api", action="查询", message=message)

    data_infos = []
    conn, cur = get_conn(host='192.168.18.68', user='loguser', passwd='f693b823', db='log')
    sql_yqms = """ SELECT date,self,phone,pc40,phone40,wechat 
                FROM `WK_T_USERACTIVITY` 
                WHERE date >= %s AND date <= %s AND uid = %s
                ORDER BY date"""
    uid = request.POST.get("uid")
    # print('-------uid-------', uid)
    start_date = (datetime.date.today() - datetime.timedelta(days=61)).strftime("%Y%m%d")
    end_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")
    cur.execute(sql_yqms, (start_date, end_date, uid))
    all_infos = cur.fetchall()

    for infos in all_infos:
        operate_date = infos[0]
        if operate_date != None:
            operate_date = infos[0][0:4] + "-" + infos[0][4:6] + "-" + infos[0][6:8]
        pc30 = infos[1]
        app30 = infos[2]
        pc40 = infos[3]
        app40 = infos[4]
        wechat = infos[5]

        if pc30 > 0:
            info_dict = {
                "title": "PC3.0：" + str(pc30),
                "date": operate_date,
                "color": "#3788d8",
            }
            data_infos.append(info_dict)
        if app30 > 0:
            info_dict = {
                "title": "APP3.0：" + str(app30),
                "date": operate_date,
                "color": "#9860ec",
            }
            data_infos.append(info_dict)
        if pc40 > 0:
            info_dict = {
                "title": "PC4.0：" + str(pc40),
                "date": operate_date,
                "color": "#8a237a",
            }
            data_infos.append(info_dict)
        if app40 > 0:
            info_dict = {
                "title": "APP4.0：" + str(app40),
                "date": operate_date,
                "color": "#ae8d08",
            }
            data_infos.append(info_dict)
        if wechat > 0:
            info_dict = {
                "title": "微信：" + str(wechat),
                "date": operate_date,
                "color": "#5cbd34",
            }
            data_infos.append(info_dict)

    result = data_infos
    print('-------------------------------------')
    print(result)
    print(type(result))
    print('-------------------------------------')
    cur.close()
    conn.close()
    return JsonResponse(result, safe=False)  # safe值默认是true, 如果返回是列表则safe置为False, 如果返回是字典则safe置为true.


"""舆情秘书-操作日志-总览，数据接口"""


@permission_required("product.accounts_manage.view", login_url=JSON_403)
def yqms_log_overview_api(request):
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                           model="舆情秘书-操作日志-总览api", action="查询", message=message)

    conn, cur = get_conn(host='192.168.18.68', user='loguser', passwd='f693b823', db='log')
    data_infos = []
    sql_yqms = """ SELECT uid, uname,date,activity_self,self,phone,pc40,phone40,wechat 
                FROM `WK_T_USERACTIVITY` 
                WHERE date >= %s AND date <= %s AND uid = %s
                ORDER BY date DESC"""
    uid = request.GET.get("uid")
    start_date = request.GET.get("start_date").replace('-', '')
    end_date = request.GET.get("end_date").replace('-', '')
    cur.execute(sql_yqms, (start_date, end_date, uid))
    all_infos = cur.fetchall()

    for infos in all_infos:
        operate_date = infos[2]
        if operate_date != None:
            operate_date = infos[2][0:4] + "-" + infos[2][4:6] + "-" + infos[2][6:8]

        info_dict = {
            "user_id": infos[0],
            "account_name": infos[1],
            "operate_date": operate_date,
            "operate_sum": infos[3],
            "pc30": infos[4],
            "app30": infos[5],
            "pc40": infos[6],
            "app40": infos[7],
            "wechat": infos[8],
        }
        data_infos.append(info_dict)

    total = len(data_infos)
    page = 1
    result = {'data': {"data": data_infos, "page": page, "num": total, "total": total}, 'code': 1, 'error': '测试'}
    # print(result)
    cur.close()
    conn.close()
    return JsonResponse(result)


"""舆情秘书4.0-操作日志，数据接口"""


@permission_required("product.accounts_manage.view", login_url=JSON_403)
def yqms4_log_detail_api(request):
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                           model="舆情秘书-操作日志-4.0详情api", action="查询", message=message)

    uid = request.GET.get("uid")
    log_date = request.GET.get("log_date")
    today = datetime.date.today().strftime("%Y%m%d")

    # 数据库只存储了当天之前的日志（不含当天）
    if int(log_date) < int(today):
        conn, cur = get_conn(host='192.168.18.68', user='loguser', passwd='f693b823', db='log')
        data_infos = []
        sql_yqms = "SELECT access_date,platform,phone,mod1_name,mod2_name,request_body,ip FROM mod_access_log_40_%s" % log_date + " WHERE msuid = %s ORDER BY access_date"
        cur.execute(sql_yqms, (uid))
        all_infos = cur.fetchall()

        for infos in all_infos:
            """操作平台：小写转大写"""
            platform = infos[1]
            if platform == 'pc':
                platform = 'PC'
            elif platform == 'app':
                platform = 'APP'
            else:
                platform = ''

            """根据ip获取ip地域信息"""
            url = "http://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php"
            data = {"query": infos[6], 'co': '', "resource_id": '6006'}
            r = requests.get(url=url, params=data)
            r = json.loads(r.text)
            ip_location = r['data'][0]['location']
            # print('-------------------------------------')
            # print(ip_location)
            # print('-------------------------------------')

            info_dict = {
                "operate_time": infos[0],
                "platform": platform,
                "phone": infos[2],
                "mod1_name": infos[3],
                "mod2_name": infos[4],
                "request_body": infos[5],
                "ip": infos[6],
                "ip_location": ip_location,
            }
            data_infos.append(info_dict)

        total = len(data_infos)
        page = 1
        result = {'data': {"data": data_infos, "page": page, "num": total, "total": total}, 'code': 1, 'error': '测试'}
        cur.close()
        conn.close()
    else:
        result = {'data': {"data": [], "page": 1, "num": 0, "total": 0}, 'code': 1, 'error': '测试'}

    # print(result)
    return JsonResponse(result)


"""舆情秘书3.0-操作日志，数据接口"""


@permission_required("product.accounts_manage.view", login_url=JSON_403)
def yqms3_log_detail_api(request):
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                           model="舆情秘书-操作日志-3.0详情api", action="查询", message=message)

    uid = request.GET.get("uid")
    log_date = request.GET.get("log_date")
    today = datetime.date.today().strftime("%Y%m%d")

    # 数据库只存储了当天之前的日志（不含当天）
    if int(log_date) < int(today):

        conn, cur = get_conn(host='192.168.18.68', user='loguser', passwd='f693b823', db='log')
        conn2, cur2 = get_conn(host='192.168.110.85', user='wangyin', passwd='wy#admin', db='log')
        data_infos = []
        sql_yqms = "SELECT access_date,access_type,phone,mod1,mod2,param,ip FROM mod_access_log_%s" % log_date + " WHERE uid = %s ORDER BY access_date"
        cur.execute(sql_yqms, (uid))
        all_infos = cur.fetchall()

        """关于3.0一级模块具体名称的查询并封装成字典"""
        sql_mod1 = """ SELECT id,modname FROM mod_access """
        cur2.execute(sql_mod1)
        mod1_infos = cur2.fetchall()
        # 遍历查询结果，封装成字典：key为mod_access的id，与mod_access_log_日期表中的mod1一一对应
        dic1 = {}
        for infos in mod1_infos:
            mod1_id = infos[0]
            dic1[mod1_id] = infos

        """关于3.0二级模块具体名称的查询并封装成字典"""
        sql_mod2 = """ SELECT id,modname FROM mod_access_l2 """
        cur2.execute(sql_mod2)
        mod1_infos = cur2.fetchall()
        # 遍历查询结果，封装成字典：key为mod_access的id，与mod_access_log_日期表中的mod1一一对应
        dic2 = {}
        for infos in mod1_infos:
            mod2_id = infos[0]
            dic2[mod2_id] = infos

        for infos in all_infos:
            """处理操作时间格式"""
            operate_time = infos[0]
            if operate_time != None:
                operate_time = infos[0][0:4] + "-" + infos[0][4:6] + "-" + infos[0][6:8] + " " + infos[0][8:10] + ":" + \
                               infos[0][10:12] + ":" + infos[0][12:14]

            """操作平台"""
            platform = infos[1]
            if platform == 1:
                platform = 'PC'
            elif platform == 2:
                platform = 'APP'
            elif platform == 3:
                platform = '微信'
            else:
                platform = ''

            """一级模块、二级模块的具体模块名"""
            mod1 = infos[3]
            mod2 = infos[4]
            if mod1 in dic1.keys():
                mod1_name = dic1[mod1][1]
            else:
                mod1_name = None
            if mod2 in dic2.keys():
                mod2_name = dic2[mod2][1]
            else:
                mod2_name = None

            """根据ip获取ip地域信息"""
            url = "http://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php"
            data = {"query": infos[6], 'co': '', "resource_id": '6006'}
            r = requests.get(url=url, params=data)
            r = json.loads(r.text)
            ip_location = r['data'][0]['location']

            info_dict = {
                "operate_time": operate_time,
                "platform": platform,
                "phone": infos[2],
                "mod1_name": mod1_name,
                "mod2_name": mod2_name,
                "param": infos[5],
                "ip": infos[6],
                "ip_location": ip_location,
            }
            data_infos.append(info_dict)

        total = len(data_infos)
        page = 1
        result = {'data': {"data": data_infos, "page": page, "num": total, "total": total}, 'code': 1, 'error': '测试'}
        cur.close()
        conn.close()
        cur2.close()
        conn2.close()
    else:
        result = {'data': {"data": [], "page": 1, "num": 0, "total": 0}, 'code': 1, 'error': '测试'}

    return JsonResponse(result)


# 导出日志
@permission_required("product.accounts_manage.view", login_url=JSON_403)
def export_log(request):
    data = request.POST
    start_time = data.get('start_time', '')
    end_time = data.get('end_time', '')
    if not start_time or not end_time:
        return JsonResponse({'code': 400, 'msg': '请输入查询时间'})
    uid = data.get("uid")
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                           model="舆情秘书-操作日志-日志导出", action="查询", message=json.dumps(data))
    data = export_mslog.main(uid, start_time, end_time)
    if data.get('code', '') == 200:
        filename = data['file_name']
        res = FileResponse(open(filename, 'rb'))
        res["Content-Type"] = "application/octet-stream"
        res["Content-Disposition"] = filename
        return res
    else:
        return JsonResponse({'code': 4001, 'msg': '日志导出异常'})
