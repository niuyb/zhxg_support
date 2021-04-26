import os
import json
import time
import random
import pymysql
import pandas as pd
import datetime
import logging

from urllib.parse import quote
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from mandala.auth import get_user_model
from mandala.auth.decorators import  permission_required, login_required
from django.conf import settings

from customer.forms import ActivitySelectForm
from customer.models import Account, Opportunity, CrmIndustryL1, CrmIndustryL2
from customer.utils import get_industry_data
from user_center.models import LocationInfo, UserLog
from user_center.utils import make_jump_url, get_user_group_map
from public.utils import parse_kwargs_for_pymysql
from secretary.utils import (get_departments_about_sale, get_can_see, 
        get_group_members, get_can_see_new, get_group_istarshine_ids)
from django.conf import settings
from public.config import SaleSure

URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("customer")

# Create your views here.

User = get_user_model()

"""获取客户活跃度统计页面初始数据"""
def get_activity_init_data():
    init_data = {"row_list": [10, 20, 50], "row_num": 20}
    # init_data["col_names"] = ["账号名称", "账号状态", "登录天数", "商务", "部门",
    #         "区总确认开始", "合同截止日期", "客户名称", "客户省份", "操作"]#, "客户ID", "客户城市", "客户区县"]"ID",
    init_data["col_names"] = ["账号名称", "客户名称", "商机名称", "销售确认","结单日期", "合同截止日期", "商务", "部门",
            "账号创建日期", "一级行业", "二级行业", "账号当前状态", "客户省份", "登录天数", "操作"]#, "客户ID", "客户城市", "客户区县"]"ID",
    init_data["col_model"] = [
        {
            "name": 'account_name',
            # "index": 'id',
            "width": 16,
            # "sorttype": "int"
        },
        {
            "name": 'customer_name',
            # "index": 'note',
            "width": 20,
            # "sortable": false
        },
        {
            "name": 'opportunity_name',
            # "index": 'note',
            "width": 15,
            # "sortable": false
        },
        {
            "name":'dbcselect26',
            "width":8,
        },
        {
            "name": 'closedate',
            # "index": 'tax',
            "width": 12,
            # "align": "right",
            "sorttype": "date",
            "formatter": "date", "formatoptions":{"srcformat": 'Y-m-d H:i', "newformat": 'Y-m-d'}
        },
        {
            "name": 'dbcdate10',
            # "index": 'total',
            "width": 12,
            # "align": "right",
            "sorttype": "date",
            "formatter": "date", "formatoptions":{"srcformat": 'Y-m-d H:i', "newformat": 'Y-m-d'}
        },
        {
            "name": 'saler',
            # "index": 'amount',
            "width": 6,
            # "align": "right",
            # "sorttype": "float",
            # "formatter": "number"
        },
        {
            "name": 'department_name',
            # "index": 'amount',
            "width": 6,
            # "align": "right",
            # "sorttype": "float",
            # "formatter": "number"
        },
        {
            "name": 'ctime',
            # "index": 'amount',
            "width": 12,
            # "align": "right",
            # "sorttype": "float",
            # "formatter": "number"
        },
        {
            "name": 'industry_l1',
            # "index": 'amount',
            "width": 8,
            # "align": "right",
            # "sorttype": "float",
            # "formatter": "number"
        },
        {
            "name": 'industry_l2',
            # "index": 'amount',
            "width": 8,
            # "align": "right",
            # "sorttype": "float",
            # "formatter": "number"
        },
        {
            "name": 'account_status',
            # "index": 'invdate',
            "width": 12,
            # "sorttype": "date",
        },
        {
            "name": 'customer_province',
            # "index": 'note',
            "width": 8,
            # "sortable": false
        },
        {
            "name": 'login_days',
            # "index": 'name',
            "width": 7,
            "sorttype": "int",
        },
        {
            "name": 'operations',
            # "index": 'note',
            "width": 25,
            "sortable": False,
            # "formatter": "constructOperationCell"
        },
    ]
    init_data["items"] = []
    return init_data

"""客户活跃度统计页面"""
@login_required
@permission_required("customer.activity.view",login_url=URL_403)
def activity(request):
    if request.method == "GET":

        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=request.user.username, user_id=request.user.id,
                model="客户管理-客户活跃度统计", action="访问", message=message)

        title = "客户活跃度统计"
        # login_days
        form = ActivitySelectForm(request.GET)
        init_data = get_activity_init_data()
        if request.user.has_perm("customer.activity.export"):
            init_data["export_activity_data_access"] = 1
        ########## 跳转舆情秘书用户首页 #############
        yqms_account_jump_url = settings.YQMS_ACCOUNT_JUMP_URL + quote(request.user.username)
        ########## 跳转态势感知用户首页 #############
        tsgz_account_jump_url = settings.TSGZ_ACCOUNT_JUMP_URL + quote(request.user.username)
        ########## 跳转网评用户首页 #############
        wp_account_jump_url = settings.WP_ACCOUNT_JUMP_URL + quote(request.user.username)
        ########## 跳转CRM客户名称首页 #############
        crm_customer_jump_url = settings.CRM_CUSTOMER_JUMP_URL
        ########## 跳转查看秘书用户信息 #############
        msuser_next_url = settings.MSUSER_NEXT_URL
        msuser_jump_url = make_jump_url(request.user.mobile, msuser_next_url)
        ########## 跳转查看态势感知用户信息 #############
        tsgz_user_next_url = settings.TSGZ_USER_NEXT_URL
        tsgz_user_jump_url = make_jump_url(request.user.mobile, tsgz_user_next_url)
        ########## 跳转查看网评用户信息 #############
        wp_user_next_url = settings.WP_USER_NEXT_URL
        wp_user_jump_url = make_jump_url(request.user.mobile, wp_user_next_url)
        ########## 跳转查看客户画像 ################
        crmuser_next_url = settings.CRMUSER_NEXT_URL
        crmuser_jump_url = make_jump_url(request.user.mobile, crmuser_next_url)

        init_data = json.dumps(init_data)
        user_log_url = reverse("user_center:user_log")
        departments_api = reverse("secretary:departments_api")
        department_data = get_departments_about_sale()
        department_data = json.dumps(department_data)
        department_data_1 =[["", "--------"]] + list(settings.SALE_DEPARTMENT_LEVEL_1.items())
        department_data_1 = json.dumps(department_data_1)
        industry_data = [["", "--------"]] + get_industry_data() + [["0", "未知"]]
        industry_data = json.dumps(industry_data)
        login_days_min = 0
        login_days_max = 180
        return render(request, "customer/activity_list.html", locals())

"""查询商机信息"""
def get_opportunities(quzong_ok_start, quzong_ok_finish, no_quzong_ok, sale_sure,opp_ids=None):
    params = {}
    if opp_ids:
        params["id__in"] = opp_ids
    if quzong_ok_start or quzong_ok_finish:
        if quzong_ok_start and quzong_ok_finish:
            if quzong_ok_start == quzong_ok_finish:
                params["closedate__icontains"] = quzong_ok_start
            else:
                start = min(quzong_ok_start, quzong_ok_finish)
                params["closedate__gte"] = start + " 00:00"
                finish = max(quzong_ok_start, quzong_ok_finish)
                params["closedate__lte"] = finish + " 00:00"
        else:
            if quzong_ok_start:
                params["closedate__gte"] = quzong_ok_start
            else:
                params["closedate__lte"] = quzong_ok_finish + " 00:00"
    if no_quzong_ok in ["1", 1, True, "True"]:
        for key in list(params.keys()):
            if key.startswith("closedate"):
                params.pop(key)
        params["closedate__in"] = [None, ""]
    if sale_sure:
        if int(sale_sure) > 0:
            params["dbcselect26"] = int(sale_sure)
        else:
            params["dbcselect26"] = None
    keys = ("opportunity_id", "opportunity_name", "closedate", "dbcselect26","dbcdate10")
    items = Opportunity.objects.filter(**params).extra(
        select = {'opportunity_id': 'id', 'opportunity_name': 'opportunityname'}
    ).values(*keys)
    items = list(items)
    if (no_quzong_ok in [1, "1", True, "True"] or not (quzong_ok_start or quzong_ok_finish)) and (not sale_sure or int(sale_sure)==0):
        item = {key: None for key in keys}
        item["opportunity_id"] = 0
        items.append(item)
    return items

# 舆情秘书
"""wktuser, wktuserservice, crmaccountmapping三表联合查询"""# 又增加了一个子查询，四个表了
def select_x_yqms(account_name=None, account_status=None, saler=None,
        customer_ids=None, customer_name=None, customer_province_id=None, salers=None,  
        ctime_start=None, ctime_finish=None, account_status_history=None, team=None, maint=None, **kwargs):

    sql = """
        SELECT
            1 as product_type, a.ku_id as id, a.ku_passwd as pas, a.ku_lid as account_name, b.ku_userstatus as account_status,
            b.ku_sale as saler, c.opportunityid as opp_id, c.crmname as customer_name,
            c.province as customer_province, c.crmuid as customer_id, DATE_FORMAT(a.ku_regdate, "%Y-%m-%d") as ctime
        FROM
            WK_T_USER a, WK_T_USERSERVICE b, CRMACCOUNTMAPPING c, ms_salerid d
        WHERE
            {};
        """
    where = ["a.ku_id=b.ku_id", "b.ku_id=c.msuid", "c.crmuid > 0", "c.msuid=d.uid"]#, "c.opportunityid > 0"
    """
    特别注释：
    账号状态这个选项，需要用账号活跃日志里面的账号状态，这样相对准确一些。
    wk_t_user, wk_t_userservice两表中账号状态是当前的状态，用当前的账号状态来查询过去的活跃日志，显然是不准确的。
    举例说明：账号状态由试用变成正式，wk_t_user中的账号状态已经变更为正式，但如果你查询上个月的试用高活的时候，就查询不到这个账号的活跃日志了。
    如果account_status_history=1，则用账号活跃日志中的账号状态，否则用秘书账号表中的数据
    """
    if account_status_history in [1, "1", True, "True"]:
        pass
    else:
        if account_status:
            where.append("b.ku_userstatus={}".format(pymysql.escape_string(str(account_status))))
    if account_name:
        where.append('a.ku_lid like \"%{}%\"'.format(pymysql.escape_string(account_name)))
    if saler:
        ops = [''' b.ku_sale like \"%{}%\" '''.format(pymysql.escape_string(saler))]
        if maint in [1, "1", True, "True"]:
            ops.append(''' b.ku_maint like \"%{}%\" '''.format(pymysql.escape_string(saler)))
        if team in [1, "1", True, "True"]:
            ops.append(''' (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where salename like \"%{}%\")) '''.format(pymysql.escape_string(saler)))
        ops = " (" + " OR ".join(ops)  + ") "
        where.append(ops)

    if customer_ids:
        crmuids = str(tuple(customer_ids)).replace(",)", ")")
        where.append('crmuid in {}'.format(crmuids))
    if customer_name:
        where.append('c.crmname like \"%{}%\"'.format(pymysql.escape_string(customer_name)))
    if customer_province_id:
        where.append("c.province_id={}".format(pymysql.escape_string(str(customer_province_id))))
    if salers:
        _salers = str(tuple(salers))
        if len(salers) == 1:
            _salers = _salers.replace(",", "")

        ops = [''' (d.s_istarshineid in {}) '''.format(_salers)]
        if maint in [1, "1", True, "True"]:
            ops.append(''' (d.m_istarshineid in {}) '''.format(_salers))

        if team in [1, "1", True, "True"]:
            # ops.append(''' (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where salename in {})) '''.format(_salers))
            ops.append(''' (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where istarshineId in {})) '''.format(_salers))

        ops = " (" + " OR ".join(ops) + ") "
        where.append(ops)

    if ctime_start:
        where.append('STR_TO_DATE(a.ku_regdate, "%Y%m%d") >= STR_TO_DATE("{}", "%Y-%m-%d")'.format(ctime_start))

    if ctime_finish:
        where.append('STR_TO_DATE(a.ku_regdate, "%Y%m%d") <= STR_TO_DATE("{}", "%Y-%m-%d")'.format(ctime_finish))

    sql = sql.format(" AND ".join(where))
    # logger.info(sql)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    conn199 = pymysql.connect(**kws)
    cursor = conn199.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    items = cursor.fetchall()
    cursor.close()
    conn199.close()
    result = {}
    mcrms = {}
    ocrms = {}
    for item in items:
        mcrms[item["id"]] = item
        ocrms[item["opp_id"]] = item
    result["items"] = items
    result["mcrms"] = mcrms
    result["ocrms"] = ocrms
    return result

"""态势感知 """
def select_x_tsgz(account_name=None, account_status=None, saler=None,
        customer_ids=None, customer_name=None, customer_province_id=None, salers=None,  
        ctime_start=None, ctime_finish=None, team=None, maint=None, **kwargs):
    sql = """
        SELECT
            2 as product_type, a.id as id, a.password as pas, a.login_name as account_name, a.user_status as account_status,
            b.ku_sale as saler, c.opportunityid as opp_id, c.crmname as customer_name,
            c.province as customer_province, c.crmuid as customer_id, DATE_FORMAT(a.create_time, "%Y-%m-%d") as ctime
        FROM
            tsgz.tsgz_user a, WK_T_USERSERVICE b, CRMACCOUNTMAPPING c, ms_salerid d
        WHERE
            {};
        """
    where = ["a.user_type IN (0, 4)", "a.relate_id=b.ku_id", "b.ku_id=c.msuid", "c.crmuid > 0", "c.msuid=d.uid"]#, "c.opportunityid > 0"
    if account_status:
        where.append("a.user_status={}".format(pymysql.escape_string(str(account_status))))
    if account_name:
        where.append('a.login_name like \"%{}%\"'.format(pymysql.escape_string(account_name)))
    if saler:
        where.append('b.ku_sale like \"%{}%\"'.format(pymysql.escape_string(saler)))
    if customer_ids:
        crmuids = str(tuple(customer_ids)).replace(",)", ")")
        where.append('crmuid in {}'.format(crmuids))
    if customer_name:
        where.append('c.crmname like \"%{}%\"'.format(pymysql.escape_string(customer_name)))
    if customer_province_id:
        where.append("c.province_id={}".format(pymysql.escape_string(str(customer_province_id))))
    if salers:
        _salers = str(tuple(salers))
        if len(salers) == 1:
            _salers = _salers.replace(",", "")

        # where.append('(b.ku_sale in {})'.format(_salers))
        # where.append('((b.ku_sale in {}) or (b.ku_maint in {}))'.format(_salers, _salers))
        # where.append('((b.ku_sale in {}) or (b.ku_maint in {}) or (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where salename in {})))'.format(_salers, _salers, _salers))
        
        ops = [''' (d.s_istarshineid in {}) '''.format(_salers)]
        if maint in [1, "1", True, "True"]:
            ops.append(''' (d.m_istarshineid in {}) '''.format(_salers))

        if team in [1, "1", True, "True"]:
            ops.append(''' (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where istarshineId in {})) '''.format(_salers))

        ops = " (" + " OR ".join(ops) + ") "
        where.append(ops)

    if ctime_start:
        where.append('STR_TO_DATE(a.create_time, "%Y-%m-%d") >= STR_TO_DATE("{}", "%Y-%m-%d")'.format(ctime_start))
    if ctime_finish:
        where.append('STR_TO_DATE(a.create_time, "%Y-%m-%d") <= STR_TO_DATE("{}", "%Y-%m-%d")'.format(ctime_finish))
    sql = sql.format(" AND ".join(where))
    # logger.info(sql)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    conn199 = pymysql.connect(**kws)
    cursor = conn199.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    items = cursor.fetchall()
    cursor.close()
    conn199.close()
    result = {}
    mcrms = {}
    ocrms = {}
    for item in items:
        mcrms[item["id"]] = item
        ocrms[item["opp_id"]] = item
    result["items"] = items
    result["mcrms"] = mcrms
    result["ocrms"] = ocrms
    return result

"""智慧网评 """
def select_x_zhwp(account_name=None, account_status=None, saler=None,
        customer_ids=None, customer_name=None, customer_province_id=None, salers=None, 
        ctime_start=None, ctime_finish=None, team=None, maint=None, **kwargs):
    sql = """select id, org_type as account_status, from_unixtime(created_time/1000, "%Y-%m-%d") as ctime from sys_organization_ext Where """
    where = ["customerType IN (0, 4)"]
    if account_status:
        item = " org_type=%s"%account_status
        where.append(item)
    if ctime_start and ctime_finish:
        where.append('FROM_UNIXTIME(created_time/1000, "%Y-%m-%d") BETWEEN DATE_FORMAT("{}", "%Y-%m-%d") AND DATE_FORMAT("{}", "%Y-%m-%d")'.format(ctime_start, ctime_finish))
    elif ctime_start:
        where.append('FROM_UNIXTIME(created_time/1000, "%Y-%m-%d") >= STR_TO_DATE("{}", "%Y-%m-%d")'.format(ctime_start))
    elif ctime_finish:
        where.append('FROM_UNIXTIME(created_time/1000, "%Y-%m-%d") <= STR_TO_DATE("{}", "%Y-%m-%d")'.format(ctime_finish))
    query = " AND ".join(where)
    sql += query
    kws = {
        "host": "192.168.19.6",
        "port": 3306,
        "database": "zhwp_new",
        "user": "fuser",
        "password": "7ga7iv13a5",
        "charset": "utf8"
    }
    conn19_6 = pymysql.connect(**kws)
    cursor = conn19_6.cursor(pymysql.cursors.DictCursor)
    # cursor = conn19_6.cursor()
    cursor.execute(sql)
    orgs = cursor.fetchall()
    cursor.close()
    conn19_6.close()
    if not orgs:
        result = {}
        result["items"] = {}
        result["mcrms"] = {}
        result["ocrms"] = {}
        return result
    org_dict = {}
    for org in orgs:
        org_dict[org["id"]] = org
    org_id_list = list(org_dict.keys())
    
    sql = """
        SELECT
            3 as product_type, a.wpId as id, a.wpName as account_name,
            b.ku_sale as saler, c.opportunityid as opp_id, c.crmname as customer_name,
            c.province as customer_province, c.crmuid as customer_id
        FROM
            CRMWPMAPPING a, WK_T_USERSERVICE b, CRMACCOUNTMAPPING c, ms_salerid d
        WHERE
            {};
        """
    where = ["a.oppId=c.opportunityid", "a.crmId=c.crmuid", "b.ku_id=c.msuid", "c.crmuid > 0", "c.msuid=d.uid"]#, "c.opportunityid > 0"
    where.append("a.wpId in %s"%(str(tuple(org_id_list))))
    # if account_status:
    #     where.append("a.user_status={}".format(pymysql.escape_string(str(account_status))))
    if account_name:
        where.append('a.wpName like \"%{}%\"'.format(pymysql.escape_string(account_name)))
    if saler:
        where.append('b.ku_sale like \"%{}%\"'.format(pymysql.escape_string(saler)))
    if customer_ids:
        crmids = str(tuple(customer_ids)).replace(",)", ")")
        where.append('a.crmid in {}'.format(crmids))
    if customer_name:
        where.append('c.crmname like \"%{}%\"'.format(pymysql.escape_string(customer_name)))
    if customer_province_id:
        where.append("c.province_id={}".format(pymysql.escape_string(str(customer_province_id))))
    if salers:
        _salers = str(tuple(salers))
        if len(salers) == 1:
            _salers = _salers.replace(",", "")

        # where.append('(b.ku_sale in {})'.format(_salers))
        # where.append('((b.ku_sale in {}) or (b.ku_maint in {}))'.format(_salers, _salers))
        # where.append('((b.ku_sale in {}) or (b.ku_maint in {}) or (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where salename in {})))'.format(_salers, _salers, _salers))
        
        ops = [''' (d.s_istarshineid in {}) '''.format(_salers)]
        if maint in [1, "1", True, "True"]:
            ops.append(''' (d.m_istarshineid in {}) '''.format(_salers))

        if team in [1, "1", True, "True"]:
            ops.append(''' (c.opportunityid in (select distinct opportunityid from CRMSALEMAPPING where istarshineId in {})) '''.format(_salers))

        ops = " (" + " OR ".join(ops) + ") "
        where.append(ops)

    sql = sql.format(" AND ".join(where))
    # logger.info(sql)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    conn199 = pymysql.connect(**kws)
    cursor = conn199.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    items = cursor.fetchall()
    cursor.close()
    conn199.close()
    result = {}
    mcrms = {}
    ocrms = {}
    for item in items:
        iid = item["id"]
        item["account_status"] = str(org_dict.get(iid, {}).get("account_status"))
        item["ctime"] = str(org_dict.get(iid, {}).get("ctime"))
        mcrms[item["id"]] = item
        ocrms[item["opp_id"]] = item
    # items中数据存在重复
    items = list(mcrms.values())
    result["items"] = items
    result["mcrms"] = mcrms
    result["ocrms"] = ocrms
    return result

"""获取舆情秘书账号活跃数据"""
def get_activity_data_yqms(user_ids, activity_start, activity_finish, 
        login_days, account_status=None, account_status_history=None, **kwargs):
    """
    加入了account_status这个参数，秘书日志查询，要求尽可能准确，所以用活跃日志表里面的账号状态为准。
    """
    if len(user_ids) == 1:
        _user_ids = str(tuple(user_ids)).replace(",", "")
    else:
        _user_ids = str(tuple(user_ids))
    """
    sql中会比态势感知和智慧网评中多查了一个status字段，作为account_status,
    同时，也会比态势感知和智慧网评的查询语句多了一个筛选条件，账号状态，即status
    """

    s = ""
    if account_status_history in [1, "1", True, "True"]:
        if (account_status != "") and (account_status is not None):
            if account_status in [2, "2"]:
                s += " status IN (2, 3, 4, 5) AND "
            else:
                s = " status=%s AND "%account_status

    if login_days == 0:
        sql = """
            SELECT uid, 0 as login_days
            FROM WK_T_USERACTIVITY
            WHERE """ + s + """ uid in %s AND date BETWEEN '%s' AND '%s'
            GROUP BY uid
            HAVING sum( activity_self )=%s;
            """
    else:
        sql = """
            SELECT uid, count(activity_self) as login_days
            FROM WK_T_USERACTIVITY
            WHERE """ + s + """uid in %s AND date BETWEEN '%s' AND '%s' AND activity_self > 0
            GROUP BY uid
            HAVING count( activity_self )>=%s;
            """
    sql %= (_user_ids, activity_start.replace("-", ""), activity_finish.replace("-", ""), login_days)
    # logger.info(sql)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["log_120"])
    try:
        # conn120 =pymysql.connect(host='192.168.19.120',user='loguser',password='f693b823',db='log',charset='utf8')
        conn120 = pymysql.connect(**kws)
        acts = pd.read_sql(sql, conn120)
        conn120.close()
        if len(acts) == 0:
            return (acts, 0, "未查找到相关客户活跃信息")
        return (acts, 1, "")
    except Exception as e:
        logger.error(str(e))
        return ([], -1, "服务器繁忙，请稍后再查")

"""查询态势感知账号活跃数据"""
def get_activity_data_tsgz(user_ids, activity_start, activity_finish, login_days, **kwargs):
    if len(user_ids) == 1:
        _user_ids = str(tuple(user_ids)).replace(",", "")
    else:
        _user_ids = str(tuple(user_ids))

    _login_days = login_days
    if login_days == 0:
        _login_days = 1

    sql = """
        SELECT user_id as uid, count(DISTINCT online_day) as login_days
        FROM back_online_day
        WHERE user_id in %s AND (online_day BETWEEN '%s' AND '%s')
        GROUP BY user_id
        HAVING count(DISTINCT online_day )>=%s;
    """
    sql %= (_user_ids, activity_start, activity_finish, _login_days)
    # logger.info(sql)
    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    kws["database"] = "tsgz"
    try:
        conn199 = pymysql.connect(**kws)
        cursor = conn199.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        _acts = acts = cursor.fetchall()
        cursor.close()
        conn199.close()
    except Exception as e:
        logger.error(str(e))
        return ([], -1, "服务器繁忙，请稍后再查")

    if login_days == 0:
        _acts = []
        for act in acts:
            _acts.append(act["uid"])
        acts = []
        for act in (set(user_ids) - set(_acts)):
            _act = {}
            _act["uid"] = act
            _act["login_days"] = 0
            acts.append(_act)

    if len(acts) == 0:
        return (acts, 0, "未查找到相关客户活跃信息")

    else:
        return (pd.DataFrame(acts), 1, "")

"""查询智慧网评账号活跃数据"""
def get_activity_data_zhwp(user_ids, activity_start, activity_finish, login_days, **kwargs):
    _login_days = login_days
    if len(user_ids) == 1:
        _user_ids = str(tuple(user_ids)).replace(",", "")
    else:
        _user_ids = str(tuple(user_ids))
    if login_days == 0:
        _login_days = 1
    # 排除公司办公室ip，机房ip，办事处ip，排除后台跳转的 title='系统登录-后台'
    sql = """
        SELECT
            sub_sys_log.org_id AS uid,
            COUNT(sub_sys_log.login_times) AS login_days
        FROM (
            SELECT org_id,
                COUNT(org_id) as login_times,
                FROM_UNIXTIME(created_time/1000, '%Y-%m-%d') as ctime
            FROM `sys_log`
            WHERE org_id>0
                AND org_id in {}
                AND created_time >= (UNIX_TIMESTAMP('{}')*1000 )
                AND created_time < (UNIX_TIMESTAMP('{}')*1000 + 3600*24*1000)
                AND client_ip NOT IN ('110.249.208.157', '110.249.208.116',
                    '43.239.122.130', '192.168.254.8', '124.204.41.226',
                    '124.239.196.45', '36.5.181.196')
                AND title <> '系统登录-后台'
            GROUP BY org_id, ctime) sub_sys_log
        GROUP BY uid
        HAVING COUNT(sub_sys_log.login_times)>={};"""
    sql = sql.format(_user_ids, activity_start, activity_finish, _login_days)
    kws = {
        "host": "192.168.19.6",
        "port": 3306,
        "database": "zhwp_new",
        "user": "fuser",
        "password": "7ga7iv13a5",
        "charset": "utf8"
    }
    try:
        conn19_6 = pymysql.connect(**kws)
        cursor = conn19_6.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        #acts = pd.read_sql(sql, conn19_6)
        _acts = acts = cursor.fetchall()
        cursor.close()
        conn19_6.close()
    except Exception as e:
        logger.error(str(e))
        return ([], -1, "服务器繁忙，请稍后再查")
    if login_days == 0:
        _acts = []
        for act in acts:
            _acts.append(act["uid"])
        acts = []
        for act in (set(user_ids) - set(_acts)):
            _act = {"uid": act, "login_days": 0}
            acts.append(_act)
    if len(acts) == 0:
        return (acts, 0, "未查找到相关客户活跃信息")
    else:
        return (pd.DataFrame(acts), 1, "")

"""获取客户活跃度统计出来的数据"""
def get_activity_data(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    result = {"status": 0, "message": ""}
    form = ActivitySelectForm(kws)
    if form.is_valid():
        cdata = form.cleaned_data
        product_type = cdata.get("product_type")
        if not product_type:
            result["message"] = "必须指定账号类别"
            return result
        if not (product_type in [1, "1", 2, "2", 3, "3", 4, "4"]):#1, 舆情秘书  2，态势感知  3，智慧网评  4，智慧商情
            result["message"] = "参数非法"
            return result
        account_name = cdata.get("account_name")
        account_status = cdata.get("account_status")
        account_status_history = cdata.get("account_status_history")
        if product_type in [3, "3", 4, "4"]:#智慧网评和智慧商情的账号状态都是0：试用  1：正式，秘书和态势感知的账号状态是0：正式  1：试用
            account_status = {"0": "1", "1": "0"}.get(str(account_status), account_status)
        saler = cdata.get("saler")

        # 是否属于商机团队成员
        team = cdata.get("team")

        # 是否属于账号维护人员
        maint = cdata.get("maint")
        customer_name = cdata.get("customer_name")
        customer_province_id = cdata.get("customer_province")
        # customer_city_id = cdata.get("customer_city")
        # customer_county_id = cdata.get("customer_county")
        ctime_start = cdata.get("ctime_start")
        ctime_finish = cdata.get("ctime_finish") 
        no_quzong_ok = cdata.get("no_quzong_ok")
        quzong_ok_start = cdata.get("quzong_ok_start")
        quzong_ok_finish = cdata.get("quzong_ok_finish")
        sale_sure = cdata.get("sale_sure")
        activity_start_real = activity_start = cdata.get("activity_start")
        activity_finish_real = activity_finish = cdata.get("activity_finish")
        login_days = cdata.get("login_days")
        department_id = cdata.get("department")
        industry_l1 = cdata.get("industry_l1")
        industry_l2 = cdata.get("industry_l2")
        customer_ids = []
        if industry_l1 or industry_l2:
            params = {}
            if industry_l1:
                if industry_l1 == "0":
                    industry_l1 = None
                params["dbcselect5"] = industry_l1
            if industry_l2:
                if industry_l2 == "0":
                    industry_l2 = None
                params["dbcselect9"] = industry_l2
            customer_ids = list(Account.objects.filter(**params).values_list("id", flat=True))
            if not customer_ids:
                result["message"] = "没有查询到关于此行业的相关客户信息"
                return JsonResponse(result)

        now = datetime.datetime.now()
        if not activity_start:
            activity_start_real = (now - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

        if not activity_finish:
            activity_finish_real = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        salers = None
        # 按部门条件筛选
        group_members = []
        if department_id:
            # group_members = get_group_members(department_id)
            group_members = get_group_istarshine_ids(department_id)
            if not group_members:
                result["message"] = "部门成员为空，请检查部门是否存在"
                return result

        # 管理员可以查看所有商务的数据
        if request.user.is_superuser:
            salers = set(group_members)

        else:
            # 权限控制，可以查看哪些商务的数据？
            # can_see = get_can_see(request.user.username)
            can_see = get_can_see_new(request.user.istarshine_id)
            salers = set(can_see)
            if not salers:
                result["status"] = 0
                result["message"] = "您无权查看任何数据"
                return result

            if department_id:
                # 取交集
                salers = salers & set(group_members)
                if not salers:
                    result["status"] = 0
                    result["message"] = "您无权查看此部门"
                    return result

        account_status_map = settings.ACCOUNT_STATUS_MAP
        if product_type in [1, "1"]:
            select_x = select_x_yqms
        elif product_type in [2, "2"]:
            select_x = select_x_tsgz
            account_status_map = settings.TSGZ_ACCOUNT_STATUS_MAP
        elif product_type in [3, "3"]:
            select_x = select_x_zhwp
            account_status_map = settings.ZHWP_ACCOUNT_STATUS_MAP
        else:
            pass
        try:
            x = select_x(account_name, account_status, saler, customer_ids, customer_name,
                    customer_province_id, salers=salers, ctime_start=ctime_start, 
                    ctime_finish=ctime_finish, account_status_history=account_status_history, team=team, maint=maint)

        except Exception as e:
            logger.error(str(e))
            result["status"] = -1
            result["message"] = "服务器繁忙，请稍后重试"
            return result

        items = x["items"]
        mcrms = x["mcrms"]
        msuser_ids = list(mcrms.keys())
        if not msuser_ids:
            result["message"] = "未查到相关客户活跃信息"
            return result

        ocrms = x["ocrms"]

        logger.info(datetime.datetime.now() - now)

        opp_ids = list(ocrms.keys())
        opps = get_opportunities(quzong_ok_start, quzong_ok_finish, no_quzong_ok,sale_sure, opp_ids)
        if not opps:
            result["message"] = "未查到相关客户活跃信息"
            return result

        # logger.info(datetime.datetime.now() - now)
        if login_days < 0:
            result["message"] = "登录天数必须大于0"
            return result

        # 舆情秘书
        if product_type in [1, "1"]:
            _get_activity_data= get_activity_data_yqms

        # 态势感知
        elif product_type in [2, "2"]:
            _get_activity_data = get_activity_data_tsgz

        # 舆情秘书
        elif product_type in [3, "3"]:
            _get_activity_data = get_activity_data_zhwp

        else:
            def get_activity_data_x(*args, **kwargs):
                return [], 0, "目前不支持此种账号类型"
            _get_activity_data = get_activity_data_x

        acts, status, error = _get_activity_data(msuser_ids, activity_start_real, activity_finish_real, 
                login_days, account_status=account_status, account_status_history=account_status_history)

        # logger.info(datetime.datetime.now() - now)
        if status < 1:
            result["status"] = status
            result["message"] = error
            return result

        df = pd.DataFrame(items)
        df = pd.merge(acts, df, how='inner', left_on='uid',right_on='id')
        items = []
        opps = pd.DataFrame(opps)
        if no_quzong_ok in [1, "1", True, "True"] or sale_sure :
            df = pd.merge(df, opps, how='inner', left_on='opp_id', right_on="opportunity_id")
        else:
            if quzong_ok_start or quzong_ok_finish:
                df = pd.merge(df, opps, how='inner', left_on='opp_id', right_on="opportunity_id")
            else:
                df = pd.merge(df, opps, how='left', left_on='opp_id', right_on="opportunity_id")

        if len(df) == 0:
            result["message"] = "未查到相关客户活跃信息"
            return result

        df["dbcselect26"] = df["dbcselect26"].apply(lambda x: SaleSure.get(x))
        customer_ids = list(set(df["customer_id"]))
        accounts = Account.objects.filter(id__in=customer_ids).extra(
                select={'customer_id': 'id', 'industry_l1_id': 'dbcselect5', 'industry_l2_id': 'dbcselect9'}
                ).values("customer_id", "industry_l1_id", "industry_l2_id")
        adf = pd.DataFrame(data=list(accounts))
        industry1 = CrmIndustryL1.objects.all().extra(
                select={'industry_l1_id': 'id', 'industry_l1': 'name'}
                ).values("industry_l1_id", "industry_l1")
        industry2 = CrmIndustryL2.objects.all().extra(
                select={'industry_l2_id': 'id', 'industry_l2': 'name'}
                ).values("industry_l2_id", "industry_l2")
        df1 = pd.DataFrame(data=list(industry1))
        df2 = pd.DataFrame(data=list(industry2))
        adf = pd.merge(adf, df1, how="left", left_on="industry_l1_id", right_on="industry_l1_id")
        adf = pd.merge(adf, df2, how="left", left_on="industry_l2_id", right_on="industry_l2_id")
        df = pd.merge(df, adf, how="left", left_on="customer_id", right_on="customer_id")
        df = df.drop(["industry_l1_id", "industry_l2_id"], axis=1)
        df = df.fillna('')
        # df = df.drop(["uid", "opportunity_id", "id"], axis=1)
        df.drop_duplicates(subset=["id"], keep="first", inplace=True)
        df = df.drop(["opportunity_id", "id"], axis=1)
        df["account_status"] = df["account_status"].apply(lambda x: account_status_map.get(str(x)))
        # 获取用户 - 部门对应关系
        try:
            user_group_map = get_user_group_map()
        except Exception as e:
            logger.error(e)
            result["message"] = "服务器繁忙，请稍后重试"
            return result

        df["department_name"] = df["saler"].apply(lambda x: user_group_map.get(x, ""))
        items = list(df.to_dict(orient="index").values())

        result["status"] = 1
        result["items"] = items
        # logger.info(datetime.datetime.now() - now)
    return result

"""账号活跃度统计查询数据接口，返回json格式的数据"""
@permission_required("customer.activity.view",login_url=JSON_403)
def activity_api(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="客户管理-客户活跃度统计api", action="查询", message=message)

    result = get_activity_data(request)
    return JsonResponse(result)

@login_required
@permission_required("customer.activity.export",login_url=URL_403)
def activity_export_file(request):
    file_type = request.GET.get("fileType")
    if not file_type:
        file_type = "csv"
    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 0 # 导出全部
    fields = request.GET.get("fields", [])
    if fields:
        fields = fields.split(",")
    init_data = get_activity_init_data()
    col_names = init_data["col_names"]
    col_model = init_data["col_model"]
    col_dict = {}
    for i in range(len(col_model)):
        k = col_model[i]["name"]
        if k in ["operations"]:
            continue
        v = col_names[i]
        col_dict[k] = v
    filename = str(int(time.time())) + "_" + str(random.randint(10000, 100000)) + ".csv"

    temp_dir = os.path.join(os.path.abspath("."), "download")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    filepath = os.path.join(temp_dir, filename)
    result = get_activity_data(request)
    items = result["items"]
    df = pd.DataFrame(items, columns=list(col_dict.keys()))
    df.rename(columns=col_dict, inplace=True)
    # df = df.drop(["operations"], axis=1)
    df.to_csv(filepath, index=False, encoding="utf_8_sig")
    # 设置HTTPResponse的类型
    # 创建一个sheet对象
    with open(filepath, "rb") as f:
        content = f.read()
    response = HttpResponse(content_type='application/vnd.ms-csv', content=content)
    # 创建一个文件对象
    response['Content-Disposition'] = 'attachment;filename='+filename
    response['Content-Length'] = len(content)
    os.remove(filepath)
    user = request.user
    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=user.username, user_id=user.id,
            model="客户管理-客户活跃度统计", action="导出", message=message)
    return response

@permission_required("customer.activity.view", login_url=JSON_403)
def get_wp_account_ajax(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    org_id = kws.get("org_id")
    sql = ("select * from sys_user where org_id={}".format(org_id))
    result = run_query(settings.DATABASES['zhwp_new'], sql)
    return JsonResponse(result, safe=False)


def run_query(db, sql=''):
    """sql查询公共方法"""
    try:
        kws = parse_kwargs_for_pymysql(db)
        conn = pymysql.connect(**kws)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return items
    except Exception as e:
        logger.error(str(e))
        return []

