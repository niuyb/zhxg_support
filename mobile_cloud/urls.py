#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-22 10:34:42
# @Author  : ztf (itwhboy@gmail.com)
# @Link    : https://www.baidu.com
# @Version : $Id$

from django.urls import re_path
from mobile_cloud import views

urlpatterns = [
     re_path(r'^index$', views.index, name='index'),
     re_path(r'^send_to_crm$', views.send_to_crm, name='send_to_crm'),
]

app_name = "mobile_cloud"
