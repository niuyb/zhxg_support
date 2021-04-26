#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("/var/www/crm_info/")

from interface.tools.utils import get_conn
from interface.tools.database import DB_CRM_NEW, DB_33_xgyypt
from support.base import DATABASES




custCheckbox5_dict = {
    "标准化产品-舆情秘书服务系统": 1,
    "标准化产品-智慧网评管理系统": 2,
    "标准化产品-智慧研判系统": 3,
    "标准化产品-舆情OA": 4,
    "数据服务-原始数据": 5,
    "数据服务-数据采集": 6,
    "舆情报告-数据报告": 7,
    "解决方案-本地化部署": 8,
    "解决方案-行业应用": 9,
    "数据服务-API定制": 10,
    "标准化产品-舆情专家": 11,
    "标准化产品-重点人物监控": 12,
    "智慧编++": 13,
    "数据服务-数据分析": 14,
    "标准化产品-智慧商情": 15,
    "标准化产品增项-电视监测": 16,
    "标准化产品-igraph": 17,
    "人工推送服务": 18,
    "星光智库舆情课堂": 19,
    "危机事件重点研判": 20,
    "星光数据平台": 21,
    "报告": 22,
    "标准化产品-地方网媒管理系统": 23,
    "服务一体化": 24,
    "城市领导者参阅": 25,
    "智慧舆情指挥平台": 26,
    "舆情态势感知可视化分析系统": 27,
    "星光快搜平台V1.0": 28,
    "CEM": 29,
}


class mappingDict(object):
    def __init__(self):
        # self.conn_crm, self.cur_crm = get_conn(DB_CRM_NEW)
        self.conn_crm, self.cur_crm = get_conn(DATABASES["crminfo_33"])
        self.conn_xgyypt, self.cur_xgyypt = get_conn(DB_33_xgyypt)
        # print('------------连接数据库-----------')


    def user(self):
        # 从user表拿到新、老userId、name、email的映射关系，存在字典
        sql_user = """ SELECT id,new_user_id,name,email FROM user WHERE new_user_id != '' """
        self.cur_crm.execute(sql_user)
        user_infos = self.cur_crm.fetchall()
        # print('++++++++++++++++++++', sql_user)
        user_dict = {}
        userId_name = {}
        userId_email = {}
        email_userId = {}
        for infos in user_infos:
            key = infos[1]
            user_dict[key] = infos[0]  # key是新userId，value是老userId
            key2 = infos[0]
            userId_name[key2] = infos[2]  # key是老userId，value是name
            key3 = infos[0]
            userId_email[key3] = infos[3]  # key是老userId，value是email
            key4 = infos[3]
            email_userId[key4] = infos[0]  # key是email，value是老userId

        # 从185.33 xgyypt库hr.employee表拿到员工email、istarshine_id的映射关系，存在字典
        sql_employee = """ SELECT work_email,istarshine_id FROM `hr.employee` WHERE work_email != '' """
        self.cur_xgyypt.execute(sql_employee)
        employee_infos = self.cur_xgyypt.fetchall()
        # print('++++++++++++++++++++', sql_employee)
        email_istarshineId = {}
        for infos in employee_infos:
            key = infos[0]
            email_istarshineId[key] = infos[1]  # key是email，value是istarshine_id

        self.closeMysql()
        return user_dict, userId_name, userId_email, email_userId, email_istarshineId


    def account(self):
        # 从account表拿到新、老accountId的映射关系，存在字典
        sql_account = """ SELECT id,new_account_id FROM account WHERE new_account_id != '' """
        self.cur_crm.execute(sql_account)
        account_infos = self.cur_crm.fetchall()
        # print('++++++++++++++++++++', sql_account)
        account_dict = {}
        account_dict2 = {}
        for infos in account_infos:
            key = infos[1]
            account_dict[key] = infos[0]  # key是新accountId，value是老accountId
            key1 = infos[0]
            account_dict2[key1] = infos[1]  # key是老accountId，value是新accountId

        self.closeMysql()
        return account_dict, account_dict2

    def opp(self):
        # 从opportunity表拿到新、老oppId的映射关系，存在字典
        sql_opp = """ SELECT id,new_opp_id FROM opportunity WHERE new_opp_id != '' """
        self.cur_crm.execute(sql_opp)
        opp_infos = self.cur_crm.fetchall()
        # print('++++++++++++++++++++', sql_opp)
        opp_dict = {}
        for infos in opp_infos:
            key = infos[1]
            opp_dict[key] = infos[0]  # key是新oppId，value是老oppId

        # 从opportunity表拿到新、老oppId分别与最终客户（dbcRelation1）的映射关系，存在字典
        sql_oppAcc = """ SELECT id,new_opp_id,dbcRelation1 FROM opportunity WHERE dbcRelation1 IS NOT NULL AND new_opp_id IS NOT NULL """
        self.cur_crm.execute(sql_oppAcc)
        oppAcc_infos = self.cur_crm.fetchall()
        # print('++++++++++++++++++++', sql_oppAcc)
        opp_acc = {}
        newOpp_acc = {}
        for infos in oppAcc_infos:
            opp_acc[infos[0]] = infos[2]  # key是老oppId，value是最终客户id
            newOpp_acc[infos[1]] = infos[2]  # key是新oppId，value是最终客户id

        self.closeMysql()
        return opp_dict, opp_acc, newOpp_acc


    def closeMysql(self):
        self.cur_crm.close()
        self.conn_crm.close()
        self.cur_xgyypt.close()
        self.conn_xgyypt.close()
        # print('-------------------关闭数据库---------------------')





