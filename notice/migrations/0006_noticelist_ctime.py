# Generated by Django 2.2.4 on 2020-03-19 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20200319_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticelist',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='ειζΆι΄'),
            preserve_default=False,
        ),
    ]
