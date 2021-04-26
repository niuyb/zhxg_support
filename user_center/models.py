# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from hashlib import md5

from django.core import validators
from django.utils import six

from django.utils.translation import ugettext_lazy as _
from mandala.auth.models import (Permission, AbstractUser)

from mandala.auth.hashers import make_password, check_password
from mandala.auth.validators import UnicodeUsernameValidator

def md5_encode(string):
    return md5(string.encode("utf8")).hexdigest().upper()

"""20200708添加唯一ID字段，istarshine_id"""
class UserNew(AbstractUser):
    # username = models.CharField(verbose_name="用户名", max_length=30)
    password_md5 = models.CharField(verbose_name="老后台密码", max_length=128, default="")
    password = models.CharField(verbose_name="新后台密码", max_length=128, default=make_password("123456"))
    avatar = models.CharField(verbose_name="头像", max_length=255, blank=True, null=True, default="/static/img/a7.jpg")
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)
    # gid = models.IntegerField(blank=True, null=True)
    dtalkid = models.CharField(max_length=50, unique=True)  # Field name made lowercase.
    # passwd = models.CharField(max_length=32)
    frame = models.IntegerField(blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    # email = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(verbose_name="用户状态", blank=True, null=True) #0：关闭、1：开启、2：离职
    dingframe = models.CharField(max_length=255, blank=True, null=True)
    job = models.IntegerField(default=0)
    position = models.CharField(verbose_name="职位", max_length=127, blank=True, null=True)
    
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        # unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    ehr_department_code = models.CharField(_("ehr_department_code"), max_length=150, blank=True, null=True)
    istarshine_id = models.CharField(
        _('unique_id'),
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )
    USERNAME_FIELD = 'istarshine_id'

    class Meta:
        # managed = False
        db_table = 'support_user_new'
        verbose_name = "用户"
        verbose_name_plural = verbose_name


    def set_password(self, password):
        super(UserNew, self).set_password(password)
        self.password_md5 = md5_encode(password)

    def save(self, *args, **kwargs):
        super(UserNew, self).save(*args, **kwargs)        


class LocationInfo(models.Model):
    uuid = models.AutoField(primary_key=True)
    province = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    parent_uuid = models.CharField(max_length=40, blank=True, null=True)
    arg0 = models.CharField(max_length=50, blank=True, null=True)
    proshot = models.CharField(max_length=255, blank=True, null=True)
    lname_en = models.CharField(max_length=255, blank=True, null=True)
    lname_ft = models.CharField(max_length=255, blank=True, null=True)
    landmark_word = models.TextField(blank=True, null=True)

    class Meta:
        # managed = True
        db_table = 'location_info'
        verbose_name = "地域信息"
        verbose_name_plural = verbose_name


# class SiderBar(models.Model):
#     content = models.CharField(verbose_name="内容", max_length=255)
#     url = models.CharField(verbose_name="URL", max_length=255)
#     desc = models.CharField(verbose_name="备注", max_length=255, blank=True, null=True)
#     icon = models.CharField(verbose_name="图标", max_length=20, blank=True, null=True, default="fa-circle-o")
#     parent = models.ForeignKey("self", verbose_name="父标签", blank=True, null=True, on_delete=models.DO_NOTHING)
#     perm = models.ForeignKey(Permission, verbose_name="权限", blank=True, null=True, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'sider_bar'
#         verbose_name = "侧边栏"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.content

#     def get_perm(self):
#         if not self.perm:
#             return ""
#         return self.__class__._meta.app_label + "." + self.perm.codename


class UserLog(models.Model):
    ctime = models.DateTimeField(verbose_name="操作时间", auto_now_add=True)
    model = models.CharField(verbose_name="Model", null=True, blank=True, max_length=255)
    object_id = models.IntegerField(null=True, blank=True)
    object_repr = models.CharField(null=True, blank=True, max_length=255)
    action = models.CharField(verbose_name="动作", null=True, blank=True, max_length=255)
    message = models.CharField(verbose_name="详情", null=True, blank=True, max_length=1023) 
    user_id = models.IntegerField(verbose_name="用户ID", null=True, blank=True)
    username = models.CharField(verbose_name="用户名", null=True, blank=True, max_length=255)

    class Meta:
        db_table = 'user_log'
        verbose_name = "用户操作记录"
        verbose_name_plural = verbose_name


class HrDepartment(models.Model):
    department_code = models.CharField(primary_key=True, max_length=100)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    parent_code = models.CharField(max_length=100, blank=True, null=True)
    parent_name = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr.department'


class HrEmployee(models.Model):
    employee_number = models.BigIntegerField(primary_key=True)
    employee_name = models.CharField(max_length=100, blank=True, null=True)
    work_activity = models.CharField(max_length=100, blank=True, null=True)
    hiredate = models.CharField(max_length=50, blank=True, null=True)
    departure_time = models.CharField(max_length=50, blank=True, null=True)
    work_email = models.CharField(max_length=100, blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    dingtalk_account = models.CharField(max_length=100, blank=True, null=True)
    department_code = models.CharField(max_length=100, blank=True, null=True)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    job_code = models.CharField(max_length=100, blank=True, null=True)
    job_name = models.CharField(max_length=100, blank=True, null=True)
    identification_id = models.CharField(max_length=20, blank=True, null=True)
    istarshine_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr.employee'


class HrJob(models.Model):
    job_code = models.CharField(primary_key=True, max_length=100)
    job_name = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr.job'


class Material(models.Model):
    code = models.CharField(verbose_name="资料唯一ID", max_length=100, unique=True) #资料的唯一标识，跟id一样，防止遍历
    name = models.CharField(verbose_name="资料名称", max_length=255)
    path = models.CharField(verbose_name="路径", max_length=255)
    title = models.CharField(verbose_name="标题", max_length=255)
    comment = models.TextField(verbose_name="描述")
    typ = models.IntegerField(verbose_name="资料类型") #  2、图片   3、音频   4、视频   5、其他
    istarshine_id = models.CharField(verbose_name="创建人", max_length=100)
    ctime = models.IntegerField(verbose_name="创建时间")

    class Meta:
        managed = False
        db_table = 'material'
