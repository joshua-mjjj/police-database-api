# Generated by Django 3.1.5 on 2021-02-08 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210124_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='createDateTime',
            field=models.IntegerField(default=datetime.date(2021, 2, 8)),
        ),
        migrations.AlterField(
            model_name='note',
            name='lastEditDateTime',
            field=models.IntegerField(default=datetime.time(15, 53, 0, 288943)),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='contact',
            field=models.CharField(max_length=105),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='location',
            field=models.CharField(blank=True, choices=[('kampala', 'Kampala'), ('kayinga', 'Kayinga'), ('katwe', 'Katwe'), ('kakiri', 'Kakiri'), ('Nsambya', 'Nsambya'), ('Entebbe', 'Entebbe'), ('Munyonyo', 'Munyonyo'), ('Wandegeya', 'Wandegeya')], max_length=32),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='other',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='owner_username',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='service',
            field=models.CharField(blank=True, choices=[('wiring', 'Car wiring'), ('tyres', 'Wheel Alignment'), ('electric', 'Electric Cars'), ('engine', 'Engine Checking'), ('balancing', 'Wheel Balancing')], max_length=32),
        ),
    ]
