# Generated by Django 2.2.4 on 2020-01-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0009_auto_20200108_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$nhRU4Y8sxbUb$lo18YyB1eshmIM9f4GaQpj/Mq7Pcn8TusEAQSYbmvpg=', max_length=128, verbose_name='密码'),
        ),
    ]