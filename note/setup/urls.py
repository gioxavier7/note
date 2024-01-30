from django.contrib import admin
from django.urls import path

from note.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
]
