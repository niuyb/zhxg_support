import os
import pandas as pd
import logging
import math
import time
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from public.utils import engine
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from mandala.auth.decorators import login_required, permission_required
from datetime import datetime
URL_403 = settings.URL_403
JSON_403 = settings.JSON_403
logger = logging.getLogger("financial_statements")
# Create your views here.

@login_required()
@permission_required("financial_statements_index.view", login_url=JSON_403)
def index(request):
    upload_file = request.FILES.get('uploadFile', None)
    if upload_file:
        df = pd.read_excel(upload_file, sheet_name="Sheet1")
        engine_xgyypt = engine(settings.DATABASES['default'])
        # 重命名表头
        columns = {
            '序号': 'serial_number',
            '发票类别': 'invoice_category',
            '合同号': 'contract_number',
            '开票日期': 'billing_date',
            '发票号码': 'invoice_number',
            '购方名称': 'purchaser_name',
            '发票金额': 'invoice_amount',
            '合计金额': 'total_amount',
            '税率': 'tax_rate',
            '合计税额': 'total_tax',
            '主要商品名称': 'commodity_name',
            '备注': 'remarks',
            '回款日期': 'payment_date',
            '回款金额': 'payment_amount',
        }
        df.rename(columns=columns, inplace=True)
        # 处理各字段类型
        df['billing_date'] = df['billing_date'].astype('str')
        df['invoice_number'] = df['invoice_number'].astype('str')
        df['invoice_amount'] = df['invoice_amount'].astype('int')
        df['total_amount'] = df['total_amount'].round(decimals=2)
        df['tax_rate'] = df['tax_rate'].astype('str')
        df['total_tax'] = df['total_tax'].round(decimals=2)
        # 删掉已存在的发票记录
        if len(df) < 10000:
            invoice_number_ids = "','".join([str(x) for x in list(df['invoice_number'])])
            invoice_number_del_sql = ("delete from financial_statements where invoice_number in('{}')".format(invoice_number_ids))
            engine_xgyypt.execute(invoice_number_del_sql)
            df.to_sql('financial_statements', engine_xgyypt, if_exists='append', index=False)
        else:
            df.to_sql('financial_statements', engine_xgyypt, if_exists='replace', index=False)
        # 修改表字段类型
        sql_update = (
            """
                ALTER table financial_statements
                MODIFY column `serial_number` bigint(20) DEFAULT NULL COMMENT '序号',
                MODIFY column `invoice_category` varchar(100) DEFAULT NULL COMMENT '发票类别',
                MODIFY column `contract_number` varchar(255) DEFAULT NULL COMMENT '合同号',
                MODIFY column `billing_date` varchar(50) DEFAULT NULL COMMENT '开票日期',
                MODIFY column `invoice_number` varchar(50) DEFAULT  NULL COMMENT '发票号码',
                MODIFY column `purchaser_name` varchar(100) DEFAULT NULL COMMENT '购方名称',
                MODIFY column `invoice_amount` bigint(20) DEFAULT NULL COMMENT '发票金额',
                MODIFY column `total_amount` varchar(50) DEFAULT NULL COMMENT '合计金额',
                MODIFY column `tax_rate` varchar(20) DEFAULT NULL COMMENT '税率',
                MODIFY column `total_tax` varchar(50) DEFAULT NULL COMMENT '合计税额',
                MODIFY column `commodity_name` varchar(100) DEFAULT NULL COMMENT '主要商品名称',
                MODIFY column `remarks` text DEFAULT NULL COMMENT '备注',
                MODIFY column `payment_date` varchar(100) DEFAULT NULL COMMENT '回款日期',
                MODIFY column `payment_amount` varchar(50) DEFAULT NULL COMMENT '回款金额'
            """)
        engine_xgyypt.execute(sql_update)
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    star_date = kws.get('star_date', '')
    end_data = kws.get('end_data', '')
    contract_number = kws.get('contract_number', '')
    invoice_number = kws.get('invoice_number', '')
    purchaser_name = kws.get('purchaser_name', '')
    return render(request, "financial_statements/index.html", locals())


@login_required()
@permission_required("financial_statements_index.view", login_url=JSON_403)
def getlist(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    page_size = kws.get('rows')
    page = kws.get('page')
    limit = (int(page) - 1)*int(page_size)
    engine_xgyypt = engine(settings.DATABASES['default'])
    where = " where 1=1 "
    if kws.get('star_date') and kws.get('end_data'):
        where += " and billing_date between '{}' and '{}'".format(kws.get('star_date'), kws.get('end_data'))
    if kws.get('contract_number'):
        where += " and contract_number='{}'".format(kws.get('contract_number'))
    if kws.get('invoice_number'):
        where += " and invoice_number='{}'".format(kws.get('invoice_number'))
    if kws.get('purchaser_name'):
        where += " and purchaser_name like \'%%{}%%\'".format(kws.get('purchaser_name'))
    count_sql = ("select count(1) as count from financial_statements {}".format(where))
    count_df = pd.read_sql_query(count_sql, engine_xgyypt)
    if len(count_df) > 0:
        records = int(count_df['count'][0])
    else:
        records = 0
    total = math.ceil(int(records)/int(page_size))
    sql = ("select * from financial_statements {} order by serial_number desc limit {},{}".format(where, limit, page_size))
    df = pd.read_sql_query(sql, engine_xgyypt)
    data = {}
    data['page'] = page
    data['total'] = total
    data['records'] = records
    data['rows'] = df.to_dict(orient='records')

    # json = {"page": "1", "total": 2, "records": "13", "rows": [{"id": "13", "cell": ["13", "2007-10-06", "Client 3", "1000.00", "0.00", "1000.00", None]}, {"id": "12", "cell": ["12", "2007-10-06", "Client 2", "700.00", "140.00", "840.00", None]}, {"id": "11", "cell": ["11", "2007-10-06", "Client 1", "600.00", "120.00", "720.00", None]}, {"id": "10", "cell": ["10", "2007-10-06", "Client 2", "100.00", "20.00", "120.00", None]}, {"id": "9", "cell": ["9", "2007-10-06", "Client 1", "200.00", "40.00", "240.00",None]}, {"id": "8", "cell": ["8", "2007-10-06", "Client 3", "200.00", "0.00", "200.00", None]}, {"id": "7", "cell": ["7", "2007-10-05", "Client 2", "120.00", "12.00", "134.00", None]}, {"id": "6", "cell": ["6", "2007-10-05", "Client 1", "50.00", "10.00", "60.00", ""]}, {"id": "5", "cell": ["5", "2007-10-05", "Client 3", "100.00", "0.00", "100.00", "no tax at all"]}, {"id": "4", "cell": ["4", "2007-10-04", "Client 3", "150.00", "0.00", "150.00", "no tax"]}], "userdata": {"amount": 3220, "tax": 342, "total": 3564, "name": "Totals: "}}
    return JsonResponse(data)

@login_required()
@permission_required("financial_statements_index.view", login_url=JSON_403)
def staging(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    star_date = kws.get('star_date', '')
    end_data = kws.get('end_data', '')
    contract_number = kws.get('contract_number', '')
    invoice_number = kws.get('invoice_number', '')
    purchaser_name = kws.get('purchaser_name', '')
    return render(request, "financial_statements/staging.html", locals())

@login_required()
@method_decorator(csrf_exempt, name='dispatch')
@permission_required("financial_statements_index.view", login_url=JSON_403)
def getStagingList(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    page_size = kws.get('rows', 30)
    page = kws.get('page',1)
    limit = (int(page) - 1)*int(page_size)
    engine_default = engine(settings.DATABASES['default'])
    engine_crm = engine(settings.DATABASES['contract_33'])
    where = ' where approvalStatus=3 '
    if kws.get('star_date') and kws.get('end_data'):
        where += " and customItem43__c between '{}' and '{}'".format(kws.get('star_date'), kws.get('end_data'))
    if kws.get('contract_number'):
        where += " and customItem37__c='{}'".format(kws.get('contract_number'))
    if kws.get('purchaser_name'):
        where += " and customItem66__c like \'%%{}%%\'".format(kws.get('purchaser_name'))
    count_sql = ("select count(1) as count from customEntity15 {}".format(where))
    count_df = pd.read_sql_query(count_sql, engine_crm)
    if len(count_df) > 0:
        records = int(count_df['count'][0])
    else:
        records = 0
    total = math.ceil(int(records)/int(page_size))
    sql = (
        """
            select a.name,a.entityType,a.customItem43__c,a.customItem66__c,a.customItem6,a.customItem30__c,a.customItem37__c,
            a.customItem53__c,a.customItem34__c,a.customItem28__c,a.customItem29__c,a.customItem50__c,
            a.customItem48__c,a.customItem40__c,a.customItem8
            from customEntity15 as a
            
            {} order by customItem43__c  desc limit {},{}
        """.format(where, limit, page_size))
    df = pd.read_sql_query(sql, engine_crm)
    # 开票类型map    
    entityType_map = {
        '100395031': '专票',
        '100387618': '普票',
    }
    # 合同类型map
    customItem30__map = {
        '1': '标准产品销售合同',
        '2': '技术服务合同',
        '3': '报告服务合同',
        '4': '数据服务合同',
        '5': '技术开发合同',
        '6': '大数据应用项目',
        '7': 'OEM定制开发',
        '8': '复合业务合同',
        '9': '标准产品服务合同',
    }
    df_entityType = []
    df_customItem28 = []
    df_customItem29 = []
    df_customItem30 = []
    df_long = []
    df_rate = []
    df_income = []
    df_average = []
    # 字段格式转换
    df['entityType'] = df['entityType'].astype('str')
    df['customItem30__c'] = df['customItem30__c'].astype('str')
    df['customItem28__c'] = df['customItem28__c'].astype('int')
    df['customItem29__c'] = df['customItem29__c'].astype('int')
    df['customItem40__c'] = df['customItem40__c'].astype('int')
    # 获取历史开票金额
    customItem37_ids = "','".join([str(x) for x in list(df['customItem37__c'])])
    history_sql = (
        """
            select contract_number as customItem37__c,total_amount from financial_statements where contract_number in ('{}')
        """.format(customItem37_ids))
    history_df = pd.read_sql_query(history_sql, engine_default)
    history_df['total_amount'] = history_df['total_amount'].astype('float')
    group_df = history_df.groupby('customItem37__c', as_index=False)['total_amount'].sum()
    # for index, group in group_df.iterrows():
    #     print(index)
    # 合并数据
    new_df = pd.merge(df, group_df, how='left', on='customItem37__c')
    # 补充字段
    for index, row in new_df.iterrows():
        time_long = 0
        rate = 0.00
        income = 0.00
        # 处理税率 不含税金额
        if row['customItem30__c'] == '1':
            rate = '13%'
            income = round(row['customItem40__c']/1.13, 2)
        else:
            rate = '6%'
            income = round(row['customItem40__c']/1.06, 2)
        df_rate.append(rate)
        df_income.append(income)
        #  处理发票类型
        df_entityType.append(entityType_map[row['entityType']])
        # 处理合同类型
        df_customItem30.append(customItem30__map[row['customItem30__c']])
        # 计算服务时长 月
        time_long = math.floor((row['customItem29__c']-row['customItem28__c'])/2592000000)
        df_long.append(time_long)
        # 月平均分摊金额
        average = round(income/time_long, 2)
        df_average.append(average)
        # 转换 日期
        df_customItem28.append(datetime.fromtimestamp(row['customItem28__c']/1000).strftime("%Y-%m-%d"))
        df_customItem29.append(datetime.fromtimestamp(row['customItem29__c']/1000).strftime("%Y-%m-%d"))
    # 字段替换
    new_df['entityType'] = df_entityType
    new_df['customItem28__c'] = df_customItem28
    new_df['customItem29__c'] = df_customItem29
    new_df['customItem30__c'] = df_customItem30
    new_df['time_long'] = df_long
    new_df['rate'] = df_rate
    new_df['income'] = df_income
    new_df['average'] = df_average
    # NaN值处理
    new_df['total_amount'] = new_df['total_amount'].fillna(0.00)
    # 重命名表头
    columns = {
        'entityType': '开票类型',
        'customItem43__c': '发票审批通过时间',
        'customItem66__c': '最终客户名称',
        'customItem6': '开票项目',
        'customItem30__c': '合同类型',
        'customItem37__c': '合同编号',
        'customItem53__c': '订单实际负责人',
        'customItem34__c': '省份',
        'customItem28__c': '合同开始日期',
        'customItem29__c': '合同结束日期',
        'customItem50__c': '赠送开始日期',
        'customItem48__c': '赠送结束日期',
        'customItem40__c': '合同金额',
        'customItem8': '开票金额',
        'time_long': '合同时长',
        'rate': '税率',
        'income': '不含税金额',
        'average': '月分摊金额',
        'total_amount': '已开票金额',
    }
    new_df.rename(columns=columns, inplace=True)
    # print(sql)
    data = {}
    data['page'] = page
    data['total'] = total
    data['records'] = records
    data['rows'] = new_df.to_dict(orient='records')
    # json = {"page": "1", "total": 2, "records": "13", "rows": [{"id": "13", "cell": ["13", "2007-10-06", "Client 3", "1000.00", "0.00", "1000.00", None]}, {"id": "12", "cell": ["12", "2007-10-06", "Client 2", "700.00", "140.00", "840.00", None]}, {"id": "11", "cell": ["11", "2007-10-06", "Client 1", "600.00", "120.00", "720.00", None]}, {"id": "10", "cell": ["10", "2007-10-06", "Client 2", "100.00", "20.00", "120.00", None]}, {"id": "9", "cell": ["9", "2007-10-06", "Client 1", "200.00", "40.00", "240.00",None]}, {"id": "8", "cell": ["8", "2007-10-06", "Client 3", "200.00", "0.00", "200.00", None]}, {"id": "7", "cell": ["7", "2007-10-05", "Client 2", "120.00", "12.00", "134.00", None]}, {"id": "6", "cell": ["6", "2007-10-05", "Client 1", "50.00", "10.00", "60.00", ""]}, {"id": "5", "cell": ["5", "2007-10-05", "Client 3", "100.00", "0.00", "100.00", "no tax at all"]}, {"id": "4", "cell": ["4", "2007-10-04", "Client 3", "150.00", "0.00", "150.00", "no tax"]}], "userdata": {"amount": 3220, "tax": 342, "total": 3564, "name": "Totals: "}}
    
    return JsonResponse(data)

@login_required()
@permission_required("financial_statements_index.view", login_url=JSON_403)
def standing_book(request):
    upload_file = request.FILES.get('uploadFile', None)
    if upload_file:
        df = pd.read_excel(upload_file, sheet_name="Sheet1")
        engine_xgyypt = engine(settings.DATABASES['default'])
        # 重命名表头
        columns = {
            '归档编号': 'filing_number',
            '归档日期': 'filing_date',
            '合同编号': 'contract_number',
            '合同审核日期': 'contract_review_date',
            '合同签订日期': 'contract_signing_date',
            '合同类型': 'contract_type',
            '标的/项目名称': 'subject_matter_name',
            '产品版本': 'product_version',
            '所属行业': 'industry',
            '合同金额': 'contract_amount',
            '实际金额': 'actual_amount',
            '合同赠买月份': 'contract_purchase_month',
            '合同生效日期': 'contract_start_date',
            '合同终止日期': 'contract_end_date',
            '合同服务月份': 'contract_service_moths',
            '合同服务年限': 'contract_service_years',
            '销售人员': 'salesman',
            '销售部门': 'sales_department',
            '所在区域': 'region',
            '客户名称（盖章客户名称）': 'customer_name',
            '最终用户名称': 'end_user_name',
            '客户类型/行业': 'customer_type',
            '代理商': 'agent',
            '省': 'province',
            '市': 'city',
            '区县': 'county',
            '合同份数': 'contract_copies',
            '是否原件': 'original',
            '合同属性': 'contract_attribute',
            '合同状态': 'contract_status',
            '赠送开始日期': 'gift_start_date',
            '赠送结束日期': 'gift_end_date',
            '赠送月份': 'gift_month',
            '赠送期限': 'gift_period',
            '备注': 'remarks',
            '续单原合同号': 'original_contract_number',
            '回款方式': 'payment_method',
            '是否一体化成单': 'single_unit',
            '代理商与用户合同是否已签订': 'been_signed',
            '关键词': 'key_word',
            '账号名称': 'account_name',
            '项目名称': 'subject_name',
            '是否为项目合同': 'projec_contract',
        }
        df.rename(columns=columns, inplace=True)
        # 处理各字段类型
        df['filing_number'] = df['filing_number'].astype('str')
        df['filing_date'] = df['filing_date'].astype('str')
        # df['invoice_amount'] = df['invoice_amount'].astype('int')
        # df['total_amount'] = df['total_amount'].round(decimals=2)
        # df['tax_rate'] = df['tax_rate'].astype('str')
        # df['total_tax'] = df['total_tax'].round(decimals=2)
        # 删掉已存在的合同记录
        # if len(df) < 10000:
        #     contract_number_ids = "','".join([str(x) for x in list(df['contract_number'])])
        #     try:
        #         contract_number_del_sql = ("delete from standing_book where contract_number in('{}')".format(contract_number_ids))
        #         engine_xgyypt.execute(contract_number_del_sql)
        #     except Exception as e:
        #         pass
        #     df.to_sql('standing_book', engine_xgyypt, if_exists='append', index=False)
        # else:
            # df.to_sql('standing_book', engine_xgyypt, if_exists='replace', index=False)
        df.to_sql('standing_book', engine_xgyypt, if_exists='append', index=False)
        # 修改表字段类型
        sql_update = (
            """
                ALTER table standing_book
                MODIFY column `filing_number` varchar(100) DEFAULT NULL COMMENT '归档编号',
                MODIFY column `filing_date` varchar(100) DEFAULT NULL COMMENT '归档日期',
                MODIFY column `contract_number` varchar(255) DEFAULT NULL COMMENT '合同编号',
                MODIFY column `contract_review_date` varchar(50) DEFAULT NULL COMMENT '合同审核日期',
                MODIFY column `contract_signing_date` varchar(50) DEFAULT  NULL COMMENT '合同签订日期',
                MODIFY column `contract_type` varchar(100) DEFAULT NULL COMMENT '合同类型',
                MODIFY column `subject_matter_name` varchar(100) DEFAULT NULL COMMENT '标的/项目名称',
                MODIFY column `product_version` varchar(50) DEFAULT NULL COMMENT '产品版本',
                MODIFY column `industry` varchar(20) DEFAULT NULL COMMENT '所属行业',
                MODIFY column `contract_amount` varchar(100) DEFAULT NULL COMMENT '合同金额',
                MODIFY column `actual_amount` varchar(100) DEFAULT NULL COMMENT '实际金额',
                MODIFY column `contract_purchase_month` varchar(100) DEFAULT NULL COMMENT '合同赠买月份',
                MODIFY column `contract_start_date` varchar(100) DEFAULT NULL COMMENT '合同生效日期',
                MODIFY column `contract_end_date` varchar(100) DEFAULT NULL COMMENT '合同终止日期',
                MODIFY column `contract_service_moths` int(11) DEFAULT NULL COMMENT '合同服务月份',
                MODIFY column `contract_service_years` varchar(100) DEFAULT NULL COMMENT '合同服务年限',
                MODIFY column `salesman` varchar(100) DEFAULT NULL COMMENT '销售人员',
                MODIFY column `sales_department` varchar(100) DEFAULT NULL COMMENT '销售部门',
                MODIFY column `region` varchar(100) DEFAULT NULL COMMENT '所在区域',
                MODIFY column `customer_name` varchar(100) DEFAULT NULL COMMENT '客户名称（盖章客户名称）',
                MODIFY column `end_user_name` varchar(100) DEFAULT NULL COMMENT '最终用户名称',
                MODIFY column `customer_type` varchar(100) DEFAULT NULL COMMENT '客户类型',
                MODIFY column `agent` varchar(100) DEFAULT NULL COMMENT '代理商',
                MODIFY column `province` varchar(100) DEFAULT NULL COMMENT '省',
                MODIFY column `city` varchar(100) DEFAULT NULL COMMENT '市',
                MODIFY column `county` varchar(100) DEFAULT NULL COMMENT '区县',
                -- MODIFY column `contract_copies` varchar(100) DEFAULT NULL COMMENT '合同份数',
                -- MODIFY column `original` varchar(100) DEFAULT NULL COMMENT '是否原件',
                MODIFY column `contract_attribute` varchar(100) DEFAULT NULL COMMENT '合同属性',
                MODIFY column `contract_status` varchar(100) DEFAULT NULL COMMENT '合同状态',
                MODIFY column `gift_start_date` varchar(100) DEFAULT NULL COMMENT '赠送开始日期',
                MODIFY column `gift_end_date` varchar(100) DEFAULT NULL COMMENT '赠送结束日期',
                MODIFY column `gift_month` varchar(100) DEFAULT NULL COMMENT '赠送月份',
                MODIFY column `gift_period` varchar(100) DEFAULT NULL COMMENT '赠送期限',
                MODIFY column `remarks` text DEFAULT NULL COMMENT '备注',
                MODIFY column `original_contract_number` varchar(100) DEFAULT NULL COMMENT '续单原合同号',
                MODIFY column `payment_method` varchar(100) DEFAULT NULL COMMENT '回款方式',
                -- MODIFY column `single_unit` varchar(100) DEFAULT NULL COMMENT '是否一体化成单',
                MODIFY column `been_signed` varchar(100) DEFAULT NULL COMMENT '代理商与用户合同是否已签订',
                -- MODIFY column `key_word` varchar(100) DEFAULT NULL COMMENT '关键词',
                MODIFY column `account_name` varchar(100) DEFAULT NULL COMMENT '账号名称',
                MODIFY column `subject_name` varchar(100) DEFAULT NULL COMMENT '项目名称',
                MODIFY column `projec_contract` varchar(50) DEFAULT NULL COMMENT '是否为项目合同'
            """)
        engine_xgyypt.execute(sql_update)
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    contract_number = kws.get('contract_number', '')
    customer_name = kws.get('customer_name', '')
    return render(request, "financial_statements/standing_book.html", locals())

@login_required()
@permission_required("financial_statements_index.view", login_url=JSON_403)
def get_standing_book(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    page_size = kws.get('rows')
    page = kws.get('page')
    limit = (int(page) - 1)*int(page_size)
    engine_xgyypt = engine(settings.DATABASES['default'])
    where = ' where 1=1 '
    if kws.get('contract_number'):
        where += " and contract_number='{}'".format(kws.get('contract_number'))
    if kws.get('customer_name'):
        where += " and customer_name like \'%%{}%%\'".format(kws.get('customer_name'))
    count_sql = ("select count(1) as count from standing_book {}".format(where))
    count_df = pd.read_sql_query(count_sql, engine_xgyypt)
    if len(count_df) > 0:
        records = int(count_df['count'][0])
    else:
        records = 0
    total = math.ceil(int(records)/int(page_size))
    sql = ("select * from standing_book {} order by filing_number desc limit {},{}".format(where, limit, page_size))
    df = pd.read_sql_query(sql, engine_xgyypt)
    # 字段格式转换
    df['contract_amount'] = df['contract_amount'].astype('int')
    df['contract_service_moths'] = df['contract_service_moths'].fillna(0)
    df['contract_service_years'] = df['contract_service_years'].fillna(0)
    data = {}
    data['page'] = page
    data['total'] = total
    data['records'] = records
    data['rows'] = df.to_dict(orient='records')

    # json = {"page": "1", "total": 2, "records": "13", "rows": [{"id": "13", "cell": ["13", "2007-10-06", "Client 3", "1000.00", "0.00", "1000.00", None]}, {"id": "12", "cell": ["12", "2007-10-06", "Client 2", "700.00", "140.00", "840.00", None]}, {"id": "11", "cell": ["11", "2007-10-06", "Client 1", "600.00", "120.00", "720.00", None]}, {"id": "10", "cell": ["10", "2007-10-06", "Client 2", "100.00", "20.00", "120.00", None]}, {"id": "9", "cell": ["9", "2007-10-06", "Client 1", "200.00", "40.00", "240.00",None]}, {"id": "8", "cell": ["8", "2007-10-06", "Client 3", "200.00", "0.00", "200.00", None]}, {"id": "7", "cell": ["7", "2007-10-05", "Client 2", "120.00", "12.00", "134.00", None]}, {"id": "6", "cell": ["6", "2007-10-05", "Client 1", "50.00", "10.00", "60.00", ""]}, {"id": "5", "cell": ["5", "2007-10-05", "Client 3", "100.00", "0.00", "100.00", "no tax at all"]}, {"id": "4", "cell": ["4", "2007-10-04", "Client 3", "150.00", "0.00", "150.00", "no tax"]}], "userdata": {"amount": 3220, "tax": 342, "total": 3564, "name": "Totals: "}}
    return JsonResponse(data)

@login_required()
@method_decorator(csrf_exempt, name='dispatch')
@permission_required("financial_statements_index.view", login_url=JSON_403)
def download_standing_book(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    engine_xgyypt = engine(settings.DATABASES['default'])
    engine_crm = engine(settings.DATABASES['contract_33'])
    where = ' where 1=1 '
    if kws.get('contract_number'):
        where += " and contract_number='{}'".format(kws.get('contract_number'))
    if kws.get('customer_name'):
        where += " and customer_name like \'%%{}%%\'".format(kws.get('customer_name'))
   
    sql = ("select filing_number,filing_date,contract_number,contract_type,subject_matter_name,product_version,industry,customer_name,contract_amount,contract_start_date,contract_end_date from standing_book {} order by contract_start_date desc".format(where))
    df = pd.read_sql_query(sql, engine_xgyypt)
    # 获取销售易订单信息
    contract_number_ids = "','".join([str(x) for x in list(df['contract_number'])])
    order_sql = (
        """
            select o.po,op.dbcVarchar4 as contract_number,op.dbcDate1,op.dbcDate2,op.dbcVarchar16,op.dbcSelect3,p.productName,op.priceTotal 
            from `orderProduct` as op left join `order` as o on op.orderId=o.id 
            left join product as p on p.id=op.productId
            where op.dbcVarchar4 in ('{}')
            order by op.dbcVarchar4
        """.format(contract_number_ids))
    order_df = pd.read_sql_query(order_sql, engine_crm)
    new_df = pd.merge(df, order_df, how='left', on='contract_number')
    # 字段格式转换
    new_df['contract_amount'] = new_df['contract_amount'].astype('float')
    new_df['priceTotal'] = new_df['priceTotal'].fillna(0)
    new_df['dbcSelect3'] = new_df['dbcSelect3'].fillna(0)
    df_rate = []
    df_amount = []
    df_income = []
    df_average = []
    df_long = []
    df_dbcSelect3 = []
    df_check = []
    # 补充字段
    for index, row in new_df.iterrows():
        # 处理税率 
        if row['dbcVarchar16'] == '标准产品销售合同':
            rate = '13%'
        elif row['dbcVarchar16'] == '复合业务合同' and int(row['dbcSelect3']) == 1:
            rate = '13%'
        else:
            rate = '6%'
        # 计算不含税金额 税额
        rate_float = 1 + float(rate.strip('%'))/100
        if int(row['priceTotal']) > 0:
            income = round(row['priceTotal']/rate_float, 2)
            amount = round(row['priceTotal']-income, 2)
        else:
            income = round(row['contract_amount']/rate_float, 2)
            amount = round(row['contract_amount']-income, 2)
        df_rate.append(rate)
        df_amount.append(amount)
        df_income.append(income)
        # 处理订单明细属性
        if int(row['dbcSelect3']) == 1:
            df_dbcSelect3.append('产品')
        elif int(row['dbcSelect3']) == 2:
            df_dbcSelect3.append('服务')
        else:
            df_dbcSelect3.append(row['dbcSelect3'])
        # 计算服务时长 月
       
        try:
            dbcDate1 = int(time.mktime(time.strptime(row['dbcDate1'], '%Y-%m-%d %H:%M')))
            dbcDate2 = int(time.mktime(time.strptime(row['dbcDate2'], '%Y-%m-%d %H:%M')))
            if dbcDate1 > dbcDate2:
                dbcDate1 = int(time.mktime(time.strptime(row['contract_start_date'], '%Y-%m-%d %H:%M:%S')))
                dbcDate2 = int(time.mktime(time.strptime(row['contract_end_date'], '%Y-%m-%d %H:%M:%S')))
        except Exception as e:
            dbcDate1 = int(time.mktime(time.strptime(row['contract_start_date'], '%Y-%m-%d %H:%M:%S')))
            dbcDate2 = int(time.mktime(time.strptime(row['contract_end_date'], '%Y-%m-%d %H:%M:%S')))
        time_long = math.floor((dbcDate2-dbcDate1)/2592000)
        
        # 月平均分摊金额
        # if time_long > 0:
        #     average = round(income/time_long, 2)
        # else:
        #     average = 0.00
        if time_long < 1:
            time_long = 1
        average = round(income/time_long, 2)
        df_long.append(time_long)
        df_average.append(average)
        # 计算月度差额
        check = income - round(average * time_long, 2)
        df_check.append(check)
        
    
    # 字段替换
    new_df['time_long'] = df_long
    new_df['tax_rate'] = df_rate
    new_df['tax_amount'] = df_amount
    new_df['total_tax'] = df_income
    new_df['average'] = df_average
    new_df['dbcSelect3'] = df_dbcSelect3
    new_df['check'] = df_check
    # 计算这十年，每年确认的月份
    for x1 in range(2020,2031):
        month_str = '{}年确认月份'.format(x1)
        df_year_value = []
        is_last = 0
        for index1, row1 in new_df.iterrows():
            year_value1 = 0
            for y1 in range(1,13):
                if y1 < 10:
                    month1 = '0{}'.format(y1)
                else:
                    month1 = str(y1)
                year_month1 = '{}-{}'.format(x1, month1)
                try:
                    dbcDate1_1 = int(time.mktime(time.strptime(row1['dbcDate1'][0:10], '%Y-%m-%d')))
                    dbcDate2_1 = int(time.mktime(time.strptime(row1['dbcDate2'][0:10], '%Y-%m-%d')))
                    if dbcDate1_1 > dbcDate2_1:
                        dbcDate1_1 = int(time.mktime(time.strptime(row1['contract_start_date'][0:10], '%Y-%m-%d')))
                        dbcDate2_1 = int(time.mktime(time.strptime(row1['contract_end_date'][0:10], '%Y-%m-%d')))
                except Exception as e:
                    dbcDate1_1 = int(time.mktime(time.strptime(row1['contract_start_date'][0:10], '%Y-%m-%d')))
                    dbcDate2_1 = int(time.mktime(time.strptime(row1['contract_end_date'][0:10], '%Y-%m-%d')))
                curent_data_1 = int(time.mktime(time.strptime(year_month1, '%Y-%m')))
                if dbcDate1_1 <= curent_data_1 <=dbcDate2_1:
                    year_value1 += 1
            if year_value1 == 0:
                year_value1 = None
            
            df_year_value.append(year_value1)
        new_df[month_str] = df_year_value

    # 计算这十年，每年确认收入
    for x3 in range(2020,2031):
        year_str = '{}年确认收入'.format(x3)
        df_year_sum = []
        is_last = 0
        for index3, row3 in new_df.iterrows():
            year_value3 = 0
            year_sum = 0
            try:
                last_year3 = int(row3['dbcDate2'][0:4])
            except Exception as e:
                last_year3 = int(row3['contract_end_date'][0:4])
            for y3 in range(1,13):
                if y3 < 10:
                    month3 = '0{}'.format(y3)
                else:
                    month3 = str(y3)
                year_month3 = '{}-{}'.format(x3, month3)
                try:
                    dbcDate1_3 = int(time.mktime(time.strptime(row3['dbcDate1'][0:10], '%Y-%m-%d')))
                    dbcDate2_3 = int(time.mktime(time.strptime(row3['dbcDate2'][0:10], '%Y-%m-%d')))
                    if dbcDate1_3 > dbcDate2_3:
                        dbcDate1_3 = int(time.mktime(time.strptime(row3['contract_start_date'][0:10], '%Y-%m-%d')))
                        dbcDate2_3 = int(time.mktime(time.strptime(row3['contract_end_date'][0:10], '%Y-%m-%d')))
                except Exception as e:
                    dbcDate1_3 = int(time.mktime(time.strptime(row3['contract_start_date'][0:10], '%Y-%m-%d')))
                    dbcDate2_3 = int(time.mktime(time.strptime(row3['contract_end_date'][0:10], '%Y-%m-%d')))
                curent_data_3 = int(time.mktime(time.strptime(year_month3, '%Y-%m')))
                if dbcDate1_3 <= curent_data_3 <=dbcDate2_3:
                    year_value3 += 1
            if year_value3 == 0:
                year_sum = None
            else:
                if last_year3 == x3:
                    year_sum = row3['average'] * year_value3 + row3['check']
                else:
                    year_sum = row3['average'] * year_value3
            
            df_year_sum.append(year_sum)
        new_df[year_str] = df_year_sum

    # 生成十年的年月
    for x2 in range(2020,2031):
        for y2 in range(1,13):
            if y2 < 10:
                month2 = '0{}'.format(y2)
            else:
                month2 = str(y2)
            year_month2 = '{}-{}'.format(x2, month2)
            df_year_month = []
            for index2, row2 in new_df.iterrows():
                try:
                    dbcDate1_2 = int(time.mktime(time.strptime(row2['dbcDate1'][0:10], '%Y-%m-%d')))
                    dbcDate2_2 = int(time.mktime(time.strptime(row2['dbcDate2'][0:10], '%Y-%m-%d')))
                    last_moth2 = int(time.mktime(time.strptime(row2['dbcDate2'][0:7], '%Y-%m')))
                    if dbcDate1_2 > dbcDate2_2:
                        dbcDate1_2 = int(time.mktime(time.strptime(row2['contract_start_date'][0:10], '%Y-%m-%d')))
                        dbcDate2_2 = int(time.mktime(time.strptime(row2['contract_end_date'][0:10], '%Y-%m-%d')))
                        last_moth2 = int(time.mktime(time.strptime(row2['contract_end_date'][0:7], '%Y-%m')))
                except Exception as e:
                    dbcDate1_2 = int(time.mktime(time.strptime(row2['contract_start_date'][0:10], '%Y-%m-%d')))
                    dbcDate2_2 = int(time.mktime(time.strptime(row2['contract_end_date'][0:10], '%Y-%m-%d')))
                    last_moth2 = int(time.mktime(time.strptime(row2['contract_end_date'][0:7], '%Y-%m')))
                curent_data_2 = int(time.mktime(time.strptime(year_month2, '%Y-%m')))
                if dbcDate1_2 <= curent_data_2 <=dbcDate2_2:
                    if last_moth2 == curent_data_2:
                        df_year_month.append(row2['average'] + row2['check'])
                    else:
                        df_year_month.append(row2['average'])
                else:
                    df_year_month.append('')
            new_df[year_month2] = df_year_month
    
            
    
    # 重命名表头
    columns = {
        'filing_number': '归档编号',
        'filing_date': '归档日期',
        'contract_number': '合同编号',
        # 'contract_review_date': '合同审核日期',
        # 'contract_signing_date': '合同签订日期',
        'contract_type': '合同类型',
        'subject_matter_name': '标的/项目名称',
        'product_version': '产品版本',
        'industry': '所属行业',
        'contract_amount': '合同金额',
        # 'actual_amount': '实际金额',
        # 'contract_purchase_month': '合同赠买月份',
        # 'contract_start_date': '合同生效日期',
        # 'contract_end_date': '合同终止日期',
        # 'contract_service_moths': '合同服务月份',
        # 'contract_service_years': '合同服务年限',
        # 'salesman': '销售人员',
        # 'sales_department': '销售部门',
        # 'region': '所在区域',
        'customer_name': '客户名称（盖章客户名称）',
        # 'end_user_name': '最终用户名称',
        # 'customer_type': '客户类型/行业',
        # 'agent': '代理商',
        # 'province': '省',
        # 'city': '市',
        # 'county': '区县',
        # 'contract_copies': '合同份数',
        # 'original': '是否原件',
        # 'contract_attribute': '合同属性',
        # 'contract_status': '合同状态',
        # 'gift_start_date': '赠送开始日期',
        # 'gift_end_date': '赠送结束日期',
        # 'gift_month': '赠送月份',
        # 'gift_period': '赠送期限',
        # 'remarks': '备注',
        # 'original_contract_number': '续单原合同号',
        # 'payment_method': '回款方式',
        # 'single_unit': '是否一体化成单',
        # 'been_signed': '代理商与用户合同是否已签订',
        # 'key_word': '关键词',
        # 'account_name': '账号名称',
        # 'subject_name': '项目名称',
        # 'projec_contract': '是否为项目合同',
        'po':'订单编号',
        'dbcVarchar16': '服务类型',
        'dbcSelect3': '订单明细属性',
        'productName': '产品名称',
        'dbcDate1': '合同开始时间',
        'dbcDate2': '合同结束时间',
        'time_long': '服务月份',
        'priceTotal': '销售金额',
        'tax_rate': '税率',
        'tax_amount': '税额',
        'total_tax': '不含税金额',
        'average': '月均摊金额',
        
    }
    new_df.rename(columns=columns, inplace=True)
    file_name = ('result_{}.xls'.format(datetime.now().strftime("%Y%m%d%H%M%S")))
    file_path = os.path.join(settings.TMP_DIR, file_name)
    writer = pd.ExcelWriter(file_path)
    new_df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    return JsonResponse({'status': 1, 'data': file_name})
