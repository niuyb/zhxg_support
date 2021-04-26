import requests

def upper_dict_key(dict_data):
    if isinstance(dict_data, list):
        for data in dict_data:
            upper_dict_key(data)

    if isinstance(dict_data, dict):
        for k in list(dict_data):
            k_upper = k.upper()
            if k_upper != k:
                dict_data[k_upper] = dict_data[k]
                del dict_data[k]
            upper_dict_key(dict_data[k_upper])

    return dict_data


REMOTE_API_TIMEOUT = 60
def req_get(url, upper=False):
    header = {'content-type': 'application/json'}
    r = requests.get(url, headers=header, verify=False, timeout=REMOTE_API_TIMEOUT)

    if r.status_code == 200:
        if upper:
            return upper_dict_key(r.json())
        return r.json()


def req_post(url, data):
    headers = {'content-type': 'application/json'}
    r = requests.post(url, headers=headers, data=data, verify=False, timeout=REMOTE_API_TIMEOUT)
    if r.status_code in [200, 201]:
        if 'X-Subject-Token' in r.headers:
            return dict(r.json(), **r.headers)
        else:
            return r.json()




#如果字符串在 目标字符串中 返回 此字符串及后面的
def strstr(s, target):
    if not s:
        return ""

    if target in s:
        return s[str.index(target[0]):]
    else:
        return ""

if __name__ == '__main__':
    # r = req_get('http://www.baidu.com')
    # print(r)

    print(strstr("你好批量啊啊批量啊啊", "批量"))