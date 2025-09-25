from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length = 50)
    company_location = models.CharField(max_length=50)
    company_about = models.TextField()
    company_type = models.CharField(max_length=100, choices =(
        ('IT','IT'),
        ('Non IT','Non IT'),
        ('Mobiles Phones','Mobile Phones'),
        ('BA','BA')
    ))
    added_data = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    def __str__(self):
        return self.company_name + self.company_location
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('project Leader','pl'),
    ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    