# Generated by Django 2.1.1 on 2018-10-30 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabusevent',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='user',
            name='syllabi',
        ),
        migrations.AddField(
            model_name='syllabusevent',
            name='class_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_data.Class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='classes',
            field=models.ManyToManyField(to='user_data.Class'),
        ),
    ]
