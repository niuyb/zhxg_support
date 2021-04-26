from django.db import models

# Create your models here.


from mandala.auth import get_user_model
from mandala.auth.models import Role, Permission
User = get_user_model()

# 角色和权限多对多mapping表

app_label = "xman"

class RolePermissionMapping(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = False
        app_label = app_label
        db_table = 'mandala_auth_role_permissions'
        unique_together = (('role', 'permission'),)


# 用户和角色多对多关联表
class UserRoleMapping(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='usernew_id')
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        app_label = app_label
        db_table = 'support_user_new_roles'
        unique_together = (('user', 'role'),)


# 用户和权限多对多关联表
class UserPermissionMapping(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='usernew_id')
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = False
        app_label = app_label
        db_table = 'support_user_new_user_permissions'
        unique_together = (('user', 'permission'),)

