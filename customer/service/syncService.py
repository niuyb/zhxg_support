'''
同步数据
'''
import datetime
import json
import threading
import time
import traceback
from queue import Queue
import requests
from django.db import connection
from django.forms import model_to_dict
from customer.models import Crmaccountsalemapping, User, Account, CrmIndustryL1, CrmIndustryL2, CrmLocationState, \
    CrmLocationCity, CrmLocationDistrict, Opportunity, Crmsalemapping
from interface.tools.mapping import custCheckbox5_dict
from interface.tools.utils import more_split, timestamp13_to_str
from user_center.models import HrEmployee

#同步account表
def syncAccount(account_id, status):
    '''

    :param account_id: 客户 新id
    :param status: 客户判断是否在数据库中
    :return:
    '''
    highSeaStatus_mapping = {
        "自建": 1,
        "未领取": 2,
        "已领取": 3,
        "已签约": 4,
        "已废弃": 5,
        "已冻结": 6
    }

    level_mapping = {
        "重点客户": 1,
        "开发客户": 4,
        "正式客户": 5
    }
    try:
        token = '4e33e00381c94a9bba251ebb44996c0f'
        url_account = 'http://192.168.16.90:8800/account/api?field_name=id&field_value={}&token={}'.format(account_id, token)
        r_account = requests.get(url=url_account)
        account_data = json.loads(r_account.text)["data"][0]
        '''
        {
            "code": 1,
            "data": [
                {
                    "id": "00e0e711de6d858b",
                    "crm_id": "0012021660376C1SQAie",                           
                    "account_name": "君势智盟（北京）国际公关顾问有限公司",
                    "industry_1": "企业",
                    "industry_2": "文化传媒",
                    "address_province": null,
                    "address_city": null,
                    "address_area": null,
                    "xsy_id": "16194813",
                    "owner_id": "7a71691aeae32f88",
                    "created_at": "1500019800000",
                    "level": "开发客户",
                    "sea_status": "已领取",
                    "contact_phone": null,
                    "recent_activity_time": "1604332800000"
                }
            ],
            "msg": ""
        }
        '''
        account = Account.objects.filter(new_account_id=account_id).first()
        if not account:
            account = Account()
        #同步时间
        account.update_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account.crm_id = account_data['crm_id']  if account_data['crm_id'] else ""

        if account_data["industry_1"]:
            crmindustryl1 = CrmIndustryL1.objects.filter(name=account_data["industry_1"]).first()
            dbcselect5 = crmindustryl1.id
        else:
            dbcselect5 = None
        account.dbcselect5 = dbcselect5

        if account_data["industry_2"]:
            crmindustryl2 = CrmIndustryL2.objects.filter(name=account_data["industry_2"]).first()
            dbcselect9 = crmindustryl2.id
        else:
            dbcselect9 = None
        account.dbcselect9 = dbcselect9

        if account_data["address_province"]:
            crmlocationstate = CrmLocationState.objects.filter(lname=account_data["address_province"]).first()
            fstate = crmlocationstate.lid
        else:
            fstate = None
        account.fstate = fstate

        if account_data["address_city"]:
            crmlocationcity = CrmLocationCity.objects.filter(lname=account_data["address_city"]).first()
            fcity = crmlocationcity.lid
        else:
            fcity = None
        account.fcity = fcity

        if account_data["address_area"]:
            crmlocationdistrict = CrmLocationDistrict.objects.filter(lname=account_data["address_area"]).first()
            fdistrict = crmlocationdistrict.lid
        else:
            fdistrict = None
        account.fdistrict = fdistrict
        #新id
        account.new_account_id = account_data["id"]
        #旧id
        if account_data["xsy_id"] == "None":
            account.id = account_data["id"] + "old"
        elif account_data["xsy_id"]:
            account.id = account_data["xsy_id"]
        else:
            account.id = account_data["id"] + "old"
        # account.id = account_data["xsy_id"]
        #用户id
        account.ownerid = account_data["owner_id"] if account_data["owner_id"] else account_data["id"] + "old"
        account.accountname = account_data["account_name"]
        if account_data["created_at"]:
            try:
                closeDate_int = int(account_data["created_at"])
                closeDate = timestamp13_to_str(closeDate_int, format_str="%Y-%m-%d %H:%M")
                account.createdat = closeDate
            except Exception as e:
                print(traceback.print_exc())
                account.createdat = None
        else:
            account.createdat = None

        account.highseastatus = highSeaStatus_mapping[account_data["sea_status"]]
        account.dbcvarchar2 = account_data["contact_phone"]

        if account_data["recent_activity_time"]:
            try:
                closeDate_int = int(account_data["recent_activity_time"])
                closeDate = timestamp13_to_str(closeDate_int, format_str="%Y-%m-%d %H:%M")
                account.recentactivityrecordtime = closeDate
            except Exception as e:
                print(traceback.print_exc())
                account.recentactivityrecordtime = None
        else:
            account.recentactivityrecordtime = None


        if not account_data["level"]:
            account.level = None
        else:
            account.level = level_mapping[account_data["level"]]
        account.save()

        # q.put((True, ""))
        print("account表成功")
        return True, ""
    except Exception as e:
        print(traceback.print_exc())
        print("account表失败")
        # q.put((False, str(e)))
        return False, ""


#同步opportunity表
def syncOpportunity(account_id, status):
    '''

    :param account_id: 客户 新id
    :param status: 客户判断是否在数据库中
    :return:
    '''
    saleStageId = {
        '产品新单-潜在商机(新)': 1172739,
        '产品新单-商机确认(新)': 1172741,
        '产品新单-商务谈判(新)': 1186830,
        '产品新单-合同确认(新)': 1172743,
        '产品新单-赢单（新）': 1209860,
        '产品新单-输单(新)': 1172744,
        '产品续单-商机确认（续）': 1186615,
        '产品续单-商务谈判（续）': 1197988,
        '产品续单-合同确认（续）': 1186616,
        '产品续单-赢单（续）': 1595051,
        '产品续单-输单（续）': 1186617,
        '项目型业务-初步沟通（项目）': 1723501,
        '项目型业务-意向客户（项目）': 1723502,
        '项目型业务-商机确认（项目）': 1723701,
        '项目型业务-需求确认（项目）': 1723503,
        '项目型业务-商务谈判（项目）': 1723504,
        '项目型业务-合同确认（项目）': 1723003,
        '项目型业务-赢单（项目）': 1723505,
        '项目型业务-输单（项目）': 1723506,
        '星光数据-初步沟通（数据）': 1850762,
        '星光数据-需求确认（数据）': 1850763,
        '星光数据-商务谈判（数据）': 1850764,
        '星光数据-合同确认（数据）': 1850765,
        '星光数据-赢单（数据）': 1850766,
        '星光数据-输单（数据）': 1850767,
        '1-建立信任阶段': 1850768,
        '2-商业调研阶段': 1850769,
        '3-业案&商案准备': 1850770,
        '4-方案验证&汇报': 1850771,
        '5-商务竞争阶段': 1850772,
        '6-合同交互阶段': 1850773,
        '7-合同签署阶段': 1850774,
        '8-合同归档阶段': 1850775,
        '8-输单': 1850776,
        '8-无效': 1850777
    }

    dbcSelect26_mapping = {
        "承诺": 1,
        '争取': 4,
        "跟进中": 2,
        "否": 0
    }
    try:
        token = '4e33e00381c94a9bba251ebb44996c0f'
        url_opportunity = 'http://192.168.16.90:8800/opportunity/api?field_name=account_id&field_value={}&token={}'.format(
            account_id, token)

        r_opportunity = requests.get(url=url_opportunity)
        if r_opportunity.json()["data"]:
            opportunity_datas = json.loads(r_opportunity.text)["data"]
        else:
            return True, ""
        '''
            {
                "code": 1,
                "data": [
                    {
                        "opportunity_name": "运营支撑0302",
                        "id": "4a804a94d0cb72fd",                           对应 Opportunity数据表中的new_opp_id
                        "account_id": "55981b376a2690e8",                   对应 Account 表中的 new_account_id 改为旧id 再存入   Opportunity表中的dbcrelation1
                        "xsy_id": "None",                                   对应 Opportunity数据表中的  id
                        "owner_id": "c472942abd99c0ce",                     对应 User表中的 new_user_id 改为旧id 再存入 Opportunity表中的 owner_id 
                        "intended_product": " 标准化产品-舆情秘书服务系统",
                        "close_date": 1914336000000,
                        "phone": "15010461883",
                        "sale_stage": "1-建立信任阶段",
                        "saler_promise": "跟进中"
                    },
                    {
                        "opportunity_name": "政务运营支撑3舆情秘书新签326",
                        "id": "24bc3f7cac5bc918",
                        "account_id": "55981b376a2690e8",
                        "xsy_id": "None",
                        "owner_id": "c472942abd99c0ce",
                        "intended_product": " 标准化产品-舆情秘书服务系统",
                        "close_date": 1914336000000,
                        "phone": "15010461883",
                        "sale_stage": "1-建立信任阶段",
                        "saler_promise": "跟进中"
                    }
                ],
                "msg": ""
            }
        '''

        for opportunity_data in opportunity_datas:
            if status:
                opportunity = Opportunity.objects.filter(new_opp_id=opportunity_data["id"]).first()
                if not opportunity:
                    opportunity = Opportunity()
            else:
                opportunity = Opportunity()
            opportunity.new_opp_id = opportunity_data["id"]

            if opportunity_data["xsy_id"] == "None":
                opportunity.id = opportunity_data["id"] + "old"
            elif opportunity_data["xsy_id"]:
                opportunity.id = opportunity_data["xsy_id"]
            else:
               opportunity.id = opportunity_data["id"] + "old"

            if opportunity_data["owner_id"]:

                user = User.objects.filter(new_user_id=opportunity_data["owner_id"]).first()
                if user:
                    opportunity.ownerid = user.id
                else:
                    opportunity.ownerid = opportunity_data["owner_id"] + "old"
            else:
                opportunity.ownerid = None


            opportunity.opportunityname = opportunity_data["opportunity_name"]
            account = Account.objects.filter(new_account_id=opportunity_data["account_id"]).first()
            if account:
                opportunity.dbcrelation1 = account.id
            else:
                opportunity.dbcrelation1 = opportunity_data["account_id"] + "old"
            opportunity.dbcselect26 = dbcSelect26_mapping[opportunity_data["saler_promise"]] if opportunity_data[
                "saler_promise"] else None
            opportunity.salestageid = saleStageId[opportunity_data["sale_stage"]]
            opportunity.dbcjoin10 = opportunity_data["phone"]
            try:
                intended_product = "".join(opportunity_data["intended_product"])  # 去掉字符串中的\xa0
                pro_name_list = more_split(intended_product)  # 将"产品1,产品2;产品3"转换为[产品1,产品2,产品3]
                pro_id_list = []
                for pro_name in pro_name_list:
                    try:
                        pro_id = custCheckbox5_dict[pro_name]
                        pro_id_list.append(pro_id)
                    except:
                        pass
                pro_id_str = ",".join(str(i) for i in pro_id_list)  # 将[1,27]转换为"1,27"
                custCheckbox5 = pro_id_str
                opportunity.custCheckbox5 = custCheckbox5
            except:
                opportunity.custCheckbox5 = ""

            if opportunity_data["close_date"]:
                try:
                    closeDate_int = int(opportunity_data["close_date"])
                    closeDate = timestamp13_to_str(closeDate_int, format_str="%Y-%m-%d %H:%M")
                    opportunity.closedate = closeDate
                except Exception as e:
                    print(traceback.print_exc())
                    opportunity.closedate = None
            else:
                opportunity.closedate = None

            opportunity.save()
        print("Opportunity表同步成功")
        return True, ""
    except Exception as e:
        print(traceback.print_exc())
        print("Opportunity表同步失败")
        # q.put((False, str(e)))
        return False,""


def casm_work(i, q):
    try:
        Crmaccountsalemapping.objects.create(
            crmuid=User.objects.filter(new_user_id=i["id"]).first().id,
            saleid=i["id"],
            salename=i["username"],
            ownerflag=2 if i["rowcause"] == "Owner" else 1,
        )
        connection.close()
        time.sleep(0.5)
        q.put(True)
    except Exception as e:
        q.put(False)
    # crmaccountsalemapping = Crmaccountsalemapping()
    # crmaccountsalemapping.crmuid = User.objects.filter(new_user_id=i["id"]).first().id
    # crmaccountsalemapping.saleid = i["id"]
    # crmaccountsalemapping.salename = i["username"]
    # crmaccountsalemapping.ownerflag = 2 if i["rowcause"] == "Owner" else 1
    # crmaccountsalemapping.save()

#同步Crmaccountsalemapping表
def syncCrmaccountsalemapping(id):
    try:
        token = '4e33e00381c94a9bba251ebb44996c0f'
        url_team = 'http://192.168.16.90:8800/user/team_member?type=account&value={}&token={}'.format(id, token)
        r_team = requests.get(url=url_team)
        account_data = json.loads(r_team.text)["data"]

        '''
        {
            "code": 1,
            "data": [
                {
                    "id": "7a71691aeae32f88",                        User表的 new_user_id  改为旧的 在存入  Crmaccountsalemapping 的id
                    "username": "无效企业客户公海池",
                    "email": "zhangwenwen@yqzbw.com",
                    "rowcause": "Owner"                              # Owner是 领导   其余 员工
                },
                {
                    "id": "79541f8b9353773f",
                    "username": "胡克雅",
                    "email": "hukeya@istarshine.com",
                    "rowcause": "All"
                }
            ],
            "msg": ""
        }
        '''
        #查询 account表的 数据
        account = Account.objects.filter(new_account_id=id).first()
        #crmuid 对应  account的 旧 id 查询删除所有
        Crmaccountsalemapping.objects.filter(crmuid=account.id).delete()
        lst = []
        for i in account_data:
            user = User.objects.filter(new_user_id=i["id"]).first()
            # Crmaccountsalemapping.objects.create(
            #     crmuid=account.id if account else None,               #存入  account 旧 id
            #     saleid=user.id,                                       #存入  用户的 旧 id
            #     salename=i["username"],
            #     ownerflag=2 if i["rowcause"] == "Owner" else 1,
            # )
            casm = Crmaccountsalemapping(
                crmuid=account.id if account else None,  # 存入  account 旧 id
                saleid=user.id,  # 存入  用户的 旧 id
                salename=i["username"],
                ownerflag=2 if i["rowcause"] == "Owner" else 1,
            )
            lst.append(casm)
        Crmaccountsalemapping.objects.bulk_create(lst)

        # qe = Queue(maxsize=len(account_data))
        # thread_list = []
        # for i in account_data:
        #     t = threading.Thread(target=casm_work, args=(i, qe))
        #     t.start()
        #     thread_list.append(t)
        #
        # for t in thread_list:
        #     t.join()
        #
        # while True:
        #     time.sleep(0.5)
        #     if qe.full():
        #         break
        #
        # while not qe.empty():
        #     r = qe.get()
        #     if not r:
        #         raise Exception
        print("Crmaccountsalemapping表同步成功")
        # q.put((True, ""))
        return True, ""
    except Exception as e:
        print("Crmaccountsalemapping表同步失败")
        print(traceback.print_exc())
        # q.put((False, str(e)))
        return False, ""


def csm(i, q):
    # crmsalemapping = Crmsalemapping()
    # crmsalemapping.crmuid = user.id if user else i["id"] + "old"
    # crmsalemapping.opportunityid = i["id"]
    # crmsalemapping.ownerflag = 2 if i["rowcause"] == "Owner" else 1
    # crmsalemapping.saleid = i["id"]
    # crmsalemapping.salename = i["username"]
    # crmsalemapping.istarshineid = hremployee.istarshine_id if hremployee else None
    # crmsalemapping.save()
    try:
        user = User.objects.filter(new_user_id=i["id"]).first()
        hremployee = HrEmployee.objects.filter(work_email=i["email"]).first()
        Crmsalemapping.objects.create(
            crmuid=user.id if user else i["id"] + "old",
            opportunityid=i["id"],
            ownerflag=2 if i["rowcause"] == "Owner" else 1,
            saleid=i["id"],
            salename=i["username"],
            istarshineid=hremployee.istarshine_id if hremployee else None
        )
        connection.close()
        time.sleep(0.5)
        q.put(True)
    except Exception as e:
        print(traceback.print_exc())
        q.put(False)

#同步crmsalemapping表
def syncCrmsalemapping(account_id):
    try:
        token = '4e33e00381c94a9bba251ebb44996c0f'
        url_opportunity = 'http://192.168.16.90:8800/opportunity/api?field_name=account_id&field_value={}&token={}'.format(
            account_id, token)
        r_opportunity = requests.get(url=url_opportunity)
        if r_opportunity.json()["data"]:
            # 获取所有 客户下的 所有商机
            opportunity_datas = json.loads(r_opportunity.text)["data"]

        else:
            return True, ""
        '''
            {
                "code": 1,
                "data": [
                    {
                        "opportunity_name": "运营支撑0302",
                        "id": "4a804a94d0cb72fd",                           对应 Opportunity数据表中的new_opp_id
                        "account_id": "55981b376a2690e8",                   对应 Account 表中的 new_account_id 改为旧id 再存入   Opportunity表中的dbcrelation1
                        "xsy_id": "None",                                   对应 Opportunity数据表中的  id
                        "owner_id": "c472942abd99c0ce",                     对应 User表中的 new_user_id 改为旧id 再存入 Opportunity表中的 owner_id 
                        "intended_product": " 标准化产品-舆情秘书服务系统",
                        "close_date": 1914336000000,
                        "phone": "15010461883",
                        "sale_stage": "1-建立信任阶段",
                        "saler_promise": "跟进中"
                    },
                    {
                        "opportunity_name": "政务运营支撑3舆情秘书新签326",
                        "id": "24bc3f7cac5bc918",
                        "account_id": "55981b376a2690e8",
                        "xsy_id": "None",
                        "owner_id": "c472942abd99c0ce",
                        "intended_product": " 标准化产品-舆情秘书服务系统",
                        "close_date": 1914336000000,
                        "phone": "15010461883",
                        "sale_stage": "1-建立信任阶段",
                        "saler_promise": "跟进中"
                    }
                ],
                "msg": ""
            }
        '''

        #查询 客户
        account = Account.objects.filter(new_account_id=account_id).first()
        #使用 客户的 旧 id 查数据  全部删掉
        Crmsalemapping.objects.filter(crmuid=account.id).delete()

        for opportunity_data in opportunity_datas:
            #循环把 所有的 商机 下的 所有 成员查询出来
            url_opportunity_team = 'http://192.168.16.90:8800/user/team_member?type=opportunity&value={}&token={}'.format(
                opportunity_data["id"], token)
            r_opportunity_team = requests.get(url=url_opportunity_team)
            opportunity_team_data = json.loads(r_opportunity_team.text)["data"]
            '''
                {
                    "code": 1,
                    "data": [
                        {
                            "id": "32c1909b917dc4c4",
                            "username": "武迎春",
                            "email": "wuyingchun@istarshine.com",
                            "rowcause": "Owner"
                        },
                        {
                            "id": "79541f8b9353773f",
                            "username": "胡克雅",
                            "email": "hukeya@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "014a71f65b29d147",
                            "username": "李德虎",
                            "email": "lidehu@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "66f61ce3f66f3f91",
                            "username": "郭申申",
                            "email": "guoshenshen@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "c6759cd194d0986e",
                            "username": "高媛",
                            "email": "gaoyuan@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "28834e09d8828134",
                            "username": "安龙波",
                            "email": "bob.an@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "93303f48669db1ce",
                            "username": "王丽群",
                            "email": "wangliqun@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "d34d6b20d09587d1",
                            "username": "罗紫薇",
                            "email": "luoziwei@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "62b69fff14ffe790",
                            "username": "肖凌",
                            "email": "xiaoling@istarshine.com",
                            "rowcause": "All"
                        },
                        {
                            "id": "e3179fd003715964",               # 这是 商机Opportunity表的 new_opp_id   改为 旧 id 放入 Crmsalemapping的 crmuid
                            "username": "李雪",
                            "email": "lixue@istarshine.com",        # 查HrEmployee表   获取istarshine_id 存入 Crmsalemapping的 istarshineid
                            "rowcause": "All"
                        }
                    ],
                    "msg": ""
                }
            '''


            lst = []
            if opportunity_team_data:
                for i in opportunity_team_data:

                    hremployee = HrEmployee.objects.filter(work_email=i["email"]).first()
                    opportunity = Opportunity.objects.filter(new_opp_id=opportunity_data["id"]).first()
                    user = User.objects.filter(new_user_id=i["id"]).first()
                    # Crmsalemapping.objects.create(
                    #     crmuid=account.id if account else i["id"] + "old",
                    #     opportunityid=opportunity.id,
                    #     ownerflag= 2 if i["rowcause"] == "Owner" else 1,
                    #     saleid=user.id,
                    #     salename=i["username"],
                    #     istarshineid= hremployee.istarshine_id if hremployee else None
                    # )
                    csm = Crmsalemapping(
                        crmuid=account.id if account else i["id"] + "old",
                        opportunityid=opportunity.id,
                        ownerflag=2 if i["rowcause"] == "Owner" else 1,
                        saleid=user.id,
                        salename=i["username"],
                        istarshineid=hremployee.istarshine_id if hremployee else None
                    )
                    lst.append(csm)
                Crmsalemapping.objects.bulk_create(lst)


        # qe = Queue(maxsize=len(opportunity_team_data))
        # thread_list = []
        # for i in opportunity_team_data:
        #     t = threading.Thread(target=csm, args=(i, qe))
        #     t.start()
        #     thread_list.append(t)
        #
        # for t in thread_list:
        #     t.join()
        #
        # while True:
        #     time.sleep(0.5)
        #     if qe.full():
        #         break
        #
        # while not qe.empty():
        #     r = qe.get()
        #     if not r:
        #         raise Exception
        print("syncCrmsalemapping同步成功")
        # q.put((True, ""))
        return True, ""
    except Exception as e:
        print(traceback.print_exc())
        print("syncCrmsalemapping同步失败")
        # q.put((False, str(e)))
        return False, ""