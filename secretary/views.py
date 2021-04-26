from django.urls import reverse
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from mandala.auth import get_user_model
from mandala.auth.decorators import login_required, permission_required
from django.forms import model_to_dict

from django.conf import settings

# Create your views here.

from secretary.utils import get_ding_groups

@login_required
def departments_api(request):
    if request.method == "GET":
        kws = request.GET
    else:
        kws = request.POST
    dpid = kws.get("dpid")
    departments = get_ding_groups(dpid)
    return JsonResponse(departments)

    