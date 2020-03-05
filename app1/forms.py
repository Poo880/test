from django import forms

from app1.models import Employee

class EmployeeForm(forms.ModelForm):
   class Meta:
       model = Employee
       #fields =['name','mobile','salary','email']
       fields='__all__'