# Generated by Django 2.2.4 on 2020-01-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0007_auto_20200108_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationinfo',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$UVAq40ilii3M$qG6+xOO8XLFHB/IFkYrlXtYMlyMZ/seKtj8LCBiYLIo=', max_length=128, verbose_name='密码'),
        ),
        migrations.AlterModelTable(
            name='usernew',
            table='support_user_new',
        ),
    ]
