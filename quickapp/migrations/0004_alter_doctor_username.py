# Generated by Django 5.0.6 on 2024-06-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickapp', '0003_doctor_email_doctor_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='username',
            field=models.CharField(default='no name', max_length=200),
        ),
    ]
