# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .forms import MapForm
from .models import UserInfo , City, Area,Schools

# Create your views here.
def home(request):
	cities = City.objects.all()	
	areas = Area.objects.all()

	context = {
	'cities':cities,
	# 'areas' : areas
	}
	return render(request,'schools/home.html',{'context':context})

def login(request):
	return render(request,'schools/login.html',{'context':'this is login'})

def registration(request):
	return render(request,'schools/registration.html',{'context':'this is login'})
def about(request):
	return render(request,'schools/about.html',{'context':'this is about'})
def regForm(request):
	# form  = RegstrationForm()
	FirstName = request.POST.get('FirstName','')
	LastName = request.POST.get('LastName','')
	Email = request.POST.get('Email','')
	PhoneNumber = request.POST.get('PhoneNumber','')
	Password = request.POST.get('Password','')
	# Dob = request.POST.get('Dob','')
	Gender = request.POST.get('Gender','')
	City = request.POST.get('City','')
	ZipCode = request.POST.get('ZipCode','')
	Country = request.POST.get('Country','')
	Address = request.POST.get('Address','')
	user = UserInfo(FirstName = FirstName, LastName = LastName, Email = Email , PhoneNumber = PhoneNumber ,Password= Password ,Gender =Gender, City =City,  ZipCode = ZipCode, Country = Country, Address =Address)
	user.save()

	return render(request,'schools/home.html',{'context':'this is home'})

def showSchoolsList(request):
	city_id = request.POST.get('city','')
	area_id = request.POST.get('area','')
	
	schoolsList = Schools.objects.filter(area__city__pk =city_id, area__pk = area_id)
	print(schoolsList)
	return render(request,'schools/schoolList.html',{'schoolsList':schoolsList})
	
def validateLogin(request):
	FirstName = request.POST.get('userName','')
	Password = request.POST.get('Password','')

	if UserInfo.objects.filter(FirstName = FirstName ,Password = Password).exists():
		
		return render(request,'schools/home.html',{'context':'valid user'})
	else :
		
		return render(request,'schools/login.html',{'context':'invalid'})

def loadArea(request):
	city_id = request.GET.get('cityId')

	city = City()
	areas = Area.objects.filter(city__pk = city_id)
	print(areas)
	return render(request,'schools/home.html',{'areas':areas})
	# return render(request, 'schools/loadAreas.html',  {'areas': areas})

def school_sub(request):
	if request.method == 'POST':
		Address = request.POST.get('Address','')
		
	else:
		Address = 'hyderabad'

	context = { 'name': Address }
	print(context)	
	return render(request, 'schools/school_sub.html',  {'context':context})

