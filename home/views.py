from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Employee, Project
from .forms import UserForm
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_employee'

    def get_queryset(self):
        return Employee.objects.all()

class DetailView(generic.DetailView):
    model = Employee
    template_name = 'home/details.html'

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['Name', 'Department', 'Contact', 'Employee_image','is_favourite']

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['Name', 'Department', 'Contact', 'Employee_image','is_favourite']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('home:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user= authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home:index')
        return render(request, self.template_name, {'form': form})

class FavouriteView(generic.ListView):
    model = Employee
    success_url = reverse_lazy('home:index')

class ProjectCreate(CreateView):
    model = Project
    fields = [ 'projectName','type']