from django.contrib import admin
from django.urls import path
from about.views import splash

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash)
]
