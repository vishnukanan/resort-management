# Generated by Django 4.2.4 on 2024-07-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_resort_packs_select_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort_packs',
            name='select_pack',
            field=models.CharField(choices=[('family', 'family'), ('friends', 'friends'), ('couple', 'couple'), ('comapnya pack', 'company pack'), ('get together', 'get together'), ('students pack', 'students pack')], max_length=50),
        ),
    ]
