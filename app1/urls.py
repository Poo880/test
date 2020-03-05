from django.urls import path 

from app1 import views

urlpatterns = [

		#path('app1/',views.app1,name='app1'),
	    path('home/',views.home,name='home'),
	    path('about/',views.about,name='about'),
	    path('contact/',views.contact,name='contact'),
	    path('services/',views.services,name='services'),
	    path('form/',views.form,name='form'),
	    path('adddata/',views.adddata,name='adddata'),
	    path('getdata/',views.getdata),
		
]