from django.shortcuts import render
import json
from user_center.models import UserLog
# Create your views here.

def upload(request):
    title = "微信群管理"

    user = request.user
    if user.username not in ["武翠霞", "丛大侠", "王寅", "张太锋", "黄远", "朱铭鑫", "袁战梅"]:
        message = json.dumps(dict(request.GET))
        UserLog.objects.create(username=user.username, user_id=user.id,
                               model="微信群管理", action="进入页面", message=message)
    return render(request, 'work_platform/date_index.html', locals())