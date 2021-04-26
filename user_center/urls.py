from django.urls import re_path, path

# from . import views
from user_center import views
from django.conf import settings

urlpatterns = [
    path(r'',views.index),
    re_path(r'^index$',views.index, name='index'),
    re_path(r'^base$',views.base, name='base'),
    re_path(r'^login$',views.LoginView.as_view(),name='login'),
    re_path(r'^logout$', views.log_out, name="logout"),
    re_path(r'^login/fast$', views.login_from_old_backend, name="login_fast"),
    re_path(r'^jump$', views.jump_to_old_backend, name="jump"),
    re_path(r'^user/log$', views.user_log, name="user_log"),
    re_path(r'^set_code$',views.set_code, name='set_code'), # 设置随机验证码
    re_path(r'^read_code$',views.read_code, name='read_code'), # 读取缓存中随机验证码
    # path('', views.login),
    # re_path(r'^active$', views.search_active_account, name="search_active_account"),
    path('mirror', views.mirror, name="mirror"),
    path('ding_talk/login', views.ding_talk_login, name="ding_talk_login"),
    path('is/logined', views.is_logined, name="is_logined"),

    # 星光资料相关
    path('user_center/material-list', views.material_list, name="material-list"),
    path('user_center/material/list', views.MaterialListView.as_view(), name="material_list"),
    path('user_center/material', views.MaterialView.as_view(), name="material"),
    path('user_center/video', views.video, name="video"),
    re_path('^user_center/video/(?P<code>.+)$', views.video_stream_handler, name="video_stream_handler"),
]

if settings.MODE in ["develop", "beta"]:
    urlpatterns.append(re_path(r'^api/quick/login$', views.quick_login, name="quick_login"))

app_name = "user_center"
