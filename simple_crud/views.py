from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def view_products(request):
    products = Product.objects.all()
    return render(request, 'simple_crud/products.html', {'products' : products})

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('view_products')

    return render(request, 'simple_crud/product-form.html', {'form' : form})


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('view_products')

    return render(request, 'simple_crud/product-form.html', {'form' : form, 'product': product})

def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('view_products')

    return render(request, 'simple_crud/product-delete-confirm.html', {'product' : product})