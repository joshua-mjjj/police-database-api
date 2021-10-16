# Generated by Django 3.1.5 on 2021-02-15 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210215_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lastEditDateTime',
            field=models.IntegerField(default=datetime.time(7, 36, 41, 242785)),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='service',
            field=models.CharField(blank=True, choices=[('wiring', 'Car wiring'), ('alignment', 'Wheel Alignment'), ('electrics', 'Electric Cars'), ('engines', 'Engine Checking'), ('wheel_balancing', 'Wheel Balancing'), ('flat_tyres', 'Flat Tyres'), ('computer_aided_mechanics', 'Computer Aided Mechanics')], max_length=32),
        ),
    ]
