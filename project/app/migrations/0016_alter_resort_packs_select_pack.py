# Generated by Django 4.2.4 on 2024-07-24 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_order_delete_visit_package_delete_visit_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort_packs',
            name='select_pack',
            field=models.CharField(choices=[('family', 'family'), ('friends', 'friends'), ('couple', 'couple'), ('comapnya_pack', 'company_pack'), ('get together', 'get together')], max_length=50),
        ),
    ]
