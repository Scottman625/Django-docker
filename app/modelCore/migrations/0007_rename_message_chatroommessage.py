# Generated by Django 4.0.5 on 2022-09-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0006_user_is_fcm_notify'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='ChatroomMessage',
        ),
    ]
