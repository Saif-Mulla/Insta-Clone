# Generated by Django 3.1.2 on 2021-02-01 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myInsta', '0012_auto_20210201_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(auto_now_add=datetime.datetime(2021, 2, 1, 12, 48, 42, 481634), verbose_name='Time'),
        ),
    ]
