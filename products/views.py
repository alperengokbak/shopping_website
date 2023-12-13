# products/views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        Q(product_id__icontains=query) |
        Q(description__icontains=query) |
        Q(price__icontains=query) |
        Q(category__title__icontains=query) |
        Q(brand__icontains=query)
    )
    return render(request, 'search_results.html', {'products': products, 'query': query})

def search_input(request):
    query = request.GET.get('search')
    products = Product.objects.filter(
        Q(product_id__icontains=query) |
        Q(description__icontains=query) |
        Q(price__icontains=query) |
        Q(category__title__icontains=query) |
        Q(brand__icontains=query)
    )
    return render(request, 'search_input.html', {'products': products, 'query': query})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})
