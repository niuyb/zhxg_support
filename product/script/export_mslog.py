"""
秘书操作日志导出脚本
AUTHOR:GJH
"""
import os
import threading
import time
import requests
import xlsxwriter
import redis
from dbutils.pooled_db import PooledDB
import pymysql
from collections import deque

OPTION_PLATFORM = {1: 'PC', 2: 'APP', 3: '微信'}
NAME = '/work/excel_log_export'


class Redis:
    def __init__(self):
        self._redis = redis.StrictRedis.from_url('redis://192.168.149.41:6666/14')
        self.ip_location = 'ip_location'  # 存放IP对应的location,有就get,没有就请求接口并存入
        self.MODE1_NAME = {int(k.decode('utf-8')): v.decode('utf-8') for k, v in self._redis.hgetall('mod1').items()}
        self.MODE2_NAME = {int(k.decode('utf-8')): v.decode('utf-8') for k, v in self._redis.hgetall('mod2').items()}

    def close_redis(self):
        self._redis.close()


class Pool(Redis):
    def __init__(self):
        super(Pool, self).__init__()
        self.POOL = PooledDB(creator=pymysql, maxconnections=10, mincached=5, maxcached=10, maxshared=0, blocking=True,
                             maxusage=None, setsession=[], ping=0, host='192.168.18.68', port=3306, user='loguser',
                             password='f693b823', database='log', charset='utf8')

    def conn_mysql(self):
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return cursor, conn

    def close_mysql(self, cursor, conn):
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass


class ExportLog(Pool):

    def __init__(self, uid, start_time, end_time):
        super(ExportLog, self).__init__()
        self.result = {}
        self.uid = uid
        self.start_time = start_time
        self.end_time = end_time
        self.queue = deque()
        self.sql_queue = deque()
        self.add_sql()

    def option_log_all(self):
        start_time = self.start_time.replace('-', '')
        end_time = self.end_time.replace('-', '')
        sql = f""" SELECT uid, uname,date,activity_self,self,phone,pc40,phone40,wechat 
                    FROM `WK_T_USERACTIVITY` WHERE date >= {start_time} AND date <= {end_time} AND uid = {self.uid}"""
        cursor, conn = self.conn_mysql()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
        except Exception as e:
            return {}
        finally:
            self.close_mysql(cursor, conn)
        return data

    def add_sql(self):
        data = self.option_log_all()
        if not data:
            self.result.update({'code': 1001, 'msg': '查询总操作日志异常'})
            return self.result
        for dic_data in data:
            date_ = dic_data['date']
            if dic_data['self'] or dic_data['phone'] or dic_data['wechat']:
                sql = f'SELECT access_date,access_type,phone,mod1,mod2,param,ip FROM mod_access_log_{date_} WHERE uid = {self.uid}'
                self.sql_queue.append({'sql': sql, 'sign': '3.0'})
            if dic_data['pc40'] or dic_data['phone40']:
                sql = f'SELECT access_date,platform,phone,mod1_name,mod2_name,request_body,ip FROM mod_access_log_40_{date_} WHERE msuid = {self.uid}'
                self.sql_queue.append({'sql': sql, 'sign': '4.0'})

    def get_ip_location(self, ip):
        if not ip:
            return ''
        location = self._redis.hget('IP_LOCATION', ip)
        if not location:
            url = "http://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php"
            data = {"query": ip, 'co': '', "resource_id": '6006'}
            response = requests.get(url=url, params=data).json()
            location = response.get('data', [{}])[0].get('location', '未查询到ip位置 ,')
            self._redis.hset('IP_LOCATION', ip, location)
        if isinstance(location, bytes):
            location = location.decode('utf-8')
        return location

    def get_data(self):
        cursor, conn = self.conn_mysql()
        while 1:
            try:
                sql_data = self.sql_queue.pop()
            except:
                self.close_mysql(conn, cursor)
                break
            try:
                cursor.execute(sql_data['sql'])
                data = cursor.fetchall()
            except Exception as e:
                print(e)
                self.result.update({'code': 1001, 'msg': '执行日志查询时出错:%s' % e})
                return
            finally:
                self.close_mysql(cursor, conn)
            sign = sql_data['sign']
            if data:
                for data_dict in data:
                    access_date = data_dict['access_date']
                    ip_location = self.get_ip_location(data_dict.get('ip'))
                    data_dict.update({'ip_location': ip_location})
                    if sign == '3.0':
                        access_ymd = access_date[0:4] + "-" + access_date[4:6] + "-" + access_date[6:8]
                        access_hms = access_date[8:10] + ":" + access_date[10:12] + ":" + access_date[12:14]
                        access_date = ' '.join([access_ymd, access_hms])
                        data_dict.update({'access_date': access_date})
                        mode1_name = self.MODE1_NAME[data_dict['mod1']]
                        mode2_name = self.MODE2_NAME[data_dict['mod2']]
                        data_dict.update({'mod1_name': mode1_name if mode1_name else ''})
                        data_dict.update({'mod2_name': mode2_name if mode2_name else ''})
                        data_dict.update({'platform': OPTION_PLATFORM.get(int(data_dict['access_type']), '')})
                    data_dict.update({'_type': sign})
                    self.queue.append(data_dict)

    def generate_log(self, filename=None):
        title = {'A1': '操作时间', 'B1': '操作平台', 'C1': '操作版本', 'D1': '一级模块', 'E1': '二级模块', 'F1': '请求体', 'G1': 'IP',
                 'H1': 'IP地域信息', 'I1': '手机号'}
        if not filename:
            filename = int(time.time() * 1000)
        # file_name = os.path.join(NAME, './{}.xlsx'.format(filename))
        file_name = os.path.join('./{}.xlsx'.format(filename))
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()
        bold_format = workbook.add_format({'bold': True})
        worksheet.set_column(1, 1, 15)
        for k, v in title.items():
            worksheet.write(k, v, bold_format)
        row = 1
        col = 0
        for data in self.queue:
            worksheet.write_string(row, col, str(data.get('access_date', '')))
            worksheet.write_string(row, col + 1, str(data.get('platform', '')))
            worksheet.write_string(row, col + 2, str(data.get('_type', '')))
            worksheet.write_string(row, col + 3, str(data.get('mod1_name', '')))
            worksheet.write_string(row, col + 4, str(data.get('mod2_name', '')))
            worksheet.write_string(row, col + 5, str(data.get('request_body', '')))
            worksheet.write_string(row, col + 6, str(data.get('ip', '')))
            worksheet.write_string(row, col + 7, str(data.get('ip_location', '')))
            worksheet.write_string(row, col + 8, str(data.get('phone', '')))
            row += 1
        workbook.close()
        self.close_redis()
        self.result.update({'code': 200, 'msg': '写入完成', 'file_name': file_name})


def main(uid, start_time, end_time):
    e = ExportLog(uid=uid, start_time=start_time, end_time=end_time)
    sql_number = len(e.sql_queue)
    thread_number = sql_number if sql_number <= 10 else 10
    thread_pool = [threading.Thread(target=e.get_data) for _ in range(thread_number)]
    for i in thread_pool:
        i.start()
    for j in thread_pool:
        j.join()
    e.generate_log()
    return e.result


if __name__ == '__main__':
    start_time = int(time.time() * 1000)
    main(uid=87984, start_time='2021-03-10', end_time='2021-03-16')
    end_time = int(time.time() * 1000)
    print(end_time - start_time)
    # e = ExportLog(uid=87984, start_time='2021-03-10', end_time='2021-03-16')
    # e.option_log_all()
