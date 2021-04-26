#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-08-29 13:33:42
# @Author  : ztf (itwhboy@gmail.com)
# @Link    : https://www.baidu.com
# @Version : $Id$

from django.urls import re_path
from financial_statements import views

urlpatterns = [
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^getlist$', views.getlist, name='getlist'),
    re_path(r'^staging$', views.staging, name='staging'),
    re_path(r'^getStagingList$', views.getStagingList, name='getStagingList'),
    re_path(r'^standing_book$', views.standing_book, name='standing_book'),
    re_path(r'^get_standing_book$', views.get_standing_book, name='get_standing_book'),
    re_path(r'^download_standing_book$', views.download_standing_book, name='download_standing_book'),
]
app_name = "financial_statements"
