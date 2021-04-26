import pymysql
from django.conf import settings

from public.utils import parse_kwargs_for_pymysql


def yqmsSynchroUpdate(tab_name,where,uid, data):
    if settings.MODE == 'develop' or settings.MODE == 'beta':
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_32"])
    else:
        kws = parse_kwargs_for_pymysql(settings.DATABASES["yqms2_199"])
    conn = pymysql.connect(**kws)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    set = ", ".join('`{}` = "{}"'.format(k,v) for k,v in data.items())

    sql = '''
        UPDATE {} SET {} WHERE {} = '{}'
    '''.format(tab_name,set,where, uid)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()