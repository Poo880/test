from django.db import models

# Create your models here.

class Employee(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	image=models.FileField(default='')
	salary=models.IntegerField()
	mobile=models.BigIntegerField()
	class Meta:
		db_table = 'employee'

