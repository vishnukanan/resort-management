# Generated by Django 4.2.5 on 2024-06-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_visit_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit_package',
            name='package_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
