#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    接口功能：
        1、调用cloudCC的接口，增量更新192.168.185.33 crm_info库的account表
"""
import sys
# sys.path.append("/var/www/crm_info/")

import requests
import time
import json
import datetime
import hashlib
import pandas as pd
from urllib import parse
from django.http import HttpResponse, JsonResponse
from interface.utils import update_acc

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)




"""将获取到的数据，写入数据库account表"""
def update_account_table(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST

    # data = request.GET.get("data")  # 拿到data参数的value
    data = kws.get("data")  # 拿到data参数的value
    # print(data)
    data = parse.unquote(data)  # url解码
    # print('data_test:', data)
    try:
        data = json.loads(data)    # json格式的str转dict或list（此处为list）。且可以将数据中的null转为None
        # print('222222222', data)
    except:
        pass

    result = update_acc(data)

    return JsonResponse(result)


