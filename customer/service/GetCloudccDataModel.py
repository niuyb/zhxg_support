import json

import requests


getTokenUrl = "http://192.168.16.90:8800/general/token?username=ZW_001&password=123"
updateAccountDataUrl = 'http://192.168.16.90:8800/account/api?'


def getToken():
    try:
        r = requests.get(getTokenUrl)
        r = json.loads(r.text)
        token = r['data']['token']
        return token
    except Exception as e:
        return ''


def updateAccountData(accountid, modify_field, modify_value):
    token = getToken()
    url = updateAccountDataUrl + 'account_id=' + accountid + '&modify_field=' + modify_field + '&modify_value=' \
          + modify_value + '&token=' + token
    try:
        r = requests.put(url=url)
        data = json.loads(r.text)
        return data['data']
    except:
        return False




if __name__ == '__main__':
    # requests.get(url='https://support.istarshine.com/DataCount/single_user_activity_count?uid=55981b376a2690e8old')
    updateAccountData('55981b376a2690e8', 'back_url', 'https://support.istarshine.com/DataCount/single_user_activity_count?uid=55981b376a2690e8old')