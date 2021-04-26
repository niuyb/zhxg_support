# from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from multiple_api.xiaoshouyi_api import XiaoshouyiApi
# Create your views here.


@api_view(['POST', 'GET'])
def index(request):
    a = XiaoshouyiApi().queryV2('select id from account')
    return Response(a)


@api_view(['POST', 'GET'])
def getlist(request, format=None):
    """获取列表"""
    a = XiaoshouyiApi().queryV2('select id from account')
    return Response(a)
