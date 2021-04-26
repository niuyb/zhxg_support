# Generated by Django 2.2.4 on 2020-02-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0019_auto_20200212_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernew',
            name='position',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$L2USbCaXUgB9$gdAFGw86m2XaocQtPFwDTG5TTpp+q/nq9s2EXko+9kc=', max_length=128, verbose_name='新后台密码'),
        ),
    ]