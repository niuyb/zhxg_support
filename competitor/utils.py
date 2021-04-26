import numpy
import pandas as pd

from competitor.models import Competitor, Product, CrmIndustryL1, CrmIndustryL2, CrmCompetitorMap, Account
from customer.utils import get_states, get_industry_data_1, get_industry_data
from public.utils import get_value_list

def get_competitor():
    competitor = get_value_list(Competitor, {}, ["competitorid", "competitorname"])
    return competitor

def get_product():
    product = get_value_list(Product, {}, ["id", "productname"])
    product += [["0", "其他"]]
    return product

# 获取1级行业列表，每条数据结构为元组
def get_industry_l1_list():
    industry_l1 = get_value_list(CrmIndustryL1,{},["id","name"])
    return list(industry_l1) + [["0", "未知"]]

# 获取2级行业列表，每条数据结构为元组
def get_industry_l2_list():
    industry_l1 = get_value_list(CrmIndustryL2,{},["id","name"])
    return list(industry_l1) + [["0", "未知"]]


# 根据竞品id获取竞品签约的客户信息
def baseinfo(competitor_id):
    accountList = get_value_list(CrmCompetitorMap, {"competitorid": competitor_id},
                                 ["accountid", "competitormoney","competitorproductid","accountstatus"])
    if len(accountList):
        crm_competitor_info = pd.DataFrame(data=accountList, columns=["customer_id", "money","productid","customer_status"])

        # 获取产品名称
        product_list = get_product()
        product_info = pd.DataFrame(data=product_list, columns=["productid", "product_name"])

        # competitor_df1 = crm_competitor_info.loc[crm_competitor_info.productid.notnull()]
        # competitor_df2 = crm_competitor_info.loc[crm_competitor_info.productid.isnull()]
        # # print(competitor_df2)
        # competitor_df1 = pd.merge(competitor_df1, product_info, how="left", on="productid")
        crm_competitor_info = pd.merge(crm_competitor_info, product_info, how="left", on="productid")
        # # 按列拼接数据
        # competitor_df2 = pd.concat([competitor_df2, pd.DataFrame(columns=["product_name"])], sort=False)
        # print(competitor_df2)
        # 按行拼接数据
        # crm_competitor_info = pd.concat([competitor_df1, competitor_df2], axis=0, sort=False)

        accountList = list(set(crm_competitor_info["customer_id"]))
        if len(accountList) == 1:
            crm_condition = {"id": accountList[0]}
        else:
            crm_condition = {"id__in": accountList}
        crminfo_list = get_value_list(Account, crm_condition, ["id", "accountname", "fstate","dbcselect5","dbcselect9"])
        crm_info = pd.DataFrame(data=crminfo_list, columns=["customer_id", "customer_name", "fState","industry1_id","industry2_id"])
        crm_info[["fState", "industry1_id", "industry2_id"]] = crm_info[
            ["fState", "industry1_id", "industry2_id"]].fillna(0)

        crm_info = pd.merge(crm_competitor_info, crm_info, how="left", on="customer_id")
        crm_info = crm_info.loc[~ crm_info.customer_name.isna()]
        # 获取省份名称
        province_list = get_states()
        province_info = pd.DataFrame(data=province_list, columns=["fState", "customer_province"])
        province_info["fState"] = province_info["fState"].astype(numpy.int64)
        # province_info["customer_province"] = province_info["customer_province"].apply(lambda x: x[:2])


        crm_info = pd.merge(crm_info, province_info, how="left", on="fState")

        # 拼接行业数据
        industry1_data = get_industry_data_1()
        industry1_df = pd.DataFrame(industry1_data,columns=["industry1_id","industry1_name"])

        industry2_data = get_industry_data() +[{'id': 0, 'name': '未知', 'pid': 0}]
        industry2_df = pd.DataFrame(data=industry2_data)
        industry2_df = industry2_df.rename(columns={"id": "industry2_id", "name": "industry2_name"})
        industry2_df = industry2_df.drop(['pid'],axis=1)
        crm_info = pd.merge(crm_info, industry1_df,how='left',on='industry1_id')
        crm_info = pd.merge(crm_info, industry2_df,how='left',on='industry2_id')

    else:
        crm_info = []

    return crm_info
