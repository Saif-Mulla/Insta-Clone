# Generated by Django 3.1.2 on 2021-02-11 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myInsta', '0023_auto_20210211_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='curr_profile_pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='com_profile_pic', to='myInsta.profile'),
        ),
    ]