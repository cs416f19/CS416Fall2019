
from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', views.addUser, name='addUser'),
    path('register/', views.register, name='register'),
]
