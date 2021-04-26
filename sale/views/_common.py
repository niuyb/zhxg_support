
import arrow
import logging
from mandala.auth import get_user_model

logger = logging.getLogger("sale")
User = get_user_model()

# # Create your views here.

def get_left_days(_from, _to):
    if not _to:
        _to = arrow.now()
    _to = arrow.get(_to)
    _from = arrow.get(_from)
    return (_from - _to).days

def get_left_days_by_utimestamp(_from, _to):
    if not _from:
        return 0
    _from = float(_from) / 1000
    days_left = get_left_days(_from, _to)
    if days_left < 0:
        days_left = 0
    return days_left

def translate_level(level):
    if level == 5:
        level = "正式"
    elif level == 1:
        level = "重点"
    elif level == 4:
        level = "开发"
    else:
        level = "其他"
    return level

"""生成json结果"""
def make_result(data, code, error):
    return {"data": data, "code": code, "error": error}
