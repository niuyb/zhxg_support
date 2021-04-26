import requests
import json
import pandas as pd

class XiaoshouyiApi(object):
    """销售易接口类"""
    def oauth2token(self):
        """销售易获取token信息"""
        url = 'https://api.xiaoshouyi.com/oauth2/token'
        data = {
            'grant_type': 'password',
            'client_id': '2bcb9662ae9f2048431b58fdc5789394',
            'client_secret': 'e7b96e5c62022780d455bceb9267673f',
            'redirect_uri': 'https://www.istarshine.com/',
            'username': 'Alan.Zhu@istarshine.com',
            # 'password': 'zmx2000K8HwLIxe'
            'password': 'admin000000K8HwLIxe'

        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        result = requests.post(url, data=data, headers=headers)
        return json.loads(result.text)

    def get_token(self):
        """获取token值"""
        token = self.oauth2token()
        if 'access_token' in token:
            return token['access_token']
        else:
            print(token)
            return ''

    def set_headers(self):
        """设置header头"""
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self.get_token()
        }
        return headers

    def queryV1(self, sql):
        """查询接口 最大支持条数100条"""
        url = 'https://api.xiaoshouyi.com/data/v1/query'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self.get_token()
        }
        data = {}
        data['q'] = sql
        result = requests.post(url, headers=headers, data=data)
        return json.loads(result.text)

    def queryV2(self, sql):
        """查询接口 最大支持条数100条"""
        url = 'https://api.xiaoshouyi.com/rest/data/v2/query?q=' + sql
        result = requests.get(url, headers=self.set_headers())
        return json.loads(result.text)

    def updateAccount(self, id='0', data={}):
        """修改客户表"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/account/update'
        record = {}
        record['id'] = id
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.get_token()
        }
        result = requests.post(url, headers=headers, data=json.dumps(record))
        jsonArr = json.loads(result.text)
        if 'status' in jsonArr and jsonArr['status'] == 0:
            return '成功'
        else:
            return jsonArr

    def createAccount(self, record={}):
        """创建客户"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/account/create'
        headers = {
            'Authorization': 'Bearer '+self.get_token()
        }
        data = {}
        data['public'] = False
        data['record'] = record
        result = requests.post(url, headers=headers, data=json.dumps(data))
        jsonArr = json.loads(result.text)
        if 'error_code' in jsonArr:
            print('createAccount', data, jsonArr)
            return False
        else:
            return jsonArr['id']

    def createOpportunity(self, record={}):
        """创建商机"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/opportunity/create'
        headers = {
             'Authorization': 'Bearer '+self.get_token()
        }
        data = {}
        data['record'] = record
        result = requests.post(url, headers=headers, data=json.dumps(data))
        jsonArr = json.loads(result.text)
        if 'error_code' in jsonArr:
            print('createOpportunity', data, jsonArr)
            return False
        else:
            return jsonArr['id']

    def createOrder(self, record={}):
        """创建订单"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/order/create'
        headers = {
            'Authorization': 'Bearer '+self.get_token()
        }
        data = {}
        data['record'] = record
        result = requests.post(url, headers=headers, data=json.dumps(data))
        jsonArr = json.loads(result.text)
        if 'error_code' in jsonArr:
            print('createOrder', data, jsonArr)
            return False
        else:
            return jsonArr['id']

    def createOrderProduct(self, record={}):
        """创建订单明细"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/orderProduct/create'
        headers = {
            'Authorization': 'Bearer '+self.get_token()
        }
        data = {}
        data['record'] = record
        result = requests.post(url, headers=headers, data=json.dumps(data))
        jsonArr = json.loads(result.text)
        if 'error_code' in jsonArr:
            print('createOrderProduct', data, jsonArr)
            return False
        else:
            return jsonArr['id']

    def getAreList(self, level=0):
        """获取省市县"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/account/describe'
        headers = {
            'Authorization': self.get_token()
        }

        result = requests.get(url, headers=headers)
        jsonArr = json.loads(result.text)
        if 'error_code' in jsonArr:
            print('getAreList', jsonArr)
            return False
        else:
            df = pd.DataFrame(jsonArr['fields'])
            if level == 1:
                fCity = df.loc[df['propertyname'] == 'fCity']
                return fCity['selectitem'].tolist()[0]
            elif level == 2:
                fDistrict = df.loc[df['propertyname'] == 'fDistrict']
                return fDistrict['selectitem'].tolist()[0]
            else:
                fState = df.loc[df['propertyname'] == 'fState']
                return fState['selectitem'].tolist()[0]

    def getIndustryList(self, level=0):
        """获取行业"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/account/describe'
        headers = {
            'Authorization': self.get_token()
        }

        result = requests.get(url, headers=headers)
        jsonArr = json.loads(result.text)
        if 'error_code' in jsonArr:
            print('getIndustryList', jsonArr)
            return False
        else:
            df = pd.DataFrame(jsonArr['fields'])
            if level == 2:
                dbcSelect9 = df.loc[df['propertyname'] == 'dbcSelect9']
                return dbcSelect9['selectitem'].tolist()[0]
            else:
                dbcSelect5 = df.loc[df['propertyname'] == 'dbcSelect5']
                return dbcSelect5['selectitem'].tolist()[0]

    def groupQueryMember(self, businessId='0', belongId='0', ownerFlag='2'):
        """获取团队成员"""
        url = 'https://api.xiaoshouyi.com/data/v1/objects/group/query-member'
        data = {}
        params = {
            'businessId': businessId,
            'belongId': belongId,
            'ownerFlag': ownerFlag
        }
        data['params'] = json.dumps(params)
        # print(data)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self.get_token()
        }
        result = requests.post(url, headers=headers, data=data)
        jsonArr = json.loads(result.text)
        if 'status' in jsonArr and jsonArr['status'] == 0:
            return '成功'
        else:
            return jsonArr

    def groupJoinMember(self, businessId='0', belongId='0', users=[]):
        """添加负责员工
            users数据格式 [1,2,3,4]
        """
        url = 'https://api.xiaoshouyi.com/data/v1/objects/group/join-owner'
        data = {}
        users_list = []
        for user in users:
            users_list.append({'id': str(user)})
        params = {
            'businessId': businessId,
            'belongId': belongId,
            'users': users_list
        }
        data['params'] = json.dumps(params)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self.get_token()
        }
        result = requests.post(url, headers=headers, data=data)
        jsonArr = json.loads(result.text)
        if 'users' in jsonArr and len(jsonArr['users']) > 0:
            return '成功'
        else:
            return jsonArr


if __name__ == '__main__':
    a = XiaoshouyiApi().getAreList()
    print(a)
