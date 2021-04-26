from django.http import JsonResponse
from  secretary.models import DingGroupMemberMap
from  user_center.models import UserNew
from django.conf import settings
from statistical.utils import ger_area
from  competitor.models import SalesPortraitSaler
import pandas as pd
import numpy as np
from public.utils import get_value_list
import json
from mandala.auth.decorators import login_required


@login_required
def saler_info(request):
    '''查询商务的基本信息，姓名 入职日期 三级部门 四级部门 '''
    # 查询入职日期的
    pd.set_option('display.max_rows', None)
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    result = {"status": 0, "message": "","items":[]}
    # 获取所有的部门及下属部门和人员
    columns = ["group_name","sub_group_names_all","member_names_all"]
    all_groups = get_value_list(DingGroupMemberMap,{},columns)
    all_groups_df = pd.DataFrame(data=all_groups,columns=columns)
    all_groups_df["sub_group_names_all"] = all_groups_df["sub_group_names_all"].apply(lambda x:json.loads(x))
    all_groups_df["member_names_all"] = all_groups_df["member_names_all"].apply(lambda x:json.loads(x))


    # 获取政务销售中心的所有大区名
    did = settings.SALE_DEPARTMENT_LEVEL_0['政务销售中心']
    zw_area = ger_area(did)
    # print(zw_area)

    # 按照所有下属部门和下属的人进行展开
    '''
       A       B
    0  1  [1, 2]
    1  2  [1, 2]
    df=pd.DataFrame({'A':df.A.repeat(df.B.str.len()),'B':np.concatenate(df.B.values)})
    '''
    # 获取大区和省份部门，按照省份部门展开
    zw_groups_df1 = all_groups_df.loc[all_groups_df.group_name.isin(zw_area), ["group_name", "sub_group_names_all"]]
    # 单独处理行业拓展部/上海特区
    zw_groups_df1["sub_group_names_all"] = zw_groups_df1.sub_group_names_all.apply(lambda x:["行业拓展二部"] if x==[] else x)
    zw_groups_df1.loc["new"] = ["上海特区", ["上海特区"]]
    zw_groups_df1 = pd.DataFrame(
        {'group_name': zw_groups_df1.group_name.repeat(zw_groups_df1.sub_group_names_all.str.len()),
         'sub_group_names_all': np.concatenate(zw_groups_df1.sub_group_names_all.values)})

    # print(zw_groups_df1)

    # 获取省份部门和对应的人，按照商务人员展开
    zw_groups_df2 = all_groups_df.loc[all_groups_df.group_name.isin(zw_groups_df1.sub_group_names_all), ["group_name", "member_names_all"]]
    zw_groups_df2 = pd.DataFrame(
        {'group_name': zw_groups_df2.group_name.repeat(zw_groups_df2.member_names_all.str.len()),
         'member_names_all': np.concatenate(zw_groups_df2.member_names_all.values)})
    zw_groups_df2 = zw_groups_df2.rename(columns={"group_name":"sub_group_names_all"})
    # print(zw_groups_df2)
    # 拼接人员三级部门四级部门信息
    zw_all_salers = pd.merge(zw_groups_df1,zw_groups_df2,how="left",on="sub_group_names_all")
    zw_all_salers = zw_all_salers.rename(
        columns={"group_name": "daqu_name", "sub_group_names_all": "province", "member_names_all": "name"})

    # 查询所有的人员入职/职位/钉钉信息
    columns1 = ["name","hireddate"]
    saler_df1 =pd.DataFrame(data=get_value_list(SalesPortraitSaler,{},columns1),columns=columns1)
    columns2 = ["username","dtalkid","position"]
    saler_df2 = pd.DataFrame(data=get_value_list(UserNew,{},columns2),columns=["name","dtalkid","position"])

    zw_all_salers = pd.merge(zw_all_salers,saler_df1,how="inner",on="name")
    zw_all_salers = pd.merge(zw_all_salers,saler_df2,how="left",on="name")
    zw_all_salers.drop_duplicates(subset=["name"], keep="first", inplace=True)
    zw_all_salers = zw_all_salers.fillna("")
    # zw_all_salers = zw_all_salers.loc[zw_all_salers]
    # print(zw_all_salers)
    items = list(zw_all_salers.to_dict(orient="index").values())
    result["items"] = items
    result["status"] = 1
    return JsonResponse(result)