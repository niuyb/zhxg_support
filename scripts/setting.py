databases = {    
    'default': {'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xgyypt',
        'USER': 'root',
        'PASSWORD': '1CzoOCywfJ*h',
        'HOST': '192.168.185.33',
        'PORT':3306,
        'OPTIONS':{'isolation_level':None}
    },
    'yqms2_32': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yqms2',
        'USER': 'fbeta',
        'PASSWORD': '9yacto9659d',
        'HOST': '192.168.30.2',
        'PORT':3306,
        'OPTIONS':{'isolation_level':None}
    },

    'contract_33': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'contract',
        'USER': 'root',
        'PASSWORD': '1CzoOCywfJ*h',
        'HOST': '192.168.185.33',
        'PORT':3306,
        'OPTIONS':{'isolation_level':None}
    },
    'yqms2_199': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yqms2',
        'USER': 'fuser',
        'PASSWORD': '97yu1r221pxeyt3',
        'HOST': '192.168.16.199',
        'PORT':3306,
        'OPTIONS':{'isolation_level':None}
    },
    'log_120': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'log',
        'USER': 'loguser',
        'PASSWORD': 'f693b823',
        'HOST': '192.168.19.120',
        'PORT':3306,
        'OPTIONS':{'isolation_level':None}
    },
    'yqht_199': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yqht',
        'USER': 'fuser',
        'PASSWORD': '97yu1r221pxeyt3',
        'HOST': '192.168.16.199',
        'PORT':3306,
        'OPTIONS':{'isolation_level':None}
    },
}


"""将settings中的数据库参数转换成pymysql能够接收的参数"""
def parse_kwargs_for_pymysql(kwargs):
    host = kwargs.get("HOST")
    user = kwargs.get("USER")
    password = kwargs.get("PASSWORD")
    port = kwargs.get("PORT")
    database = kwargs.get("NAME")
    charset = kwargs.get("CHARSET", "utf8")
    return {
        "host": host, 
        "port": port, 
        "database": database, 
        "user": user, 
        "password": password, 
        "charset": charset
    }

