# Generated by Django 3.1.5 on 2021-01-24 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210124_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lastEditDateTime',
            field=models.IntegerField(default=datetime.time(18, 31, 51, 672636)),
        ),
    ]