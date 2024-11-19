from django.db import models
from django.contrib import admin
class Loan(models.Model):
	Name=models.CharField(max_length=20)
	Numno=models.IntegerField(primary_key="Numno")
	Adderes=models.CharField(max_length=30)
	Aadhar=models.IntegerField()
	Email=models.EmailField()
class LoanAdmin(admin.ModelAdmin):
	list_display=('Name','Numno','Adderes','Aadhar','Email')