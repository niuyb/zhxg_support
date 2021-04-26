import logging
import traceback
import datetime

import pymysql
import requests
import json

from dateutil.relativedelta import relativedelta
from django.http import HttpResponse, JsonResponse
from mandala.auth.decorators import login_required, permission_required

from customer.models import Questionaire, Account
from customer.service.NewcustService import newInternal
from customer.utils import (
    get_cities, get_counties, get_acc_data, get_opp_data, get_team_acc_data, get_team_opp_data
)
from interface.utils import update_acc, update_opp, update_team
from interface.tools.mapping import mappingDict
from django.conf import settings
from public.utils import get_all_data, parse_kwargs_for_pymysql
from support.settings import environment, domain_support, MODE

logger = logging.getLogger("customer")

# Create your views here.

"""通过省份获取城市"""
# @login_required
def cities_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    pid = kws.get("pid")
    cities = [("", "--------")]
    if pid:
        cities += get_cities(pid)
    return JsonResponse(cities, safe=False)

"""通过城市获取区县"""
# @login_required
def counties_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    pid = kws.get("pid")
    counties = [("", "--------")]
    if pid:
        counties += get_counties(pid)
    return JsonResponse(counties, safe=False)


"""
    接口功能：将客户、商机的最新实时信息，写入account、opportunity表；
    参数：account_id
"""
def sync_crm_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    account_id = kws.get("account_id")
    # print('+++++++++++++++++++++++++++++', account_id)
    account_dict = mappingDict().account()[1]
    new_account_id = account_dict[account_id]
    # print('+++++++++++++++++++++++++++++++', new_account_id)
    acc_data = get_acc_data(new_account_id)
    # print('+++++++++++++++++++++++++++++++', acc_data)
    opp_data = get_opp_data(new_account_id)
    # print('+++++++++++++++++++++++++++++++', opp_data)

    try:
        # # acc_url = 'http://172.16.251.246:8000/interface/update_account'
        # acc_url = 'http://172.16.251.246:8000/interface/update_account?data={}'.format(acc_data)
        # acc_dict = {
        #     "data": acc_data
        # }
        #
        # print(acc_dict)
        # # acc_r = requests.post(url=acc_url, data=acc_dict)
        # acc_r = requests.get(url=acc_url)
        # acc_message = json.loads(acc_r.text)
        # acc_message = acc_message["message"]
        #
        # opp_url = 'http://172.16.251.246:8000/interface/update_opportunity'
        # opp_dict = {
        #     "data": opp_data,
        # }
        # opp_r = requests.post(url=opp_url, data=opp_dict)
        # opp_message = json.loads(opp_r.text)
        # opp_message = opp_message["message"]
        acc_message = update_acc(acc_data)
        acc_message = acc_message["message"]
        print('+++++++++++++++++++++++++++++++', acc_message)
        opp_message = update_opp(opp_data)
        opp_message = opp_message["message"]
        print('+++++++++++++++++++++++++++++++', opp_message)

        # team_acc_message = update_team(new_account_id)
        # acc_message = "成功！"
        # opp_message = "成功！"




        mes = '成功'
        if (mes in acc_message) and (mes in opp_message) :
            result = {'code': 1, 'message': "成功！"}
        else:
            result = {'code': 0, 'message': "失败！"}

    except Exception as e:
        result = {'code': -1, 'message': "失败！"}

    # print('++++++++++++++++++++', result)
    return JsonResponse(result, safe=False)


"""
    接口功能：模糊搜索代理商，返回代理商name、id；
    参数：agent_name
"""
def agent_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    try:
        agent_name = kws.get("agent_name")
        database = settings.DATABASES["yqms2_199"]
        if agent_name is None:
            sql = """ SELECT KA_ID,KA_NAME FROM WK_T_AGENTS WHERE KA_STATUS = '0' """
        else:
            sql = """ SELECT KA_ID,KA_NAME FROM WK_T_AGENTS WHERE KA_STATUS = '0' 
                    AND KA_NAME LIKE '%{}%' """.format(agent_name)

        agent_tuple = get_all_data(database, sql)
        agent_list = []
        for info in agent_tuple:
            agent_dict = {}
            agent_dict["agent_id"] = info[0]
            agent_dict["agent_name"] = info[1]
            agent_list.append(agent_dict)

        result = {'code': 1, 'message': "成功！", "data": agent_list}
    except:
        result = {'code': 0, 'message': "失败！", "data": []}
    return JsonResponse(result, safe=False)


"""
    接口功能:获取某个客户关联的所有商机负责人的api;
    传参：account_id(老)
    返回:含多个键值对的字典，其中字典的key是opp_id，value是opp_owner
"""
def opp_owner_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    try:
        account_id = kws.get("account_id")
        database = settings.DATABASES["crminfo_33"]

        opp_sql = """ SELECT
                        o.id AS opp_id,
                        u.name AS owner
                    FROM
                        opportunity o
                    LEFT JOIN user u ON o.ownerId = u.id 
                    WHERE dbcRelation1 ='{}' """.format(account_id)

        opp_data = get_all_data(database, opp_sql)
        opp_dict = {}

        # opp_data是一个可能有一个或多个info的元组
        for info in opp_data:
            opp_dict[info[0]] = info[1]     # key是opp_id，value是opp_owner
            opp_dict.update(opp_dict)

        result = {"status": 1, "message": "成功获取创建账号基础数据", "data": opp_dict}
    except:
        result = {"status": 0, "message": "失败", "data": {}}
    # print(result)
    return JsonResponse(result)

"""
    接口功能：获取当前环境(product、beta、develop)；
"""
def get_environment(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    try:
        envi = environment
        result = {'code': 1, 'message': "成功！", "data": envi}
    except:
        result = {'code': 0, 'message': "失败！", "data": ''}
    return JsonResponse(result, safe=False)

"""
    接口功能：
        1、调用PHP生成舆情秘书账号接口，供本项目JS调用
        2、生成秘书账号后，调用2组的接口通知他们已经创建了一个秘书账号（传参：token、userId）
"""
def add_account_php(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    try:
        if environment == 'product':
            # 线上环境
            support_url = 'https://support.istarshine.com'
            port_number = '30002'
        else:
            # beta环境
            support_url = 'http://support-beta.istarshine.com'
            port_number = '32002'
        # 1、调用PHP生成舆情秘书账号接口
        url = '{}/Api/doAddAccount'.format(support_url)
        # print('*********************************')
        # print(url)
        # print('*********************************')
        data = {
            "crmName": kws.get("crmName"),
            "crmUid": kws.get("crmUid"),
            "opportunityName": kws.get("opportunityName"),
            "opportunityId": kws.get("opportunityId"),
            "logName": kws.get("logName"),
            "pasd": kws.get("pasd"),
            "classify": kws.get("classify"),
            "agent_id": kws.get("agent_id"),
            "classpid": kws.get("classpid"),
            "classid": kws.get("classid"),
            "province_id": kws.get("province_id"),
            "city_id": kws.get("city_id"),
            "county_id": kws.get("county_id"),
            "ssdiyu": kws.get("ssdiyu"),
            'ss_city': kws.get("ss_city"),
            "ss_county": kws.get("ss_county"),
            "xiaoshou": kws.get("xiaoshou"),
            "templateType": kws.get("templateType"),
            "kusex": kws.get("kusex"),
            "userLeve": kws.get("userLeve"),
            "keywordnum": kws.get("keywordnum"),
            "region_lock_word": kws.get("region_lock_word"),
            "bindphone": kws.get("bindphone")
        }
        r = requests.post(url=url, data=data)
        r = json.loads(r.text)

        # 创建账号成功以后判断是否有 调研表
        questionaire = Questionaire.objects.filter(account_id=kws.get("crmUid"))
        if questionaire:
            r["has_syc"] = 1
        else:
            r["has_syc"] = 0

        create_notice = {}
        try:
            if r["status"] == 1:

                #查询  秘书账号密码
                wtuser_sql = '''
                            SELECT KU_LID, KU_NAME, KU_PASSWD FROM WK_T_USER WHERE KU_ID = {} AND KU_NAME = '{}'

                        '''.format(r["result"], kws.get("logName"))
                if MODE == 'develop' or MODE == 'beta':
                    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
                else:
                    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
                conn = pymysql.connect(**kws)
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(wtuser_sql)
                wtuserinfo = cursor.fetchall()
                cursor.close()
                conn.close()
                # kws_30 = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
                #
                # conn_30 = pymysql.connect(**kws_30)
                # cursor_30 = conn_30.cursor(pymysql.cursors.DictCursor)
                # cursor_30.execute(wtuser_sql)
                # wtuserinfo_30 = cursor_30.fetchall()
                # cursor_30.close()
                # conn_30.close()
                #
                # kws_199 = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
                # conn_199 = pymysql.connect(**kws_199)
                # cursor_199 = conn_199.cursor(pymysql.cursors.DictCursor)
                # cursor_199.execute(wtuser_sql)
                # wtuserinfo_199 = cursor_199.fetchall()
                # cursor_199.close()
                # conn_199.close()
                print(wtuserinfo)
                if wtuserinfo:
                    r["uname"] = wtuserinfo[0]['KU_LID']
                    r["passwd"] = wtuserinfo[0]['KU_PASSWD']



                # 2、生成秘书账号后，调用2组的接口通知他们已经创建了一个秘书账号
                create_url = "http://192.168.223.230:{}/user/create".format(port_number)


                # 新增加的参数：账号id、客户id、商机id、二级行业id
                create_data = {
                    "userId": r["result"],
                    "crmUid": data["crmUid"],
                    "opportunityId": data["opportunityId"],
                    "classid": data["classid"]
                }


                headers = {"token": "emh4Zy1zdXBwb3J0",
                           "userId": '{}'.format(r["result"])
                           }
                try:
                    create_notice = requests.post(url=create_url, headers=headers)
                except Exception as e:
                    print("cccccc",traceback.print_exc())
                    print(e)
                create_notice = json.loads(create_notice.text)
        except:
            print("xxx",traceback.print_exc())
            pass
        result = {'code': 1, 'message': "成功！", "data": r, "create_notice": create_notice}
    except:
        result = {'code': 0, 'message': "失败！", "data": {}, "create_notice": {}}
    return JsonResponse(result, safe=False)


#获取crm_id
def get_crm_Id(request):
    if request.method == 'GET':
        result = {"code": 200, "msg": "", "data": None}

        account_id = request.GET.get('account_id')
        account = Account.objects.filter(id=account_id).first()
        if account:
            crm_id = account.crm_id if account.crm_id else ""
            if not crm_id:
                result["code"] = 201
                result["msg"] = ""
                return JsonResponse(result)
        else:
            result["code"] = 201
            result["msg"] = ""
            return JsonResponse(result)

        result["data"] = {
            "crm_id": crm_id
        }
        return JsonResponse(result)

#python添加秘书账号
def add_account(request):
    if request.method == "POST":
        result = {"code": 200, "msg":"success", "data":None}
        if request.body:
            req_data = json.loads(request.body, encoding="utf-8")
        else:
            req_data = {}

        crmName = req_data.get("crmName"),
        crmUid = req_data.get("crmUid"),
        opportunityName = req_data.get("opportunityName"),
        opportunityId = req_data.get("opportunityId"),
        logName = req_data.get("logName"),
        pasd = req_data.get("pasd"),
        classify = req_data.get("classify"),
        agent_id = req_data.get("agent_id"),
        classpid = req_data.get("classpid"),
        classid = req_data.get("classid"),
        province_id = req_data.get("province_id"),
        city_id = req_data.get("city_id"),
        county_id = req_data.get("county_id"),
        ssdiyu = req_data.get("ssdiyu"),
        ss_city = req_data.get("ss_city"),
        ss_county = req_data.get("ss_county"),
        xiaoshou = req_data.get("xiaoshou"),
        templateType = req_data.get("templateType"),
        kusex = req_data.get("kusex"),
        userLeve = req_data.get("userLeve"),
        keywordnum = req_data.get("keywordnum"),
        region_lock_word = req_data.get("region_lock_word"),
        bindphone = req_data.get("bindphone")
        newksid = req_data.get("newksid")


        data = {
            "crmName": crmName,
            "crmUid": crmUid,
            "newksid": newksid,
            "opportunityName": opportunityName,
            "opportunityId": opportunityId,
            "logName": logName,
            "zsname": logName,
            "pasd": pasd,
            "classify": classify,
            "classpid": classpid,
            "classid": classid,
            "province_id": province_id,
            "city_id": city_id,
            "county_id": county_id,
            "ssdiyu": ssdiyu,
            'ss_city': ss_city,
            "ss_county": ss_county,
            "xiaoshou": xiaoshou,
            "templateType": templateType,
            "tag": '快速创建帐号',
            "F_TIME": (datetime.date.today() + relativedelta(months=+1)).strftime('%Y-%m-%d'),
            "noiseAllsub": '0',
            "remova": '0',
            "kusex": kusex,
            "userLeve": userLeve,
            "keywordnum": keywordnum,
            "bindphone": bindphone,
        }

        #判断是否有代理商
        if agent_id:
            #获取代理商
            agentInfo_sql = '''
                SELECT * FROM WK_T_AGENTS WHERE KA_ID = %d
            ''' % (agent_id)

            if MODE == 'develop' or MODE == 'beta':
                kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
            else:
                kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
            conn = pymysql.connect(**kws)
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(agentInfo_sql)
            agentInfo = cursor.fetchone()
            # 获取用户个数
            count_sql = '''
                SELECT COUNT(*) as count FROM WK_T_USER WHERE KD_ID = %d
            ''' % (agent_id)
            cursor.execute(count_sql)
            count = cursor.fetchone()
            if count["count"] >= agentInfo["KA_CUSTOMER_NUMBER"]:
                result["code"] = 201
                result["msg"] = "此代理商可创建帐号数量超限"
                return JsonResponse(result)

            #代理商为3607的 模板设置为4
            if data['agent_id'] == 3607:
                data['templateType'] = '4'
            data['agent_id'] = agent_id

        if data["classify"] == '4' and data["classpid"] == '1' and not data["province_id"]:
            data['region_lock_word'] = region_lock_word
        if data["classify"] == '4' and data["kusex"] == '4':
            data['company_lock_word'] = req_data.get('company_lock_word')
        cookie = request.COOKIES.get("username") if "username" in request.COOKIES else ""
        r = newInternal(data, cookie)
        return JsonResponse(result)
