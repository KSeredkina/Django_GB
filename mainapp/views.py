from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.

def index(request):
    title = 'Главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
# def index(request):
#     products_list = Product.objects.all()
#     context = {'page_title': 'home',
#                'products': products_list}
#     return render(request, 'mainapp/index.html')


def products(request):
    products = Product.objects.all()
    product_category = ProductCategory.objects.all()
    content = {'products': products,
               'categories': product_category}

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')

def products_by_category(request, pk=None):
    prods_by_category = Product.objects.filter(category=pk)
    product_category = ProductCategory.objects.all()
    context = {'page_title': prods_by_category[0].category.name if prods_by_category else 'Error',
               'products': prods_by_category,
               'categories': product_category
               }
    return render(request, 'mainapp/products.html', context)
