from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('new/', views.create_product, name='create_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

]