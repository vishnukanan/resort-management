# Generated by Django 4.2.4 on 2024-07-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
