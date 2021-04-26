from django.shortcuts import render
from django.http import JsonResponse

def show_html(request, hid):
    html = "%s.html"%hid
    return render(request, html)

def json_403(request):
    return JsonResponse({
            "code": 0, "data": None, "error": "暂时无权限，如需要请联系管理员！",
            "status": 0,  "items": None, "message": "暂时无权限，如需要请联系管理员！"
        }) 