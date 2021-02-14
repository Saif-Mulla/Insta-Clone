# Generated by Django 3.0.3 on 2021-02-04 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myInsta', '0017_post_curr_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myInsta.Post')),
                ('user', models.ManyToManyField(related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]