# Generated by Django 4.0.5 on 2022-09-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0004_alter_case_hospital_name_alter_case_road_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='apple_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
