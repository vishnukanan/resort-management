# Generated by Django 4.2.5 on 2024-06-20 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_visit_package_package_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit_Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_pack', models.CharField(choices=[('family', 'family'), ('friends', 'friends'), ('couple', 'couple'), ('comapnya_pack', 'company_pack')], max_length=50)),
                ('price', models.IntegerField()),
                ('details', models.TextField()),
                ('package_no', models.IntegerField()),
            ],
        ),
    ]
