import os
import json
import math
import time
import pandas as pd
import logging
import redis
import copy
import calendar
import base64
from django.shortcuts import render
from django.conf import settings
from Industry.industry import CusrtomerIndustry
from competitor.models import CrmIndustryL1, CrmIndustryL2
from customer.models import Account, Opportunity
from multiple_api.xiaoshouyi_api import XiaoshouyiApi
from datetime import timedelta, datetime
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms import model_to_dict
from public.utils import cncurrency
from mandala.auth.decorators import login_required, permission_required
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("mobile_cloud")
# Create your views here.


@login_required()
@permission_required("mobile_cloud_index.view", login_url=URL_403)
def index(request):
    upload_file = request.FILES.get('uploadFile', None)
    if upload_file:
        # 加载行业匹配类
        CI = CusrtomerIndustry()
        # 获取一级行业
        # industry_list1 = CrmIndustryL1.objects.all().values()
        # industry_list2 = CrmIndustryL2.objects.all().values()
        xiaoshouyi = XiaoshouyiApi()
        industry1_df = pd.DataFrame(xiaoshouyi.getIndustryList(1))
        industry1_list = xiaoshouyi.getIndustryList(1)
        industry2_df = pd.DataFrame(xiaoshouyi.getIndustryList(2))
        df = pd.read_excel(upload_file, sheet_name="Sheet1")
        print(df)
        df['客户编码'] = df['客户编码'].astype('str')
        # 存入redis
        json_data = df.to_dict(orient='records')
        r = redis.Redis(host='192.168.187.55', port=6379, db=3)
        r.hset('mobile_cloud_file', str(request.user), str(json.dumps(json_data, ensure_ascii=False)))
        # 分组汇总数据
        group_df = df.groupby(['客户编码'])
        result = []
        for index, group in group_df:
            group = group.reset_index()
            data = {}
            data['account_code'] = str(group['客户编码'][0])
            data['account_name'] = group['客户名称'][0]
            data['start_date'] = str(group['订购开始时间'].min())
            data['end_date'] = str(group['订购结束时间'].min())
            data['sum_money'] = str(round(group['云合作伙伴结算金额'].sum(), 2))
            data['province'] = group['省份'][0]
            data['city'] = group['地市'][0]
            industryMap = CI.judge(group['客户名称'][0])
            data['industry1'] = industryMap[0]['cat']
            industry1_list_df = industry2_df.loc[industry2_df['label'] == industryMap[0]['cat']]
            if len(industry1_list_df) > 0 and industryMap[0]['cat'] != '其他':
                industry1_list_df = industry1_list_df.reset_index(drop=True)
                industry1_id = industry1_list_df.loc[0,'value']
            else:
                industry1_id = 1
            industry1_list_df = copy.deepcopy(industry2_df)
            for index,row in industry1_list_df.iterrows():
                if industry1_id not in row['dependentValue']:
                    industry1_list_df.drop([index], inplace=True)
            industry1_list_df.drop(['dependentValue', 'disabled'],  axis=1, inplace=True)
            data['industry2_list'] = industry1_list_df.to_dict(orient='records')
            data['industry2'] = industryMap[0]['industry']
            result.append(data)
        # 汇总结果存入redis
        r.hset('mobile_cloud_result', str(request.user), str(json.dumps(result, ensure_ascii=False)))
    return render(request, "mobile_cloud/index.html", locals())


@login_required()
@method_decorator(csrf_exempt, name='dispatch')
@permission_required("mobile_cloud_index.view", login_url=JSON_403)
def send_to_crm(request):
    data = request.POST['data']
    df1 = pd.DataFrame(json.loads(data))
    df1['account_code'] = df1['account_code'].astype('str')
    r = redis.Redis(host='192.168.187.55', port=6379, db=3)
    json_result = r.hget('mobile_cloud_result', str(request.user))
    df2 = pd.DataFrame(json.loads(json_result))
    df2['account_code'] = df2['account_code'].astype('str')
    df2 = df2.drop(['industry1', 'industry2'],  axis=1)
    # 合并数据
    df = pd.merge(df2, df1, how='inner', on='account_code')
    # 获取原始文件数据
    json_file = r.hget('mobile_cloud_file', str(request.user))
    df_file = pd.DataFrame(json.loads(json_file))
    if len(df_file) < 1:
        return JsonResponse({'status': -1000, 'msg': '文件已过期，请重新上传'})
    # return JsonResponse({'status': 100})
    xiaoshouyi = XiaoshouyiApi()
    fState_data = pd.DataFrame(xiaoshouyi.getAreList(0))
    fCity_data = pd.DataFrame(xiaoshouyi.getAreList(1))
    fCity_data['dependentValue'] = fCity_data['dependentValue'].apply(lambda x:x[0])
    fDistrict_data = pd.DataFrame(xiaoshouyi.getAreList(2))
    fDistrict_data['dependentValue'] = fDistrict_data['dependentValue'].apply(lambda x:x[0])
    result_list = []
    for key, value in df.iterrows():
        account_msg = ''
        opportunity_msg = ''
        order_msg = ''
        fState = 0
        fCity = 0
        fDistrict = 0
        # owner_id = '744537'
        owner_id = '989552'
        # depart_id = '729202508841262'
        depart_id = '1223273056518550'
        start_date = time.strftime('%Y-%m-%d', time.strptime(str(value['start_date']), '%Y%m%d'))
        end_date = time.strftime('%Y-%m-%d', time.strptime(str(value['end_date']), '%Y%m%d'))
        fState_df = fState_data.loc[fState_data['label'].str.contains(value['province'])]
        if len(fState_df) > 0:
            fState_df = fState_df.reset_index(drop=True)
            fState = fState_df.loc[0,'value']
        fCity_df = fCity_data.loc[fCity_data['label'].str.contains(value['city'])]
        if len(fCity_df) > 0:
            fCity_df = fCity_df.reset_index(drop=True)
            fCity = fCity_df.loc[0,'value']
        fDistrict_df = fDistrict_data.loc[fDistrict_data['dependentValue'] == fCity]
        if len(fDistrict_df) > 0:
            fDistrict_df = fDistrict_df.reset_index(drop=True)
            fDistrict = fDistrict_df.loc[0,'value']
        # 获取本月最后一天的时间戳 毫秒
        now = datetime.now()
        last_day = str(datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]))
        last_mtime = int(round(time.mktime(time.strptime(last_day, "%Y-%m-%d %H:%M:%S")))*1000)
        # 查询客户是否存在
        # value['account_name'] = '安徽三建工程有限公司'
        account_sql = ("select id,ownerId,dimDepart from account where accountName='{}'".format(value['account_name']))
        account_result = xiaoshouyi.queryV1(account_sql)

        if 'totalSize' in account_result and account_result['totalSize'] > 0:
            account_detail = account_result['records'][0]
            account_msg = '客户已存在'
            account_id = str(account_detail['id'])
            owner_id = str(account_detail['ownerId'])
            depart_id = str(account_detail['dimDepart'])
        else:
            # 创建客户
            account_record = {}
            account_record['accountName'] = value['account_name']
            account_record['entityType'] = '4173069'
            account_record['level'] = '5'
            account_record['dbcSelect2'] = '7'
            account_record['dbcSelect3'] = '2'
            account_record['dimDepart'] = str(depart_id)
            account_record['highSeaId'] = '239276'
            account_record['fState'] = str(fState)
            account_record['fCity'] = str(fCity)
            account_record['fDistrict'] = str(fDistrict)
            account_record['dbcSelect5'] = str(value['industry1'])
            account_record['dbcSelect9'] = str(value['industry2'])
            account_record['ownerId'] = str(owner_id)  # 744537 鲍海靖
            account_id = xiaoshouyi.createAccount(account_record)
        creted_at = int(round(time.mktime(time.strptime(datetime.now().strftime('%Y-%m-01'), "%Y-%m-%d"))*1000))
        if int(account_id) > 0:
            # 回写跳转链接
            dbc_svarchar2 = 'https://support.istarshine.com/CustomerPortrait/index?accountId=' + base64.b64encode(str(account_id).encode('utf-8')).decode('utf-8')
            account_update = {}
            account_update['dbcSVarchar2'] = dbc_svarchar2
            account_update['dbcVarchar6'] = 'YDY'+value['account_code']
            xiaoshouyi.updateAccount(account_id, account_update)
            # 添加客户主要团队成员
            xiaoshouyi.groupJoinMember(account_id, 1, ['744537'])
            if not account_msg:
                account_msg = '客户创建成功'
            opportunity_name = ('移动云-{}'.format(value['account_name']))
            # 查询商机是否存在
            opportunity_sql = (
                """
                    select id,ownerId,dimDepart from opportunity where
                    dbcRelation1='{}' and opportunityName='{}' and createdAt>{}
                """.format(account_id, opportunity_name, creted_at))
            opportunity_result = xiaoshouyi.queryV1(opportunity_sql)
            if 'totalSize' in  opportunity_result and opportunity_result['totalSize'] > 0:
                opportunity_detail = opportunity_result['records'][0]
                opportunity_msg = '商机已存在'
                opportunity_id = str(opportunity_detail['id'])
            else:
                # 创建商机
                opportunity_record = {}
                opportunity_record['opportunityName'] = opportunity_name
                opportunity_record['saleStageId'] = '1319784510538064'
                opportunity_record['ownerId'] = owner_id
                # opportunity_record['accountId'] = '16204183' #固定 中移苏州
                opportunity_record['accountId'] = account_id #测试数据
                opportunity_record['dbcRelation1'] = account_id
                opportunity_record['money'] = value['sum_money']
                opportunity_record['closeDate'] = end_date
                opportunity_record['entityType'] = '1319785962701185'
                opportunity_id = xiaoshouyi.createOpportunity(opportunity_record)
        else:
            account_msg = '客户创建失败'
        if int(opportunity_id) > 0:
            # 添加商机主要团队成员
            xiaoshouyi.groupJoinMember(opportunity_id, 3, ['744537'])
            if not opportunity_msg:
                opportunity_msg = '商机创建成功'
            # 查询订单是否存在
            order_sql = (
                """
                    select id from _order where
                    dbcRelation1='{}' and createdAt>{}
                """.format(account_id, creted_at))
            order_result = xiaoshouyi.queryV1(order_sql)
            if 'totalSize' in order_result and order_result['totalSize'] > 0:
                order_msg = '订单已存在'
                order_id = False
            else:
                # 创建订单
                days = math.ceil((int(time.mktime(time.strptime(str(value['end_date']), '%Y%m%d'))) - int(time.mktime(time.strptime(str(value['start_date']), '%Y%m%d'))))/86400)
                if 30 < days < 365:
                    days_str = str(math.ceil(days/30)) + '个月'
                elif days > 365:
                    days_str = str(math.ceil(days/365)) + '年'
                else:
                    days_str = str(days) + '天'
                order_record = {}
                order_record['ownerId'] = owner_id
                order_record['dimDepart'] = depart_id
                order_record['entityType'] = '4173225'
                order_record['contractId'] = '1056584538702175'
                order_record['dbcSelect1'] = 9
                order_record['dbcSelect4'] = 1
                order_record['dbcVarchar7'] = 'YDY'+value['account_code']
                order_record['dbcSelect9'] = 1
                order_record['dbcDate1'] = start_date
                order_record['dbcDate2'] = end_date
                order_record['dbcDate5'] = start_date
                order_record['dbcReal2'] = value['sum_money']
                order_record['dbcSelect2'] = 2
                order_record['dbcSelect7'] = 2
                order_record['dbcSelect8'] = 2
                order_record['dbcSelect19'] = 2
                order_record['dbcSelect20'] = 2
                order_record['dbcSelect23'] = 2
                order_record['dbcReal16'] = 0
                order_record['dbcSelect5'] = 1
                order_record['dbcJoin1'] = 7
                order_record['dbcSelect6'] = 2
                order_record['dbcSelect12'] = 2
                order_record['dbcSelect15'] = 2
                order_record['opportunityId'] = opportunity_id
                order_record['dbcDate11'] = last_day
                order_record['accountId'] = '16204183'  # 固定 中移苏州
                # order_record['accountId'] = account_id  # 测试数据
                order_record['dbcRelation1'] = account_id

                order_record['dbcRelation9'] = owner_id  #第一提成人
                order_record['dbcReal7'] = 0.8
                order_record['dbcRelation8'] = '744537'  #第二提成人
                order_record['dbcReal8'] = 0.2

                order_record['initAmount'] = value['sum_money']
                order_record['amount'] = value['sum_money']
                order_record['dbcVarchar16'] = cncurrency(value['sum_money'], classical=None)
                order_record['dbcVarchar17'] = days_str
                order_id = xiaoshouyi.createOrder(order_record)

        else:
            opportunity_msg = '商机创建失败'
        if int(order_id) > 0:
            # 添加商机主要团队成员
            xiaoshouyi.groupJoinMember(order_id, 35, ['744537'])
            order_msg = '订单创建成功'
            # 创建订单明细
            for keys, detail in df_file.loc[df_file['客户编码'] == value['account_code']].iterrows():
                product_record = {}
                product_record['orderId'] = order_id
                product_record['entityType'] = '4225368'
                product_record['ownerId'] = owner_id
                product_record['priceTotal'] = detail['云合作伙伴结算金额']
                # product_record['productId'] = detail['销售易产品ID']
                # product_record['dbcVarchar2'] = detail['客户名称']
                product_record['productId'] = '1261408'
                product_record['dbcVarchar2'] = '舆情秘书区县版'
                product_record['unitPrice'] = detail['云合作伙伴结算金额']
                product_record['quantity'] = 1
                product_record['dbcReal1'] = detail['云合作伙伴结算金额']
                product_record['dbcDate1'] = end_date
                product_record['dbcDate2'] = end_date
                product_record['dbcSelect1'] = 3
                product_record['dbcSelect2'] = 1
                product_record['dbcSelect3'] = 2
                xiaoshouyi.createOrderProduct(product_record)
        else:
            if not order_msg:
                order_msg = '订单创建失败'
        result_list.append('{}，{}，{}'.format(account_msg, opportunity_msg, order_msg))
    df['result'] = result_list
    file_name = ('result_{}.xls'.format(datetime.now().strftime("%Y%m%d%H%M%S")))
    file_path = os.path.join(settings.TMP_DIR, file_name)
    df.drop(['industry1', 'industry2', 'industry2_list'], axis=1, inplace=True)
    writer = pd.ExcelWriter(file_path)
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    return JsonResponse({'status': 1, 'data': file_name})
