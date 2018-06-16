from django.db import models

# Create your models here.

class Employee  (models.Model):
    Name =  models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    Contact = models.CharField(max_length=100)

    def __str__(self):
        return self.Name + '-' + self.Department

class Project(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    projectName = models.CharField(max_length=250)

    def __str__(self):
        return self.projectName
