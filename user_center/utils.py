import base64

from hashlib import md5
from django.conf import settings
from urllib.parse import urlencode
from django.contrib.auth import get_user_model
from secretary.models import DingGroupMemberMap

User = get_user_model()

# 生成老后台的跳转链接
def make_jump_url(username, next_url=""):
    base_url = settings.LOGIN_URL_OLD_BACKEND
    salt = settings.LOGIN_SALT
    string = salt + username
    token = md5(string.encode("utf8")).hexdigest()
    username = base64.b64encode(username.encode("utf8")).decode("utf8")
    params = {
        "username": username,
        "token": token,
        "jump": next_url
    }
    url = base_url + "?" + urlencode(params)
    return url

"""获取用户和部门对应关系, {用户名：部门...}"""
def get_user_group_map():
    group_id_name_map = dict(DingGroupMemberMap.objects.all().values_list("group_id", "group_name"))
    user_group_map = dict(User.objects.all().values_list("username", "dingframe"))
    for k, v in list(user_group_map.items()):
        #同一个人，可能会属于多个部门
        group_list = []
        if v:
            vs = v.split(",")
            for v in vs:
                group = group_id_name_map.get(v)
                if group:
                    group_list.append(group)
        user_group_map[k] = "|".join(group_list)
    return user_group_map
        