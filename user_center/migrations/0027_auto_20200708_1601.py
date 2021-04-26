# Generated by Django 2.2.4 on 2020-07-08 08:01

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0026_auto_20200708_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$gvIAKMzU6isU$UPgRICKbkiQx2chFEt7IkkXh0+NqGHjuh8lFwP7l5VY=', max_length=128, verbose_name='新后台密码'),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
