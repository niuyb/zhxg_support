# Generated by Django 2.2.4 on 2020-01-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0003_auto_20200103_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$6HyOLpNlEHR4$a4KoZx8MgcsRPrUAbh49/glfQIqSvQN4RVo7ThHuG4U=', max_length=128, verbose_name='密码'),
        ),
    ]
