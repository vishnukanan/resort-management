# Generated by Django 4.2.4 on 2024-07-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_order_status_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]