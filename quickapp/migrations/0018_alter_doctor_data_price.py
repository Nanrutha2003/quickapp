# Generated by Django 5.0.6 on 2024-08-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickapp', '0017_usrdata_name_alter_usrdata_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_data',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
