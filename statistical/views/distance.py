from django.http import JsonResponse

from statistical.utils import getDistance


def cal_distance(request):
    '''
        计算两个经纬度距离
        :param lat1: 纬度1
        :param lng1: 经度1
        :param lat2: 纬度2
        :param lng2: 经度2
        :return: 单位公里
        '''
    lat1, lng1 = request.GET.get('location1')
    lat2, lng2 = request.GET.get('location1')
    s = getDistance(lat1, lng1,lat2, lng2)

    return JsonResponse(s)