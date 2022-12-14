# Generated by Django 4.0.5 on 2022-10-03 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0017_chatroommessage_order_systemmessage_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='nameE',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='taken_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
