import json

from django.http import JsonResponse
from django.views import View

from secretary.models import DingGroupMemberMap
from support.base import SALE_DEPARTMENT_LEVEL_0
import pandas as pd
from public.utils import get_value_list, get_all_data

from  datetime import datetime,timedelta
from django.conf import settings
import logging
logger = logging.getLogger("sale")

class Tenders(View):
    '''操作招标信息的接口'''
    def get(self,request):
        # 根据不同的人获取不同招标信息, 近7天的招标公告信息
        # 参数{'did':''}  support_user_new 表中的dingframe 可能含有逗号
        # 返回可见省份的招标信息
        did = request.GET.get("did")
        result = get_tenders_data(did)
        return JsonResponse(result)



def get_tenders_data(did):
    # 根据不同的人获取不同招标信息, 近7天的招标公告信息
    # 参数{'did':''}  support_user_new 表中的dingframe 可能含有逗号
    # 返回可见省份的招标信息
    result = {"status": 0, "msg": "", "data": {}}
    province_list = []
    group_id = [id for id in did.split(',')]
    # print(group_id)
    # 查询map表中所有部门信息
    columns = ["group_id","group_name","sub_group_ids","sub_group_names","sub_group_ids_all","sub_group_names_all"]
    all_groups = get_value_list(DingGroupMemberMap,{},columns)
    all_groups_df = pd.DataFrame(data=all_groups,columns=columns)

    sub_group_ids_all = all_groups_df.loc[all_groups_df.group_name == "政务事业部"]

    # 判断是否是政务事业部下属部门或者政务事业部和管理层
    df = sub_group_ids_all.loc[sub_group_ids_all.sub_group_ids_all.str.contains('|'.join(group_id))]

    if (str(SALE_DEPARTMENT_LEVEL_0["政务事业部"]) not in group_id and  str(SALE_DEPARTMENT_LEVEL_0["管理层"]) not in group_id and str(SALE_DEPARTMENT_LEVEL_0["政务销售中心"]) not in group_id):
        if len(df) == 0:
            return JsonResponse({"status": -1, "msg": "此部门不属于政务事业部","data":{}})
        else:
            for id in group_id:
                # 判断本身的部门名是否包含‘区’
                g_center = all_groups_df.loc[all_groups_df.group_id == id]
                for index, row in g_center.iterrows():
                    group_name = g_center.loc[index, "group_name"]
                    if '区' in group_name:
                        province_list.extend(json.loads(g_center.loc[index, "sub_group_names"]))
                    else:
                        # 判断部门id的所有上级部门是否包含‘区’
                        f_center = all_groups_df.loc[all_groups_df.sub_group_names_all.str.contains(group_name)] #上级部门
                        # print(f_center)
                        df = f_center.loc[f_center.group_name.str.contains('区')]
                        if len(df)>0 :
                            # 说明为大区下的部门
                            if group_name != '行业拓展部' and group_name != '渠道部':
                                province_list.append(group_name)
                            else:
                                province_list = ["all"]
            else:
                if len(province_list) == 0:
                    province_list = ["all"]
    else:
        province_list = ['all']

    province_list = list(set(province_list))

    # 准备查询招标数据的条件，查询数据并返回
    date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')
    if province_list[0] != 'all':

        province_condition = " AND (" + "OR".join(" province like '%{}%' ".format(i) for i in province_list) + ")"
    else:
        province_condition = ""

    try:
        sql = ("SELECT title,detail_url FROM invite_tenders "
               "WHERE bid_pub_date> '{}' AND purchase_type like '招标公告%'".format(date)) + province_condition
        tenders_data_dict = dict(get_all_data(settings.DATABASES["log_120"], sql))
        # print(tenders_data_dict)
        result["status"] = 1
        result["msg"] = 'ok'
        result["data"] = tenders_data_dict
    except Exception as e:
        logger.error(e)
        result["msg"] = "服务器繁忙，请稍后重试"
        result["status"] = -1
        result["data"] = {}


    return result