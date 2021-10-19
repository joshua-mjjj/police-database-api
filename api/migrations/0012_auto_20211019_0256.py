# Generated by Django 3.1.5 on 2021-10-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='on_leave',
            field=models.CharField(blank=True, choices=[('pass_leave', 'Pass leave'), ('annual_leave', 'Annual leave'), ('marternity_leave', 'Marternity leave')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('sick', 'Sick'), ('absent', 'Absent'), ('dead', 'Dead'), ('transferred', 'Transferred'), ('suspension', 'Suspension'), ('dismissed', 'Disnissed')], max_length=100, null=True),
        ),
    ]