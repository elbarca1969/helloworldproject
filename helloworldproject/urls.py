from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('helloworld/', admin.site.urls),
    path('helloworld2/', admin.site.urls),
]
