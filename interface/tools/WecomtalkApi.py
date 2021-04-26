#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json


class WecomApi(object):
    """企业微信接口类"""
    def getToken(self):
        corpid = 'ww60d12cbe3d4a82be'
        corpsecret = '5BIgHw22QkxT9oW90u4crduirvu6WceQkHeFAh8dS5k'
        url = ('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(corpid, corpsecret))
        result = requests.get(url)
        token = json.loads(result.text)
        if 'access_token' in token:
            return token['access_token']
        else:
            print(token)
            return ''

    def sendMsg(self, wecomId="10290", msg="测试内容"):
        """发送政务消息通知"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(self.getToken())
        data = {}
        data["agentid"] = 1000023
        data["msgtype"] = 'text'
        data["touser"] = wecomId
        data["text"] = {
            "content": msg
        }
        data = json.dumps(data)
        result = requests.post(url, data)
        return json.loads(result.text)

    def getStaffInfo(self, did=0):
        if did == 0:
            print('缺少必要参数')
            exit()

        url = "http://192.168.16.90:8900/?obj=qywx_userlist&userid={}".format(did)
        res = result = requests.get(url)
        return json.loads(res.text)

    def getAllStaffInfo(self):
        url = "http://192.168.16.90:8900/?obj=qywx_userlist"
        res = requests.get(url)
        res = json.loads(res.text)["data"]
        return res

    def getDepartmentList(self):
        """部门列表"""
        # url = 'https://oapi.dingtalk.com/department/list?access_token={}'.format(self.getToken())
        # result = requests.get(url)
        # department = json.loads(result.text)
        # if 'department' in department:
        #     return department['department']
        # else:
        #     print(department)
        #     return []
        pass

    def getDepartmentUser(self, departId=1):
        """部门用户列表"""
        # url = 'https://oapi.dingtalk.com/user/listbypage?access_token={}&department_id={}&offset=0&size=100'.format(self.getToken(), departId)
        # result = requests.get(url)
        # user = json.loads(result.text)
        # if 'userlist' in user:
        #     return user['userlist']
        # else:
        #     print(user)
        #     return []
        pass



# 测试区域
if __name__ == '__main__':
    # print(WecomApi().getStaffInfo('10704')["data"][0]["userid"])
    # print(WecomApi().getAllStaffInfo())
    WecomApi().sendMsg(wecomId="10290", msg="测试内容123456")

