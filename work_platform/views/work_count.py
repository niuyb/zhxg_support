#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/9/25 9:49
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
import datetime
import json

import redis
from django.http import JsonResponse
from django.shortcuts import render

from public.config import work_count_type
from public.utils import Result, date_ms, engine
from salerVisit.utils import get_groups
from django.conf import settings
import pandas as pd

pd.set_option('display.max_rows', 1000) # 展示所有行
pd.set_option('display.max_columns', 1000) # 展示所有列
pd.set_option('display.width', 1000)


def work_count(request):
    user = request.user
    data_api = "/work_platform/count/departapi"

    # if user.has_perm("work_platform-task.TeamView"):
    return render(request, "work_platform/work_count.html",locals())
    # else:
    #     return render(request, "403.html")



def result_order_by(result_dict,order_by):
    result_list = result_dict["data"]
    result_sorted = sorted(result_list, key=lambda x:x[order_by], reverse=True)
    result_dict["data"] = result_sorted
    return result_dict
# 返回当前人下部门的所有人
def find_crm_depart(saler_rank,departId,is_super):
    conn_33 = engine(settings.DATABASES['contract_33'])
    # 政务高层
    if saler_rank == "5962898" or is_super:
        f_parent_depart_sql = """ select id from department where parentDepartId="432566" and id not in ("435633") """
        f_parent_df = pd.read_sql_query(f_parent_depart_sql, conn_33)
        f_parent_str = str(f_parent_df["id"].to_list())[1:-1]

        parent_depart_sql = """ select id from department where parentDepartId in (%s) """ % (f_parent_str)
        parent_df = pd.read_sql_query(parent_depart_sql, conn_33)
        parent_str = str(parent_df["id"].to_list())[1:-1]

        person_sql = """  select employeeCode as istarshine_id,name from user where departId in (%s) and statusInt ="1"  """ % (parent_str+","+f_parent_str)
        res_df = pd.read_sql_query(person_sql, conn_33)
        conn_33.close()
        return res_df
    # 区总
    elif saler_rank == "5962825":
        parent_depart_sql = """ select id from department where parentDepartId="%s" """ % (departId)
        parent_df = pd.read_sql_query(parent_depart_sql, conn_33)
        parent_str = str(parent_df["id"].to_list())[1:-1] + ",'"+departId+"'"

        person_sql = """  select employeeCode as istarshine_id,,name from user where departId in (%s) and statusInt ="1"  """ % (parent_str)
        res_df = pd.read_sql_query(person_sql, conn_33)
        conn_33.close()
        return res_df
    # 省总
    elif saler_rank == "5962716":
        person_sql = """  select employeeCode as istarshine_id, name from user where departId="%s" and statusInt ="1"  """ % (departId)
        res_df = pd.read_sql_query(person_sql, conn_33)
        conn_33.close()
        return res_df
    else:
        return "None"

# 2 高层 部门内各区
# 1 区  区内各省
# 0 省  省内各人
# crm部门id 查找人
def find_depart(departId):
    conn_33 = engine(settings.DATABASES['contract_33'])

    # make depart list
    parent_depart_sql = """ select id from department where parentDepartId = "%s" """ % (departId)
    parent_df = pd.read_sql_query(parent_depart_sql, conn_33)

    depart_sql = """ select departName,parentDepartId from department where id = "%s" """ % (departId)
    depart_df = pd.read_sql_query(depart_sql, conn_33)

    depart_name = str(depart_df["departName"].to_list()[0])

    parent_id = str(depart_df["parentDepartId"].to_list()[0])

    # 省级
    if parent_df.shape[0] == 0:
        depart_str = str(departId)
        if depart_str in  ["665498088571089"]:
            level = 1
        else:
            level = 0
    elif parent_id == "432566":
    # 区级
        parent_str = str(parent_df["id"].to_list())[1:-1]
        depart_str = parent_str+",'"+str(departId) +"'"
        level = 1
    else:
        f_parent_depart_sql = """ select id from department where parentDepartId="432566" and id not in ("435633") """
        f_parent_df = pd.read_sql_query(f_parent_depart_sql, conn_33)
        f_parent_str = str(f_parent_df["id"].to_list())[1:-1]

        parent_depart_sql = """ select id,departName from department where parentDepartId in (%s) """ % (f_parent_str)
        parent_df = pd.read_sql_query(parent_depart_sql, conn_33)
        depart_str = str(parent_df["id"].to_list())[1:-1] + ","+f_parent_str
        level = 2

    person_sql = """  select employeeCode as istarshine_id,name,departId from user where departId in (%s) and statusInt ="1"  """ % (depart_str)
    res_df = pd.read_sql_query(person_sql, conn_33)

    conn_33.close()
    return res_df,depart_name,level



# 暂不使用
def work_count_api(request):
    # 5962898 高层
    # 5962825 区总
    # 5962716 省总
    # 5962718 商务经理
    istar_id = request.GET.get("id")
    istarshine_id = request.user.istarshine_id
    is_super=request.user.is_superuser

    result={"data":[],"type":"saler","code":1}
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    yesterday_time = date_ms(yesterday)
    conn_xgyypt = engine(settings.DATABASES['default'])
    conn_199 = engine(settings.DATABASES['yqms2_199'])
    conn_33 = engine(settings.DATABASES['contract_33'])

    if istar_id is None:
        saler_sql = """  select employeeCode,departId,rankId from user where employeeCode="%s" and statusInt="1" """ % (istarshine_id)

    else:
        # istarshine_id = istar_id
        saler_sql = """  select employeeCode,departId,rankId from user where name="%s" and statusInt="1" """ % (istar_id)
    # 职位等级
    if not is_super:
        saler_df = pd.read_sql_query(saler_sql, conn_33)
        saler_rank = str(saler_df["rankId"].to_list()[0])
        departId = str(saler_df["departId"].to_list()[0])
        istarshine_id = str(saler_df["employeeCode"].to_list()[0])
    else:
        saler_rank="None"
        departId="None"

    count_sql = """ select istarshine_id,`type`,`number` from saler_quota_count where `date`="%s" """ %(yesterday_time)
    saler_count_df = pd.read_sql_query(count_sql, conn_xgyypt)

    if saler_rank in ["5962898","5962716","5962825"]or is_super:
        person_df = find_crm_depart(saler_rank, departId, is_super)
        saler_count_df = pd.merge(saler_count_df,person_df,how="left",on="istarshine_id")

        cansee_list_df = saler_count_df.drop_duplicates(['istarshine_id'])
        cansee_list = cansee_list_df["istarshine_id"].to_list()
        cansee_str = str(cansee_list)[1:-1]
    # 销售
    elif str(saler_rank) =="5962718":
        cansee_sql = """ select canSee from SALERCANSEENEW where saleId="%s" """ % (istarshine_id)
        cansee_df = pd.read_sql_query(cansee_sql, conn_199)
        cansee_list= eval(cansee_df.loc[0,"canSee"])
        cansee_str = cansee_df.loc[0,"canSee"][1:-1]
    else:
        return JsonResponse(result)

    user_sql = """  select istarshine_id,username from support_user_new where istarshine_id in (%s) and status="1" """ % cansee_str
    user_df = pd.read_sql_query(user_sql, conn_xgyypt)

    for istarid in cansee_list:
        depart_df = get_groups([istarid])
        if depart_df.shape[0]!=0:
            depart = depart_df.loc[0, "departments"]
        else:
            continue
        try:
            name = user_df.loc[user_df["istarshine_id"] == istarid, "username"].to_list()[0]
        except:
            continue
        result_t = {
            "account_num": 0,
            "opp_num": 0,
            "approve_num": 0,
            "order_num": 0,
            "order_back_num": 0,
            "wechat_group": 0,
            "wechat_message_num": 0,
            "kpi_num": 0,
            "visit_num": 0,
            "phone_num": 0,
            "ms_num": 0,
            "depart": depart,
            "name": name,
            "date": yesterday,
        }
        df = saler_count_df.loc[saler_count_df["istarshine_id"] == istarid]
        for row in df.itertuples():
            type = getattr(row, 'type')
            number = getattr(row, 'number')
            key = work_count_type.get(str(type))
            result_t[key] = number

        result["data"].append(result_t)

    conn_xgyypt.close()
    conn_33.close()
    conn_199.close()

    return JsonResponse(result)



#搜索查询个人
def work_per_api(request):
    is_super=request.user.is_superuser
    saler_name = request.GET.get("id")
    date = str(request.GET.get("date"))
    istar_id = request.user.istarshine_id
    conn_33 = engine(settings.DATABASES['contract_33'])
    conn_xgyypt = engine(settings.DATABASES['default'])
    conn_199 = engine(settings.DATABASES['yqms2_199'])

    result={"data":[],"type":"saler","code":1}

    if date is not None and date != "None" and date !="":
        yesterday = date
        yesterday_time = date_ms(date)
        # yesterday_time = yesterday_time - (86400000*7)

    else:
        yesterday = datetime.date.today() + datetime.timedelta(-1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        yesterday_time = date_ms(yesterday)
        # yesterday_time = yesterday_time - (86400000*7)


    if saler_name is None:
        istarshine_id  = istar_id
    else:
        try:
            # istarshine_id = istar_id
            saler_sql = """  select employeeCode from user where name="%s" and statusInt="1" """ % (saler_name)
            saler_df = pd.read_sql_query(saler_sql, conn_33)
            istarshine_id = str(saler_df["employeeCode"].to_list()[0])
        except:
            return JsonResponse(result)

    if is_super:
        cansee_list=[istarshine_id]
    else:
        cansee_sql = """ select canSee from SALERCANSEENEW where saleId="%s" """ % (istar_id)
        cansee_df = pd.read_sql_query(cansee_sql, conn_199)
        cansee_list = eval(cansee_df.loc[0, "canSee"])
        # cansee_str = cansee_df.loc[0, "canSee"][1:-1]

    count_sql = """ select istarshine_id,`type`,`number` from saler_quota_count where `date`>="%s" """ %(yesterday_time)
    saler_count_df = pd.read_sql_query(count_sql, conn_xgyypt)
    if istarshine_id in cansee_list:
        depart_df = get_groups([istarshine_id])
        if depart_df.shape[0] != 0:
            depart = depart_df.loc[0, "departments"]
        else:
            depart="暂无数据"
        result_t = {
            "account_num": 0,
            "opp_num": 0,
            "approve_num": 0,
            "order_num": 0,
            "order_back_num": 0,
            "wechat_group": 0,
            "wechat_message_num": 0,
            "kpi_num": 0,
            "visit_num": 0,
            "phone_num": 0,
            "ms_num": 0,
            "depart": depart,
            "name": saler_name,
            "date": yesterday,
        }
        df = saler_count_df.loc[saler_count_df["istarshine_id"] == istarshine_id]
        for row in df.itertuples():
            type = getattr(row, 'type')
            number = getattr(row, 'number')
            key = work_count_type.get(str(type))
            if key == "kpi_num":
                result_t[key] = number
            else:
                result_t[key] = number +result_t[key]

        result["data"].append(result_t)
    else:
        pass

    conn_xgyypt.close()
    conn_33.close()
    conn_199.close()
    return JsonResponse(result)

# 部门点击事件
def work_depart_api(request):
    # flag 1 查询部门下的所有人具体信息 只有str(1) 触发 其他都为部门汇总统计信息
    # depart id 查询部门的下级 具体统计信息
    # 不传参数 部门id 返回登录人的部门下级统计信息

    depart_id = request.GET.get("depart")
    flag = str(request.GET.get("flag"))
    date = str(request.GET.get("date"))
    order = str(request.GET.get("order","null"))

    is_super=request.user.is_superuser
    istarshine_id = request.user.istarshine_id

    result={"data":[],"type":"depart","level":"None","code":1}

    if date is not None and date != "None"and date!="":
        yesterday = date
        yesterday_time = date_ms(date)

        # yesterday_time = yesterday_time - (86400000*7)

    else:
        yesterday = datetime.date.today() + datetime.timedelta(-1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        yesterday_time = date_ms(yesterday)
        # yesterday_time = yesterday_time - (86400000*7)

    conn_xgyypt = engine(settings.DATABASES['default'])
    conn_33 = engine(settings.DATABASES['contract_33'])

    if depart_id is not None:
        pass
    elif is_super or request.user.has_perm("work_platform-task.LeaderView"):
        depart_id="432566"
    elif depart_id is None:
        try:
            saler_sql = """  select employeeCode,departId,rankId from user where employeeCode="%s" and statusInt="1" """ % (istarshine_id)
            saler_df = pd.read_sql_query(saler_sql, conn_33)
            depart_id = str(saler_df["departId"].to_list()[0])
        except:
            return JsonResponse(result)
    else:
        return JsonResponse(result)

    count_sql = """ select istarshine_id,`type`,`number` from saler_quota_count where `date` >="%s" """ % (yesterday_time)
    saler_count_df = pd.read_sql_query(count_sql, conn_xgyypt)
    if flag == "1":
        person_df  = find_crm_depart("5962716",depart_id,False)
        saler_count_df = pd.merge(person_df,saler_count_df,how="outer",on="istarshine_id")
        # 删除不是本部门的saler_quota_count 信息
        saler_count_df = saler_count_df.dropna(subset=["name"])
        # nan 转为 0
        saler_count_df = saler_count_df.fillna(0)
        cansee_list = person_df["istarshine_id"].to_list()
        for istarid in cansee_list:
            depart_df = get_groups([istarid])
            if depart_df.shape[0] != 0:
                depart = depart_df.loc[0, "departments"]
            else:
                continue
            try:
                name = saler_count_df.loc[saler_count_df["istarshine_id"] == istarid, "name"].to_list()[0]
            except:
                continue

            result_t = {
                "id":istarid,
                "account_num": 0,
                "opp_num": 0,
                "approve_num": 0,
                "order_num": 0,
                "order_back_num": 0,
                "wechat_group": 0,
                "wechat_message_num": 0,
                "kpi_num": 0,
                "visit_num": 0,
                "phone_num": 0,
                "ms_num": 0,
                "depart": depart,
                "name": name,
                "date": yesterday,
                "act_account_num":0,

            }
            df = saler_count_df.loc[saler_count_df["istarshine_id"] == istarid]
            for row in df.itertuples():
                type = getattr(row, 'type')
                number = getattr(row, 'number')
                key = work_count_type.get(str(int(type)))
                if key == "kpi_num":
                    result_t[key] = number
                else:
                    result_t[key] = number + result_t[key]

            result["data"].append(result_t)
        result["type"]="saler"
        if order == "null":
            pass
        else:
            result = result_order_by(result,order)
        return JsonResponse(result)
    else:
        pass
    if depart_id == "432566":
        parent_depart_sql = """ select id,departName from department where parentDepartId = "%s" and id not in ("435633") order by  FIELD(departName, "一大区","二大区","三大区","四大区","五大区","六大区","七大区","八大区","九大区","上海特区","行业拓展二部")""" % (depart_id)
    else:
        parent_depart_sql = """ select id from department where parentDepartId = "%s" and id not in ("435633")""" % (depart_id)

    parent_df = pd.read_sql_query(parent_depart_sql, conn_33)
    depart_list = parent_df["id"].to_list()

    if len(depart_list) == 0:
        depart_list = [depart_id]
    else:
        pass
    # level 判断 部门为各区组成的list 所以在find_depart返回的level中level+1
    # 同理 区为各省组成的list,也需要+1
    # 省级只有一个自己省,level不能加+1,所以if单独判断为0
    for depart_id in depart_list:
        saler_df,depart_name,level=find_depart(depart_id)
        saler_count_df_t = pd.merge(saler_count_df,saler_df,how="left",on="istarshine_id")
        saler_count_df_t = saler_count_df_t.dropna()
        saler_count_df_t = saler_count_df_t.drop_duplicates(['istarshine_id'])
        cansee_list = saler_count_df_t["istarshine_id"].to_list()
        level= str(level+1)
        if len(depart_list) == 1:
            level="0"
        result_t = {
            "account_num": 0,
            "opp_num": 0,
            "approve_num": 0,
            "order_num": 0,
            "order_back_num": 0,
            "wechat_group": 0,
            "wechat_message_num": 0,
            "kpi_num": 0,
            "visit_num": 0,
            "phone_num": 0,
            "ms_num": 0,
            "depart": depart_name,
            "date": yesterday,
            "depart_id":depart_id,
            "level":level,
            "act_account_num":0,
        }
        for istarid in cansee_list:
            df = saler_count_df.loc[saler_count_df["istarshine_id"] == istarid]
            person_kpi_df = df.loc[df["type"]== 7]
            if person_kpi_df.shape[0] > 0:
                person_kpi = person_kpi_df.loc[person_kpi_df["type"]== 7,"number"].max()
            else:
                person_kpi = 0
            for row in df.itertuples():
                type = getattr(row, 'type')
                number = getattr(row, 'number')
                key = work_count_type.get(str(type))
                if key == "kpi_num":
                    pass
                else:
                    result_t[key] = number + result_t[key]

            result_t["kpi_num"] += int(person_kpi)

        result["data"].append(result_t)
    conn_xgyypt.close()
    conn_33.close()
    if order == "null":
        pass
    else:
        result = result_order_by(result, order)
    return JsonResponse(result)



def count_detail_api(request):
    # 暂时未加权限

    istar_id = request.GET.get("id")
    type = request.GET.get("type")
    result={"data":[],"type":"","code":1}
    detail_redis = redis.Redis(host='192.168.187.55', port=6379, db=9)

    redis_name = "daily_" + istar_id
    type = work_count_type.get(str(type))
    detail_list = detail_redis.hget(redis_name,type)
    if detail_list:
        detail_list = json.loads(detail_list)
        result["data"] = detail_list[1:]
    else:
        result["data"] = []
    result["type"] = type

    return JsonResponse(result)


