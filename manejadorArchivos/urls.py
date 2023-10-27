from django.urls import path
from . import views


app_name="archivos"

urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
    path('success/', views.success, name='success'),
]