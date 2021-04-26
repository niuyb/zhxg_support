
from django.shortcuts import render
from mandala.auth.decorators import login_required, permission_required

from django.conf import settings
URL_403 = settings.URL_403

@login_required
@permission_required("sale.department_portrait.view", login_url=URL_403)
def department_portrait(request):
    title = "政务销售中心 - 一大区"
    base_info = {"department_name": "一大区"}
    return render(request, "sale/department_portrait.html", locals())
