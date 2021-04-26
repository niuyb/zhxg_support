import json

from django.conf import settings
from secretary.models import WkTDinggroup, Salercansee, DingGroupMemberMap, SalercanseeNew

"""通过部门ID获取下级部门的部门ID和部门名称[{"did": xxx, "name": "yyy"}, ...]"""
def get_ding_groups(dpid):
    ding_groups = WkTDinggroup.objects.filter(dpid=dpid).values("did", "name")
    return ding_groups

"""获取公司所有部门"""
def get_all_departments():
    departments = list(WkTDinggroup.objects.all().values("dpid", "did", "name"))
    return departments

"""通过部门did获取下属部门"""
def get_sub_departments(did, all=None):
    if all is None:
        all = get_all_departments()
    sub_departments = []
    other = []
    for department in all:
        if department["dpid"] == did:
            sub_departments.append(department)
        else:
            other.append(department)
    return sub_departments, other

"""根据部门did获取所有下属部门"""
def get_all_sub_departments(did, all=None):
    def _get_all_sub_departments(did, all, departments):
        sub_departments, all = get_sub_departments(did, all)
        if not sub_departments or not all:
            return departments, all
        departments.extend(sub_departments)
        for department in sub_departments:
            did = department["did"]
            departments, all = _get_all_sub_departments(did, all, departments)
        return departments, all 

    if all is None:
        all = get_all_departments()            
    departments = []
    _get_all_sub_departments(did, all, departments)
    return departments
    

"""获取政务和企业两个中心的销售部门"""
def get_departments_about_sale():
    all = get_all_departments()
    dpids = settings.SALE_DEPARTMENT_LEVEL_1
    department_data = []
    for dpid in dpids:
        departments = get_all_sub_departments(dpid, all=all)
        department_data.extend(departments)
    return department_data

"""查看某商务都能查看谁"""
def get_can_see(salename):
    scs = Salercansee.objects.filter(salename=salename).first()
    if not scs:
        return []
    js = scs.cansee
    return list(set(json.loads(js)))

"""查看某商务都能查看谁"""
def get_can_see_new(istarshine_id):
    scs = SalercanseeNew.objects.filter(saleid=istarshine_id).first()
    if not scs:
        return []
    js = scs.cansee
    return list(set(json.loads(js)))

"""查看部门下所有成员名字"""
def get_group_members(group_id):
    dgmm = DingGroupMemberMap.objects.filter(group_id=group_id).first()
    if not dgmm:
        return []
    js = dgmm.member_names_all
    return json.loads(js)

"""查看部门下所有成员的istarshine_id"""
def get_group_istarshine_ids(group_id):
    dgmm = DingGroupMemberMap.objects.filter(group_id=group_id).first()
    if not dgmm:
        return []
    js = dgmm.istarshine_ids_all
    return json.loads(js)
