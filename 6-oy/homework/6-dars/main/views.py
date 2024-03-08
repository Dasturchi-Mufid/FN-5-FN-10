from django.shortcuts import render
from . import models


def index(request):
    baner = models.Banner.objects.last()
    about_us = models.AboutUs.objects.last()
    services = models.Service.objects.all()

    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

    context = {
        'baner':baner,
        'about_us':about_us,
        'services':services,
        'prices':prices_list
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')

def about(request):
    about_us = models.AboutUs.objects.last()
    context = {'about_us':about_us}
    return render(request,'about.html',context)

def price(request):
    prices = models.Price.objects.all()
    banner = models.Banner.objects.last()

    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

    context = {
        'prices':prices_list,
        'banner':banner
        }

    return render(request,'price.html',context)

def service(request):
    services = models.Service.objects.all()
    context = {'services':services}
    return render(request,'service.html',context)