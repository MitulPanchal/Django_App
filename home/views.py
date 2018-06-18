from django.views import generic
from .models import Employee


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_employee'

    def get_queryset(self):
        return Employee.objects.all()


class DetailView(generic.DetailView):
    model = Employee
    template_name = 'home/details.html'

