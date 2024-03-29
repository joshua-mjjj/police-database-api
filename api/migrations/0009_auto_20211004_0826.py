# Generated by Django 3.1.5 on 2021-10-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210215_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('force_number', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_work', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_enlishment', models.DateField(blank=True, null=True)),
                ('date_of_posting', models.DateField(blank=True, null=True)),
                ('computer_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('rank', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('sick', 'Sick'), ('absent', 'Absent'), ('dead', 'Dead'), ('transferred', 'Transferred')], max_length=100, null=True)),
                ('on_leave', models.CharField(blank=True, choices=[('pass_leave', 'Pass leave'), ('annual_leave', 'Annual leave')], max_length=100, null=True)),
                ('date_of_establishment', models.DateField(blank=True, max_length=100, null=True)),
                ('file_number', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='location',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='service',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
