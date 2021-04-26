import arrow

from mandala.auth import get_user_model

from customer.models import User as CrmUser
from secretary.utils import get_can_see_new
from user_center.models import HrEmployee

User = get_user_model()

# Create your views here.


def get_government_sale_center_employees(is_leaf=False):
    government_sale_center_department_code = "^ZHXG011403"
    if is_leaf:
        government_sale_center_department_code += ".{4}"
    salers = HrEmployee.objects.filter(work_activity="in_service",
            department_code__regex=government_sale_center_department_code)
    return salers

def get_government_sale_center_salers(is_leaf=True):
    istarshine_ids = list(get_government_sale_center_employees(is_leaf=is_leaf).values_list("istarshine_id", flat=True))
    salers = User.objects.filter(istarshine_id__in=istarshine_ids)
    return salers

def get_government_sale_center_salers_crm(is_leaf=True):
    istarshine_ids = list(get_government_sale_center_employees(is_leaf=is_leaf).values_list("istarshine_id", flat=True))
    salers = CrmUser.objects.filter(employeecode__in=istarshine_ids)
    return salers
    

"""通过钉钉id获取crm里面的人员"""
def get_crmusers_by_dtalkids(dtalkids):
    """返回一个queryset对象"""
    usernames = list(User.objects.filter(dtalkid__in=dtalkids).values_list("username", flat=True))
    crmusers = CrmUser.objects.filter(name__in=usernames)
    return crmusers


def get_date_range_of_month(month=None):
    """
    month: 2020-02
    """
    if month is None:
        month = arrow.now()
    else:
        month = arrow.get(month)
    start = month.floor("month")
    end = month.shift(months=1).floor("month").shift(days=-1)
    date_range = list(month.range("day", start, end))
    return date_range


def get_last_date_of_month(month=None):
    """
    month: 2020-02
    """
    if month is None:
        month = arrow.now()
    else:
        month = arrow.get(month)
    last_date = month.shift(months=1).floor("month").shift(days=-1)
    return last_date


def get_can_see_istarshine_ids(request, is_leaf=True):
    salers = get_government_sale_center_salers_crm(is_leaf=is_leaf)
    if request.user.is_superuser:
        istarshine_ids = list(salers.values_list("employeecode", flat=True))
    else:
        istarshine_ids = get_can_see_new(request.user.istarshine_id)
        # if len(istarshine_ids) > 1:
        #     istarshine_ids.remove(request.user.istarshine_id)
    return istarshine_ids

def get_can_see_istarshine_ids_new(request):
    salers = CrmUser.objects.all()
    if request.user.is_superuser:
        istarshine_ids = list(salers.values_list("employeecode", flat=True))
    else:
        istarshine_ids = get_can_see_new(request.user.istarshine_id)
        # if len(istarshine_ids) > 1:
        #     istarshine_ids.remove(request.user.istarshine_id)
    return istarshine_ids

def get_can_see_owner_ids_new(user, see_type=None):
    """
    see_type:  0，默认查看 1，查看自己 2，查看团队成员
    """
    if see_type in [1, "1"]:
        # istarshine_ids = [user.istarshine_id]
        salers = CrmUser.objects.filter(employeecode=user.istarshine_id)
    elif see_type in [2, "2"]:# 待实现
        istarshine_ids = []
        salers = None
    else:
        if user.is_superuser:
            salers = CrmUser.objects.all()
        else:
            istarshine_ids = get_can_see_new(user.istarshine_id)
            salers = CrmUser.objects.filter(employeecode__in=istarshine_ids)
    
    if salers:
        owner_ids = list(salers.values_list("id", flat=True))
    else:
        owner_ids = []
    return owner_ids

