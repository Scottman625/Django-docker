# Generated by Django 4.0.5 on 2022-09-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0003_case_hospital_name_case_road_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='hospital_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='case',
            name='road_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='tempcase',
            name='hospital_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='tempcase',
            name='road_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
