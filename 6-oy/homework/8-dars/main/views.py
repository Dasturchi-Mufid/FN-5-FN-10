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
    return render(request, 'front/index.html', context)

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
    return render(request, 'front/contact.html')

def about(request):
    about_us = models.AboutUs.objects.last()
    context = {'about_us':about_us}
    return render(request,'front/about.html',context)

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

    return render(request,'front/price.html',context)

def service(request):
    services = models.Service.objects.all()
    context = {'services':services}
    return render(request,'front/service.html',context)

def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)


def create_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        icon = request.POST.get('file')
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon
        )
    return render(request,'dashboard/service/create.html')

def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request,'dashboard/service/list.html',context)

def create_aboutus(request):
    if request.method == 'POST':
        body = request.POST.get('body')
        models.AboutUs.objects.create(
            body=body
        )
    return render(request,'dashboard/aboutus/create.html')

def list_aboutus(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }
    return render(request,'dashboard/aboutus/list.html',context)

def create_price(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        body = request.POST.get('body')
        models.Price.objects.create(
            title=title,
            price=price,
            body=body
        )
    return render(request,'dashboard/price/create.html')

def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request,'dashboard/price/list.html',context)