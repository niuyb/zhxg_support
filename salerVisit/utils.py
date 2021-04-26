from user_center.models import UserNew
from secretary.models import DingGroupMemberMap,WkTDinggroup
from public.utils import get_value_list
import pandas as pd

"""根据istarshine_id查询部门和上级部门"""
def get_groups(id_list):
    if id_list:
        staff_df = pd.DataFrame(get_value_list(UserNew,{'istarshine_id__in':id_list},['dingframe','istarshine_id']),
                            columns=['dingframe','istarshine_id'])
    else:
        staff_df = pd.DataFrame(get_value_list(UserNew, {}, ['dingframe', 'istarshine_id']),
                                columns=['dingframe', 'istarshine_id'])
    group_df = pd.DataFrame(get_value_list(WkTDinggroup,{},['did','dpid','name']),
                            columns=['did','dpid','name'])

    for index,row in staff_df.iterrows():
        did_list = []
        for i in row['dingframe'].split(','):
            did_list.append(int(i))
        dname = list(group_df.loc[group_df.did.isin(did_list), 'name'])
        dpid = list(group_df.loc[group_df.did.isin(did_list), 'dpid'])
        staff_df.loc[index, 'departments'] = '|'.join(dname)
        staff_df.loc[index, 'departments_top'] = '|'.join(list(group_df.loc[group_df.did.isin(dpid), 'name']))

    # print(staff_df)
    return staff_df

"""根据dingframe_list查询部门和上级部门"""
def get_department(dingframe_list):
    if dingframe_list:
        staff_df = pd.DataFrame(data={'dingframe':dingframe_list},columns=['dingframe'])
    else:
        staff_df = pd.DataFrame(data=list(set(get_value_list(UserNew, {}, ['dingframe']))),
                                columns=['dingframe'])
    group_df = pd.DataFrame(get_value_list(WkTDinggroup,{},['did','dpid','name']),
                            columns=['did','dpid','name'])
    for index,row in staff_df.iterrows():
        did_list = []
        for i in row['dingframe'].split(','):
            did_list.append(int(i))
        dname = list(group_df.loc[group_df.did.isin(did_list),'name'])
        dpid = list(group_df.loc[group_df.did.isin(did_list),'dpid'])
        staff_df.loc[index, 'dpid'] = ','.join([str(i) for i in dpid])
        staff_df.loc[index, 'departments'] = '|'.join(dname)
        staff_df.loc[index, 'departments_top'] = '|'.join(list(group_df.loc[group_df.did.isin(dpid),'name']))
    staff_df = staff_df.fillna('')
    # print(staff_df[['departments','departments_top','dpid']])

    return staff_df
