from django.db import models

# Create your models here.

class Employee  (models.Model):
    Name =  models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    Contact = models.CharField(max_length=100)

class Manager(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    managerName = models.CharField(max_length=250)
