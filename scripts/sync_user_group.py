#coding:utf8
import json
import pymysql
import collections

import setting

class MySql(object):
    def __init__(self, **kwargs):
        self.conn = pymysql.connect(**kwargs)
        self.kwargs = kwargs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return True

    def select(self, sql):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        items = cursor.fetchall()
        cursor.close()
        return items

    def insert(self, sql):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return True

"""获取所有用户信息"""
def get_users_all():
    table = "WK_T_WARNSPECIAL_ALLDINGUSER"
    sql = "select * from {} where KW_POSITION !='';".format(table)

    kws = setting.parse_kwargs_for_pymysql(setting.databases["yqms2_199"])
    with MySql(**kws) as mysql:
        items = mysql.select(sql)
    return items

"""获取所有部门信息"""
def get_groups_all():
    table = "WK_T_DINGGROUP"
    sql = "select * from {};".format(table)

    kws = setting.parse_kwargs_for_pymysql(setting.databases["yqms2_199"])
    with MySql(**kws) as mysql:
        items = mysql.select(sql)
    return items

"""将部门信息制作成一个以部门ID为key，部门信息为value的字典"""
def dict_groups(groups):
    groups_dict = {}
    for group in groups:
        group_id = group["Did"]
        groups_dict[group_id] = group
    return groups_dict

"""将用户和部门信息整合到一起"""
def map_user_group(users, groups_dict):
    _users = []
    for user in users:
        _user = {}
        _user["duname"] = user["KW_DNAME"]
        _user["duid"] = user["KW_DINGID"]
        
        group_ids = user["KW_DGROUP"].strip(",")
        group_name = ""
        if group_ids:
            for group_id in group_ids.strip(",").split(","):
                group_name += groups_dict[int(group_id)]["name"]
        _user["dgname"] = group_name
        _user["dgid"] = group_ids
        _user["duposition"] = user["KW_POSITION"]
        _users.append(_user)
    return _users

"""将整合之后的用户部门信息保存到数据库中"""
def save_user_group_map(users):
    table = "user_group_map"
    keys = ["duid", "duname", "duposition", "dgid", "dgname"]
    values = []
    for user in users:
        value = []
        for k in keys:
            value.append(user[k])
        value = str(tuple(value))
        values.append(value)

    keys_str = ", ".join(keys)
    values_str = ", ".join(values)

    sql = """insert into {}(
        {}
    ) values{};""".format(table, keys_str, values_str)
    # print(sql)

    kws = setting.parse_kwargs_for_pymysql(setting.databases["yqms2_199"])
    with MySql(**kws) as mysql:
        mysql.insert(sql)
    return

"""同步用户和部门信息"""
def sync_user_group():
    users_all = get_users_all()
    groups_all = get_groups_all()
    groups_dict = dict_groups(groups_all)
    users = map_user_group(users_all, groups_dict)
    # print(len(users))
    # print(users[: 10])
    save_user_group_map(users)
    return

if __name__ == "__main__":
    sync_user_group()
    