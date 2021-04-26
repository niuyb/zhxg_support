import json
import time
import uuid
import arrow
import redis
import base64
import requests
import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from mandala.auth.decorators import login_required, permission_required

from user_center.models import UserLog
from work_platform.models import CrmWechatMapping, WechatGroupMessage
from public.utils import Result

from customer.forms import CustomerListSelectForm
from work_platform.forms import WechatMessagePushForm
from customer.views import get_customer_list
from django.conf import settings

logger = logging.getLogger("default")

URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

REDIS_URL = settings.WECHAT_QR_CODE_BINDING_RESULT_REDIS_URL
RESULT_HASH = settings.WECHAT_QR_CODE_BINDING_RESULT_HASH
TASK_LIST = settings.WECHAT_QR_CODE_VERIFING_TASK_LIST
TASK_CUSTOMER_HASH = settings.WECHAT_QR_CODE_TASK_CUSTOMER_HASH

CONN = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)

# UPLOAD_API = "http://127.0.0.1/mirror"
UPLOAD_API = settings.WECHAT_QR_CODE_UPLOAD_API
UPLOAD_TOKEN = settings.WECHAT_QR_CODE_UPLOAD_TOKEN

UPLOAD_RESULT_TOKEN = settings.WECHAT_QR_CODE_UPLOAD_RESULT_TOKEN

# 微信群消息推送相关
PUSH_REDIS_URL = settings.WECHAT_GROUP_MESSAGE_PUSH_REDIS_URL
PUSH_LIST = settings.WECHAT_GROUP_MESSAGE_PUSH_LIST
WGM_CONN = redis.StrictRedis.from_url(PUSH_REDIS_URL, decode_responses=True)

def save_task_id_customer_id_to_redis(task_id, customer_id):
    CONN.hset(TASK_CUSTOMER_HASH, task_id, customer_id)

def get_customer_id_by_task_id_from_redis(task_id, delete=True):
    customer_id = CONN.hget(TASK_CUSTOMER_HASH, task_id)
    if customer_id:
        if delete:
            CONN.hdel(TASK_CUSTOMER_HASH, task_id)
    return customer_id

# 将微信群二维码发送给卢达
def upload_qr_code(qr_code, group_name, robot_name, file_name, extend_id):

    ro = Result()
    if qr_code:
        qr_code = qr_code.read()

    if not qr_code:
        ro.code = -1
        ro.error = "图片不能为空"
        return ro

    qr_code = "data:image/jpg;base64," + base64.b64encode(qr_code).decode("utf8")
    
    data = {
        "groupName": group_name,
        "nickName": robot_name,
        "qrcode": qr_code,
        "fileName": file_name,
        "extendId": extend_id
    }
    js = json.dumps(data)
    headers = {"ACCESS-TOKEN": UPLOAD_TOKEN}
    res = requests.post(UPLOAD_API, data=js, headers=headers, timeout=15).json()
    status = res.get("status")
    msg = res.get("msg")

    if status == 200:
        task = json.loads(msg)
        ro.data = task
        ro.code = 1
        ro.error = "微信群二维码已经上传，请等待返回结果"
    else:
        ro.error = msg

    return ro


@method_decorator(csrf_exempt, name="dispatch")
class Wechat(generic.View):

    # 上传微信群二维码图片
    # @method_decorator(login_required)
    # @method_decorator(permission_required("work_platform.wechat.upload", login_url=JSON_403))
    def post(self, request):
        ro = Result()
        _type = request.POST.get("type", "1")
        if _type in [1, "1"]:
            customer_id = request.POST.get("customer_id", "")
            customer_id = customer_id.strip()
            if not customer_id:
                ro.error = "参数错误，客户id不能为空"
                return JsonResponse(ro.dict())

            qr_code = request.FILES.get("qr_code")
            file_name = qr_code.name
            group_name = request.POST.get("wechat_group_name")
            robot_name = request.POST.get("robot_name", "客服")
            extend_id = str(uuid.uuid1())

            params = {
                "customer_id": customer_id,
                "extend_id": extend_id,
                "status": 0,
                "ctime": arrow.now().format("YYYY-MM-DD HH:mm:ss"),
                "istarshine_id": request.user.istarshine_id
            }
            user = request.user
            if not user.roles.filter(code="developer").count():
                message = {"group_name": group_name, "robot_name": robot_name}
                message = json.dumps(message)
                UserLog.objects.create(username=user.username, user_id=user.id,
                                    model="上传微信群二维码", action="上传", message=message)

            try:
                # ########################################
                # ro.code = 1
                # ro.data = {"taskId": '68795514380169296'}
                # ro.error = "测试上传二维码成功"
                # #########################################

                ro = upload_qr_code(qr_code, group_name, robot_name, file_name, extend_id)

                if ro.code == 1:
                    task = ro.data
                    task_id = task.get("taskId")
                    istarshine_id = request.user.istarshine_id

                    if not task_id:
                        ro.code = 0
                        ro.error = "没有找到任务ID"
                        return JsonResponse(ro.dict())
                    
                    params["status"] = 3
                    try:
                        CrmWechatMapping.objects.filter(customer_id=customer_id).update(status=0)
                        CrmWechatMapping.objects.create(**params)
                    except Exception as e:
                        logger.info(str(params))
                        logger.error(e)
                        pass

                    c_i_id = "%s,%s"%(customer_id, istarshine_id)
                    save_task_id_customer_id_to_redis(task_id, c_i_id)

                    # #######################################
                    # # 测试，给自己发通知，微信群绑定成功了
                    # requests.post("http://127.0.0.1/work_platform/wechat/result?access_token=4a849e31-a3dc-469f-bc6a-9ebd8a3de8c1", 
                    #         data='{"data":"{\\"wxRoomId\\":\\"17993524938@chatroom\\",\\"taskId\\":68795514380169296,\\"status\\":1}","type":1}')
                    # #######################################
                else:
                    
                    params["status"] = 2
                    try:
                        CrmWechatMapping.objects.filter(customer_id=customer_id).update(status=0)
                        CrmWechatMapping.objects.create(**params)
                    except Exception as e:
                        logger.info(str(params))
                        logger.error(e)
                        pass

            except Exception as e:
                ro.code = -1
                ro.error = "微信群二维码上传失败，失败原因：%s"%e

        else:
            ro.error = "错误的类型"
            
        return JsonResponse(ro.dict())

    def patch(self, request):
        ro = Result()
        _type = request.GET.get("type", "1")
        #解绑微信群
        if _type in [1, "1"]:
            customer_id = request.GET.get("customer_id", "")
            customer_id = customer_id.strip()
            if not customer_id:
                ro.error = "参数错误，客户id不能为空"
                return JsonResponse(ro.dict())

            message = dict(request.GET)
            user = request.user
            if user.username not in ["武翠霞", "丛大侠", "王寅", "张太锋", "黄远", "朱铭鑫", "袁战梅"]:
                message = json.dumps(message)
                UserLog.objects.create(username=user.username, user_id=user.id,
                                    model="解绑微信群", action="解绑", message=message)

            try:
                CrmWechatMapping.objects.filter(customer_id=customer_id).update(status=0)
                ro.code = 1
                ro.error = "微信群成功解绑。"
            except Exception as e:
                ro.code = -1
                ro.error = "微信群解绑失败，失败原因：%s"%e

        else:
            ro.error = "错误的类型"
            
        return JsonResponse(ro.dict())


def save_qr_code_binding_result_to_redis(task_id, result):
    CONN.hset(RESULT_HASH, task_id, json.dumps(result))


def save_qr_code_verifing_task_to_redis(task):
    CONN.lpush(TASK_LIST, json.dumps(task))

"""
code=0,或者1时，前端会立即停止访问接口，而为 -1时，会继续访问接口，获取结果
"""
def get_qr_code_binding_result_from_redis(task_id, delete=True):

    res = CONN.hget(RESULT_HASH, task_id)
    if res:
        result = json.loads(res)
        if delete:
            CONN.hdel(RESULT_HASH, task_id)
    else:
        result = {"code": -1, "data": None, "error": "没有查询到结果"}
    return result


@method_decorator(csrf_exempt, name="dispatch")
class WechatResult(generic.View):

    # 获取微信相关的结果，比如：type=1, 群二维码绑定结果
    # @method_decorator(login_required)
    # @method_decorator(permission_required("work_platform.wechat.upload", login_url=JSON_403))
    def get(self, request):
        """
        因为前端会间隔1秒钟访问此接口，所以规定code=1为绑定成功，code=0为绑定失败，code=-1为未查询到结果
        无论1或者0，都会立即停止访问此接口，只有是 -1 时，会继续访问此接口
        """
        ro = Result()

        _type = request.GET.get("type", "1")
        if _type in ['1', 1]:
            task_id = request.GET.get("task_id")
            if not task_id:
                ro.error = "参数错误"
                return JsonResponse(ro.dict())

            try:
                res = get_qr_code_binding_result_from_redis(task_id, delete=True)
                code = res.get("code", -1)
                ro.code = code
                if code == 1:
                    ro.error = "微信群绑定成功"
                else:
                    ro.error = res["error"]
                    
            except Exception as e:
                ro.code = -1
                ro.error = "查询失败，原因：%s"%e

        else:
            ro.error = "错误的类型"

        return JsonResponse(ro.dict())


    def post(self, request):
        ro = Result()
        token = request.GET.get("access_token")
        if not token:
            token = request.POST.get("access_token")

        if not token:
            ro.error = "token不能为空"
            return JsonResponse(ro.dict())

        if token != UPLOAD_RESULT_TOKEN:
            ro.error = "token不正确"
            return JsonResponse(ro.dict())
        
        if request.body:
            kwargs = json.loads(request.body.decode("utf8"))
        else:
            kwargs = {}

        # type: 1、微信群绑定结果通知----成功或者失败
        # type: 2、微信群预警信息推送结果通知----成功或者失败
        # type: 3、微信群中采集到的消息
        _type = kwargs.get("type", 1)
        data = kwargs.get("data")
        if data:
            info = json.loads(data)
        else:
            info = {}

        status = info.get("status")
        extend_id = info.get("extendId")
        task_id = info.get("taskId")

        res = {"code": 0, "error": ""}

        # 微信群绑定结果通知
        if _type in ['1', 1]:

            wechat_group_id = info.get("wxRoomId")
            msg = info.get("msg", "")
            customer_id = ""
            istarshine_id = ""

            try:
                c_i_id = get_customer_id_by_task_id_from_redis(task_id, delete=True)
                if c_i_id:
                    customer_id, istarshine_id = c_i_id.split(",")
                # if customer_id and wechat_group_id and istarshine_id:
                    
                    # 重新绑定微信群时，需要将原来绑定过的status都设置成0
                    CrmWechatMapping.objects.filter(customer_id=customer_id).update(status=0)

                    ctime = arrow.now().format("YYYY-MM-DD HH:mm:ss")

                    if status == 1:
                        _status = 1
                        res["code"] = 1
                        res["error"] = "微信群绑定成功"
                    else:
                        _status = 2
                        res["code"] = 0
                        res["error"] = "微信群绑定失败"

                    params = {
                        "customer_id": customer_id,
                        "wechat_group_id": wechat_group_id,
                        "ctime": ctime,
                        "status": _status,
                        "istarshine_id": istarshine_id,
                        "extend_id": str(uuid.uuid1())
                    }
                    
                    save_qr_code_verifing_task_to_redis(params)
                    CrmWechatMapping.objects.create(**params)

                else:
                    res["code"] = 0
                    if not customer_id:
                        res["error"] = "客户ID不能为空"
                    elif not wechat_group_id:
                        res["error"] = "微信群ID不能为空"
                    elif not istarshine_id:
                        res["error"] = "用户唯一ID不能为空"

            except Exception as e:
                logger.error(e)
                res["code"] = 0
                res["error"] = "微信群绑定失败：原因：%s"%str(e)

                
            try:
                save_qr_code_binding_result_to_redis(task_id, res)
                ro.code = 1
                ro.data = {"taskId": task_id, "status": status, "msg": msg}
                ro.error = "知道了"
            except Exception as e:
                ro.code = -1
                ro.error = "任务结果保存失败，原因：%s"%(str(e))

        # 微信群预警信息推送结果通知
        elif _type in [2, "2"]:
            if extend_id:
                try:
                    if status == 1:
                        WechatGroupMessage.objects.filter(extend_id=extend_id).update(status=1, description="消息发送成功")
                    else:
                        WechatGroupMessage.objects.filter(extend_id=extend_id).update(description=data)
                except Exception as e:
                    logger.error(e)
            elif task_id:
                try:
                    if status == 1:
                        WechatGroupMessage.objects.filter(task_id=task_id).update(status=1, description="消息发送成功")
                    else:
                        WechatGroupMessage.objects.filter(task_id=task_id).update(description=data)
                except Exception as e:
                    logger.error(e)

        # 微信群消息采集        
        elif _type in [3, "3"]:
            wechat_group_id = info.get("wxRoomId")
            wechat_id = info.get("wxId")
            content = info.get("data")

            if wechat_group_id and wechat_id and content:
                data_ex = info.get("dataEx", "")

                wechat_group_nick = info.get("groupNick", "")
                wechat_nick = info.get("nick", "")
                wechat_head_img = info.get("headImg", "")

                Type = info.get("type", 0)
                ctime = info.get("time", 0)

                ###############################################
                customer_id = 0
                cwm = CrmWechatMapping.objects.filter(wechat_group_id=wechat_group_id, status=1).last()
                if not cwm:
                    cwm = CrmWechatMapping.objects.filter(wechat_group_id=wechat_group_id).last()
                if cwm:
                    customer_id = cwm.customer_id

                is_read = 0
                ###############################################
                
                try:
                    WechatGroupMessage.objects.create(wechat_group_id=wechat_group_id, wechat_id=wechat_id, content=content, is_read=is_read,
                            wechat_group_nick=wechat_group_nick, wechat_nick=wechat_nick, wechat_head_img=wechat_head_img, receive_or_send=1,
                            data_ex=data_ex, task_id=task_id, extend_id=extend_id, type=Type, ctime=ctime, customer_id=customer_id)
                    ro.code = 1
                    ro.data = data
                    ro.error = "消息保存成功"
                except Exception as e:
                    logger.error(e)
                    ro.code = -1
                    ro.error = "消息保存失败，原因：%s"%(str(e))

        else:
            ro.error = "错误的消息类型"

        return JsonResponse(ro.dict())

@csrf_exempt
def wechat_test(request):
    time.sleep(10)
    return JsonResponse({"code": 1, "data": {"taskId": "sjflksjf"}, "error": "操作成功"})
    # return JsonResponse({"code": 0, "data": {"taskId": "sjflksjf"}, "error": "操作失败"})

@csrf_exempt
def wechat_result_test(request):
    time.sleep(40)
    return JsonResponse({"code": 1, "data": {"taskId": "sjflksjf"}, "error": "操作成功"})


def get_wechat_group_message_list(_type, customer_id, cur_id=None, page_size=20):
    ro = Result()
    if not _type:
        _type = "0"

    if cur_id:
        try:
            cur_id = int(cur_id)
        except:
            ro.code == -1
            ro.error = "参数错误"
            return ro.dict()

    try:
        page_size = int(page_size)
    except:
        page_size = 20

    if page_size > 100:
        page_size = 20

    params = {}
    if customer_id:
        params["customer_id"] = customer_id

    messages = None    
    if _type in ['0', '1', '4', '5']:
        if cur_id:
            params["id__lt"] = cur_id

        messages = WechatGroupMessage.objects.filter(**params).order_by("-ctime")

    elif _type in ['2', '3', '6', '7']:
        if cur_id:
            params["id__gt"] = cur_id

        messages = WechatGroupMessage.objects.filter(**params).order_by("ctime")
        
    if _type in ['0', '2', '4', '6']:
        ro.data = list(messages[: page_size].values())
        ro.code = 1
    elif _type in ['1', '3', '5', '7']:
        ro.data = messages.count()
        ro.code = 1
    else:
        ro.error = "错误的类型"

    return ro.dict()

def wechat_group_message_list_api(request):
    _type = request.GET.get("type", '0')
    customer_id = request.GET.get("customerId", 0)
    cur_id = request.GET.get("curId", None)
    page_size = request.GET.get("pageSize", 20)
    result = get_wechat_group_message_list(_type, customer_id, cur_id, page_size)
    # WechatGroupMessage.objects.filter(customer_id=customer_id, is_read=0).update(is_read=1)
    return JsonResponse(result)

def wechat_group_list(request):
    to_url = "/work_platform/customer/list"
    path = request.get_full_path()
    try:
        query = path.split("?")[1]
    except:
        query = ""
    if query:
        to_url = to_url + "?" + query
    return redirect(to_url)

def wechat_group_members_api(request):
    wechat_group_id = request.GET.get("wechatGroupId")
    res = Result()
    if wechat_group_id:
        sql = """
            SELECT id, customer_id, wechat_group_id, wechat_group_nick, wechat_id, wechat_nick, wechat_head_img 
            FROM `wechat_group_message` 
            WHERE wechat_group_id='{}'
            GROUP BY wechat_id;
            """.format(wechat_group_id)

        members = WechatGroupMessage.objects.raw(sql)
        data = []
        for m in members:
            member = {}
            member["customer_id"] = m.customer_id
            member["wechat_group_id"] = m.wechat_group_id
            member["wechat_group_nick"] = m.wechat_group_nick
            member["wechat_id"] = m.wechat_id
            member["wechat_nick"] = m.wechat_nick
            member["wechat_head_img"] = m.wechat_head_img
            data.append(member)

        res.data = data
        res.code = 1

    else:
        res.error = "参数错误"
    
    return JsonResponse(res.dict())

@csrf_exempt
def push_wechat_group_message(request):
    res = Result()
    kws = request.GET
    cres = get_customer_list(request, kws)
    customers = cres.get("items")
    if not customers:
        customers = []
        
    cids = set()
    for customer in customers:
        if customer.get("id"):
            cids.add(str(customer["id"]))

    wmpf = WechatMessagePushForm(request.POST)
    if not wmpf.is_valid():
        res.code = -1 
        res.error = "参数错误"
        return JsonResponse(res.dict())

    cdata = wmpf.cleaned_data

    title = cdata.get("messageTitle", "")        
    message = cdata.get("messageContent", "")
    url = cdata.get("messageUrl", "")
    push_type = cdata.get("pushType")

    if push_type not in ["1", "2", "3", 1, 2, 3]:
        res.error = "参数错误"
        res.code = -1
        return JsonResponse(res.dict())

    c_ids = set()
    customer_ids = cdata.get("customerIds", "")
    if not customer_ids:
        customer_ids = ""

    for cid in customer_ids.split(","):
        cid = cid.strip()
        if cid:
            c_ids.add(cid)

    if push_type in [1, "1", 2, "2"]:
        c_ids = c_ids & cids

    if push_type in [3, "3"]:
        c_ids = cids
    
    if not c_ids:
        res.error = "没有符合条件的微信群"
        return JsonResponse(res.dict())
 
    data = []
    for c_id in c_ids:
        task_id = str(uuid.uuid1())
        task = {
            "extendId": task_id,
            "loguser": request.user.username,
            "istarshineId": request.user.istarshine_id,
            "title": title,
            "summary": message,
            "url": url,
            "ctime": arrow.now().format("YYYYMMDDHHmmss"),
            "customerId": c_id,
        }
        data.append({c_id: task_id})
        WGM_CONN.lpush(PUSH_LIST, json.dumps(task))

    res.code = 1
    res.data = data
    res.error = "消息推送任务已经生成"

    return JsonResponse(res.dict())
