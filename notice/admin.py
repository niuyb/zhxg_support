from django.contrib import admin

from support import support_admin
from .models import NoticeType, NoticeList, NoticeSetting

# Register your models here.

# site = admin.site
site = support_admin.site

@admin.register(NoticeType, site=site)
class NoticeTypeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'comment')
    list_display = ('id', 'name', 'comment')
    fields = ('name', 'comment')
            
    ordering = ('id',)
    # filter_horizontal = ('groups', 'user_permissions',)

    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         return self.add_fieldsets
    #     return super(UserNewAdmin, self).get_fieldsets(request, obj)

@admin.register(NoticeList, site=site)
class NoticeListAdmin(admin.ModelAdmin):
    # search_fields = ("ding_user", "content")
    list_display = ("id", "ding_user", "content", "notice_type", "object_type", "object_id", "status")
    fields = ("content", "ding_user", "notice_type", "object_type", "object_id", "status")

    list_filter = ("ding_user", "notice_type", "object_type")

@admin.register(NoticeSetting, site=site)
class NoticeSettingAdmin(admin.ModelAdmin):
    # search_fields = ("ding_user",)
    list_display = ("id", "ding_user", "notice_type", "status")
    fields = ("status", "notice_type", "ding_user")

    list_filter = ("notice_type", "status", "ding_user")
