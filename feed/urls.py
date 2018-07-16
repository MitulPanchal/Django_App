from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alter/$', views.ContentView.as_view(), name='FeedHome')
]