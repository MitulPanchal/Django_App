from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , include('home.urls')),
    path('login/' , include('login.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)