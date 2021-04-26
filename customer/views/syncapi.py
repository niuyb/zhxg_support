import json
import logging
import threading
import time
import traceback
from queue import Queue
from urllib.parse import quote

import requests
from django.http import JsonResponse

from customer.models import Account
from customer.service.syncService import syncCrmaccountsalemapping, syncAccount, syncOpportunity, syncCrmsalemapping


logger = logging.getLogger("customer")


#最终客户搜索
def get_finalaccount(request):
    if request.method == "GET":
        result = {"code": 200, "msg": "", "data": None}

        #搜索框key
        key = request.GET.get("key")
        if not key:
            result["code"] = -1
            return JsonResponse(result)
        key = quote(key)

        try:
            token = '4e33e00381c94a9bba251ebb44996c0f'
            url_account = 'http://192.168.16.90:8800/account/api?field_name=name&field_value={}&token={}'.format(key, token)

            r = requests.get(url_account)
            result["data"] = json.loads(r.text)["data"]
        except Exception as e:
            print(e)
            result["code"] = 500
            result["msg"] = "http://192.168.16.90:8800/account/api down"
            result["data"] = []
            return JsonResponse(result)

        if not result["data"]:
            result["code"] = 201
            result["msg"] = "http://192.168.16.90:8800/account/api down"
            result["data"] = []
            return JsonResponse(result)

        for i in result["data"]:
            acount = Account.objects.filter(new_account_id=i["id"]).exists()
            if acount:
                i["status"] = True
            else:
                i["status"] = False

        return JsonResponse(result)



#点击同步
try:
    def sync_account_data_bak(request):
        if request.method == "GET":
            result = {"code":200, "msg": "", "data": None}
            id = request.GET.get("id")
            status = request.GET.get("status")
            control = 0


            q = Queue(maxsize=4)
            account_t = threading.Thread(target=syncAccount, args=(id, status, q))
            opp_t = threading.Thread(target=syncOpportunity, args=(id, status, q))
            casm_t = threading.Thread(target=syncCrmaccountsalemapping, args=(id, q))
            csm_t = threading.Thread(target=syncCrmsalemapping, args=(id, q))

            casm_t.start()
            csm_t.start()
            account_t.start()
            opp_t.start()

            casm_t.join()
            csm_t.join()
            account_t.join()
            opp_t.join()

            while True:
                time.sleep(0.5)
                if q.full():
                    break

            while not q.empty():
                r, m = q.get()
                if not r:
                    control += 1
                    result["msg"] += m



            # 同步account 表
            synca, _ = syncAccount(id, status)

            if not synca:
                control +=1
                result["msg"] += "account sync failed account1;"

            # 同步opportunity表
            l = []
            synco, _ = syncOpportunity(id, status)
            if not synco:
                control += 1
                result["msg"] += "account sync failed Opportunity;"


            # 同步Crmaccountsalemapping
            syncc, _ = syncCrmaccountsalemapping(id)
            if not syncc:
                control += 1
                result["msg"] += "account sync failed Crmaccountsalemapping;"

            #同步Crmsalemapping
            syncs, _ = syncCrmsalemapping(id)
            if not syncs:
                control += 1
                result["msg"] += "account sync failed Crmsalemapping;"

            if not control:
                result["msg"] += "success"

            if control == 4:
                result["code"] = -1
                result["msg"] = "all sync failed"
                return JsonResponse(result)

            if not control:
                result["msg"] = "success"
                return JsonResponse(result)
            result["code"] = 500
            return JsonResponse(result)
except Exception as e:
    print(traceback.print_exc())


#点击同步
def sync_account_data(request):
    if request.method == "GET":
        result = {"code":200, "msg": "", "data": None}
        id = request.GET.get("id")
        status = request.GET.get("status")
        control = 0

        # 同步opportunity表
        synco, _ = syncAccount(id, status)
        if not synco:
            control += 1
            result["msg"] += "account sync failed;"

        # syncOpportunity
        syncc, _ = syncOpportunity(id, status)
        if not syncc:
            control += 1
            result["msg"] += "opportunity sync failed;"

        # 同步Crmaccountsalemapping
        sync, _ = syncCrmaccountsalemapping(id)
        if not syncc:
            control += 1
            result["msg"] += "accountsalemapping sync failed;"

        # 同步Crmsalemapping
        syncs, _ = syncCrmsalemapping(id)
        if not syncs:
            control += 1
            result["msg"] += "salemapping sync failed;"


        if not control:
            result["msg"] = "success"
            return JsonResponse(result)
        result["code"] = 500
        return JsonResponse(result)