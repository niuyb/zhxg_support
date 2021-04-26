import hashlib
import random

import pymysql
from django.conf import settings

from public.utils import parse_kwargs_for_pymysql


def inserUserindex(kusex, theNewid):
    num = random.randint(1,999999999)
    md = hashlib.md5()
    md.update(str(num).encode('utf-8'))
    md = md.hexdigest()
    data = [
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '7', 'KP_POSITION': '2', 'KP_CONDITION': '',
         'KM_ID': '10', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '10', 'KP_POSITION': '3', 'KP_CONDITION': '',
         'KM_ID': '1', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '3', 'KP_POSITION': '1', 'KP_CONDITION': '',
         'KM_ID': '3', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '9', 'KP_POSITION': '2', 'KP_CONDITION': '',
         'KM_ID': '9', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '4', 'KP_POSITION': '1', 'KP_CONDITION': '',
         'KM_ID': '4', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '1', 'KP_POSITION': '1', 'KP_CONDITION': '',
         'KM_ID': '7', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '5', 'KP_POSITION': '1', 'KP_CONDITION': '',
         'KM_ID': '5', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '6', 'KP_POSITION': '1', 'KP_CONDITION': '',
         'KM_ID': '6', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '2', 'KP_POSITION': '1', 'KP_CONDITION': '',
         'KM_ID': '2', 'KP_TYPE': '1'},
        {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '8', 'KP_POSITION': '2', 'KP_CONDITION': '',
         'KM_ID': '8', 'KP_TYPE': '1'}
    ]
    if kusex == '4':
        data = [
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '7', 'KP_POSITION': '2', 'KP_CONDITION': '',
             'KM_ID': '10', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '10', 'KP_POSITION': '3', 'KP_CONDITION': '',
             'KM_ID': '1', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '3', 'KP_POSITION': '1', 'KP_CONDITION': '',
             'KM_ID': '3', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '9', 'KP_POSITION': '2', 'KP_CONDITION': '',
             'KM_ID': '9', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '1', 'KP_POSITION': '1', 'KP_CONDITION': '',
             'KM_ID': '7', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '5', 'KP_POSITION': '1', 'KP_CONDITION': '',
             'KM_ID': '5', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '6', 'KP_POSITION': '1', 'KP_CONDITION': '',
             'KM_ID': '6', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '2', 'KP_POSITION': '1', 'KP_CONDITION': '',
             'KM_ID': '2', 'KP_TYPE': '1'},
            {'KP_ID': md, 'KU_ID': theNewid, 'KP_ALIAS': '', 'KP_ORDER': '8', 'KP_POSITION': '2', 'KP_CONDITION': '',
             'KM_ID': '8', 'KP_TYPE': '1'}
        ]
    d_list = []
    for d in data:
        d_list.append([v for k,v in  d.items()])


    kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
    conn = pymysql.connect(**kws)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''
     INSERT INTO WK_T_USERINDEX_MODULE (KP_ID,KU_ID,KP_ALIAS,KP_ORDER,KP_POSITION,KP_CONDITION) VALUES 
     (%s,%s,%s,%s,%s,%s)
    '''

    cursor.executemany(sql, d_list)
    conn.commit()

    cursor.close()
    conn.close()



