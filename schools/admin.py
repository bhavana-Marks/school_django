# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserInfo , City, Area, Schools
import json
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Schools)

	 
#json to django

# f = open('schools\static\schoolList\json\\Vizag.json')
# json_string = f.read()
# f.close()
#print(json_string)

# Convert json string to python object
# data = json.loads(json_string)


# city = City()
# area = Area()
# a = Area.objects.get(city_areas = 'Seetammadara')

# for schl in data['Seetammadara']:
# 	s = Schools()
# 	s.area = a
# 	print('+++++++++++++++++++++++++++++++')
# 	print(schl['schoolName'])
# 	s.school_Name = schl['schoolName']
# 	s.school_Img = schl['imgPath']
# 	s.school_distance = 12
# 	s.school_address = schl['address']
# 	s.school_desc = schl['desc']
# 	s.school_Location = schl['schoolLocation']
# 	s.school_contact =1234
# 	s.school_Email = schl['email']
# 	s.school_WebAddress = schl['webAddress']
# 	s.save()
# print('+++++++++++++++++++++++++++++++')


