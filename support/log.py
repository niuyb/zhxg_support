import os
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#LOGGING_DIR 日志文件存放目录
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/all.log',  # 日志输出文件
            'maxBytes': 1024 * 1024 * 10,  # 文件大小
            'backupCount': 10,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/error.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'user_center': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/user_center.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'customer': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/customer.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'competitor': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/competitor.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'secretary': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/secretary.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'recorder': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/recorder.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'sale': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/sale.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'notice': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/notice.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
        'mobile_cloud': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '%s/mobile_cloud.log' % LOG_DIR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
    },
    'loggers': {
        'default': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'django': {
            'handlers': ['default', 'console', 'mail_admins'],
            'level': 'INFO',
            'propagate': False
        },
        'user_center': {
            'handlers': ['user_center', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'customer': {
            'handlers': ['customer', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'competitor': {
            'handlers': ['competitor', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'secretary': {
            'handlers': ['secretary', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'recorder': {
            'handlers': ['recorder', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sale': {
            'handlers': ['sale', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'notice': {
            'handlers': ['notice', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'mobile_cloud': {
            'handlers': ['mobile_cloud', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
#########################
## Django Logging  END
#########################
