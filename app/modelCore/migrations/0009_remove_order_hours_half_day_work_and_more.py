# Generated by Django 4.0.5 on 2022-09-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0008_order_hours_half_day_work_order_hours_hour_work_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='hours_half_day_work',
        ),
        migrations.RemoveField(
            model_name='order',
            name='hours_hour_work',
        ),
        migrations.RemoveField(
            model_name='order',
            name='hours_one_day_work',
        ),
        migrations.RemoveField(
            model_name='order',
            name='wage_half_day',
        ),
        migrations.RemoveField(
            model_name='order',
            name='wage_one_day',
        ),
        migrations.AddField(
            model_name='order',
            name='amount_transfer_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_transfer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='transfer_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
