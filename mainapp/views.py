from django.shortcuts import render
import json


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    with open('mainapp/database/products.json', encoding="utf-8") as json_file:
        json_object = json.load(json_file)
        json_file.close()
    context = {'products': [product for product in json_object]}

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')
