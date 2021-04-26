
from secretary.models import WkTDinggroup
from django.db.models import Q
from math import cos, sin, asin, sqrt,pow


"""获取销售中心的大区名"""
def ger_area(did):

    # area_list = get_value_list(WkTDinggroup,{"dpid":did,"name__contains":"区"},["name"])
    area_list = WkTDinggroup.objects.filter(Q(dpid=did),(Q(name__contains="区") | Q(name__contains="行业拓展"))).values("name")

    item = []
    for i in area_list:
        item.append(i["name"])
    return item




def getDistance(lat1, lng1, lat2, lng2):
    '''
    计算经纬度距离
    :param lat1: 纬度1
    :param lng1: 经度1
    :param lat2: 纬度2
    :param lng2: 经度2
    :return: 单位公里
    '''
    EARTH_REDIUS = 6371
    PI = 3.1415926

    def rad(d):
        return d * PI / 180.0

    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * asin(sqrt(pow(sin(a/2), 2) + cos(radLat1) * cos(radLat2) * pow(sin(b/2), 2)))
    s = s * EARTH_REDIUS
    s = "%.4f" %s
    return s

if __name__ == '__main__':
    print(getDistance(40.05,116.35,40,116))