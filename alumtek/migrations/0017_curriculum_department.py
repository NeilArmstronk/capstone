# Generated by Django 3.2.7 on 2022-11-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumtek', '0016_auto_20221102_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='department',
            field=models.CharField(default=False, max_length=50),
        ),
    ]