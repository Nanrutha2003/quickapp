# Generated by Django 5.0.6 on 2024-06-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickapp', '0006_usrdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='docData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
