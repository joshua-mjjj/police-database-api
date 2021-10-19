from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


SERVICE_TYPES = (
    ('wiring', 'Car wiring'),
    ('alignment', 'Wheel Alignment'),
    ('electrics', 'Electric Cars'),
    ('engines', 'Engine Checking'),
    ('wheel_balancing', 'Wheel Balancing'),
    ('flat_tyres', 'Flat Tyres'),
    ('computer_aided_mechanics', 'Computer Aided Mechanics'),

)

STATUS = (
    ('active', 'Active'),
    ('sick', 'Sick'),
    ('absent', 'Absent'),
    ('dead', 'Dead'),
    ('transferred', 'Transferred'),
    ('suspended', 'Suspended'),
    ('dismissed', 'Dismissed'),
)

LEAVE = (
    ('pass_leave', 'Pass leave'),
    ('annual_leave', 'Annual leave'),
    ('maternity_leave', 'Marternity leave'),
    ('not_on_leave', 'Not on leave'),
)

DEPARTMENTS = (
    ('un_agencies', 'UN AGENCIES'),
    ('embassy_high', 'EMBASSY HIGH'),
    ('jlot', 'JLOT'),
    ('body_gaurd', 'BODY GUARD'),
    ('authorities', 'AUTHORITIES'),
    ('ministries', 'MINISTRIES'),
)

TITLES = (
    ('commander', 'Commander'),
    ('deputy_commander', 'Deputy Commander'),
    ('staff_officer', 'Staff Officer'),
    ('armoury', 'Armoury'),
    ('head_operations', 'Head Operations'),
)




class Client(models.Model):
	service  = models.CharField(max_length=150)
	Location = models.CharField(max_length=150)

	def save(self, *args, **kwargs):
		super(Client, self).save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.service)

class serviceProvider(models.Model):
	#service  = models.CharField(max_length=32, choices=SERVICE_TYPES, blank=True)
	owner_username =  models.CharField(max_length=100, blank=True)
	#location = models.CharField(max_length=32, choices=LOCATIONS, blank=True)
	name     = models.CharField(max_length=100, null=False ,blank=False)
	photo = models.FileField(upload_to="media/photos/service_provider_avatars/", blank=True)
	contact  = models.CharField(max_length=105, null=False ,blank=False)
	email    = models.EmailField(max_length=100, null=True,blank=True)
	other    = models.CharField(max_length=10000)
	#profile_picture = models.ImageField(blank=True, null=True, upload_to=upload_path)
	owner    = models.ForeignKey(
	    User, related_name="profiles", 
	    on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{}'.format(self.owner)


class Employee(models.Model):
	sur_name              = models.CharField(max_length=50, blank=True, null=True)
	first_name            = models.CharField(max_length=50, blank=True, null=True)
	serial_number         = models.CharField(max_length=100, blank=True, null=True)
	force_number          = models.CharField(max_length=100, blank=True, null=True)
	place_of_work         = models.CharField(max_length=100, blank=True, null=True)
	date_of_birth         = models.DateField(blank=True, null=True)
	date_of_enlishment    = models.DateField(blank=True, null=True)
	date_of_posting       = models.DateField(blank=True, null=True)
	computer_number       = models.CharField(max_length=100, unique=True, blank=True, null=True)
	rank                  = models.CharField(max_length=100, blank=True, null=True)
	title                 = models.CharField(max_length=100, choices=TITLES, blank=True, null=True)
	department            = models.CharField(max_length=100, choices=DEPARTMENTS, blank=True, null=True)
	status                = models.CharField(max_length=100, choices=STATUS, blank=True, null=True)
	on_leave              = models.CharField(max_length=100, choices=LEAVE, blank=True, null=True)
	date_of_establishment = models.DateField(max_length=100, blank=True, null=True)
	file_number           = models.CharField(max_length=100, blank=True, null=True)
	created_at            = models.DateTimeField(auto_now_add=True)
	updated_at            = models.DateTimeField(auto_now=True)





