# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.
class UserInfo(models.Model):
	GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
	FirstName = models.CharField(max_length = 250, default='name')
	LastName = models.CharField(max_length = 250)
	# Dob = models.DateField(blank=True, null=True,default=datetime.date.today)
	Email = models.CharField(max_length = 250)
	PhoneNumber = models.IntegerField()
	Password = models.CharField(max_length = 250)
	Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	City = models.CharField(max_length = 250)
	ZipCode = models.CharField(max_length = 250)
	Country = models.CharField(max_length = 250)
	Address = models.CharField(max_length = 1000)

	def __str__(self):
		return self.FirstName + ' - ' + self.LastName

class City(models.Model):
	city_Name = models.CharField(max_length = 250)

	def __str__(self):
		return self.city_Name

class Area(models.Model):
	city = models.ForeignKey(City,on_delete = models.CASCADE)
	city_areas = models.CharField(max_length = 250)

	def __str__(self):
		return self.city_areas  + ' - ' + self.city.city_Name

class Schools(models.Model):
	area = models.ForeignKey(Area,on_delete = models.CASCADE)
	school_Name = models.CharField(max_length = 250, default='name')
	school_Img = models.CharField(max_length = 250)
	school_distance = models.IntegerField()
	school_address = models.CharField(max_length = 1000)
	school_desc = models.CharField(max_length = 1500)
	school_Location = models.CharField(max_length = 1000)
	school_contact = models.CharField(max_length = 1000)
	school_Email = models.CharField(max_length = 250)
	school_WebAddress = models.CharField(max_length = 250)

	def __str__(self):
		return self.school_Name  + ' - ' + self.area.city_areas + ' - ' + self.area.city.city_Name