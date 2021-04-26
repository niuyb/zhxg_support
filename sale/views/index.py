
import arrow
import random
import urllib
import datetime
import logging

from math import ceil
from django.urls import reverse
from django.http import  JsonResponse
from django.shortcuts import render

from public.utils import get_all_data, gen_date_list, gen_month_list

from django.conf import settings

# Create your views here.

logger = logging.getLogger("sale")

def sale_index(request):
    if request.method == "GET":
        return render(request, "sale/index.html", locals())


'''指定时间段内，公司每月回款情况'''
def payment_company_months_api(request):
    result = {"code": 0, "msg": "", "data": None}
    # date_list = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
    start = request.GET.get("start")
    if not start:
        start = arrow.now().floor("year")
    end = request.GET.get("end")
    date_list = gen_month_list(start=start, end=end)
    if not date_list:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    date_fmt = "%Y-%m"
    date_list = [date.strftime(date_fmt) for date in date_list]
    date_tuple = tuple(date_list)
    date_tuple_str = str(date_tuple) if len(date_tuple) > 1 else str(date_tuple).replace(",", "")
    # 计划回款
    sql1 = "SELECT FROM_UNIXTIME(planTime/1000, '{}') as ptime, SUM(amount) FROM `paymentplan` WHERE FROM_UNIXTIME(planTime/1000, '{}') in {} GROUP BY ptime;".format(date_fmt, date_fmt, date_tuple_str)
    # 实际回款
    sql2 = "SELECT FROM_UNIXTIME(planTime/1000, '{}') as ptime, SUM(actualAmount) FROM `paymentplan` WHERE FROM_UNIXTIME(planTime/1000, '{}') in {} GROUP BY ptime;".format(date_fmt, date_fmt, date_tuple_str)
    plan_data = []
    actual_data = []
    try:
        plan_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
        actual_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    except Exception as e:
        logger.error(e)
        result["code"] = -1
        result["msg"] = "服务器繁忙，请稍后重试！"
        return JsonResponse(result)
    for date in date_tuple:
        plan_data.append(plan_data_dict.get(date, 0))
        actual_data.append(actual_data_dict.get(date, 0))
    count = {
        "计划回款": {
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10,
                    # }
                }
            },
            "data": [int(i) for i in plan_data],
            "type": "bar",
            "color": "#fb9678",
            "barCategoryGap": '80%'
        },
        "实际回款": {
            "label": {
                "normal": {
                    "show": True,
                    "position": "right",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10,
                    # }
                }
            },
            "data": [int(i) for i in actual_data],
            "type": "bar",
            "color": "#00c292",
            "barCategoryGap": '80%'
        }
    }
    legend_data = ["计划回款", "实际回款"]
    series = []
    for legend in legend_data:
        _sery = count[legend]
        sery = {
            "name": legend,
            "type": 'bar',
            "stack": legend,
            "data": []
        }
        sery.update(_sery)
        series.append(sery)
    plan_all = ceil(sum(plan_data))
    actual_all = int(sum(actual_data))
    option = {
        "title": {
            "text": '{}年回款情况'.format(start.year),
            "textStyle": {"fontSize": 12},
            "subtext": '计划回款：%s元，实际回款：%s元'%(format(plan_all, ","), format(actual_all, ","))
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["data"] = option
    return JsonResponse(result)

'''指定时间段内，公司每天回款情况'''
def payment_company_days_api(request):
    result = {"code": 0, "msg": "", "data": None}
    start = request.GET.get("start")
    if not start:
        start = None
    start = arrow.get(start).floor("month")
    end = request.GET.get("end")
    if not end:
        end = start.shift(months=1).shift(days=-1)
    end = arrow.get(end)
    date_list = gen_date_list(start, end)
    if not date_list:
        result["code"] = -1
        result["msg"] = "参数错误"
        return JsonResponse(result)
    date_fmt = "%Y-%m-%d"
    date_fmt_short = "%m-%d"
    date_tuple = tuple([date.strftime(date_fmt) for date in date_list])
    date_tuple_str = str(date_tuple) if len(date_tuple) > 1 else str(date_tuple).replace(",", "")
    date_list = [date.strftime(date_fmt_short) for date in date_list]
    # 计划回款
    sql1 = "SELECT FROM_UNIXTIME(planTime/1000, '{}') as ptime, SUM(amount) FROM `paymentplan` WHERE FROM_UNIXTIME(planTime/1000, '{}') in {} GROUP BY ptime;".format(date_fmt, date_fmt, date_tuple_str)
    # 实际回款
    sql2 = "SELECT FROM_UNIXTIME(planTime/1000, '{}') as ptime, SUM(actualAmount) FROM `paymentplan` WHERE FROM_UNIXTIME(planTime/1000, '{}') in {} GROUP BY ptime;".format(date_fmt, date_fmt, date_tuple_str)
    plan_data = []
    actual_data = []
    try:
        plan_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
        actual_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    except Exception as e:
        logger.error(e)
        result["code"] = -1
        result["msg"] = "服务器繁忙，请稍后重试！"
        return JsonResponse(result)
    for date in date_tuple:
        plan_data.append(plan_data_dict.get(date, 0))
        actual_data.append(actual_data_dict.get(date, 0))
    count = {
        "计划回款": {
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "data": [int(i) for i in plan_data],
            "type": "bar",
            "color": "#fb9678",
            "barCategoryGap": '80%'
        },
        "实际回款": {
            "label": {
                "normal": {
                    "show": True,
                    "position": "right",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "data": [int(i) for i in actual_data],
            "type": "bar",
            "color": "#00c292",
            "barCategoryGap": '80%'
        }
    }
    legend_data = ["计划回款", "实际回款"]
    series = []
    for legend in legend_data:
        _sery = count[legend]
        sery = {
            "name": legend,
            "type": 'bar',
            "stack": legend,
            "data": []
        }
        sery.update(_sery)
        series.append(sery)
    plan_all = ceil(sum(plan_data))
    actual_all = int(sum(actual_data))
    params = {
        "plantime_start": start.strftime("%Y-%m-%d") if start else "",
        "plantime_end": end.strftime("%Y-%m-%d") if end else "",
        "overdue": 1
    }
    query = urllib.parse.urlencode(params)
    option = {
        "title": {
            "text": '{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '计划回款：%s元，实际回款：%s元'%(format(plan_all, ","), format(actual_all, ",")),
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                # "saveAsImage": {},
                "myDataView": {
                    "show": True,
                    "title": "查看详情",
                    "icon": "image://static/img/detail.png",
                    "url": reverse("sale:payment_plan_list") + "?" + query,
                    "onclick": None
                }
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["data"] = option
    return JsonResponse(result)

'''大区目标完成情况(财年)'''
def goal_regionals_year_api(request):
    date_list = ["一大区", "二大区", "三大区", "四大区", "五大区", "六大区", "七大区", "八大区", "九大区", "上海特区"]
    legend_data = ["大区目标", "确认归档", "实际完成"]
    now = arrow.now()
    sql1 = "Select goalName, month{} from goalDepart;".format(now.month)
    goal_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
    goal_data_list = []
    for r in date_list:
        pass
    series = [
        {   
            "name": "大区目标",  
            "stack": "目标",
            "data": [500000 + random.choice(range(1, 100)) * 10000 for _ in range(10)],
            "type": "line",
            "color": "#fb9678"
        },
        {   
            "name": "确认归档",  
            "stack": "归档",
            "data": [400000 + random.choice(range(10, 100)) * 10000 for _ in range(10)],
            "type": "bar",
            "color": "#00c292",
            "barCategoryGap": '80%'
        },
        {   
            "name": "实际完成",  
            "stack": "实际完成",
            "data": [300000 + random.choice(range(10, 100)) * 10000 for _ in range(10)],
            "type": "bar",
            "color": "#ab8ce4",
            "barCategoryGap": '80%'
        }
    ]
    
    option = {
        "title": {
            "text": ''
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {},
                "restore": {},
                "dataView": {},
                # "dataZoom": {},
                # "magicType": {},
                # "brush": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    return JsonResponse(option)

'''大区目标完成情况(某月)'''
def goal_regionals_month_api(request):
    result = {"code": 0, "msg": "", "data": {}}
    date_list = ["一大区", "二大区", "三大区", "四大区", "五大区", "六大区", "七大区", "八大区", "九大区", "上海特区"]
    legend_data = ["大区目标", "确认归档", "实际完成"]
    now = arrow.now()
    start = request.GET.get("start")
    if not start:
        start = arrow.now().floor("month")
    sql1 = "Select goalName, month{} from goalDepart;".format(now.month)
    goal_data_dict = dict(get_all_data(settings.DATABASES["contract_33"], sql1))
    goal_data_list = []
    for d in date_list:
        g = goal_data_dict.get(d + "汇总目标", 0)
        goal_data_list.append(g)
    company_month_goal = float(goal_data_dict.get("公司总目标", 0))
    goverment_month_goal = float(goal_data_dict.get("政务事业部汇总目标", 0))
    regional_name_map = dict([(2, "一大区"), (3, "二大区"), (4, "三大区"), (5, "四大区"), (6, "五大区"), (30, "六大区"), 
            (31, "七大区"), (32, "八大区"), (23, "九大区"), (33, "上海特区"), (39, "行业扩展二部"), (22, "政务客户成功部"), (7, "办公室")])
    # regional_id_list = [1, 2, 3, 4, 5, 6, 23, 28, 30, 31]#, 32, 33, 39]
    regional_id_list = [2, 3, 4, 5, 6, 30, 31, 32, 23, 33]#39, 22
    # 从商机表中根据政务事业部、区总确认合同归档日期等条件查询商机金额
    sql2 = """Select dbcSelect4, sum(money) as sum_money from `opportunity` WHERE dbcSelect3=1 
            AND dbcDate15 LIKE '%{}%' GROUP BY dbcSelect4;""".format(now.strftime("%Y-%m"))
    regional_datas = dict(get_all_data(settings.DATABASES["contract_33"], sql2))
    ok_data_list = [regional_datas.get(k, 0) for k in regional_id_list]

    #从订单中根据订单状态，按照大区查询政务事业部实际收款情况
    sql3 = """SELECT dbcSelect11, sum(amount), sum(dbcReal2) FROM `order` WHERE poStatus=2 AND dbcDate14 IS TRUE AND dbcSelect10=1 
            AND FROM_UNIXTIME(dbcDate14/1000, '%Y-%m')='{}' GROUP BY dbcSelect11;""".format(now.strftime("%Y-%m")) 
    datas = get_all_data(settings.DATABASES["contract_33"], sql3)
    regional_name_map = dict([(1, "一大区"), (2, "二大区"), (3, "三大区"), (4, "四大区"), (5, "五大区"), (33, "六大区"), (34, "七大区"), 
            (35, "八大区"), (26, "九大区"), (36, "上海特区"), (42, "行业扩展二部"), (7, "办公室"), (25, "政务客户成功部"), (None, "其他")])
    regional_id_list = [1, 2, 3, 4, 5, 33, 34, 35, 26, 36]
    # ok_data_list = []
    actual_data_list = []
    for i in regional_id_list:
        for x, y, z in datas:
            if x == i:
                # if not y:
                #     y = 0
                # ok_data_list.append(y)
                if not z:
                    z = 0
                actual_data_list.append(z)
    plan_all = int(sum(ok_data_list))
    actual_all = int(sum(actual_data_list))
    series = [
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "大区目标",  
            "stack": "目标",
            "data": [ceil(float(i)) for i in goal_data_list],
            "type": "line",
            "color": "#fb9678"
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "确认归档",  
            "stack": "归档",
            "data": [int(i) for i in ok_data_list],
            "type": "bar",
            "color": "#00c292",
            "barCategoryGap": '80%'
        },
        {   
            "label": {
                "normal": {
                    "show": True,
                    "position": "top",
                    # "textStyle": {
                    #     "color": 'black',
                    #     # "fontSize": 10
                    # }
                }
            },
            "name": "实际完成",  
            "stack": "实际",
            "data": [int(i) for i in actual_data_list],
            "type": "bar",
            "color": "#ab8ce4",
            "barCategoryGap": '80%'
        }
    ]
    
    option = {
        "title": {
            "text": '{}年{}月'.format(start.year, start.month),
            "textStyle": {"fontSize": 12},
            "subtext": '目标：%s元，区总确认归档：%s元，实际：%s元'%(format(ceil(goverment_month_goal), ","), format(plan_all, ","), format(actual_all, ","))
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {},
                "restore": {},
                "dataView": {},
                # "dataZoom": {},
                # "magicType": {},
                # "brush": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    result["code"] = 1
    result["msg"] = "数据获取成功"
    result["data"] = option
    return JsonResponse(result)

def get_data_customer(request):
    days = request.GET.get("days", 30)
    legend_data = ["总数", "试用", "正式"]
    data = {"all": {"legend_data": legend_data}, 
            "day": {"legend_data": legend_data}}
    now = datetime.datetime.now()
    date_list = []
    for _ in range(days):
        now -= datetime.timedelta(days=1)
        date = now.strftime("%Y-%m-%d")
        date_list.append(date)
    date_list.reverse()
    day_count = {"all": [], "trial": [], "formal": []}
    all_count = {"all": [], "trial": [], "formal": []}
    all_start = 10000
    trial_start = 7000
    formal_start = 3000
    for _ in range(days):
        trial = random.randint(0, 100)
        formal = random.randint(0, 30)
        _all = trial + formal
        day_count["all"].append(_all)
        day_count["trial"].append(trial)
        day_count["formal"].append(formal)
        all_start += _all
        trial_start += trial
        formal_start += formal
        all_count["all"].append(all_start)
        all_count["trial"].append(trial_start)
        all_count["formal"].append(formal_start)
    data["all"]["date_list"] = date_list
    data["all"]["count"] = all_count
    data["day"]["date_list"] = date_list
    data["day"]["count"] = day_count
    return data

def get_data_customer_all(request):
    data = get_data_customer(request)
    date_list = data["all"]["date_list"]
    count = data["all"]["count"]
    legend_data = data["all"]["legend_data"]
    option = {
        "title": {
            "text": ''
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [
            {
                "name": legend_data[0],
                "type": 'line',
                "stack": '总数',
                "data": count["all"]
            },
            {
                "name": legend_data[1],
                "type": 'line',
                "stack": '试用',
                "data": count["trial"]
            },
            {
                "name": legend_data[2],
                "type": 'line',
                "stack": '正式',
                "data": count["formal"]
            }
        ]
    }
    return JsonResponse(option)

def get_data_customer_day(request):
    data = get_data_customer(request)
    date_list = data["day"]["date_list"]
    count = data["day"]["count"]
    legend_data = data["day"]["legend_data"]
    option = {
        "title": {
            "text": ''
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [
            {
                "name": legend_data[0],
                "type": 'bar',
                "stack": '总数',
                "data": count["all"]
            },
            {
                "name": legend_data[1],
                "type": 'bar',
                "stack": '试用',
                "data": count["trial"]
            },
            {
                "name": legend_data[2],
                "type": 'bar',
                "stack": '正式',
                "data": count["formal"]
            }
        ]
    }
    return JsonResponse(option)

def get_data_money(request):
    days = request.GET.get("days", 30)
    legend_data = ["总数"]
    data = {"all": {"legend_data": legend_data}, 
            "day": {"legend_data": legend_data}}
    now = datetime.datetime.now()
    date_list = []
    for _ in range(days):
        now -= datetime.timedelta(days=1)
        date = now.strftime("%Y-%m-%d")
        date_list.append(date)
    date_list.reverse()
    day_count = {"总数": []}
    all_count = {"总数": []}
    all_start = 1000000
    for _ in range(days):
        _all = random.choice(range(0, 2000000, 10000))
        day_count["总数"].append(_all)
        all_start += _all
        all_count["总数"].append(all_start)
    data["all"]["date_list"] = date_list
    data["all"]["count"] = all_count
    data["day"]["date_list"] = date_list
    data["day"]["count"] = day_count
    return data

def get_data_money_all(request):
    data = get_data_money(request)
    date_list = data["all"]["date_list"]
    count = data["all"]["count"]
    legend_data = data["all"]["legend_data"]
    series = []
    for legend in legend_data:
        sery = {
            "name": legend,
            "type": 'line',
            "stack": legend,
            "data": count[legend]
        }
        series.append(sery)
    option = {
        "title": {
            "text": ''
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {}
            }
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    return JsonResponse(option)

def get_data_money_day(request):
    data = get_data_money(request)
    date_list = data["day"]["date_list"]
    count = data["day"]["count"]
    legend_data = data["day"]["legend_data"]
    series = []
    for legend in legend_data:
        sery = {
            "name": legend,
            "type": 'bar',
            "stack": legend,
            "data": count[legend]
        }
        series.append(sery)
    option = {
        "title": {
            "text": ''
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "x" : 'center',
            "y" : 'top',
            "itemWidth": 8,
            "itemHeight": 8,
            "textStyle":{# 图例文字的样式
                # "color":'#fff',
                "fontSize":12
            },
            "data": legend_data
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        # "toolbox": {
        #     "feature": {
        #         "saveAsImage": {}
        #     }
        # },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": date_list
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    return JsonResponse(option)
