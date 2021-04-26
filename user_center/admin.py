from django.contrib import admin

from .models import UserNew

from django.contrib.auth.models import Permission, Group
from django.contrib.auth.admin import GroupAdmin

from support import support_admin
from .models import UserLog

# Register your models here.

# site = admin.site
site = support_admin.site

# @admin.register(Group, site=site)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ("id", "name")
#     fields = ("name", "permissions")
site.register(Group, GroupAdmin)

@admin.register(UserNew, site=site)
class UserNewAdmin(admin.ModelAdmin):
    search_fields = ('username', 'position', 'is_superuser', 'is_active', 'is_staff', 'status')
    list_display = ('id', 'username', 'position', 'avatar', 'is_superuser', 'is_active', 'is_staff', 'status')
    fields = ('username', 'position', 'avatar', 'is_superuser', 'is_active', 
            'is_staff', 'status', 'groups', 'user_permissions')#, 'password_md5', 'password')
            
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(UserNewAdmin, self).get_fieldsets(request, obj)

@admin.register(Permission, site=site)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "content_type", "codename")
    fields = ("name", "content_type", "codename")

@admin.register(UserLog, site=site)
class UserLogAdmin(admin.ModelAdmin):
    search_fields = ('ctime', 'model', 'object_id', 'object_repr', 'action', 'message', 'user_id', 'username')
    list_display = ('ctime', 'model', 'object_id', 'object_repr', 'action', 'message', 'user_id', 'username')