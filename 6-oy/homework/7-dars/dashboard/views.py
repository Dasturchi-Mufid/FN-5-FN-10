from django.shortcuts import render
from main import models

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request,'dashboard/index.html',context)

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
    if request.method == 'POST' and request.FILES['file']:
        name = request.POST.get('name')
        body = request.POST.get('body')
        icon = request.FILES.get('file')
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