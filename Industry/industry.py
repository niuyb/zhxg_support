#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os
from django.conf import settings

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class CusrtomerIndustry:
    def __init__(self):
        self.keywords = {}

        f = open(os.path.dirname(__file__)+'/industrywords.csv')
        while True:
            line = f.readline()
            if line:
                strs = line.split(',')
                industry = strs[0]
                cat = strs[1]
                prior = int(strs[2])
                for x in range(3, len(strs)):
                    if len(strs[x]) > 1:
                        self.keywords[strs[x]] = {
                            'industry': industry,
                            'prior': prior, 'cat': cat
                         }

            else:
                break

        f.close()

        mohu = open(os.path.dirname(__file__)+"/mohu.csv")
        self.mohu = {}
        lines = mohu.readlines()
        for l in lines:
            strs = l.split(',')
            self.mohu[strs[0]] = {'industry': strs[1], 'cat': strs[2]}

    def judge(self, name):
        industrys = []
        topprior = 10

        # process mohu
        if name in self.mohu:
            industrys.append(self.mohu[name])
            return industrys

        if name.endswith("大学"):
            industrys.append({'industry': "高校", 'cat': "企业"})
            return industrys

        if name.endswith("医院"):
            industrys.append({'industry': "医院", 'cat': "企业"})
            return industrys

        for word in self.keywords.keys():

            if word in name:
                # print word
                industrynow = self.keywords[word]
                prior = industrynow['prior']

                if len(industrys) == 0:
                    industrys.append(industrynow)
                    topprior = prior
                    # print name,industrynow['industry']
                else:
                    for ind in industrys:
                        if ind['cat'] == industrynow['cat'] and topprior >= prior:
                            # print name,industrynow['industry']
                            # print topprior,prior
                            topprior = prior
                            industrys.remove(ind)
                            industrys.append(industrynow)

        if len(industrys) == 0:
            # print name,'not match'
            industrys.append({'industry': "其他", 'prior': 10, 'cat': "其他"})
        return industrys


# CI = CusrtomerIndustry()
# a = CI.judge('邹城市农业农村局')
# print(a)
# quit()
