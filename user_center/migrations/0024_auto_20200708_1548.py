# Generated by Django 2.2.4 on 2020-07-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0023_auto_20200218_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernew',
            name='istarshine_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='unique_id'),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='avatar',
            field=models.CharField(blank=True, default='/static/img/a7.jpg', max_length=255, null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='job',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$1RCn9isgwGkS$XntBIIztiiH41oxfk/vLIG4HtV5b1+1gvHdk3Lqd/7M=', max_length=128, verbose_name='新后台密码'),
        ),
    ]
