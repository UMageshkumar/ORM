# Ex02 Django ORM Web Application
## Date: 14.10.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Loan,LoanAdmin
admin.site.register(Loan,LoanAdmin)

models.py

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

```



## OUTPUT
![Screenshot 2024-12-10 092927](https://github.com/user-attachments/assets/c2546836-0810-4268-83be-d7a6cec8afd8)

Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
