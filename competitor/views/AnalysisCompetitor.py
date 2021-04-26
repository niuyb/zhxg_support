import json

import numpy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from mandala.auth.decorators import login_required,permission_required
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views import View

from competitor.views.CompetitorCrmApi import logger
from customer.utils import get_states
from public.utils import get_value_list
from competitor.models import CrmCompetitorMap, Competitor #, Account,Order
from customer.models import Account,Order
import pandas as pd
# from customer.utils import get_industry_l2_list
from competitor.utils import get_industry_l1_list, baseinfo
from user_center.models import UserLog
import time
from datetime import datetime,timedelta
from django.conf import settings
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403

"""竞品分析页面"""
@login_required()
@permission_required("competitor.competitor_analysis.view",login_url=URL_403)
def analysis(request):
    if request.method == "GET":
        print("zzz")
        title = "竞品分析"
        competitor_id = request.GET.get("id")
        if not competitor_id:
            competitor_id = 1
        accountstatus = get_value_list(CrmCompetitorMap,{"competitorid":competitor_id},["accountstatus"])
        accountstatus = [x[0] for x in accountstatus]
        account1 = len(list(filter(lambda x:x==1,accountstatus))) # 合作中
        account2 = len(list(filter(lambda x:x==2,accountstatus))) # 曾合作
        account3 = len(list(filter(lambda x:x==3,accountstatus))) # 未合作
        total = account1 + account2 + account3
        competitor_obj = Competitor.objects.get(competitorid=competitor_id)
        competitor_name = competitor_obj.competitorname
        remark = competitor_obj.remark
        if not remark or remark == 'None':
            remark = competitor_name +"，已知签单客户数为{}，其中与智慧星光未合作的客户数：{}个，合作中客户数：{}个，曾合作客户数：{}。".format(total,account3,account1,account2)
        # 地域分析
        init_data1 = {"row_list": [10, 20, 50], "row_num": 20}
        init_data1["col_names"] = ["签单地域", "签单个数", "总金额"]
        init_data1["col_model"] = [
            {
                "name": 'name',
                "width": 13
            },
            {
                "name": 'value',
                "width": 13,
                "sorttype": "int"
            },
            {
                "name": 'money',
                "width": 15,
                "sorttype": "int"
            }
        ]
        init_data1["items"] = []
        init_data1 = json.dumps(init_data1)

        # 金额分析
        init_data2 = {"row_list": [10, 20, 50], "row_num": 10}
        init_data2["col_names"] = ["客户名称","合作状态", "签单金额", "签单产品"]
        init_data2["col_model"] = [
            {
                "name": 'customer_name',
                "width": 13
            },
            {
                "name": 'customer_status',
                "width": 8
            },

            {
                "name": 'money',
                "width": 10,
                "sorttype": "int"
            },
            {
                "name": 'product_name',
                "width": 8,
            }
        ]
        init_data2["items"] = []
        init_data2 = json.dumps(init_data2)

        # 二级行业分析
        init_data3 = {"row_list": [10, 20, 50], "row_num": 10}
        init_data3["col_names"] = ["行业", "竞品签单量", "竞品平均金额:万", "星光签单量", "星光平均金额:万"]
        init_data3["col_model"] = [
            {
                "name": 'industry2_name',
                "width": 7
            },
            {
                "name": 'competitor_num',
                "width": 8,
                "sorttype": "int"
            },

            {
                "name": 'competitor_money',
                "width": 12,
                "sorttype": "int"
            },
            {
                "name": 'our_num',
                "width": 8,
                "sorttype": "int"
            },

            {
                "name": 'our_money',
                "width": 12,
                "sorttype": "int"
            }
        ]
        init_data3["items"] = []
        init_data3 = json.dumps(init_data3)

        # 记日志
        user = request.user
        if user.username not in ["武翠霞","丛大侠","王寅","张太锋","黄远","朱铭鑫","袁战梅"]:
            message = json.dumps(dict(request.GET))
            UserLog.objects.create(username=user.username, user_id=user.id,
                                   model="竞品分析", action="查询", message=message)
        return render(request, 'competitor/competitor_analysis.html', locals())


"""客户占有率数据接口,返回json格式数据"""
@login_required()
@permission_required("competitor.competitor_analysis.view",login_url=JSON_403)
def occupiedAnalysis(request):
    if request.method == "GET":
        result = {"status": 0, "message": "", "items": {}}
        # 计算智慧星光占有客户数量
        # items_df1 = pd.DataFrame(data=[["北京智慧星光信息技术有限公司", 500]],columns=["name","value"])

        # 计算竞品占有客户数
        crm_competitor_list = get_value_list(CrmCompetitorMap,{},["accountid","competitorid"])
        crm_competitor_df = pd.DataFrame(data=crm_competitor_list,columns=["accountid","competitorid"])

        competitor_list = get_value_list(Competitor, {}, ["competitorid", "competitorname"])
        items_df = pd.DataFrame(data=competitor_list,columns=["competitorid", "name"])
        items_df["value"] = 0

        for i, competitorid in items_df["competitorid"].items():
            mid_df = crm_competitor_df.loc[crm_competitor_df.competitorid == competitorid]
            items_df.loc[i, "value"] = len(mid_df)

        items_df = items_df.drop(['competitorid'],axis=1)
        # 增加一行智慧星光数据
        one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        timeArray = time.strptime(one_month_ago, "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))*1000
        conditions = {"postatus":2,"dbcselect3":4,"dbcdate7__gt":timeStamp}
        num = len(set(get_value_list(Order,conditions,["dbcrelation1"])))
        items_df.loc[len(items_df)] = ["北京智慧星光信息技术有限公司",num]
        # items_df = items_df1.append(items_df,ignore_index=True)
        items_df = items_df.loc[items_df.value>0]
        # print(items_df)
        items = {}
        items["data"] = list(items_df.to_dict(orient="index").values())
        items["legend"] = list(items_df["name"])
        # print(items)
        result["status"] = 1
        result["message"] = "成功"
        result["items"] = items
        return JsonResponse(result)


"""签单金额分布接口,返回json格式数据"""
@permission_required("competitor.competitor_analysis.view",login_url=JSON_403)
def moneyAnalysis(request):
    if request.method == "GET":
        result = {"status": 0, "message": "", "items": {}}
        competitor_id = request.GET.get("id")
        if not competitor_id:
            competitor_id = 1
        else:
            competitor_id = int(competitor_id)

        keys = ['5万以下', '5~10万','10~20万','20~50万','50~100万','100万+']
        # moneyList = get_value_list(CrmCompetitorMap, {"competitorid": competitor_id}, ["competitormoney"])
        # if len(moneyList):
        #     moneyList = [x[0] for x in moneyList]
        data = []
        crm_info = baseinfo(competitor_id)
        if len(crm_info):
            # print(crm_info.columns)
            item = crm_info[["customer_name","customer_status","money","product_name"]]
            moneyList = list(crm_info["money"])
            data.append(len(list(filter(lambda x:x<50000,moneyList))))
            data.append(len(list(filter(lambda x:50000<=x<100000,moneyList))))
            data.append(len(list(filter(lambda x:100000<=x<200000,moneyList))))
            data.append(len(list(filter(lambda x:200000<=x<500000,moneyList))))
            data.append(len(list(filter(lambda x:500000<=x<1000000,moneyList))))
            data.append(len(list(filter(lambda x:1000000<=x,moneyList))))
        else:
            data = [0,0,0,0,0,0]
            item = pd.DataFrame(columns=["customer_name","customer_status","money","product_name"])

        item = item.fillna('--')
        # 按照value列，降序排列
        item = item.sort_values(by="money", ascending=False)
        item["money"] = item["money"].apply(lambda x: format(x, ','))
        status = {1:"合作中",2:"曾合作",3:"未合作"}
        item["customer_status"] = item["customer_status"].apply(lambda x: status.get(x))
        # print(item)
        item = list(item.to_dict(orient="index").values())
        items = {}
        items["data"] = data
        items["keys"] = keys
        items["items"] = item
        # print(items)
        result["status"] = 1
        result["message"] = "成功"
        result["items"] = items
        return JsonResponse(result)


"""签单地域分布接口,返回json格式数据"""
@permission_required("competitor.competitor_analysis.view",login_url=JSON_403)
def localAnalysis(request):
    if request.method == "GET":
        result = {"status": 0, "message": "", "items": []}
        competitor_id = request.GET.get("id")
        if not competitor_id:
            competitor_id = 1
        else:
            competitor_id = int(competitor_id)
        keys = ['北京', '天津', '上海', '重庆', '河北', '河南', '云南', '辽宁', '黑龙江', '湖南', '安徽', '山东', '新疆',
                '江苏', '浙江', '江西', '湖北', '广西', '甘肃', '山西', '内蒙古', '陕西', '吉林', '福建', '贵州', '广东',
                '青海', '西藏', '四川', '宁夏', '海南', '台湾', '香港', '澳门','未知','南海诸岛']
        # ['customer_id', 'money', 'customer_name', 'fState', 'industry1_id',
        # 'industry2_id', 'customer_province', 'industry1_name','industry2_name']
        crm_info = baseinfo(competitor_id)
        if len(crm_info):
            # print(crm_info.columns)
            data = pd.DataFrame()
            data["name"] = pd.Series(list(set(crm_info["customer_province"])))
            data["value"] = [len(crm_info.loc[crm_info.customer_province==key]) for key in data["name"]]
            data["money"] = [crm_info.loc[crm_info.customer_province==key,"money"].sum() for key in data["name"]]

            # print('localAnalysis',data)
            # 处理地图中显示的省份名称
            data["name"] = data["name"].apply(lambda x: x[:2])
            data.loc[data.name == '黑龙',"name"] = '黑龙江'
            data.loc[data.name == '内蒙',"name"] = '内蒙古'

            data1 = pd.DataFrame()
            data1["name"] = pd.Series(list(set(keys)-set(data["name"])))
            data1["value"] = 0
            data1["money"] = 0
            # 按行拼接数据
            data = pd.concat([data, data1], axis=0, sort=False, ignore_index=True)
            # 按照value列，降序排列
            data = data.sort_values(by=["value","money"],ascending=False)
            data["money"] = data["money"].apply(lambda x:format(x,','))
        else:
            data = pd.DataFrame()
            data["name"] = keys
            data["value"] = 0
            data["money"] = 0

        # print(data)
        items = data[["name", "value"]]
        data = list(data.to_dict(orient="index").values())
        items = list(items.to_dict(orient="index").values())

        result["status"] = 1
        result["message"] = "成功"
        result["items"] = items
        result["data"] = data
        return JsonResponse(result)


"""签单一级行业分布接口,返回json格式数据"""
@permission_required("competitor.competitor_analysis.view",login_url=JSON_403)
def industryAnalysis(request):
    if request.method == "GET":
        result = {"status": 0, "message": "", "items": []}
        competitor_id = request.GET.get("id")
        if not competitor_id:
            competitor_id = 1
        else:
            competitor_id = int(competitor_id)
        items = []

        # 获取竞品签约的客户
        accountList = get_value_list(CrmCompetitorMap, {"competitorid": competitor_id}, ["accountid"])

        # 获取行业名称
        industry1_list = get_industry_l1_list()
        industry1_info = pd.DataFrame(data=industry1_list, columns=["industry1", "industry1_name"])
        industry1_info["industry1"] = industry1_info["industry1"].astype(int)

        keys = ["全部"] + list(industry1_info["industry1_name"])
        if len(accountList):
            accountList = [x[0] for x in accountList]
            if len(accountList) == 1:
                crm_condition = {"id": accountList[0]}
            else:
                crm_condition = {"id__in": accountList}
            # 查询签约客户的行业
            crminfo_list = get_value_list(Account, crm_condition, ["id", "dbcselect5", "dbcselect9"])
            crm_info = pd.DataFrame(data=crminfo_list, columns=["customer_id",  "industry1", "industry2"])
            crm_info[["industry1", "industry2"]] = crm_info[["industry1", "industry2"]].fillna(0)
            crm_info[["industry1", "industry2"]] = crm_info[["industry1", "industry2"]].astype(int)

            # 先填充签单总数
            items.append(len(crminfo_list))
            for id in industry1_info["industry1"]:
                items.append(len(crm_info.loc[crm_info.industry1 == id]))
        else:
            for key in keys:
                items.append(0)

        bar = [0]
        m = items[0]
        for i in range(1,len(items)):
            m -= items[i]
            bar.append(m)

        result["status"] = 1
        result["message"] = "成功"
        result["items"] = {'data':items,'keys':keys,'bar':bar}
        # print(result["items"])
        return JsonResponse(result)


"""签单二级行业和对应金额接口,返回json格式数据"""
@permission_required("competitor.competitor_analysis.view",login_url=JSON_403)
def industry2Analysis(request):
    pd.set_option('display.max_columns',None)
    if request.method == "GET":
        result = {"status": 0, "message": "", "items": {}}
        items = {}
        competitor_id = request.GET.get("id")
        if not competitor_id:
            competitor_id = 1
        else:
            competitor_id = int(competitor_id)
        items = {}
        # s1 = datetime.now()
        # ['customer_id', 'money', 'customer_name', 'fState', 'industry1_id',
        # 'industry2_id', 'customer_province', 'industry1_name','industry2_name']
        crm_info = baseinfo(competitor_id)
        if len(crm_info):
            # print('industry2Analysis',crm_info)
            index = list(set(crm_info["industry2_id"].astype(int)))
            # 组合竞品的二级行业和签单金额信息
            columns = ["industry2_id","industry2_name","competitor_num", "competitor_money", "our_num", "our_money"]
            df1 = pd.DataFrame(columns=columns)
            df1["industry2_id"] = index
            df1["industry2_name"] = [crm_info.loc[crm_info.industry2_id==x,"industry2_name"].iloc[0] for x in df1["industry2_id"]]
            df1["competitor_num"] = [len(crm_info.loc[crm_info.industry2_id==x]) for x in df1["industry2_id"]]

            df1["competitor_money"] = [crm_info.loc[crm_info.industry2_id==x,"money"].sum() for x in df1["industry2_id"]]
            df1["competitor_money"] = df1["competitor_money"].astype(numpy.float64)
            # df1["competitor_money"] = df1["competitor_money"].apply(lambda x:x/df1.loc[:,"competitor_num"])
            # df1["competitor_money"] = df1["competitor_money"].apply(lambda x: '%.4f' % (float(x) / 10000))
            # df1["competitor_money"] = df1["competitor_money"].astype(numpy.float64)
            # df1["competitor_money"] = df1["competitor_money"].astype(int)
            # 查询智慧星光的二级行业和金额信息
            if len(index) > 1:
                conditions1 = {"dbcselect9__in":index}
            else:
                conditions1 = {"dbcselect9": index[0]}
            account = get_value_list(Account,conditions1, ["id","dbcselect9"])
            account = pd.DataFrame(data=account,columns=["customer_id","industry2_id"])

            if len(account)>0:
                one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
                timeArray = time.strptime(one_month_ago, "%Y-%m-%d")
                timeStamp = int(time.mktime(timeArray)) * 1000
                conditions2 = {"postatus": 2, "dbcselect3": 4, "dbcdate7__gt": timeStamp}
                order = get_value_list(Order, conditions2, ["id","dbcreal2","dbcrelation1"])

                order_df = pd.DataFrame(data=order,columns=["order_id","money","customer_id"])
                order_df = pd.merge(order_df,account,how="inner",on="customer_id")
                df1["our_num"] = [len(order_df.loc[order_df.industry2_id == x]) for x in df1["industry2_id"]]
                # df1["our_num"] = df1["our_num"].astype(int)
                for index,x in df1.iterrows():
                    if x["our_num"] > 0:
                        df1.loc[index,"our_money"] = order_df.loc[order_df.industry2_id == x["industry2_id"], "money"].sum()/x["our_num"]
                    else:
                        df1.loc[index, "our_money"] = 0
                    if x["competitor_num"] >0:
                        df1.loc[index, "competitor_money"] = df1.loc[df1.industry2_id == x["industry2_id"], "competitor_money"].sum() / x["competitor_num"]
                    else:
                        df1.loc[index, "competitor_money"] = 0

                df1["our_money"] = df1["our_money"].apply(lambda x: '%.4f' % (float(x) / 10000))
                df1["our_money"] = df1["our_money"].astype(numpy.float64)
                df1["competitor_money"] = df1["competitor_money"].apply(lambda x: '%.4f' % (float(x) / 10000))
                df1["competitor_money"] = df1["competitor_money"].astype(numpy.float64)
                # print(df1)

                items["max_money"] = max(list(df1["our_money"])+list(df1["competitor_money"]))
                items["max_num"] = max(list(df1["our_num"])+list(df1["competitor_num"]))
                # print(items)


            else:
                # print(list(df1["competitor_money"]))
                df1 = df1.fillna(0)
                items["max_money"] = max(list(df1["competitor_money"]))
                items["max_num"] = max(list(df1["competitor_num"]))

            items["industry2"] = list(df1["industry2_name"])
            items["competitor_num"] = list(df1["competitor_num"])
            items["competitor_money"] = list(df1["competitor_money"])
            items["our_num"] = list(df1["our_num"])
            items["our_money"] = list(df1["our_money"])
            # 排序
            df1 = df1.sort_values(by="competitor_num", ascending=False)
            data = list(df1.to_dict(orient="index").values())
            # print(data)
        # print(datetime.now() - s1)


        result["status"] = 1
        result["message"] = "成功"
        result["items"] = items
        result["data"] = data

        return JsonResponse(result)


"""签单客户的状态更新接口,返回json格式数据"""

@method_decorator(csrf_exempt,name='dispatch')
class UpdateStatus(View):

    def post(self,request):
        return HttpResponse("hello")

    @method_decorator(permission_required("competitor.competitor_analysis.view", login_url=JSON_403))
    def get(self,request):
        # 1合作中/2曾合作/3未合作
        result = {"status": 0, "message": ""}
        account_list = list(set(CrmCompetitorMap.objects.all().values_list("accountid")))
        account_list = [x[0] for x in account_list]
        # 查询有过订单的客户id
        conditions1 = {"dbcrelation1__in": account_list}
        account2 = [x[0] for x in get_value_list(Order, conditions1, ["dbcrelation1"])]

        # 未合作的客户
        account3 = list(set(account_list)-set(account2))

        # 查询符合正式客户的客户id
        one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        timeArray = time.strptime(one_month_ago, "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray)) * 1000
        # postatus 订单状态
        # dbcselect3  合同状态
        # dbcdate7  最终合同截止日期 正式客户需要大于30天前的时间
        conditions2 = {"postatus": 2, "dbcselect3": 4, "dbcdate7__gt": timeStamp,"dbcrelation1__in":account2}
        account1 = [x[0] for x in get_value_list(Order, conditions2, ["dbcrelation1"])]

        account2 = list(set(account2) - set(account1))

        # print('合作中',len(account1),account1)
        # print('曾合作',len(account2),account2)
        # print('未合作',len(account3),account3)
        try:
            for id in account1:
                try:
                    competitor_obj = CrmCompetitorMap.objects.filter(accountid=id)
                except Exception as e:
                    logger.error("accountid=",id,str(e))
                for obj in competitor_obj:
                    obj.accountstatus = 1
                    obj.save()
            for id in account2:
                try:
                    competitor_obj = CrmCompetitorMap.objects.filter(accountid=id)
                except Exception as e:
                    logger.error("accountid=", id, str(e))
                for obj in competitor_obj:
                    obj.accountstatus = 2
                    obj.save()
            for id in account3:
                try:
                    competitor_obj = CrmCompetitorMap.objects.filter(accountid=id)
                except Exception as e:
                    logger.error("accountid=", id, str(e))
                for obj in competitor_obj:
                    obj.accountstatus = 3
                    obj.save()

            result["status"] = 200
            result["message"] = '修改竞品成功'
        except Exception as e:
            logger.error(str(e))
            result["message"] = '修改竞品失败'

        return JsonResponse(result)
