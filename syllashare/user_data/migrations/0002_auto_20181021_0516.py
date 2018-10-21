# Generated by Django 2.1.1 on 2018-10-21 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=datetime.datetime(2018, 10, 21, 5, 16, 59, 256839), max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]