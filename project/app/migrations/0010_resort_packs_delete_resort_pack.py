# Generated by Django 4.2.5 on 2024-06-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_visit_packages_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resort_packs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_pack', models.CharField(choices=[('family', 'family'), ('friends', 'friends'), ('couple', 'couple'), ('comapnya_pack', 'company_pack')], max_length=50)),
                ('price', models.IntegerField()),
                ('details', models.TextField()),
                ('no_of_rooms', models.IntegerField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Resort_Pack',
        ),
    ]
