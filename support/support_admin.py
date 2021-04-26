"""
因为登录、登出都是自定义的函数，
而adminsite中的login, logout等无法正常登录登出，
所以需要重写AdminSite
"""

from django.contrib.admin import AdminSite

from user_center.views import LoginView, log_out

class SupportSite(AdminSite):
    site_header = "星光运营平台"
    site_title = "星光运营平台-后台管理"
    index_title = "首页"

    def login(self, request, extra_context=None):
        return LoginView.as_view()(request)

    def logout(self, request, extra_context=None):
        return log_out(request)

site = SupportSite(name='support_admin')