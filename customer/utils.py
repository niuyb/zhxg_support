import re

import requests
import json
import random

from public.utils import get_value_list

from user_center.models import *#LocationInfo
from customer.models import CrmIndustryL1, CrmIndustryL2, CrmLocationState, CrmLocationCity, CrmLocationDistrict

# 获取所有省份
def get_provinces(parent_uuid=0):
    provinces = get_value_list(LocationInfo, {"level": 1, "parent_uuid": parent_uuid}, ["uuid", "province"])
    return provinces

# 获取某个省下面的所有城市
def get_cities(parent_uuid):
    cities = get_value_list(LocationInfo, {"level": 2, "parent_uuid": parent_uuid}, ["uuid", "city"])
    return cities

# 获取某个城市下的所有区县
def get_counties(parent_uuid):
    counties = get_value_list(LocationInfo, {"level": 3, "parent_uuid": parent_uuid}, ["uuid", "county"])
    return counties

#获取地域--state(省)
def get_states():
    states = get_value_list(CrmLocationState, {}, ["lid", "lname"])
    states += [["0", "未知"]]
    return states

# 获取1级行业列表，每条数据结构为字典
def get_industry_l1_list():
    industry_l1 = CrmIndustryL1.objects.all().values()
    return list(industry_l1)

# 获取2级行业列表，每条数据结构为字典
def get_industry_l2_list():
    industry_l2 = CrmIndustryL2.objects.all().values()
    return list(industry_l2)

# 获取1级行业字典，以id为key，信息字典为value
def get_industry_l1_dict():
    industry_l1_list = get_industry_l1_list()
    industry_l1_dict = {}
    for item in industry_l1_list:
        industry_l1_dict[item["id"]] = item
    return industry_l1_dict

# 获取2级行业字典，以id为key，信息字典为value
def get_industry_l2_dict():
    industry_l2_list = get_industry_l2_list()
    industry_l2_dict = {}
    for item in industry_l2_list:
        industry_l2_dict[item["id"]] = item
    return industry_l2_dict

# 获取省份列表，每条数据结构为字典
def get_state_list():
    states = CrmLocationState.objects.all().values()
    return list(states)

# 获取省份字典，以id为key，以省份信息为value
def get_state_dict():
    state_list = get_state_list()
    state_dict = {}
    for state in state_list:
        state_dict[state["lid"]] = state
    return state_dict

# 获取省份列表，每条数据结构为字典
def get_city_list():
    cities = CrmLocationCity.objects.all().values()
    return list(cities)

# 获取省份字典，以id为key，以省份信息为value
def get_city_dict():
    city_list = get_city_list()
    city_dict = {}
    for city in city_list:
        city_dict[city["lid"]] = city
    return city_dict

# 获取省份列表，每条数据结构为字典
def get_district_list():
    districts = CrmLocationDistrict.objects.all().values()
    return list(districts)

# 获取省份字典，以id为key，以省份信息为value
def get_district_dict():
    district_list = get_district_list()
    district_dict = {}
    for district in district_list:
        district_dict[district["lid"]] = district
    return district_dict

#获取二级industry(行业) [{"id": 46, "lname": "公安局", "pid": 51}, ...]
def get_industry_data():
    industry_data = []
    #一级行业
    # l1 = CrmIndustryL1.objects.all().values()
    # industry_data += list(l1)
    #二级行业
    l2 = CrmIndustryL2.objects.all().values()
    industry_data += list(l2)# + [(0, "未知")]
    return industry_data

#获取industry_l1(一级行业) [(1, "111"), ...]
def get_industry_data_1():
    l1 = get_value_list(CrmIndustryL1, {}, ["id", "name"])
    l1 += [(0, "未知")]
    return l1


# 获取具体客户(参数：new_account_id)的最新客户信息（与cloudCC平台实时）
def get_acc_data(new_account_id):
    token = '4e33e00381c94a9bba251ebb44996c0f'
    url = 'http://192.168.16.90:8800/account/api?field_name=id&field_value={}&token={}'.format(new_account_id, token)
    r = requests.get(url=url)
    try:
        r = json.loads(r.text)
        result = r['data']
    except:
        result = r
    return result

# 获取具体客户(参数：new_account_id)的最新商机信息（与cloudCC平台实时）
def get_opp_data(new_account_id):
    token = '4e33e00381c94a9bba251ebb44996c0f'
    url = 'http://192.168.16.90:8800/opportunity/api?field_name=account_id&field_value={}&token={}'.format(new_account_id, token)

    # print(url)
    r = requests.get(url=url)
    try:
        r = json.loads(r.text)
        result = r['data']
        # print(result)
    except:
        result = r
    return result

# 获取具体客户(参数：new_account_id)的最新商机信息（与cloudCC平台实时）
def get_team_acc_data(new_account_id):
    token = '4e33e00381c94a9bba251ebb44996c0f'
    url = 'http://192.168.16.90:8800/user/team_member?type=account&value={}&token={}'.format(new_account_id, token)
    r = requests.get(url=url)
    try:
        r = json.loads(r.text)
        result = r['data']
    except:
        result = r
    return result

# 获取具体客户(参数：new_account_id)的最新商机信息（与cloudCC平台实时）
def get_team_opp_data(new_account_id):
    opp = get_opp_data(new_account_id)[0]
    token = '4e33e00381c94a9bba251ebb44996c0f'
    url = 'http://192.168.16.90:8800/user/team_member?type=opportunity&value={}&token={}'.format(opp["id"], token)
    r = requests.get(url=url)
    try:
        r = json.loads(r.text)
        result = r['data']
    except:
        result = r
    return result



# 生成8位随机密码
def random_password():
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s3 = "1234567890"
    s4 = "~!@#$%^*()-_+=[]{}|\<>?/"
    pwd1 = ''
    pwd2 = ''
    pwd3 = ''
    pwd4 = ''
    for i in range(2):
        pwd1 += s1[random.randint(0, len(s1) - 1)]
        pwd2 += s2[random.randint(0, len(s2) - 1)]
        pwd3 += s3[random.randint(0, len(s3) - 1)]
        pwd4 += s4[random.randint(0, len(s4) - 1)]

    pwd = pwd1 + pwd2 + pwd3 + pwd4
    return pwd

# 根据一级行业，确定创建账号时默认的【用户类型】
def account_type(industry1):
    industry1 = industry1
    if industry1 == '政府':
        account_type = '政府用户'
        account_type_id = '1'
    elif industry1 == '企业':
        account_type = '企业用户'
        account_type_id = '4'
    elif industry1 == '协会及其他':
        account_type = '协会及其他'
        account_type_id = '1'
    else:
        account_type = '政府用户'
        account_type_id = '1'
    return account_type, account_type_id

# 确定创建账号时默认的【版本选择】、【版本选择id】、【关键词数量】/【品牌词数量】
def version_select(acc_type, district_level):
    if acc_type == '企业用户':
        version = '标准版'
        version_id = 'B1'
        word_num = 5
    else:
        if district_level == '省级':
            version = '省级版'
            version_id = 'B3'
            word_num = 1000
        elif district_level == '市级':
            version = '市级版'
            version_id = 'B2'
            word_num = 500
        else:
            version = '区县版'
            version_id = 'B1'
            word_num = 300
    return version, version_id, word_num



def insertsql_factory(table_name,data):
    cols = ", ".join('`{}`'.format(k) for k in data.keys())
    val_cols = ', '.join('%({})s'.format(k) for k in data.keys())
    sql = "insert into {} (%s) values (%s)".format(table_name)
    res_sql = sql % (cols, val_cols)
    return res_sql

def check_ip(ipAddr):
  compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
  if compile_ip.match(ipAddr):
    return True
  else:
    return False

