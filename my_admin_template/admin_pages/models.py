from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField(unique=True)
    edept = models.CharField(max_length=50)
    esalary = models.IntegerField()
    econtact = models.CharField(max_length=15)
    ejoindate = models.DateField()
    ecity = models.CharField(max_length=40)
    