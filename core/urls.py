from django.contrib import admin
from django.urls import path, include

from app.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls)
]
