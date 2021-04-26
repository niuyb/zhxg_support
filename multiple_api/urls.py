#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-18 13:33:42
# @Author  : ztf (itwhboy@gmail.com)
# @Link    : https://www.baidu.com
# @Version : $Id$

from django.urls import re_path
from . import views

urlpatterns = [
     re_path(r'^index$', views.index, name='index'),
     re_path(r'^getlist$', views.getlist, name='getlist'),
]
