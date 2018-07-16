from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.FavouriteView.as_view(), name='favourite'),
    url(r'^employee/add/$', views.EmployeeCreate.as_view(), name='employee-add'),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeUpdate.as_view(), name='employee-update'),
    url(r'^employee/(?P<pk>[0-9]+)/delete/$', views.EmployeeDelete.as_view(), name='employee-delete'),
    url(r'^employee/(?P<pk>[0-9]+)/project/add$', views.ProjectCreate.as_view(), name='project-add'),
]