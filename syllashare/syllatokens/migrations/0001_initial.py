# Generated by Django 2.1.2 on 2018-10-22 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyllaShareToken',
            fields=[
                ('syllashare_token', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_data.User')),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
    ]
