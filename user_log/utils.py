import numpy
import pandas as pd
from user_log.models import NewUserLog
from public.utils import get_value_list


# def get_user_log():
#     user_log = get_value_list(NewUserLog, {}, ["id", "username"])
#     return user_log

#获取操作类型--action
def get_user_action():
    # 实现方式1
    user_action = list(set(list(NewUserLog.objects.values_list("action", "action"))))
    # 实现方式2
    # user_action = []
    # user_action_set = set(list(NewUserLog.objects.values_list("action", flat=True)))
    # for action in user_action_set:
    #     user_action.append((action, action))
    return user_action





