# Generated by Django 2.2.4 on 2020-01-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0011_auto_20200108_1550'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Locationinfo',
        ),
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$nEHVipRtRnHo$uRLyU4ORmUYDHSKeb/ejFypDKUD1CAr5bfRKkuDgZjY=', max_length=128, verbose_name='密码'),
        ),
    ]
