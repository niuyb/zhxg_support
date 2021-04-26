"""support URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from django.conf import settings
from support import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^center/', include('center.urls'), name='center'),

    re_path(r'^', include('user_center.urls'), name='user_center'),
    re_path('^customer/', include('customer.urls', namespace="customer")),
    re_path('^secretary/', include('secretary.urls', namespace="secretary")),
    re_path('^(.+)\.html', views.show_html),
    re_path('^json/403$', views.json_403),
    re_path('^competitor/', include('competitor.urls')),
    re_path('^sale/', include('sale.urls')),
    re_path('^notice/', include('notice.urls')),
    re_path('^statistical/', include('statistical.urls')),
    re_path('^visit/', include('salerVisit.urls')),
    re_path('^work_platform/', include('work_platform.urls')),

    re_path(r'^xman/', include('xman.urls'), name='xman'),
    re_path('^mobile_cloud/', include('mobile_cloud.urls')),
    re_path('^financial_statements/', include('financial_statements.urls')),
    re_path('^user_log/', include('user_log.urls')),
    re_path('^product/', include('product.urls')),
    re_path('^interface/', include('interface.urls')),
]

# This will work if DEBUG is True

urlpatterns += staticfiles_urlpatterns() #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

