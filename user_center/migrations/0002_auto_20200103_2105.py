# Generated by Django 2.2.4 on 2020-01-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$i9l9P1N0YWu0$Rk3k7ylNgGLV99zkhRfLfNBszhIkZCLbUiHqGHHKkD0=', max_length=128, verbose_name='密码'),
        ),
    ]
