# Generated by Django 2.2.4 on 2020-01-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0005_auto_20200106_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernew',
            name='dtalkid',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$qhaCzEHAU5xU$0+ImEGR43w0gvct1MTSUaAzEJRrOqMDLCWkrkHvzrWE=', max_length=128, verbose_name='密码'),
        ),
    ]
