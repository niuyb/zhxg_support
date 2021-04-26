"""
查询部门时，以及部门成员时，有时会对下属部门和下属部门成员进行查询
现查太耗时间，所以需要一个定时任务，定时同步一下，到redis中
"""
#coding:utf8
import json
import pymysql
import collections

import setting

kws = setting.parse_kwargs_for_pymysql(setting.databases["yqms2_199"])

"""获取所有ding_users"""
def select_ding_users_all():
    table = "WK_T_WARNSPECIAL_ALLDINGUSER"
    conn = pymysql.connect(**kws)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select KW_DINGID as Dtalkid, KW_DNAME as uname, KW_DGROUP as dingframe from `%s` where KW_POSITION !='';" % table
    cursor.execute(sql)
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items

"""整合ding_users"""
def handle_ding_users(ding_users):
    dingframe_users_map = collections.defaultdict(dict)
    for ding_user in ding_users:
        ding_frames = ding_user["dingframe"]
        Id = ding_user["Dtalkid"]
        name = ding_user["uname"]
        if ding_frames:
            for ding_frame in ding_frames.strip(",").split(","):
                item = dingframe_users_map[ding_frame]
                if not item.get("ids"):
                    item["ids"] = set()
                item["ids"].add(Id)
                if not item.get("names"):
                    item["names"] = set()
                item["names"].add(name)
    return dingframe_users_map

"""获取所有组"""
def select_ding_groups_all():
    table = "WK_T_DINGGROUP"
    conn = pymysql.connect(**kws)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select Did, name, Dpid from `%s`;" % table
    cursor.execute(sql)
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items

"""整合ding_groups"""
def handle_ding_groups(ding_groups):
    dpid_groups_map = collections.defaultdict(dict)
    for group in ding_groups:
        dpid = group["Dpid"]
        did = group["Did"]
        name = group["name"]
        # print(dpid, did, name)
        item = dpid_groups_map[dpid]
        if not item.get("sub_group_names"):
            dpid_groups_map[dpid]["sub_group_names"] = set()
        dpid_groups_map[dpid]["sub_group_names"].add(name)

        if not item.get("sub_group_ids"):
            dpid_groups_map[dpid]["sub_group_ids"] = set()
        dpid_groups_map[dpid]["sub_group_ids"].add(did)
    return dpid_groups_map

"""通过指定部门Did，获取下一级的部门"""
def select_ding_groups(Did):
    table = "WK_T_DINGGROUP"
    conn = pymysql.connect(**kws)
    """需要返回元组"""
    cursor = conn.cursor()
    if Did:
        sql = "select Did, name from `%s` where Dpid=%s;" % (table, Did)
    else:
        sql = "select Did, name from `%s`;" % table
    cursor.execute(sql)
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items

def main():
    ding_users_all = select_ding_users_all()
    uuu = handle_ding_users(ding_users_all)
    print(uuu)
    # ding_groups_all = select_ding_groups_all()
    # ddd = handle_ding_groups(ding_groups_all)    
    # print(ddd)

if __name__ == "__main__":
    main()
