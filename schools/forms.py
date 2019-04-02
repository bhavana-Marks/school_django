from django import forms
from django.conf import settings
# class RegstrationForm(forms.Form):
# 	GENDER_CHOICES = (
#         ('F', 'Female'),
#         ('M', 'Male'),
#     )
# 	FirstName = forms.CharField()
# 	LastName = forms.CharField()
# 	Email = forms.EmailField()
# 	PhoneNumber = forms.IntegerField()
# 	Password = forms.CharField()
# 	Dob = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS)
# 	Gender = forms.ChoiceField(widget = forms.RadioSelect(), choices=GENDER_CHOICES)
# 	City = forms.CharField()
# 	ZipCode = forms.CharField()
# 	Country = forms.CharField()
# 	Address = forms.CharField()


class MapForm(forms.Form):
    Address = forms.CharField(label='Address', max_length=100)