from django.http import JsonResponse


def getIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0] # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR') # 未使用代理获取IP

    # print(x_forwarded_for,ip)
    return JsonResponse({'ip':ip})