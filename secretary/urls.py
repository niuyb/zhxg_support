from django.urls import re_path, path

from secretary import views

urlpatterns = [
    re_path(r'^api/departments$', views.departments_api, name="departments_api"),
]

app_name = "secretary"
