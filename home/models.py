from django.db import models
from django.urls import reverse

class Employee  (models.Model):
    Name =  models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    Contact = models.CharField(max_length=100)
    Employee_image = models.CharField(max_length=500,default="https://noink.abs-cbn.com/HTML/no-profile-pic.png")
    is_favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.Name + '-' + self.Department

class Project(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    projectName = models.CharField(max_length=250)


    def __str__(self):
        return self.projectName
