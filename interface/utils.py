import json
import datetime
import hashlib
import logging

import pandas as pd
import requests

from customer.models import Crmaccountsalemapping, Crmsalemapping
from customer.utils import get_team_opp_data, get_opp_data
from interface.tools.database import DB_CRM_NEW, DB_199_yqms2
from interface.tools.utils import engine, get_conn, timestamp13_to_str, more_split
from interface.tools.mapping import custCheckbox5_dict, mappingDict
from support.base import DATABASES

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)




"""将数据进行处理，写入数据库account表"""
def update_acc(data):
    data = data


    # conn = engine(DB_CRM_NEW)
    conn = engine(DATABASES["crminfo_33"])

    if (type(data) == list) and (len(data) > 0):
        #用pandas将数据写入数据库
        data_df = pd.DataFrame(data)    # 将列表转为df数据格式

        # try:
        #     data_df = data_df.drop(columns=['crm_id'])    # 丢掉crm_id列
        # except:
        #     pass
        #添加一列
        data_df.insert(data_df.shape[1], 'update_timestamp', '')
        data_df = data_df.rename(columns={'id': 'new_account_id',
                                          'xsy_id': 'id',
                                          'owner_id': 'ownerId',
                                          'account_name': 'accountName',
                                          'created_at': 'createdAt',
                                          'address_province': 'fState',
                                          'address_city': 'fCity',
                                          'address_area': 'fDistrict',
                                          'industry_1': 'dbcSelect5',
                                          'industry_2': 'dbcSelect9',
                                          'sea_status': 'highSeaStatus',
                                          'contact_phone': 'dbcVarchar2',
                                          'recent_activity_time': 'recentActivityRecordTime'
                                          })   # 接口获取的字段名和数据库存储的字段名不一致，需要将字段名重命名为account表对应的字段名

        # 将highSeaStatus的值从字符串替换为代号，和老数据保持一致
        data_df.highSeaStatus[data_df['highSeaStatus'] == '自建'] = 1
        data_df.highSeaStatus[data_df['highSeaStatus'] == '未领取'] = 2
        data_df.highSeaStatus[data_df['highSeaStatus'] == '已领取'] = 3
        data_df.highSeaStatus[data_df['highSeaStatus'] == '已签约'] = 4
        data_df.highSeaStatus[data_df['highSeaStatus'] == '已废弃'] = 5
        data_df.highSeaStatus[data_df['highSeaStatus'] == '已冻结'] = 6

        # 将level的值从字符串替换为代号，和老数据保持一致
        data_df.level[data_df['level'] == '重点客户'] = 1
        data_df.level[data_df['level'] == '开发客户'] = 4
        data_df.level[data_df['level'] == '正式客户'] = 5

        # conn2,cur2 = get_conn(DB_CRM_NEW)
        conn2, cur2 = get_conn(DATABASES["crminfo_33"])
        # 将dbcSelect5（一级行业）的值从字符串替换为代号，和老数据保持一致
        sql_industry_l1 = """ SELECT id,name FROM crm_industry_l1 """
        cur2.execute(sql_industry_l1)
        industry_l1 = cur2.fetchall()
        for infos in industry_l1:
            data_df.dbcSelect5[data_df['dbcSelect5'] == infos[1]] = infos[0]
        # 将dbcSelect9(二级行业)的值从字符串替换为代号，和老数据保持一致
        sql_industry_l2 = """ SELECT id,name FROM crm_industry_l2 """
        cur2.execute(sql_industry_l2)
        industry_l2 = cur2.fetchall()
        for infos in industry_l2:
            data_df.dbcSelect9[data_df['dbcSelect9'] == infos[1]] = infos[0]
        # 将fState的值从字符串替换为代号，和老数据保持一致
        sql_state = """ SELECT lid,lname FROM crm_location_State """
        cur2.execute(sql_state)
        state_infos = cur2.fetchall()
        for infos in state_infos:
            data_df.fState[data_df['fState'] == infos[1]] = infos[0]


        # 将City映射信息存为字典，key为lname和pid拼接的字符串（唯一），value为对应的代号
        sql_city = """ SELECT lid,lname,pid FROM crm_location_City """
        cur2.execute(sql_city)
        city_infos = cur2.fetchall()
        city_dict = {}
        for infos in city_infos:
            unique = infos[1]+str(infos[2])     # 将lname和pid拼在一起，才可作为唯一标识
            city_dict[unique] = infos[0]

        # 将District映射信息存为字典，key为lname和pid拼接的字符串（唯一），value为对应的代号
        sql_district = """ SELECT lid,lname,pid FROM crm_location_District """
        cur2.execute(sql_district)
        district_infos = cur2.fetchall()
        district_dict = {}
        for infos in district_infos:
            unique = infos[1] + str(infos[2])     # 将lname和pid拼在一起，才可作为唯一标识
            district_dict[unique] = infos[0]


        # 从user表拿到新、老ownerId的映射关系，存在字典（因为信息部的接口给的ownerId是新ownerId，但是account表需且仅需老ownerId）
        sql_owner = """ SELECT id,new_user_id FROM user WHERE new_user_id != '' """
        cur2.execute(sql_owner)
        owner_infos = cur2.fetchall()
        owner_dict = {}
        for infos in owner_infos:
            key = infos[1]
            owner_dict[key] = infos[0]  # key是新ownerId，value是老ownerId

        # 从account表查询所有id和new_account_id
        select_old_info_sql = """ SELECT id,new_account_id FROM account """
        cur2.execute(select_old_info_sql)
        select_old_infos = cur2.fetchall()
        all_id_list = []
        all_newId_list = []
        for infos in select_old_infos:
            all_id_list.append(infos[0])
            all_newId_list.append(infos[1])

        delete_id_list = []
        delete_newId_list = []
        account_id_list = []
        account_newId_list = []

        # 遍历接口获取的数据
        for index, row in data_df.iterrows():
            # 判断id或new_account_id是否在数据表存在，若存在则先记下来
            if row["id"] in all_id_list:
                delete_id_list.append(row["id"])
            if row["new_account_id"] in all_newId_list:
                delete_newId_list.append(row["new_account_id"])

            # 将fCity的值从字符串替换为代号，和老数据保持一致
            if not pd.isna(row["fCity"]):
                # 特殊处理address_city填写为海南省的情况
                if row["fCity"] == '海南省':
                    row["fCity"] = '省直辖县级行政区划'
                city_unique = row["fCity"] + str(row["fState"])
                try:
                    row["fCity"] = city_dict[city_unique]
                except:
                    # print("fCity error:", row)
                    row["fCity"] = None

            # 将fDistrict的值从字符串替换为代号，和老数据保持一致
            if not pd.isna(row["fDistrict"]):
                district_unique = row["fDistrict"] + str(row["fCity"])
                try:
                    row["fDistrict"] = district_dict[district_unique]
                except:
                    # print("fDistrict error:", row)
                    row["fDistrict"] = None

            # 接口给的createdAt是毫秒级时间戳，需要转换为"%Y-%m-%d %H:%M"格式
            if not pd.isna(row["createdAt"]):
                createdAt_int = int(row["createdAt"])
                row["createdAt"] = timestamp13_to_str(createdAt_int, format_str="%Y-%m-%d %H:%M")

            # 接口给的recentActivityRecordTime是毫秒级时间戳，需要转换为"%Y-%m-%d %H:%M"格式
            if not pd.isna(row["recentActivityRecordTime"]):
                try:
                    recentActivityRecordTime_int = int(row["recentActivityRecordTime"])
                    row["recentActivityRecordTime"] = timestamp13_to_str(recentActivityRecordTime_int, format_str="%Y-%m-%d %H:%M")
                except:
                    row["recentActivityRecordTime"] = None

            # 用老ownerId替换接口给的新ownerId
            if not pd.isna(row["ownerId"]):
                try:
                    new_ownerId = row["ownerId"]
                    row["ownerId"] = owner_dict[new_ownerId]    # 把老的ownerId赋值给row["ownerId"]
                except:
                    row["ownerId"] = None

            # 当老id为空时，生成一个老id，规则：有新id时用新id拼接old，没有新id时用name加密
            if pd.isna(row["id"]) or (row["id"] == "None") or (row["id"] == "#N/A"):
                if not pd.isna(row["new_account_id"]):
                    row["id"] = row["new_account_id"] + 'old'
                else:
                    row["id"] = hashlib.md5(row['accountName'].encode(encoding='UTF-8')).hexdigest()

            # 当行业映射表没有接口返回的一级行业时，把这个行业的代号置为None
            if type(row["dbcSelect5"]) != int:
                row["dbcSelect5"] = None

            # 当行业映射表没有接口返回的二级行业时，把这个行业的代号置为None
            if type(row["dbcSelect9"]) != int:
                row["dbcSelect9"] = None

            # 当没有映射关系时，把代号置为None
            if type(row["level"]) != int:
                row["level"] = None

            # 当没有映射关系时，把代号置为None
            if type(row["highSeaStatus"]) != int:
                row["highSeaStatus"] = None
            #同步时间
            row["update_timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            account_id_list.append(row["id"])
            account_newId_list.append(row["new_account_id"])
            data_df.iloc[index] = row  # iterrows只对原始数据进行copy，不会修改原始数据，所以需要将处理后的结果重新赋值给原始df





        # 如果数据库已经存在某些接口返回的记录（判断条件为：存在相同的id或new_account_id），则将其在数据库删除
        delete_id_tuple = tuple(delete_id_list)
        delete_newId_tuple = tuple(delete_newId_list)
        try:
            if delete_id_tuple:
                old_info_sql = """ DELETE FROM account WHERE id IN %s """
                cur2.execute(old_info_sql, (delete_id_tuple,))
                conn2.commit()
                # print('delete_id_tuple不为空元组')

            if delete_newId_tuple:
                old_info_sql = """ DELETE FROM account WHERE new_account_id IN %s """
                cur2.execute(old_info_sql, (delete_newId_tuple,))
                conn2.commit()
                # print('delete_newId_tuple不为空元组')

            # print("----完成删除----")
        except:
            # print("----没有需要删除的重复数据----")
            pass

        data_df = data_df[['id', 'ownerId', 'accountName', 'fState', 'fCity', 'fDistrict', 'createdAt',
             'dbcSelect5', 'dbcSelect9', 'level','highSeaStatus','dbcVarchar2','recentActivityRecordTime','new_account_id', 'crm_id', 'update_timestamp']]

        # data_df内部根据id字段去重，保留最后一条数据
        data_df = data_df.drop_duplicates(['id'], keep="last")

        # print(data_df)
        total = len(data_df)
        # 将数据写入数据库

        print(data_df)
        try:
            data_df.to_sql('account', conn, index=False, if_exists='append')
            result = {'message': "客户信息更新成功！", 'total': total, 'id': account_id_list, 'newId': account_newId_list}
        except:
            result = {'message': "客户信息更新失败！", 'total': total, 'id': account_id_list, 'newId': account_newId_list}

        cur2.close()
        conn2.close()
    elif data is None:
        result = {'message': "客户信息获取成功，客户为空！"}
    else:
        # print(data)
        result = {'message': "客户信息获取失败！"}
    finish_time = datetime.datetime.now()
    # print("---------------------------------------finish_time:", finish_time)
    conn.close()
    return result



"""将数据进行处理，写入数据库opportunity表"""
def update_opp(data):
    data = data
    # conn = engine(DB_CRM_NEW)
    conn = engine(DATABASES["crminfo_33"])

    if (type(data) == list) and (len(data) > 0):

        #用pandas将数据写入数据库
        data_df = pd.DataFrame(data)    # 将列表转为df数据格式
        try:
            data_df = data_df.drop(columns=['crm_id'])    # 丢掉crm_id列
        except:
            # print("----商机增量更新接口返回结果已经去掉'crm_id'列----")
            pass
        data_df = data_df.rename(columns={'id': 'new_opp_id',
                                          'xsy_id': 'id',
                                          'owner_id': 'ownerId',
                                          'opportunity_name': 'opportunityName',
                                          'account_id': 'dbcRelation1',     # 最终客户的id
                                          'saler_promise': 'dbcSelect26',
                                          'intended_product': 'custCheckbox5',
                                          'close_date': 'closeDate',
                                          'sale_stage': 'saleStageId',
                                          'phone': 'dbcJoin10',
                                          })   # 接口获取的字段名和数据库存储的字段名不一致，需要将字段名重命名为opportunity表对应的字段名

        # 将closeDate列的数据类型转为str类型(之前是str类型也可)
        data_df['closeDate'] = data_df['closeDate'].apply(str)

        # 将saleStageId的值从字符串替换为代号，和老数据保持一致
        data_df.saleStageId[data_df['saleStageId'] == '产品新单-潜在商机(新)'] = 1172739
        data_df.saleStageId[data_df['saleStageId'] == '产品新单-商机确认(新)'] = 1172741
        data_df.saleStageId[data_df['saleStageId'] == '产品新单-商务谈判(新)'] = 1186830
        data_df.saleStageId[data_df['saleStageId'] == '产品新单-合同确认(新)'] = 1172743
        data_df.saleStageId[data_df['saleStageId'] == '产品新单-赢单（新）'] = 1209860
        data_df.saleStageId[data_df['saleStageId'] == '产品新单-输单(新)'] = 1172744
        data_df.saleStageId[data_df['saleStageId'] == '产品续单-商机确认（续）'] = 1186615
        data_df.saleStageId[data_df['saleStageId'] == '产品续单-商务谈判（续）'] = 1197988
        data_df.saleStageId[data_df['saleStageId'] == '产品续单-合同确认（续）'] = 1186616
        data_df.saleStageId[data_df['saleStageId'] == '产品续单-赢单（续）'] = 1595051
        data_df.saleStageId[data_df['saleStageId'] == '产品续单-输单（续）'] = 1186617
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-初步沟通（项目）'] = 1723501
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-意向客户（项目）'] = 1723502
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-商机确认（项目）'] = 1723701
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-需求确认（项目）'] = 1723503
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-商务谈判（项目）'] = 1723504
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-合同确认（项目）'] = 1723003
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-赢单（项目）'] = 1723505
        data_df.saleStageId[data_df['saleStageId'] == '项目型业务-输单（项目）'] = 1723506
        data_df.saleStageId[data_df['saleStageId'] == '星光数据-初步沟通（数据）'] = 1850762
        data_df.saleStageId[data_df['saleStageId'] == '星光数据-需求确认（数据）'] = 1850763
        data_df.saleStageId[data_df['saleStageId'] == '星光数据-商务谈判（数据）'] = 1850764
        data_df.saleStageId[data_df['saleStageId'] == '星光数据-合同确认（数据）'] = 1850765
        data_df.saleStageId[data_df['saleStageId'] == '星光数据-赢单（数据）'] = 1850766
        data_df.saleStageId[data_df['saleStageId'] == '星光数据-输单（数据）'] = 1850767

        data_df.saleStageId[data_df['saleStageId'] == '1-建立信任阶段'] = 1850768
        data_df.saleStageId[data_df['saleStageId'] == '2-商业调研阶段'] = 1850769
        data_df.saleStageId[data_df['saleStageId'] == '3-业案&商案准备'] = 1850770
        data_df.saleStageId[data_df['saleStageId'] == '4-方案验证&汇报'] = 1850771
        data_df.saleStageId[data_df['saleStageId'] == '5-商务竞争阶段'] = 1850772
        data_df.saleStageId[data_df['saleStageId'] == '6-合同交互阶段'] = 1850773
        data_df.saleStageId[data_df['saleStageId'] == '7-合同签署阶段'] = 1850774
        data_df.saleStageId[data_df['saleStageId'] == '8-合同归档阶段'] = 1850775
        data_df.saleStageId[data_df['saleStageId'] == '8-输单'] = 1850776
        data_df.saleStageId[data_df['saleStageId'] == '9-无效'] = 1850777


        # 将dbcSelect26(销售确认)的值从字符串替换为代号，和老数据保持一致
        data_df.dbcSelect26[data_df['dbcSelect26'] == '承诺 '] = 1
        data_df.dbcSelect26[data_df['dbcSelect26'] == '争取'] = 4
        data_df.dbcSelect26[data_df['dbcSelect26'] == '跟进中'] = 2
        data_df.dbcSelect26[data_df['dbcSelect26'] == '否'] = 0


        # 从user表拿到新、老ownerId的映射关系，存在字典（因为信息部的接口给的ownerId是新ownerId，但是opportunity表需且仅需老ownerId）
        # conn2, cur2 = get_conn(DB_CRM_NEW)
        conn2, cur2 = get_conn(DATABASES["crminfo_33"])
        sql_owner = """ SELECT id,new_user_id FROM user WHERE new_user_id != '' """
        cur2.execute(sql_owner)
        owner_infos = cur2.fetchall()
        owner_dict = {}
        for infos in owner_infos:
            key = infos[1]
            owner_dict[key] = infos[0]  # key是新ownerId，value是老ownerId

        # 从account表拿到新、老accountId的映射关系，存在字典（因为信息部的接口给的account_id是新accountId，但是opportunity表需且仅需老accountId）
        sql_account = """ SELECT id,new_account_id FROM account WHERE new_account_id != '' """
        cur2.execute(sql_account)
        account_infos = cur2.fetchall()
        account_dict = {}
        for infos in account_infos:
            key = infos[1]
            account_dict[key] = infos[0]  # key是新accountId，value是老accountId

        # 从opportunity表查询所有id和new_account_id
        select_old_info_sql = """ SELECT id,new_opp_id FROM opportunity """
        cur2.execute(select_old_info_sql)
        select_old_infos = cur2.fetchall()
        all_id_list = []
        all_newId_list = []
        for infos in select_old_infos:
            all_id_list.append(infos[0])
            all_newId_list.append(infos[1])

        delete_id_list = []
        delete_newId_list = []
        opp_id_list = []

        # 遍历接口获取的数据
        for index, row in data_df.iterrows():
            # 判断id或new_account_id是否在数据表存在，若存在则先记下来
            if row["id"] in all_id_list:
                delete_id_list.append(row["id"])
            if row["new_opp_id"] in all_newId_list:
                delete_newId_list.append(row["new_opp_id"])

            # 接口给的custCheckbox5是文字（一组产品名，用英文逗号或英文分号分隔的），需要转换成对应的数字（一组数字）
            try:
                row["custCheckbox5"] = "".join(row["custCheckbox5"].split())    # 去掉字符串中的\xa0
                pro_name_list = more_split(row["custCheckbox5"])    # 将"产品1,产品2;产品3"转换为[产品1,产品2,产品3]
                pro_id_list = []
                for pro_name in pro_name_list:
                    try:
                        pro_id = custCheckbox5_dict[pro_name]
                        pro_id_list.append(pro_id)
                    except Exception as e:
                        print(e)
                pro_id_str = ",".join(str(i) for i in pro_id_list)  # 将[1,27]转换为"1,27"
                row["custCheckbox5"] = pro_id_str
            except Exception as e:
                print(e)
                pass

            # 接口给的closeDate是毫秒级时间戳，需要转换为"%Y-%m-%d %H:%M"格式
            if not pd.isna(row["closeDate"]):
                try:
                    closeDate_int = int(row["closeDate"])
                    row["closeDate"] = timestamp13_to_str(closeDate_int, format_str="%Y-%m-%d %H:%M")
                except:
                    row["closeDate"] = None

            # 用老ownerId替换接口给的新ownerId
            if not pd.isna(row["ownerId"]):
                try:
                    new_ownerId = row["ownerId"]
                    row["ownerId"] = owner_dict[new_ownerId]    # 把老的ownerId赋值给row["ownerId"]
                except:
                    row["ownerId"] = None

            # 用老accountId替换接口给的新accountId
            if not pd.isna(row["dbcRelation1"]):
                new_accountId = row["dbcRelation1"]
                try:
                    row["dbcRelation1"] = account_dict[new_accountId]  # 把老的accountId赋值给row["dbcRelation1"]
                except:
                    row["dbcRelation1"] = row["dbcRelation1"] + 'old'   # 当account表没有这个新accountId时（即account缺记录），自己生成一个老accountId

            # 当老id为空时，生成一个老id，规则：有新id时用新id拼接old，没有新id时用name加密
            if pd.isna(row["id"]) or (row["id"] == "None") or (row["id"] == "#N/A"):
                if not pd.isna(row["new_opp_id"]):
                    row["id"] = row["new_opp_id"] + 'old'
                else:
                    row["id"] = hashlib.md5(row['opportunityName'].encode(encoding='UTF-8')).hexdigest()

            # 当没有映射关系时，把代号置为None，因为str类型的无法写入数据库int类型字段
            if type(row["dbcSelect26"]) != int:
                row["dbcSelect26"] = None

            # 当没有映射关系时，把代号置为None，因为str类型的无法写入数据库int类型字段
            if type(row["saleStageId"]) != int:
                row["saleStageId"] = None

            opp_id_list.append(row["id"])
            data_df.iloc[index] = row   # iterrows只对原始数据进行copy，不会修改原始数据，所以需要将处理后的结果重新赋值给原始df



        # print(data_df)

        # 如果数据库已经存在某些接口返回的记录（判断条件为：存在相同的id或new_opp_id），则将其在数据库删除
        delete_id_tuple = tuple(delete_id_list)
        delete_newId_tuple = tuple(delete_newId_list)
        try:
            if delete_id_tuple:
                old_info_sql = """ DELETE FROM opportunity WHERE id IN %s """
                cur2.execute(old_info_sql, (delete_id_tuple,))
                conn2.commit()
                # print('delete_id_tuple不为空元组')

            if delete_newId_tuple:
                old_info_sql = """ DELETE FROM opportunity WHERE new_opp_id IN %s """
                cur2.execute(old_info_sql, (delete_newId_tuple,))
                conn2.commit()
                # print('delete_newId_tuple不为空元组')

            # print("----完成删除----")
        except:
            # print("----没有需要删除的重复数据----")
            pass

        data_df = data_df[['id','ownerId','opportunityName','custCheckbox5','dbcRelation1','dbcSelect26','closeDate','saleStageId','new_opp_id','dbcJoin10']]

        # data_df内部根据id字段去重，保留最后一条数据
        data_df = data_df.drop_duplicates(['id'], keep="last")

        total = len(data_df)
        # 将数据写入数据库
        try:
            data_df.to_sql('opportunity', conn, index=False, if_exists='append')
            result = {'message': "商机信息更新成功！", 'total': total, 'id': opp_id_list}
        except:
            result = {'message': "商机信息更新失败！", 'total': total, 'id': opp_id_list}

        cur2.close()
        conn2.close()
    elif data is None:
        result = {'message': "商机信息获取成功，商机为空！"}
    else:
        # print(data)
        result = {'message': "商机信息获取失败！"}
    finish_time = datetime.datetime.now()
    # print("---------------------------------------finish_time:", finish_time)
    # result = {'message': "测试测试！"}
    conn.close()
    return result



#============================CRMACCOUNTSALEMAPPING同步==================================

"""
    通过接口获取团队成员
    参数：type=account或opportunity
    参数：value=new_account_id或new_opp_id
    返回结果中'rowcause'为'Owner'的销售为主负责人，对应mapping表里的ownerFlaf=2；其余的销售的ownerFlaf=1。
"""
def get_team_member(type, value):
    token = '4e33e00381c94a9bba251ebb44996c0f'
    # 该接口返回结果为：具体客户或商机的团队成员的信息
    url = 'http://192.168.16.90:8800/user/team_member?token={}&type={}&value={}'.format(token, type, value)
    r = requests.get(url=url)
    try:
        r = json.loads(r.text)
        result = r['data']
    except:
        result = r
    return result


account_dict = mappingDict().account()
opp_dict = mappingDict().opp()[0]
newOpp_acc = mappingDict().opp()[2]
user_dict = mappingDict().user()[0]
email_istar_dict = mappingDict().user()[4]


def sale_mapping(type1, value):
    # 参数type需要和关键字type区分开，所以加后缀1
    team_member = get_team_member(type1, value)
    # print(team_member)
    team_member_df = pd.DataFrame()
    if (type(team_member) == list) and (len(team_member) > 0):
        team_member_df = pd.DataFrame(team_member)
        print(team_member_df)
        if type1 == 'account':
            team_member_df = team_member_df.drop(columns=['email'])  # 丢掉email列
            team_member_df.insert(0, 'crmUid', '')  # 在第1列插入列名为crmUid的空值列
            team_member_df = team_member_df.rename(columns={'id': 'saleId',
                                                            'rowcause': 'ownerFlag',
                                                            'username': 'saleName',
                                                            })

            # for index, row in team_member_df.iterrows():
            #     try:
            #         row["crmUid"] = account_dict[value]
            #     except:
            #         row["crmUid"] = value + 'old'
            #     try:
            #         row["saleId"] = user_dict[row["saleId"]]
            #     except:
            #         row["saleId"] = row["saleId"] + 'old'
            #     if row["ownerFlag"] == 'Owner':
            #         row["ownerFlag"] = 2    # ownerFlag=2 为该客户的主负责人
            #     else:
            #         row["ownerFlag"] = 1
            #
            #     if (not pd.isna(row["crmUid"])) and (not pd.isna(row["saleId"])) and (not pd.isna(row["ownerFlag"])) and (not pd.isna(row["saleName"])):
            #         team_member_df.iloc[index] = row  # 将处理后的结果重新赋值给原始df
            #     else:
            #         # print("++++++++++删除account_mapping row+++++++++++", row["saleId"])
            #         team_member_df.drop(index, inplace=True)  # 当有字段为空时，无法写入数据库，所以把这条row丢掉
            for row in team_member_df.itertuples():
                print(row)
                index = getattr(row, 'Index')
                print(type(index), index)
                print(account_dict[value])
                print(value)
                team_member_df.at[index, 'crmUid'] = account_dict[value]
                try:
                    team_member_df.at[index, 'crmUid'] = account_dict[value]
                except:
                    team_member_df.at[index, 'crmUid'] = value + 'old'
                try:
                    team_member_df.at[index, 'saleId'] = user_dict[team_member_df.at[index, 'saleId']]
                except:
                    team_member_df.at[index, 'saleId'] = team_member_df.at[index, 'saleId'] + 'old'
                if team_member_df.at[index, 'ownerFlag'] == 'Owner':
                    team_member_df.at[index, 'ownerFlag'] = 2    # ownerFlag=2 为该客户的主负责人
                else:
                    team_member_df.at[index, 'ownerFlag'] = 1

                if (not pd.isna(team_member_df.at[index, 'crmUid'])) and (team_member_df.at[index, 'crmUid'] != '') and (not pd.isna(team_member_df.at[index, 'saleId'])) and (team_member_df.at[index, 'saleId'] != ''):
                    # team_member_df.iloc[index] = row  # 将处理后的结果重新赋值给原始df
                    pass
                else:
                    # print("++++++++++删除account_mapping row+++++++++++", row)
                    team_member_df.drop(index, inplace=True)  # 当有字段为空时，无法写入数据库，所以把这条row丢掉


        elif type1 == 'opportunity':
            team_member_df.insert(0, 'crmUid', '')  # 在第1列插入列名为crmUid的空值列
            team_member_df.insert(1, 'opportunityId', '')  # 在第2列插入列名为opportunityId的空值列
            team_member_df = team_member_df.rename(columns={'id': 'saleId',
                                                            'rowcause': 'ownerFlag',
                                                            'username': 'saleName',
                                                            'email': 'istarshineId',
                                                            })

            # for index, row in team_member_df.iterrows():
            #     try:
            #         row["crmUid"] = newOpp_acc[value]
            #     except:
            #         row["crmUid"] = None
            #     try:
            #         row["opportunityId"] = opp_dict[value]
            #     except:
            #         row["opportunityId"] = value + 'old'
            #     try:
            #         row["saleId"] = user_dict[row["saleId"]]
            #     except:
            #         row["saleId"] = row["saleId"] + 'old'
            #     try:
            #         row["istarshineId"] = email_istar_dict[row["istarshineId"]]
            #     except:
            #         row["istarshineId"] = None
            #     if row["ownerFlag"] == 'Owner':
            #         row["ownerFlag"] = 2  # ownerFlag=2 为该商机的主负责人
            #     else:
            #         row["ownerFlag"] = 1
            #
            #     if (not pd.isna(row["crmUid"])) and (not pd.isna(row["opportunityId"])) and (not pd.isna(row["saleId"])) and (not pd.isna(row["ownerFlag"])) and (not pd.isna(row["saleName"])):
            #         team_member_df.iloc[index] = row  # 将处理后的结果重新赋值给原始df
            #     else:
            #         # print("++++++++++删除opp_mapping row+++++++++++", email)
            #         team_member_df.drop(index, inplace=True)  # 当有字段为空时(除了istarshineId)，无法写入数据库，所以把这条row丢掉
            for row in team_member_df.itertuples():
                index = getattr(row, 'Index')
                try:
                    team_member_df.at[index, 'crmUid'] = newOpp_acc[value]
                except:
                    team_member_df.at[index, 'crmUid'] = None
                try:
                    team_member_df.at[index, 'opportunityId'] = opp_dict[value]
                except:
                    team_member_df.at[index, 'opportunityId'] = value + 'old'
                try:
                    team_member_df.at[index, 'saleId'] = user_dict[team_member_df.at[index, 'saleId']]
                except:
                    team_member_df.at[index, 'saleId'] = team_member_df.at[index, 'saleId'] + 'old'
                try:
                    team_member_df.at[index, 'istarshineId'] = email_istar_dict[team_member_df.at[index, 'istarshineId']]
                except:
                    team_member_df.at[index, 'istarshineId'] = None
                if team_member_df.at[index, 'ownerFlag'] == 'Owner':
                    team_member_df.at[index, 'ownerFlag'] = 2  # ownerFlag=2 为该商机的主负责人
                else:
                    team_member_df.at[index, 'ownerFlag'] = 1

                crm_uid = team_member_df.at[index, 'crmUid']
                if (not pd.isna(crm_uid)) and (crm_uid is not None) and (crm_uid != ''):
                    # team_member_df.iloc[index] = row  # 将处理后的结果重新赋值给原始df
                    pass
                else:
                    # print("++++++++++删除opp_mapping row+++++++++++", row)
                    team_member_df.drop(index, inplace=True)  # 当有字段为空时(除了istarshineId)，无法写入数据库，所以把这条row丢掉


    return team_member_df


#团队信息修改
def update_team(new_account_id):
    print(sale_mapping('account', '0027088f1c27594d'))
    print(sale_mapping('opportunity', 'f35fb5d92cd37f30'))


    # #数据处理脚本
    # print(new_account_id)
    # account_data = sale_mapping("account", new_account_id)
    # opp = get_opp_data(new_account_id)[0]
    # opp_data = sale_mapping("opportunity", opp["id"])
    #
    # # 添加Crmaccountsalemapping
    # print(account_data)
    # Crmaccountsalemapping.objects.create(**account_data)
    #
    # #添加Crmsalemapping
    # print(opp_data)
    # Crmsalemapping.objects.create(**opp_data)
