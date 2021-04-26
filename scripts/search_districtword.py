"""
脚本功能：搜索某个代理商名下所有账号的主体词、事件词当中是否包含地域词
"""

import pandas as pd
from public.utils import engine
from support import settings

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)


def subject_info():

    conn_yqms = engine(settings.DATABASES['yqms2_199'])
    subject_info_sql = """ SELECT u.KU_LID,k.KK_NAME,k.KK_SHOULD,k.KK_EVENT 
                        FROM WK_T_USER u LEFT JOIN WK_T_KEYWS k ON u.KU_ID=k.KU_ID LEFT JOIN WK_T_USERSERVICE s ON u.KU_ID=s.KU_ID
                        WHERE u.KD_ID = '3607' AND ((k.KK_SHOULD != '') OR (k.KK_EVENT != '')) AND s.KU_USERSTATUS = '1' """
    subject_info_df = pd.read_sql_query(subject_info_sql, conn_yqms)

    conn_yqms.close()
    # print(subject_info_df)
    return subject_info_df


def district_words():
    conn_yqht = engine(settings.DATABASES['yqht_199'])
    province_words_sql = """ SELECT DISTINCT province FROM b_locationinfo """
    province_words_df = pd.read_sql_query(province_words_sql, conn_yqht)
    city_words_sql = """ SELECT DISTINCT city FROM b_locationinfo WHERE city != '' """
    city_words_df = pd.read_sql_query(city_words_sql, conn_yqht)
    county_words_sql = """ SELECT DISTINCT county FROM b_locationinfo WHERE county != '' """
    county_words_df = pd.read_sql_query(county_words_sql, conn_yqht)

    conn_yqht.close()
    return province_words_df, city_words_df, county_words_df


def compare_data():
    result_df = pd.DataFrame(columns=['账号名', '专题名称', '主体词', '事件词'])

    subject_info_df = subject_info()
    subject_info_df = subject_info_df.rename(columns={'KU_LID':'账号名', 'KK_NAME':'专题名称', 'KK_SHOULD':'主体词', 'KK_EVENT':'事件词' })
    province_words_df, city_words_df, county_words_df = district_words()
    province_words_df = province_words_df.rename(columns={'province':'district'})   # 替换列名为'district'
    city_words_df = city_words_df.rename(columns={'city':'district'})
    county_words_df = county_words_df.rename(columns={'county':'district'})
    district_words_df = province_words_df
    district_words_df = district_words_df.append(city_words_df)
    district_words_df = district_words_df.append(county_words_df)
    district_words_df['district'].drop_duplicates(keep='first')    # 去重，只保留第一次出现的

    district_words_list = []

    for index, row in subject_info_df.iterrows():
        # kk_should = subject_info_df.loc[index, '主体词']
        # kk_event = subject_info_df.loc[index, '事件词']
        kk_should = row['主体词']
        kk_event = row['事件词']
        for index2, row2 in district_words_df.iterrows():
            district_word = row2["district"]    #地域词

            if len(district_word) >= 3:
                # if (district_word[-1:] == '省') or (district_word[-1:] == '市') or (district_word[-1:] == '县') or (district_word[-1:] == '区'):
                #     district_word = district_word[:-1]  # 没有‘省’、‘市’、‘县’、‘区’这个字的地域词
                if district_word == ('宁夏回族自治区' or '广西壮族自治区' or '澳门特别行政区' or '香港特别行政区'):
                    district_word = district_word[0:2]  # 只取前两个字
                elif district_word == '内蒙古自治区':
                    district_word = district_word[0:3]  # 只取前三个字

            if (district_word in kk_should) or (district_word in kk_event):

                district_words_list.append(district_word)


        if district_words_list != []:
            row['主体词或事件词中，包含的地域词'] = district_words_list
            result_df = result_df.append(row, ignore_index=True)

        district_words_list = []


    return result_df





if __name__ == '__main__':
    compare_data().to_excel(r"D:\script_result\结果.xlsx", encoding="utf_8_sig")

