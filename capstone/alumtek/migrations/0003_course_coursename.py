# Generated by Django 3.2.7 on 2022-10-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumtek', '0002_course_curriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseName',
            field=models.CharField(default=False, max_length=500),
        ),
    ]