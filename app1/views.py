from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import EmployeeForm
from app1.models import Employee

# Create your views here.
def app1(request):
        return HttpResponse("<h1 style='color:blue;text-align:center'> Hello django</h1>")
def home (request):
	return render(request,'home.html',{'name':'Pooja'})
def about (request):
	return render(request,'about.html')
def contact (request):
	return render(request,'contact.html')
def services (request):
	return render(request,'services.html')

def form (request):
	return render(request,'form.html')

def adddata(request):
	if request.method =='GET':
		form = EmployeeForm(request,GET)
		if form.is_valid():
			form.save()
			return HttpResponse('data inserted')
	else :
		form = EmployeeForm()
	return render(request,'form.html',{'form':form})

def getdata(request):
	data = Employee.objects.all()
	return render(request,'show.html',{'data:data'})
