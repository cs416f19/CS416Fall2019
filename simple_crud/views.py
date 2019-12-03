from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import JsonResponse



def view_products_ajax(request):
    # This method renders a template for viewing products where delete_product_ajax method will run
    products = Product.objects.all()
    return render(request, 'simple_crud/products_ajax.html', {'products' : products})


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

def delete_product_ajax(request):
    id = request.POST.get('id', None)
    if (id is not None):
        #delere the product
        product = Product.objects.get(id=id)
        product.delete()

        #return a response to the client
        #Response in JSON format, it can contain any data that you want to send to the client
        data = {
            'deleted': True
        }

        return JsonResponse(data)
    else:
        data = {
            'deleted': False,
            'error': 'id cannot be found'
        }
        return JsonResponse(data)


