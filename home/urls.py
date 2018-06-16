from django.conf.urls import url
from . import views

urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/10/
    url(r'^(?P<employee_id>[0-9]+)/$', views.detail, name='detail'),
]
