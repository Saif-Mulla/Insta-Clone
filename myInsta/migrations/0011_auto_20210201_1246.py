# Generated by Django 3.1.2 on 2021-02-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myInsta', '0010_auto_20210201_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default='12:46:08', verbose_name='Date'),
        ),
    ]