# Generated by Django 3.2.7 on 2022-10-27 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumtek', '0012_alter_work_alumni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
