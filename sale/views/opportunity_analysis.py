#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/8/13 17:08
# 工具：PyCharm
# Python版本：3.7.0

# python 2
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# python 3
# import sys
# import importlib
# importlib.reload(sys)
import json
import os
import random
from time import time

import pymysql
import redis
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from mandala.auth.decorators import permission_required, login_required
from django.conf import settings
import pandas as pd

from public.config import opp_entityType
from public.utils import engine
from salerVisit.utils import get_groups
from user_center.models import UserLog

URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

def get_conn():
    host = "192.168.185.33"
    user = "root"
    passwd = "1CzoOCywfJ*h"
    db = "contract"
    port = 3306

    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port,
        charset='utf8')
    # 获得游标
    cur = conn.cursor()
    return cur,conn

def change_badlabel(badlabel):
    try:
        badlabel_dict = {
            "1": "赢率低",
            "2": "拜访少",
            "3": "拜访记录差",
            "4": "账号不活跃",
            "5": "无报价单",
            "6": "承诺差"
        }
        if badlabel is None or badlabel=="":
            return "无"
        else:
            badlabel_list = str(badlabel).split(",")
            badlabel_str = ""

            for single in badlabel_list:
                badlabel_str += badlabel_dict.get(str(single)) + ","
            badlabel_str = badlabel_str[:-1]

            return badlabel_str
    except Exception as e:
        # print(e)
        pass

def change_goodlabel(goodlabel):

    try:
        goodlabel_dict = {
            "1": "高赢率",
            "2": "近期有拜访记录",
            "3": "近期有电话记录",
            "4": "近期有多个记录",
            "5": "账号高活跃",
            "6": "有报价单",
            "7": "销售已承诺",
        }
        if goodlabel is None or goodlabel=="":
            return "无"
        else:
            goodlabel_list = str(goodlabel).split(",")
            goodlabel_str = ""

            for single in goodlabel_list:
                goodlabel_str += goodlabel_dict.get(str(single)) + ","
            goodlabel_str = goodlabel_str[:-1]
            return goodlabel_str
    except Exception as e:
        # print(e)
        pass
def change_permise(confirm):

    try:
        if confirm is None or str(confirm) == "NaN":
            permise = "未填写"
        elif str(int(float(confirm))) == "1":
            permise = "承诺"
        elif str(int(float(confirm))) == "2":
            permise = "跟进"
        elif str(int(float(confirm))) == "4":
            permise = "争取"
        else:
            permise = "未填写"
    except:
        permise = "未填写"

    return  permise

def change_approvalstatus(approvalstatus):

    if isinstance(approvalstatus,float):
        status = "审批未通过"
    elif approvalstatus == "审批通过":
        status = "审批通过"
    else:
        status = "审批未通过"

    return status

def change_others(depart_dict,department,level,sale_stage):
    # 客户级别
    customer_level_map = {
        '1': '重点',
        '4': '开发',
        '5': '正式',
        None: '其他'
    }
    # 商机阶段
    opp_sale_step = {

        '1172739': '产品新单-潜在商机(新)',

        '1172741': '产品新单-商机确认(新)',

        '1186830': '产品新单-商务谈判(新)',

        '1172743': '产品新单-合同确认(新)',

        '1209860': '产品新单-赢单（新）',

        '1172744': '产品新单-输单(新)',

        '1186615': '产品续单-商机确认（续）',

        '1197988': '产品续单-商务谈判（续）',

        '1186616': '产品续单-合同确认（续）',

        '1595051': '产品续单-赢单（续）',

        '1186617': '产品续单-输单（续）',

        '1723501': '项目型业务-初步沟通（项目）',

        '1723502': '项目型业务-意向客户（项目）',

        '1723701': '项目型业务-商机确认（项目）',

        '1723503': '项目型业务-需求确认（项目）',

        '1723504': '项目型业务-商务谈判（项目）',

        '1723003': '项目型业务-合同确认（项目）',

        '1723505': '项目型业务-赢单（项目）',

        '1723506': '项目型业务-输单（项目）',

        '1850762': '星光数据-初步沟通（数据）',

        '1850763': '星光数据-需求确认（数据）',

        '1850764': '星光数据-商务谈判（数据）',

        '1850765': '星光数据-合同确认（数据）',

        '1850766': '星光数据-赢单（数据）',

        '1850767': '星光数据-输单（数据）',

    }


    try:
        level_status = customer_level_map.get(str(int(level)),"")
    except:
        level_status ="其他"

    # 部门名称
    department_status = depart_dict.get(str(department), "----")

    # 销售状态
    sale_stage_status = opp_sale_step.get(str(sale_stage), "")


    return level_status,department_status,sale_stage_status

# def change_type(type):
#     opp_entityType.get()


""" 商机分析"""
@permission_required("sale-analysis.view",login_url=URL_403)
def opp_analysis(request):

    message = json.dumps(dict(request.GET))
    UserLog.objects.create(username=request.user.username, user_id=request.user.id,
            model="商机分析", action="访问", message=message)

    title = "商机分析"
    istarshine_id = request.user.istarshine_id
    return render(request, "sale/opportunity_analysis.html", locals())



# @permission_required("sale-analysis.view",login_url=JSON_403)
def get_opp_info(request):
    istarshine_id = request.user.istarshine_id
    is_support=request.user.is_superuser
    leader=False
    cansee_list=[]
    user_roles = list(request.user.roles.values_list("code",flat=True))
    if is_support :
        pass
    elif "leader" in user_roles:
        leader =True
    else:
        cansee_redis = redis.Redis(host='192.168.187.55', port=6379, db=3)
        cansee_list = eval(cansee_redis.hget("opportunity_analysis", "istarid_%s" % istarshine_id))
        canse_opp_str = ""
        for cansee_oppid in cansee_list:
            canse_opp_str += str(cansee_oppid) + ","

    cur,conn = get_conn()
    data_infos = []
    try:
        # oid = "1035186382569803"
        if len(cansee_list) ==0 or leader or is_support:
            sql_analysis = """ select opportunity_name,oid,good_label,label,win_rate,permise,close_date,
            update_time,saler,department,customer,level,money,sale_stage,archive_rate,customer_id,approvalstatus
            from opportunity_analysis  order by score  desc"""
        else:
            sql_analysis = """ select opportunity_name,oid,good_label,label,win_rate,permise,close_date,
            update_time,saler,department,customer,level,money,sale_stage,archive_rate,customer_id,approvalstatus
            from opportunity_analysis where oid in (%s) order by score  desc""" % canse_opp_str[:-1]
        cur.execute(sql_analysis)
        all_infos = cur.fetchall()


        depart_dict = {}
        sql_depart = """ select id,departName from department  """
        cur.execute(sql_depart)
        depart_infos = cur.fetchall()
        for depart in depart_infos:
            depart_dict[str(depart[0])] = str(depart[1])

        for infos in all_infos:

            level,department,sale_stage=change_others(depart_dict,infos[9],infos[11],infos[13])
            info_dict = {
                "opportunity_name": infos[0],
                "oid":infos[1],
                "good_label":change_goodlabel(infos[2]),
                "label": change_badlabel(infos[3]),
                "win_rate": infos[4],
                "promise": change_permise(infos[5]),
                "close_date": infos[6],
                "update_time": infos[7],
                "saler": infos[8],
                "department":department,
                "customer": infos[10],
                "level":level,
                "money":infos[12],
                "sale_stage":sale_stage,
                "archive_rate":infos[14],
                "customer_id":infos[15],
                "approvalstatus": change_approvalstatus(infos[16]),
            }
            data_infos.append(info_dict)
        total = len(data_infos)
        page = 1
        result = {'data':{"data": data_infos, "page": page, "num": total, "total": total}, 'code': 1, 'error': '测试'}

    except Exception as e:
        # print(e)
        result={'data':{"data": {}, "page": 0, "num": 0, "total": 0}, 'code': 1, 'error': '测试'}
    finally:
        cur.close()
        conn.close()
    return JsonResponse(result)


# @permission_required("sale-analysis.view",login_url=JSON_403)
def get_opptable_info(request):
    oid = request.GET.get("oid")

    cur,conn = get_conn()
    # try:
    sql_analysis = """ select act_days30,act_days7,visit30,visit7,phone_visit30,phone_visit7,fast_record_7,fast_record_30,content30,block_point,approvalstatus,permise,close_date,create_date,record_score,ms_score,approvalstatus_score,permise_score,activity_score,wight,win_rate,winrate_score  from opportunity_analysis where oid ="%s"   """% oid
    cur.execute(sql_analysis)
    infos = cur.fetchone()
    wight = str(infos[19])
    try:
        winrate_wight,activity_wight,record_wight,act_wight,approvalstatus_wight,permise_wight = wight.split(";")
    except :
        winrate_wight, activity_wight, record_wight, act_wight, approvalstatus_wight, permise_wight = 0,0,0,0,0,0

    activity_wight30 = float(activity_wight) *0.4
    activity_wight7 = float(activity_wight) *0.6

    if str(infos[8]).find("&") >= 0:
        content_list = str(infos[8]).split("&")
    else:
        content_list = [infos[8]]
    try:
        if len(content_list) == 1:
            content_1 = content_list[0]
            content_2 = "无"
            # content_1_time=content_list[0].split(":")[1]
            # content_2_time = ""
        elif len(content_list) == 2:
            content_1 = content_list[0]
            content_2 = content_list[1]
            # content_1_time=content_list[0].split(":")[1]
            # content_2_time=content_list[1].split(":")[1]
        else:
            content_1 = "无"
            content_2 = "无"
            # content_1_time = ""
            # content_2_time = ""
        activity_score_7 = round(float(infos[18])*0.6,2)
        activity_score_30 = round(float(infos[18]) * 0.4, 2)
        try:
            if int(infos[3]) == 0 and int(infos[5]) == 0 and int(infos[6]) == 0:
                activity_score_7 = 0
                activity_score_30 = round(float(infos[18]),2)
            else:
                pass
        except:
            pass

        result = {'items':[{"act_detail":[{
                    "act_days30": infos[0],
                    "act_days7": infos[1],
                    "visit30": infos[2],
                    "visit7": infos[3],
                    "phone_visit30": infos[4],
                    "phone_visit7": infos[5],
                    "fast_record_7": infos[6],
                    "fast_record_30":infos[7],
                    "content30_1": content_1,
                    "content30_2": content_2,
                    # "content_1_time":content_1_time,
                    # "content_2_time":content_2_time,
                    "block_point": infos[9],
                    "approvalstatus":change_approvalstatus(infos[10]),
                    "permise": change_permise(infos[11]),
                    "close_date": infos[12],
                    "create_date": infos[13],
                    "record_score": infos[14],
                    "ms_score": infos[15],
                    "approvalstatus_score": infos[16],
                    "permise_score": infos[17],
                    "activity_score_7": activity_score_7,
                    "activity_score_30": activity_score_30,
                    "winrate":infos[20],
                    "winrate_score":infos[21],

                    "winrate_wight": round(float(winrate_wight),2),
                    "activity30_wight": round(float(activity_wight30),2),
                    "activity7_wight": round(float(activity_wight7),2),
                    "record_wight": round(float(record_wight),2),
                    "act_wight": round(float(act_wight),2),
                    "approvalstatus_wight": round(float(approvalstatus_wight),2),
                    "permise_wight": round(float(permise_wight),2),

                    "winrate_wight_all": round(float(winrate_wight), 2) *100,
                    "activity30_wight_all": round(float(activity_wight30), 2)*100,
                    "activity7_wight_all": round(float(activity_wight7), 2)*100,
                    "record_wight_all": round(float(record_wight), 2)*100,
                    "act_wight_all": round(float(act_wight), 2)*100,
                    "approvalstatus_wight_all": round(float(approvalstatus_wight), 2)*100,
                    "permise_wight_all": round(float(permise_wight), 2)*100,
                }]}]}
    except Exception as e:
        # print(e)
        result = {'items':[{"act_detail":[{}]}]}
    finally:
        cur.close()
        conn.close()
    return JsonResponse(result)



def get_oppt_info_single(request):
    oid = request.GET.get("oid")
    cur,conn = get_conn()
    data_infos = []
    try:

        sql_analysis = """ select opportunity_name,oid,score,good_label,label,win_rate,permise,close_date,
        update_time,create_date,saler,department,customer,level,
        money,sale_stage,activity_score,record_score,winrate_score,ms_score,approvalstatus_score,
        permise_score,archive_rate,customer_id,wight from opportunity_analysis where oid ="%s" """ % oid

        cur.execute(sql_analysis)
        all_infos = cur.fetchall()

        depart_dict = {}
        sql_depart = """ select id,departName from department  """
        cur.execute(sql_depart)
        depart_infos = cur.fetchall()
        for depart in depart_infos:
            depart_dict[str(depart[0])] = str(depart[1])


        for infos in all_infos:

            level,department,sale_stage=change_others(depart_dict,infos[11],infos[13],infos[15])

            wight = str(infos[24])
            try:
                winrate_wight, activity_wight, record_wight, act_wight, approvalstatus_wight, permise_wight = wight.split(";")
            except:
                winrate_wight, activity_wight, record_wight, act_wight, approvalstatus_wight, permise_wight = 0, 0, 0, 0, 0, 0

            info_dict = {
                "opportunity_name": infos[0],
                "oid": infos[1],
                "score": infos[2],
                "good_label": change_goodlabel(infos[3]),
                "label": change_badlabel(infos[4]),
                "win_rate": infos[5],
                "promise": change_permise(infos[6]),
                "close_date": infos[7],
                "update_time": infos[8],
                "create_date": infos[9],
                "saler": infos[10],
                "department": department,
                "customer": infos[12],
                "level": level,
                "money": infos[14],
                "sale_stage": sale_stage,
                "activity_score":infos[16],
                "record_score":infos[17],
                "winrate_score":infos[18],
                "ms_score": infos[19],
                "approvalstatus_score": infos[20],
                "permise_score": infos[21],
                "archive_rate": infos[22],
                "customer_id": infos[23],

                "winrate_wight":float(winrate_wight)*100,
                "activity_wight": float(activity_wight)*100,
                "record_wight": float(record_wight)*100,
                "ms_wight": float(act_wight)*100,
                "approvalstatus_wight": float(approvalstatus_wight)*100,
                "permise_wight":float(permise_wight)*100,
            }
            data_infos.append(info_dict)
        total = len(data_infos)
        page = 1
        result = {'data':{"data": data_infos, "page": page, "num": total, "total": total}, 'code': 1, 'error': '测试'}

    except Exception as e:
        result={'data':{"data": {}, "page": 0, "num": 0, "total": 0}, 'code': 1, 'error': '测试'}
    finally:
        cur.close()
        conn.close()
    return JsonResponse(result)


@login_required
def get_analysis_csv(request):
    pd.set_option('display.max_rows', None)
    depart_dict={}
    conn_33 = engine(settings.DATABASES['contract_33'])
    sql_analysis = """select opp_id,opportunity_name,win_rate,archive_rate,good_label,label,type,act_days30,act_days7,visit30,visit7,phone_visit30,phone_visit7,fast_record_30,fast_record_7,approvalstatus,permise,content30,create_date,close_date,update_time,saler,department,customer_id,customer,level,money,sale_stage from opportunity_analysis  order by score  desc LIMIT 100 """
    analysis_df = pd.read_sql_query(sql_analysis, conn_33)
    sql_depart = """ select id,departName from department  """
    depart_df = pd.read_sql_query(sql_depart, conn_33)
    for row in depart_df.itertuples():
        id = getattr(row, 'id')
        departName = getattr(row, 'departName')
        depart_dict[str(id)] = str(departName)
    #转义数据库中代码所表示的意义
    for row in analysis_df.itertuples():
        index  = getattr(row, 'Index')
        permise  = getattr(row, 'permise')
        good_label = getattr(row, 'good_label')
        label = getattr(row, 'label')
        type = getattr(row, 'type')
        level = getattr(row, 'level')
        department = getattr(row, 'department')
        sale_stage = getattr(row, 'sale_stage')


        level, department, sale_stage = change_others(depart_dict,department,level,sale_stage)
        analysis_df.set_value(index, 'type', opp_entityType.get(str(type),"---"))
        analysis_df.set_value(index, 'permise', change_permise(permise))
        analysis_df.set_value(index, 'good_label', change_goodlabel(good_label))
        analysis_df.set_value(index, 'label', change_badlabel(label))
        analysis_df.set_value(index, 'level', level)
        analysis_df.set_value(index, 'department', department)
        analysis_df.set_value(index, 'sale_stage',sale_stage)

    analysis_df = analysis_df.rename(columns={"opp_id":"商机id","opportunity_name":"商机名称","type":"商机类型","win_rate":"当前赢率","archive_rate":"商机评价","good_label":"利好标签","label":"堵点标签","act_days30":"30天秘书活跃天数","act_days7":"7天秘书活跃天数","visit30":"30天签到拜访","visit7":"7天签到拜访","phone_visit30":"30天电话拜访","phone_visit7":"7天电话拜访","fast_record_7":"7天快速记录","fast_record_30":"30天快速记录","approvalstatus":"报价单状态","permise":"销售承诺","content30":"拜访记录","create_date":"创建时间","close_date":"结单日期","update_time":"更新时间","saler":"销售负责人","department":"所属部门","customer_id":"客户id","customer":"客户名称","level":"客户级别","money":"金额","sale_stage":"销售阶段"})

    filename = "opportunity_analysis_" + str(int(time())) + "_" + str(random.randint(10000, 100000)) + ".csv"
    temp_dir = os.path.join(os.path.abspath("."), "download")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    filepath = os.path.join(temp_dir, filename)
    analysis_df.to_csv(filepath, index=False, encoding="utf_8_sig")

    with open(filepath, "rb") as f:
        content = f.read()

    response = HttpResponse(content_type='application/vnd.ms-csv', content=content)
    response['Content-Disposition'] = 'attachment;filename='+filename
    response['Content-Length'] = len(content)
    # 删除文件
    os.remove(filepath)
    return response


