from unicodedata import name
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.register, name='register'),
    path('update-student/<str:pk>/', views.UpdateRegister, name='update-student'),
    path('delete-student/<str:pk>/', views.DeleteStudent, name='delete-student'),
]
