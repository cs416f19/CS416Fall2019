from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('new/', views.create_product, name='create_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    #The below urls is used to delete a product via AJAX. ID is sent via JSON
    # (other than that it is basically the same as the above delete method)
    path('delete_ajax/', views.delete_product_ajax, name='delete_product_ajax'),
    # This url is for another template for viewing products where delete_ajax method will run
    path('view_ajax/', views.view_products_ajax, name='view_products_ajax'),

]