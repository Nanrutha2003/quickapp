# Generated by Django 5.0.6 on 2024-08-29 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quickapp', '0015_delete_docdata_delete_doctor_data_delete_usrdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_data',
            fields=[
                ('fname', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('specialization', models.CharField(max_length=200)),
                ('hospital', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=30)),
                ('pname', models.CharField(max_length=30)),
                ('pemail', models.EmailField(max_length=30)),
                ('pmobile', models.IntegerField()),
                ('page', models.IntegerField()),
                ('problrm', models.CharField(max_length=50)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='usrData',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
