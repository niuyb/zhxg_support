from django.http import JsonResponse
from django.conf import settings
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import json
from public.utils import engine
from public.config import entity_type_map
import logging

app_name = "statistical"
logger = logging.getLogger(app_name)




def get_date(day=-1, date_format='%Y-%m-%d'):
    """获取日期"""
    local_date = datetime.today() + timedelta(int(day))
    return local_date.strftime(date_format)


def crm_record_info(request):
    """获取商机活动记录"""
    conn33 = engine(settings.DATABASES['contract_33'])
    result = {"status": 0, "message": "", "items": []}
    pd.set_option('display.max_rows', None)
    acc_ids = request.GET.get("account_id")
    try:
        time_long = int(request.GET.get("time_long"))
    except Exception as e:
        time_long = 30
    start_time = get_date('-{}'.format(time_long), '%Y-%m-%d 00:00')
    end_time = get_date(0, '%Y-%m-%d %H:%M')
    if not acc_ids:
        result["message"] = "请传入参数，客户ID"
        return JsonResponse(result)
    try:
        # 获取活动记录
        record_sql = ("select objectId as accountId,count(1) as record_count  from activityrecord "
                      "where createdAt between '{}' and '{}' and belongId=1 and objectId in('{}') "
                      "group by objectId".format(start_time, end_time, acc_ids))
        record_df = pd.read_sql_query(record_sql, conn33)
        # 获取最后一条活动记录
        last_sql = ("select a.objectId as accountId,a.createdAt,a.entityType,a.content,a.ownerId "
                    "from activityrecord as a ,(select b.objectId,max(b.createdAt) as createdAt  "
                    "from activityrecord as b where b.createdAt between '{}' and '{}' and b.belongId=1 "
                    "and b.objectId in({}) group by b.objectId) as c "
                    "where a.`objectId`=c.objectId "
                    "and a.createdAt=c.createdAt".format(start_time, end_time, acc_ids))
        last_df = pd.read_sql_query(last_sql, conn33)
        df = pd.merge(record_df, last_df, how='left', on='accountId')
        items = list(df.to_dict(orient="index").values())
        # print(items)
        result["message"] = "ok"
        result["items"] = items
    except Exception as e:
        logger.error("crm_record_info: %s"%e)
        result["message"] = "暂无信息"
    conn33.close()
    return JsonResponse(result)


def opp_record_info(request):
    """获取商机活动记录"""
    conn33 = engine(settings.DATABASES['contract_33'])
    result = {"status": 0, "message": "", "items": []}
    pd.set_option('display.max_rows', None)
    opp_ids = request.GET.get("opportunity_id")
    try:
        time_long = int(request.GET.get("time_long"))
    except Exception as e:
        time_long = 30
    start_time = get_date('-{}'.format(time_long), '%Y-%m-%d 00:00')
    end_time = get_date(0, '%Y-%m-%d %H:%M')
    if not opp_ids:
        result["message"] = "请传入参数，商机ID"
        return JsonResponse(result)
    entity_types = request.GET.get("entity_type")
    if not entity_types:
        entity_types = ','.join(entity_type_map.keys())
    try:
        # 获取活动记录
        record_sql = (
            """
                select objectId as opportunityId,count(1) as record_count
                from activityrecord where createdAt between '{}' and '{}'
                and entityType in ({})
                and belongId=3 and objectId in('{}') group by objectId
            """.format(start_time, end_time, entity_types, opp_ids))
        record_df = pd.read_sql_query(record_sql, conn33)
        # 获取最后一条活动记录
        last_sql = (
            """
                select a.objectId as opportunityId,a.createdAt,a.entityType,
                a.content,a.ownerId from activityrecord as a ,
                    (select b.objectId,max(b.createdAt) as createdAt
                    from activityrecord as b where b.createdAt
                    between '{}' and '{}' and b.belongId=3
                    and entityType in ({})
                    and b.objectId in({}) group by b.objectId
                    ) as c
                where a.`objectId`=c.objectId and a.createdAt=c.createdAt
            """.format(start_time, end_time, entity_types, opp_ids))
        last_df = pd.read_sql_query(last_sql, conn33)

        # 获取销售姓名
        owner_ids = "','".join([str(x1) for x1 in list(last_df['ownerId'])])
        owner_sql = ("select id,name from user where id in ('{}')".format(owner_ids))
        owner_df = pd.read_sql_query(owner_sql, conn33)
        owner_map = owner_df.set_index('id').to_dict()['name']
        owner_name = []
        entity_type_name = []
        for index, row in last_df.iterrows():
            # 处理拜访类型
            if row['entityType']:
                entity_type_name.append(entity_type_map[str(row['entityType'])])
            else:
                entity_type_name.append('')
            # 处理销售姓名
            if row['ownerId']:
                owner_name.append(owner_map[row['ownerId']])
            else:
                owner_name.append('')
        last_df['entityTypeName'] = entity_type_name
        last_df['ownerName'] = owner_name
        df = pd.merge(record_df, last_df, how='left', on='opportunityId')
        items = list(df.to_dict(orient="index").values())
        # print(items)
        result["status"] = "1"
        result["message"] = "ok"
        result["items"] = items
    except Exception as e:
        logger.error("opp_record_info: %s"%e)
        result["message"] = "暂无商机活动记录"
    conn33.close()
    return JsonResponse(result)


def opp_record_list(request):
    """获取商机活动记录"""
    conn33 = engine(settings.DATABASES['contract_33'])
    result = {"status": 0, "message": "", "items": []}
    pd.set_option('display.max_rows', None)
    opp_ids = request.GET.get("opportunity_id")
    try:
        time_long = int(request.GET.get("time_long"))
    except Exception as e:
        time_long = 30
    start_time = get_date('-{}'.format(time_long), '%Y-%m-%d 00:00')
    end_time = get_date(0, '%Y-%m-%d %H:%M')
    if not opp_ids:
        result["message"] = "请传入参数，商机ID"
        return JsonResponse(result)
    entity_types = request.GET.get("entity_type")
    if not entity_types:
        entity_types = ','.join(entity_type_map.keys())
    try:
        # 获取活动记录
        record_sql = (
            """
                select objectId as opportunityId,createdAt,entityType,content,
                ownerId from activityrecord where
                entityType in ({})
                and createdAt between '{}'
                and '{}' and belongId=3 and objectId in('{}')
                order by createdAt desc
            """.format(entity_types, start_time, end_time, opp_ids))
        record_df = pd.read_sql_query(record_sql, conn33)

        # 获取销售姓名
        owner_ids = "','".join([str(x1) for x1 in list(record_df['ownerId'])])
        owner_sql = ("select id,name from user where id in ('{}')".format(owner_ids))
        owner_df = pd.read_sql_query(owner_sql, conn33)
        owner_map = owner_df.set_index('id').to_dict()['name']
        owner_name = []
        entity_type_name = []
        for index, row in record_df.iterrows():
            # 处理拜访类型
            if row['entityType']:
                entity_type_name.append(entity_type_map[str(row['entityType'])])
            else:
                entity_type_name.append('')
            # 处理销售姓名
            if row['ownerId']:
                owner_name.append(owner_map[row['ownerId']])
            else:
                owner_name.append('')
        record_df['entityTypeName'] = entity_type_name
        record_df['ownerName'] = owner_name
        items = list(record_df.to_dict(orient="index").values())
        # print(items)
        result["status"] = "1"
        result["message"] = "ok"
        result["items"] = items
    except Exception as e:
        logger.error("opp_record_list: %s"%e)
        result["message"] = "暂无商机活动记录"
    conn33.close()
    return JsonResponse(result)




def crm_record_list(request):
    """获取客户活动记录"""
    '''根据客户id，以end_date往前推time_long天，查询拜访记录情况
        :param
            id 客户id，可传单个值,可传多个值（字符串类型，多个值逗号分隔）
            time_long 需要查询拜访的n天记录，字符串类型，不传值默认为30
            end_date 查询活跃的结束日期，不传默认为当天
        :return
                "activityId": 活动记录id,
                "createdAt":记录时间,
                "entityType": 活动类型id,
                "content": 记录内容,
                "ownerId":记录人id,
                "accountId":客户id,
                "opportunityId":商机id,
                "entityTypeName":活动记录类型
                "ownerName":记录人
        '''
    conn33 = engine(settings.DATABASES['contract_33'])
    result = {"status": 0, "message": "", "items": []}
    pd.set_option('display.max_rows', None)
    ids = request.GET.get("id")
    try:
        # 查询多长时间的活跃
        act_date = int(request.GET.get("time_long"))
    except:
        act_date = 30

    # 查询活跃的结束日期%Y%m%d
    end_time = request.GET.get("end_date")
    if not end_time:
        end_time = datetime.now().strftime("%Y-%m-%d 23:59")
    else:
        end_time = datetime.strptime(end_time,"%Y%m%d").strftime("%Y-%m-%d 23:59")
    start_time = (datetime.strptime(end_time, "%Y-%m-%d 23:59") - timedelta(days=act_date-1)).strftime("%Y-%m-%d 00:00")
    if not ids:
        result["message"] = "请传入参数，客户ID"
        return JsonResponse(result)
    entity_types = request.GET.get("entity_type")
    if not entity_types:
        entity_types = ','.join(entity_type_map.keys())
    try:
        # 获取活动记录
        # 方法一 分表查
        # record_sql = (
        #     """
        #         select id as activityId,createdAt,entityType,content,
        #         ownerId from activityrecord where
        #         entityType in ({})
        #         and createdAt BETWEEN '{}' AND '{}' order by createdAt desc
        #     """.format(entity_types, start_time,end_time))
        # print(record_sql)
        # record_df = pd.read_sql_query(record_sql, conn33)
        #
        # if len(record_df)==0:
        #     result["status"] = -1
        #     result["message"] = "暂无客户活动记录"
        #     return JsonResponse(result)
        # elif len(record_df)>1:
        #     record_condition = 'IN {}'.format(tuple(record_df["activityId"]))
        # else:
        #     record_condition = '={}'.format(list(record_df["activityId"])[0])
        #
        #
        # map_sql = ("SELECT activityId,accountId,opportunityId FROM activityrecord_mapping "
        #            "WHERE accountId IN ({}) AND activityId {} ".format(ids,record_condition))
        # # print(map_sql)
        #
        # map_df = pd.read_sql_query(map_sql,conn33)
        #
        # record_df = pd.merge(record_df,map_df,how='inner',on='activityId')
        # record_df = record_df.fillna('')

        # 方法二  连表查
        record_sql = ("SELECT a.id as activityId,a.createdAt,a.entityType,a.content,a.ownerId,m.accountId,m.opportunityId "
                      "FROM activityrecord a,activityrecord_mapping m WHERE a.id=m.activityId AND m.accountId IN ({}) "
                      "AND a.belongId IN (1,3) AND a.entityType in ({}) "
                      "and a.createdAt BETWEEN  '{}' AND '{}' "
                      "order by a.createdAt desc".format(ids,entity_types, start_time,end_time))

        record_df = pd.read_sql_query(record_sql, conn33)
        record_df = record_df.fillna('')

        # 获取销售姓名
        owner_ids = "','".join([str(x1) for x1 in list(set(record_df['ownerId']))])
        owner_sql = ("select id,name from user where id in ('{}')".format(owner_ids))
        owner_df = pd.read_sql_query(owner_sql, engine(settings.DATABASES['contract_33']))
        owner_map = owner_df.set_index('id').to_dict()['name']
        owner_name = []
        entity_type_name = []
        for index, row in record_df.iterrows():
            # 处理拜访类型
            if row['entityType']:
                entity_type_name.append(entity_type_map[str(row['entityType'])])
            else:
                entity_type_name.append('')
            # 处理销售姓名
            if row['ownerId']:
                owner_name.append(owner_map[row['ownerId']])
            else:
                owner_name.append('')
        record_df['entityTypeName'] = entity_type_name
        record_df['ownerName'] = owner_name
        items = list(record_df.to_dict(orient="index").values())
        # print(items)
        result["status"] = "1"
        result["message"] = "ok"
        result["items"] = items
    except Exception as e:
        logger.error("crm_record_list: %s" % e)
        result["message"] = "暂无客户活动记录"

    conn33.close()
    return JsonResponse(result)
