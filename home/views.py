from django.http import Http404
from .models import Employee
from django.shortcuts import render

def index(request):
    all_employee = Employee.objects.all()
    return render(request, 'home/index.html', { 'all_employee' : all_employee,})

def detail(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404("Employee Details does not exist.")
    return render(request, 'home/details.html', { 'employee' : employee})
