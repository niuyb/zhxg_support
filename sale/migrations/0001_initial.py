# Generated by Django 2.2.4 on 2020-03-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaleAppAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '商务管理模块特殊权限',
                'verbose_name_plural': '商务管理模块特殊权限',
                'db_table': 'sale_app_access',
            },
        ),
    ]
