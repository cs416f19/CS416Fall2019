
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.addUser, name='addUser'),
    path('register/', views.register, name='register'),
    path('test/', views.test, name='test'),
]
