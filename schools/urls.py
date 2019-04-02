from django.conf.urls import url
from . import views
app_name ='schools'
urlpatterns = [
	#/schools/
    url(r'^$', views.home, name= 'home'),
    url(r'^home/$', views.home, name= 'home'),
    url(r'^login/$', views.login, name= 'login'),
    url(r'^registration/$', views.registration, name= 'registration'),
    url(r'^about/$', views.about, name= 'about'),
    url(r'^school_sub/$', views.school_sub, name= 'school_sub'),
    url(r'^regForm/$',views.regForm, name = 'regForm'),
    url(r'^showSchoolsList/$',views.showSchoolsList, name = 'showSchoolsList'),
    url(r'^validateLogin/$', views.validateLogin, name = 'validateLogin'),
    url(r'^loadArea/$', views.loadArea, name='loadArea'),
]