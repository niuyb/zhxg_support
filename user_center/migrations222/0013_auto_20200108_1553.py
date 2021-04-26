# Generated by Django 2.2.4 on 2020-01-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0012_auto_20200108_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationInfo',
            fields=[
                ('uuid', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('parent_uuid', models.CharField(blank=True, max_length=40, null=True)),
                ('arg0', models.CharField(blank=True, max_length=50, null=True)),
                ('proshot', models.CharField(blank=True, max_length=255, null=True)),
                ('lname_en', models.CharField(blank=True, max_length=255, null=True)),
                ('lname_ft', models.CharField(blank=True, max_length=255, null=True)),
                ('landmark_word', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location_info',
            },
        ),
        migrations.AlterField(
            model_name='usernew',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$grquBMV775fL$nOo0WFJ7Ssg4zUgJEGbcInr9DVbQvkxvtLLCjkim+YE=', max_length=128, verbose_name='密码'),
        ),
    ]
