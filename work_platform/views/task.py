#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/8/24 9:56
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
from datetime import datetime

import redis
import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from mandala.auth.decorators import permission_required
import pandas as pd
from public.config import task_belongid_dict, task_status, task_log_field, grant_type, client_id, client_secret, \
    redirect_uri, username, password
from public.utils import get_conn
import time
from sale.views.opportunity_analysis import change_badlabel, change_permise



def change_modify_infos(field,info):
    if field in ["updatedAt","planStartDate","planFinishDate","actualFinishDate",]:
        try:
            info_str = ms_date(int(info))
        except:
            info_str="无"
    elif field in ["updatedBy-label","ownerId","name","delete"]:
        info_str = info
    elif field == "status":
        info_str = task_status.get(str(info))
    elif field =="updatedBy":
        conn, cur = get_conn("192.168.185.33", "root", "1CzoOCywfJ*h", "contract")
        user_sql = """ select name from user where id="%s" """ % int(info)
        cur.execute(user_sql)
        info_str = cur.fetchone()[0]
        cur.close()
        conn.close()
    else:
        info_str = "无"

    return info_str
def change_modifytype(task_type):
    if str(task_type) == "1":
        task = "修改"
    elif str(task_type) == "0":
        task="删除"
    else:
        task="暂不支持"
    return task
def ms_date(ms_time):
    time_local  = time.localtime(ms_time/1000)
    date = time.strftime("%Y-%m-%d", time_local)
    return date
def ms_time(ms_time):
    time_local  = time.localtime(ms_time/1000)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return date
def date_ms(date):
    # timestr = '2019-01-14 15:22:18'
    datetime_obj = datetime.strptime(date, "%Y-%m-%d")
    obj_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    return obj_stamp
def time_ms(date):
    datetime_obj = datetime.strptime(date, "%Y-%m-%d %H:%M")
    obj_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    return obj_stamp
def get_token():
    session = requests.session()
    get_token_url = "https://api.xiaoshouyi.com/oauth2/token"
    try:
        post_data = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "username":username,
            "password": password,
        }
        response = json.loads(session.post(get_token_url, post_data).text)
        # id = response.get("id")
        access_token = response.get("access_token")
        # issued_at = response.get("issued_at")
        # token_type = response.get("token_type")
    except Exception as e:
        access_token=""
    return access_token
def select_leader_infos(name):
    # 销售人员   例如 左涛
    # 普通销售返回省总区总 名称 例如  庞晓格,张志辉
    # 省总返回  省总自己和区总
    # 区总 返回自己
    # 5962898 高层
    # 5962825 区总
    # 5962716 省总
    # 5962718 商务经理
    conn,cur = get_conn("192.168.185.33","root","1CzoOCywfJ*h","contract")
    leader_list = ""
    try:
        user_sql = """select rankid,departId from `user` where name="%s"  """ % (name)
        cur.execute(user_sql)
        user_ifnos = cur.fetchone()
        rankid = str(user_ifnos[0])
        departid = str(user_ifnos[1])

        if rankid in ["5962825","5962898"]:
            return name

        depart_sql = """select parentDepartId from department where id="%s"  """ % (departid)
        cur.execute(depart_sql)
        parent_depart = cur.fetchone()[0]

        leader_sql  =""" select name from `user` where departId in ("%s","%s") and rankId in ("5962825","5962716","5962898") """ %(departid,parent_depart)
        cur.execute(leader_sql)
        leader_infos = cur.fetchall()
        for leader in leader_infos:
            leader_list = leader_list+str(leader[0])+","

        return leader_list[:-1]
    except:
        return "not support"

    finally:
        cur.close()
        conn.close()



def person_task(request):
    userid=str(request.GET.get("uid"))

    if request.user.has_perm("work_platform-task.PersonView"):
        return render(request, "work_platform/task/month_task.html",locals())
    else:
        return render(request, "403.html")

def task(request):
    user = request.user
    userid=str(request.GET.get("uid"))
    departid = str(request.GET.get("depart"))
    level = str(request.GET.get("level"))

    if user.has_perm("work_platform-task.TeamView"):
        return render(request, "work_platform/task/team_task.html",locals())
    elif user.has_perm("work_platform-task.PersonView"):
        return render(request, "work_platform/task/month_task.html",locals())
    else:
        return render(request, "403.html")



# -------- 个人页面 --------
def task_oppapi(request):
    conn,cur = get_conn("192.168.185.33","root","1CzoOCywfJ*h","contract")
    conn19,cur19 = get_conn("192.168.16.199","fuser","97yu1r221pxeyt3","yqms2")
    departid = request.GET.get("depart")
    uid = request.GET.get("id")
    istarshine_id = request.user.istarshine_id
    is_super=request.user.is_superuser
    result={"data":[]}
    user = request.user
    try:
        if user.has_perm("work_platform-task.PersonView"):
            # 对部门
            if departid is not None :
                task_redis = redis.Redis(host='192.168.185.117', port=6379, db=2)
                redis_dict = task_redis.hget("department_task_detail", "departid_"+str(departid))
                depart_dict = eval(str(redis_dict))
                depart_dict = json.loads(depart_dict)

                uid_str = ""
                name_str = ""
                for depart in depart_dict:
                    if isinstance(depart, list):
                        for key in depart:
                            id = key["id"]
                            name = key["name"]
                            uid_str += "'" + str(id) + "'" + ","
                            name_str += "'" + str(name) + "'" + ","
                    elif isinstance(depart, dict):
                        id = depart["id"]
                        name = depart["name"]
                        uid_str += "'" + str(id) + "'" + ","
                        name_str += "'" + str(name) + "'" + ","
                    else:
                        pass
                name_str=name_str[:-1]
                oppid_sql = """ select entityObjectId from task where ownerId in (%s) and entityBelongId="3" """ % uid_str[:-1]
                cur.execute(oppid_sql)
                oppid_infos = cur.fetchall()
                if len(oppid_infos) > 0:
                    oppid_str = ""
                    for oppid in oppid_infos:
                        oppid_str += "'" + str(oppid[0]) + "'" + ","
                    oppid_str = oppid_str[:-1]
                else:
                    oppid_str = ""
            # 对人
            else:
                # 写入一个uid  uid来判断
                if uid is not None:
                    user_sql = """	select employeeCode from `user` where id ="%s" """ % uid
                    cur.execute(user_sql)
                    istarshine_id = cur.fetchone()[0]
                else:
                    pass
                # 不写uid depart 通过登录istartid 判断
                # 数据权限
                cansee_sql = """ select saleName,canSee from SALERCANSEENEW where saleId="%s" """ % (istarshine_id)
                cur19.execute(cansee_sql)
                canseeinfos = cur19.fetchone()
                # username = canseeinfos[0]
                cansee_list = eval(canseeinfos[1])
                if len(cansee_list) > 0:
                    cansee_str = ""
                    for cansee in cansee_list:
                        cansee_str += "'" + str(cansee) + "'" + ","
                    cansee_str = cansee_str[:-1]
                else:
                    return HttpResponse("no permission ")

                # # salerid
                user_sql = """select id,name from `user` where employeeCode in (%s) """ % cansee_str
                cur.execute(user_sql)
                userinfos = cur.fetchall()
                if len(userinfos) > 0:
                    user_str = ""
                    name_str = ""
                    for user in userinfos:
                        user_str += "'" + str(user[0]) + "'" + ","
                        name_str += "'" + str(user[1]) + "'" + ","
                    user_str = user_str[:-1]
                    name_str = name_str[:-1]
                else:
                    name_str=""
                if is_super:
                    oppid_sql = """ select entityObjectId from task where entityBelongId="3" """
                else:
                    oppid_sql = """ select entityObjectId from task where ownerId in (%s) and entityBelongId="3" """ % user_str
                cur.execute(oppid_sql)
                oppid_infos = cur.fetchall()
                if len(oppid_infos) > 0:
                    oppid_str = ""
                    for oppid in oppid_infos:
                        oppid_str += "'" + str(oppid[0]) + "'" + ","
                    oppid_str = oppid_str[:-1]
                else:
                    oppid_str = ""

            # leader_dict = {}
            # name_list = name_str.split(",")
            # for name in name_list:
            #     name = name[1:-1]
            #     leader_infos = select_leader_infos(name)
            #     leader_dict[name] = leader_infos

            if is_super and departid is None :
                task_sql = """select oid,opportunity_name,money,customer,win_rate,permise,close_date,label,saler from opportunity_analysis where oid not in(%s) and label != "" order by score desc limit 10 """ % (oppid_str)
            # elif oppid_str != "" and name_str !="":
            #     task_sql = """select oid,opportunity_name,money,customer,win_rate,permise,close_date,label from opportunity_analysis where oid not in(%s) and  label != "" and saler in (%s) order by score desc limit 10 """ % (
            #     oppid_str, name_str)
            elif oppid_str != "":
                task_sql = """select oid,opportunity_name,money,customer,win_rate,permise,close_date,label,saler from opportunity_analysis where oid not in(%s) and label != "" and saler in (%s) order by score desc limit 10 """ % (
                oppid_str, name_str)
            else:
                task_sql = """select oid,opportunity_name,money,customer,win_rate,permise,close_date,label,saler from opportunity_analysis where saler in (%s) and label != "" order by score desc limit 10 """ % (name_str)
            cur.execute(task_sql)
            infos = cur.fetchall()
            for info in infos:
                res = {
                    "oppid":info[0],
                    "oppunity_name": info[1],
                    "customer": info[3],
                    "money": info[2],
                    "win_rate": info[4],
                    "permise": change_permise(str(info[5])),
                    "badlabel": change_badlabel(str(info[7])),
                    "close_date": info[6].split(" ")[0],
                    "saler":info[8],
                    "leader_name":select_leader_infos(str(info[8]))
                }
                result["data"].append(res)
        else:
            return HttpResponse("no permission")
    except:
        pass
    finally:
        cur.close()
        conn.close()
        cur19.close()
        conn19.close()
    return JsonResponse(result)

def task_modifyapi(request):
    uid = request.GET.get("id")
    istarshine_id = request.user.istarshine_id
    is_super=request.user.is_superuser

    conn,cur = get_conn("192.168.185.33","root","1CzoOCywfJ*h","contract")
    conn19,cur19 = get_conn("192.168.16.199","fuser","97yu1r221pxeyt3","yqms2")
    result={"data":[]}
    try:
        if request.user.has_perm("work_platform-task.PersonView"):
            if uid is not None:
                user_sql = """select employeeCode from `user` where id="%s"  """ % (uid)
                cur.execute(user_sql)
                istarshine_id = cur.fetchall()[0]
            else:
                pass
            # 数据权限
            cansee_sql = """ select saleName,canSee from SALERCANSEENEW where saleId="%s" """ % (istarshine_id)
            cur19.execute(cansee_sql)
            canseeinfos = cur19.fetchone()
            # username = canseeinfos[0]
            cansee_list = eval(canseeinfos[1])
            cansee_str = ""
            if len(cansee_list) > 0:
                for cansee in cansee_list:
                    cansee_str += "'" + str(cansee) + "'" + ","
                cansee_str = cansee_str[:-1]
            # # salerid
            user_sql = """select id from `user` where employeeCode in (%s) """ % cansee_str
            cur.execute(user_sql)
            userinfos = cur.fetchall()
            user_str = ""
            if len(userinfos) > 0:
                for user in userinfos:
                    user_str += "'" + str(user[0]) + "'" + ","
                user_str = user_str[:-1]

            if is_super:
                modify_sql = """SELECT o.operate_type,o.field_name,o.operate_date,o.before_modify,o.after_modify,t.`updatedBy-label`,o.mark_id FROM operate_log o LEFT JOIN task t  ON o.mark_id=t.id WHERE o.table_name = "task"  order by updatedAt desc limit 10 """
            else:
                modify_sql = """SELECT o.operate_type,o.field_name,o.operate_date,o.before_modify,o.after_modify,t.`updatedBy-label`,o.mark_id FROM operate_log o LEFT JOIN task t  ON o.mark_id=t.id WHERE (o.table_name = "task" and  t.ownerId in (%s))  or (o.table_name = "task"  and o.modify_by in (%s)) order by updatedAt desc limit 10""" % (user_str, user_str)
            cur.execute(modify_sql)
            infos = cur.fetchall()
            for info in infos:
                modify_type = str(info[0])
                if modify_type == "1":
                    res = {
                        "operate_type": change_modifytype(info[0]),
                        "operate_user": info[5],
                        "operate_content": change_modify_infos(str(info[1]),info[3]) + "  ------>  " + change_modify_infos(str(info[1]),info[4]),
                        "operate_time": ms_date(int(info[2])),
                        "operate_field": task_log_field.get(str(info[1]),"其他"),
                    }
                    result["data"].append(res)
                elif modify_type == "0":
                    res = {
                        "operate_type": change_modifytype(info[0]),
                        "operate_user": info[5],
                        "operate_content": info[3],
                        "operate_time": ms_date(int(info[2])),
                        "operate_field": task_log_field.get(str(info[1]),"其他"),
                    }
                    result["data"].append(res)
                else:
                    return JsonResponse(result)
        else:
            return JsonResponse(result)
    except:
        return JsonResponse(result)
    finally:
        cur.close()
        conn.close()
    return JsonResponse(result)

def task_api(request):
    result={"data":[]}
    date = request.GET.get("date")
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    date_start_num = date_ms(date)
    date_end_num = 86400000 + int(date_start_num)
    is_super=request.user.is_superuser
    istarshine_id = request.user.istarshine_id
    uid = request.GET.get("id")
    conn19,cur19 = get_conn("192.168.16.199","fuser","97yu1r221pxeyt3","yqms2")
    conn,cur = get_conn("192.168.185.33","root","1CzoOCywfJ*h","contract")
    try:
        if request.user.has_perm("work_platform-task.PersonView"):
            if is_super:
                task_sql = """select taskName,planStartDate,planFinishDate,status,entityBelongId,entityObjectId,ownerId from task where planFinishDate >= "%s" and planStartDate <= "%s" """ % (
                date_start_num, date_end_num)
            else:
                if uid is not None:
                    user_sql = """select employeeCode from `user` where id="%s"  """ % (uid)
                    cur.execute(user_sql)
                    istarshine_id = cur.fetchall()[0]
                else:
                    pass
                # 数据权限
                cansee_sql = """ select saleName,canSee from SALERCANSEENEW where saleId="%s" """ % (istarshine_id)
                cur19.execute(cansee_sql)
                canseeinfos = cur19.fetchone()
                # username = canseeinfos[0]
                cansee_list = eval(canseeinfos[1])
                cansee_str = ""
                if len(cansee_list) > 0:
                    for cansee in cansee_list:
                        cansee_str += "'" + str(cansee) + "'" + ","
                    cansee_str = cansee_str[:-1]

                # # salerid
                user_sql = """select id from `user` where employeeCode in (%s) """ % cansee_str
                cur.execute(user_sql)
                userid_infos = cur.fetchall()
                user_str = ""
                if len(userid_infos) > 0:
                    for userid in userid_infos:
                        user_str += "'" + str(userid[0]) + "'" + ","
                    user_str = user_str[:-1]

                task_sql = """select taskName,planStartDate,planFinishDate,status,entityBelongId,entityObjectId,ownerId from task where ownerId in (%s) and planFinishDate >= "%s" and planStartDate <= "%s" """ % (user_str, date_start_num, date_end_num)

            cur.execute(task_sql)
            task_infos = cur.fetchall()
            if len(task_infos) > 0:
                createby_str = ""
                opp_str = ""
                account_str = ""
                ownerid_dict = {}
                opp_dict = {}
                account_dict = {}
                for task in task_infos:
                    createby_str += "'" + str(task[6]) + "'" + ","
                    belongname = task_belongid_dict.get(str(task[4]), "none")
                    if belongname == "opportunity":
                        opp_str += "'" + str(task[5]) + "'" + ","
                    elif belongname == "account":
                        account_str += "'" + str(task[5]) + "'" + ","
                    else:
                        continue
                createby_str = createby_str[:-1]
                opp_str = opp_str[:-1]
                account_str = account_str[:-1]

                # # createby_infos
                createby_sql = """ select name,id from `user` where id in (%s)  """ % createby_str
                cur.execute(createby_sql)
                createby_user_list = cur.fetchall()
                for create in createby_user_list:
                    ownerid_dict[str(create[1])] = create[0]

                # # oppinfos
                if len(opp_str) > 0:
                    opp_sql = """ select opportunity_name,oid from opportunity_analysis where oid in (%s) """ % opp_str
                    cur.execute(opp_sql)
                    opp_infos_list = cur.fetchall()
                    for opp in opp_infos_list:
                        opp_dict[str(opp[1])] = opp[0]
                else:
                    opp_dict = {}

                # # accountinfos
                if len(account_str) > 0:
                    account_sql = """ select accountName,id from account where id in (%s) """ % account_str
                    cur.execute(account_sql)
                    account_infos_list = cur.fetchall()
                    for account in account_infos_list:
                        account_dict[str(account[1])] = account[0]
                else:
                    account_dict = {}

                for task in task_infos:
                    business_type = ""
                    start_date = ms_time(int(task[1]))
                    finish_date = ms_time(int(task[2]))
                    status = task_status.get(str(task[3]), "暂无数据")
                    type = task_belongid_dict.get(str(task[4]), "None")
                    if type == "account":
                        business_name = account_dict.get(str(task[5]), "无关联")
                        business_type = "客户___"
                    elif type == "opportunity":
                        business_name = opp_dict.get(str(task[5]), "无关联")
                        business_type = "商机___"
                    else:
                        business_name = "无关联"
                        business_type = "其他___"

                    task_dict = {
                        "task_name": task[0],
                        "start_date": start_date,
                        "finish_date": finish_date,
                        "status": status,
                        "content": business_type + business_name,
                        "owner": ownerid_dict.get(str(task[6]), "系统分配"),

                    }
                    result["data"].append(task_dict)
            else:
                return JsonResponse(result)
        else:
            return HttpResponse("no permission")
    except:
        return HttpResponse("task error")
    finally:
        cur.close()
        conn.close()
        cur19.close()
        conn19.close()

    return JsonResponse(result)

def add_task_api(request):
    if request.user.has_perm("work_platform-task.PersonView"):
        result = {"res": "failed"}
        conn, cur = get_conn("192.168.185.33", "root", "1CzoOCywfJ*h", "contract")
        try:
            # istarshine_id = request.user.istarshine_id
            taskName= request.GET.get("taskName")
            FinishDate= request.GET.get("planFinishDate")
            StartDate= request.GET.get("planStartDate")
            ownerId= request.GET.get("ownerId")
            startReminder= request.GET.get("startReminder")
            finishReminder= request.GET.get("finishReminder")
            entityBelongId= request.GET.get("entityBelongId")
            entityObjectId= request.GET.get("entityObjectId")
            description= request.GET.get("description")
            memberIds= request.GET.get("memberIds")

            planFinishDate = time_ms(FinishDate)
            planStartDate = time_ms(StartDate)

            member_list = memberIds.split(",")
            member_str = ""
            for member in member_list:
                member_str += "'" + str(member) + "'" + ","
            user_sql = """select id,name from `user` where name in ("%s",%s) """ % (ownerId,member_str[:-1])
            cur.execute(user_sql)
            uid_str=""
            uid_infos = cur.fetchall()
            for uid_info in uid_infos:
                if str(uid_info[1]) == ownerId:
                        uid = uid_info[0]
                else:
                    uid_str+= str(uid_info[0])+','
            uid_str = uid_str[:-1]
            if entityBelongId == "1":
                return HttpResponse("not support account")
            elif entityBelongId == "3":
                entityObjectId = entityObjectId
            else:
                entityObjectId=""

            try:
                session = requests.session()
                access_token = get_token()
                session.headers["Authorization"] = "Bearer "+access_token
                session.headers["Content-Type"] = "application/json"
                get_create_task_url="https://api.xiaoshouyi.com/rest/data/v2.0/xobjects/task/actions/createTaskWithMember"

                post_data = {"taskName": taskName,
                             "planFinishDate": planFinishDate,
                             "planStartDate": planStartDate,
                             "ownerId": uid,
                             "startReminder": startReminder,
                             "finishReminder": finishReminder,
                             "entityBelongId": entityBelongId,
                             "entityObjectId": entityObjectId,
                             "memberIds": uid_str,
                             "description": description
                             }
                # if startReminder is None:
                #     post_data.pop("startReminder")
                # if finishReminder is None:
                #     post_data.pop("finishReminder")

                post_data_j = json.dumps(post_data)
                response = session.post(get_create_task_url, post_data_j)
                res = response.content
                res_dict = json.loads(res)
                res_code = res_dict["code"]
                res_msg = res_dict["code"]

                if str(res_code) == "200" or str(res_msg) == "OK":
                    # res_taskid = res_dict["result"]["taskId"]
                    result = {"res": "success"}
                else:
                    pass
            except:
                return HttpResponse("crmapi error")
        except:
            pass
        finally:
            cur.close()
            conn.close()
    else:
        return HttpResponse("no permission")

    return JsonResponse(result)


# -------- 团队页面 --------
# region 区总
#province 省总
def team_pei_api(request):
    # 0 任务为0
    # 1 任务为任务数大于0小于5
    # 2 任务为大于5
    istarshine_id = request.user.istarshine_id
    user = request.user
    type = request.GET.get("type")
    depart = request.GET.get("depart")
    result={"data":[],"top":{}}
    conn,cur = get_conn("192.168.185.33","root","1CzoOCywfJ*h","contract")
    task_redis = redis.Redis(host='192.168.185.117', port=6379, db=2)
    task_infos_pd = pd.DataFrame(columns=('id', 'name', 'employeeCode', 'departId', 'task_num', 'account_num', 'delay_num', 'delete_num', 'complete_num','cover_num'))

    try:
        if depart is not None:
            departid = depart
        else:
            try:
                department_sql = """  select departId,name from user where employeeCode="%s"  """ % (istarshine_id)
                cur.execute(department_sql)
                depart_str = cur.fetchone()
                departid = depart_str[0]
                u_name = depart_str[1]
            except:
                pass
            if user.has_perm("work_platform-task.LeaderView"):
                departid = "432566"
                u_name = "政务管理员"

        if user.has_perm("work_platform-task.LeaderView") and depart is None:
            task_dict = task_redis.hgetall("department_task_detail")
            for key,value in task_dict.items():
                saler_infos = json.loads(value)
                for key in saler_infos:
                    if isinstance(key, list):
                        for k in key:
                            task_infos_pd = task_infos_pd.append(k, ignore_index=True)
                    elif isinstance(key, dict):
                        task_infos_pd = task_infos_pd.append(key, ignore_index=True)
        else:
            task_dict = task_redis.hget("department_task_detail", "departid_" + departid)
            task_dict = json.loads(task_dict)
            for key in task_dict:
                if isinstance(key,list):
                    for k in key :
                        task_infos_pd = task_infos_pd.append(k, ignore_index=True)
                elif isinstance(key,dict):
                    task_infos_pd = task_infos_pd.append(key, ignore_index=True)
        # 去重
        task_infos_pd.drop_duplicates(subset=['id','employeeCode'],keep='first',inplace=True)
        task_pd_t = task_infos_pd[task_infos_pd['task_num'] == 0]
        task_0 = task_pd_t[task_pd_t['depart_name'].notnull()]
        total_0 = task_0.shape[0]

        task_pd_t = task_infos_pd[task_infos_pd['task_num'] > 0]
        task_pd_t = task_pd_t[task_pd_t['task_num'] < 5]
        task_1 = task_pd_t[task_pd_t['depart_name'].notnull()]
        total_1 = task_1.shape[0]

        task_pd_t = task_infos_pd[task_infos_pd['task_num'] >= 5]
        task_2 = task_pd_t[task_pd_t['depart_name'].notnull()]
        total_2 = task_2.shape[0]

        if type is not None:
            if int(type) == 0:
                task = task_0
            elif int(type) == 1:
                task = task_1
            elif int(type) == 2:
                task = task_2
            else:
                return JsonResponse(result)

            for salerid in task["id"]:
                person_infos = task_redis.hget("team_task", "userid_" + str(salerid))
                result["data"].append(json.loads(person_infos))
        else:
            pass

        # try:
        if depart is not None:
            parentid_sql = """  select departName from department where id="%s"  """ % departid
            cur.execute(parentid_sql)
            departName = cur.fetchone()[0]

            try:
                department_sql = """select name from user where departId="%s" and  rankId in ('5962716','5962825','5962898')""" %(departid)
                cur.execute(department_sql)
                u_name = cur.fetchone()[0]
            except:
                # 本层级部门没有找下级
                try:
                    department_sql = """select id from department where parentDepartId="%s" """ % (departid)
                    cur.execute(department_sql)
                    departid_str = cur.fetchone()[0]
                    department_sql = """select name from user where departId="%s" and  rankId in ('5962716','5962825','5962898')""" %(departid_str)
                    cur.execute(department_sql)
                    u_name = cur.fetchone()[0]
                except :
            #         下级没有找上级
                    department_sql = """select parentDepartId from department where id="%s" """ % (departid)
                    cur.execute(department_sql)
                    departid_str = cur.fetchone()[0]
                    department_sql = """select name from user where departId="%s" and  rankId in ('5962716','5962825','5962898')""" %(departid_str)
                    cur.execute(department_sql)
                    u_name = cur.fetchone()[0]


            redis_dict=task_redis.hget("department_task", "departid_432566")
            depart_dict = eval(str(redis_dict))
            depart_dict = json.loads(depart_dict)
            task_num = int(depart_dict[departid]["task_num"])
            saler_num = int(depart_dict[departid]["saler_num"])
            result["top"] = {
                "name":u_name,
                "departName":departName,
                "task_num":task_num,
                "saler_num":round(task_num/saler_num,2),
                "total_0": total_0,
                "total_1": total_1,
                "total_2": total_2,
            }

        else:

            parentid_sql = """  select departName from department where id="%s"  """ % departid
            cur.execute(parentid_sql)
            departName = cur.fetchone()[0]

            redis_dict=task_redis.hget("department_task", "departid_432566")
            depart_dict = eval(str(redis_dict))
            depart_dict = json.loads(depart_dict)
            task_num = int(depart_dict[departid]["task_num"])
            saler_num = int(depart_dict[departid]["saler_num"])
            result["top"] = {
                "name":u_name,
                "departName":departName,
                "task_num":task_num,
                "saler_num":round(task_num/saler_num,2),
                "total_0": total_0,
                "total_1": total_1,
                "total_2": total_2,

            }
    except:
        pass

    finally:
        cur.close()
        conn.close()

    return JsonResponse(result)

def team_department_api(request):
    # flag 进入那一层   跳链只涉及 1 0
    # 2 高层
    # 1 区总
    # 0 省总
    depart = request.GET.get("depart")
    level = request.GET.get("level")
    result={"data":[],"type":'saler'}
    user = request.user
    flag = 0
    # is_super=request.user.is_superuser
    istarshine_id = request.user.istarshine_id
    # user_roles = list(request.user.roles.values_list("code",flat=True))
    conn,cur = get_conn("192.168.185.33","root","1CzoOCywfJ*h","contract")
    try:
        if depart is None:
            try:
                department_sql = """  select departId from user where employeeCode="%s"  """ %(istarshine_id)
                cur.execute(department_sql)
                departid = cur.fetchone()[0]
            except:
                pass
        else:
            departid = depart

        task_redis = redis.Redis(host='192.168.185.117', port=6379, db=2)
        if depart is None and level is None:
            if user.has_perm("work_platform-task.LeaderView"):
                flag = 2
            elif user.has_perm("work_platform-task.RegionView"):
                flag = 1
            elif user.has_perm("work_platform-task.ProvinceView"):
                flag = 0
            else:
                return JsonResponse(result)
        elif depart is not None and level is not None:
            if user.has_perm("work_platform-task.RegionView") and level == "1":
                flag = 1
            elif user.has_perm("work_platform-task.ProvinceView") and level == "0":
                flag = 0
            else:
                return JsonResponse(result)
        else:
            return JsonResponse(result)

        # 部门 没有区级概念
        if depart is not None and str(departid) in ["665498088571089"]:
            flag = 0
        # 各大区
        if flag == 2:
            result["type"]="department"
            parentid_sql ="""  select id,departName from department where parentDepartId="432566"  """
            cur.execute(parentid_sql)
            department_infos = cur.fetchall()
            redis_dict = task_redis.hget("department_task", "departid_432566")
            depart_dict = eval(str(redis_dict))
            depart_dict = json.loads(depart_dict)
            for department_id in department_infos:
                res = {
                    "id": department_id[0],
                    "employeeCode": "",
                    "name": "",
                    "departId": department_id[0],
                    "task_num": depart_dict.get(str(department_id[0]))["task_num"],
                    "account_num": depart_dict.get(str(department_id[0]))["account_num"],
                    "delay_num": depart_dict.get(str(department_id[0]))["delay_num"],
                    "delete_num": depart_dict.get(str(department_id[0]))["delete_num"],
                    "complete_num": depart_dict.get(str(department_id[0]))["complete_num"],
                    "cover_num": depart_dict.get(str(department_id[0]))["cover_num"],
                    "depart_name": department_id[1],
                }
                result["data"].append(res)
        # 各省
        elif flag == 1:
            result["type"]="region"
            parentid_sql ="""  select id,departName from department where parentDepartId="%s"  """ %(departid)
            cur.execute(parentid_sql)
            department_infos = cur.fetchall()
            redis_dict = task_redis.hget("department_task", "departid_432566")
            depart_dict = eval(str(redis_dict))
            depart_dict = json.loads(depart_dict)
            for department_id in department_infos:
                res = {
                    "id": department_id[0],
                    "employeeCode": "",
                    "name": "",
                    "departId": department_id[0],
                    "task_num": depart_dict.get(str(department_id[0]))["task_num"],
                    "account_num": depart_dict.get(str(department_id[0]))["account_num"],
                    "delay_num": depart_dict.get(str(department_id[0]))["delay_num"],
                    "delete_num": depart_dict.get(str(department_id[0]))["delete_num"],
                    "complete_num": depart_dict.get(str(department_id[0]))["complete_num"],
                    "cover_num": depart_dict.get(str(department_id[0]))["cover_num"],
                    "depart_name": department_id[1],
                }
                result["data"].append(res)
        # 各人
        elif flag == 0:
            result["type"]="province"
            redis_dict=task_redis.hget("department_task_detail","departid_"+departid)
            depart_dict = eval(str(redis_dict))
            depart_list = json.loads(depart_dict)
            for saler in depart_list:
                res = {
                    # 省id
                    "id": saler["id"],
                    "name":saler["name"],
                    "employeeCode": saler["employeeCode"],
                    # 各人所属部门id
                    "departId": saler["departId"],
                    "task_num": saler["task_num"],
                    "account_num": saler["account_num"],
                    "delay_num": saler["delay_num"],
                    "delete_num": saler["delete_num"],
                    "complete_num": saler["complete_num"],
                    "cover_num": saler["cover_num"],
                    "depart_name": saler["depart_name"],
                }
                result["data"].append(res)

        else:
            pass
    except:
        return HttpResponse("team_department_api error")

    finally:
        cur.close()
        conn.close()

    return JsonResponse(result)







