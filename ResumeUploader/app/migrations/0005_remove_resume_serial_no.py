# Generated by Django 5.0 on 2024-01-11 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_resume_serial_no_alter_resume_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='Serial_No',
        ),
    ]