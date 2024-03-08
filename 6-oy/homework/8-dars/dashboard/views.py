from django.shortcuts import render, redirect
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

def detail_banner(request,id):
    banner = models.Banner.objects.get(id=id)
    context = {'banner':banner}
    return render(request,'dashboard/banner/detail.html',context)

def edit_banner(request,id):
    banner = models.Banner.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST.get('title')
        banner.body = request.POST.get('body')
        banner.save()
        return redirect('banner-detail',banner.id)
    context = {
            'banner':banner
        }
    return render(request,'dashboard/banner/edit.html',context)

def delete_banner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('banner-list')

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

def detail_service(request,id):
    service = models.Service.objects.get(id=id)
    context = {'service':service}
    return render(request,'dashboard/service/detail.html',context)

def edit_service(request,id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.body = request.POST.get('body')
        if request.FILES:
            service.icon = request.FILES.get('icon')
        service.save()
        return redirect('service-list')
    
    context = {'service':service}

    return render(request,'dashboard/service/edit.html',context)

def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('service-list')
    
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

def detail_aboutus(request,id):
    aboutus = models.AboutUs.objects.get(id=id)
    context = {'aboutus':aboutus}
    return render(request,'dashboard/aboutus/detail.html',context)

def edit_aboutus(request,id):
    aboutus = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
        aboutus.body = request.POST.get('body')
        aboutus.save()
        return redirect('aboutus-list')
    context = {'aboutus':aboutus}
    return render(request,'dashboard/aboutus/edit.html',context)

def delete_aboutus(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('aboutus-list')

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

def detail_price(request,id):
    price = models.Price.objects.get(id=id)
    context = {'price':price}
    return render(request,'dashboard/price/detail.html',context)

def edit_price(request,id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        price.title = request.POST.get('title')
        price.body = request.POST.get('body')
        price.price = request.POST.get('price')
        price.save()
        return redirect('price-list')
    context = {'price':price}
    return render(request,'dashboard/price/edit.html',context)

def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('price-list')

def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {'contacts':contacts}
    return render(request,'dashboard/contact/list.html',context)

def detail_contact(request,id):
    contact = models.Contact.objects.get(id=id)
    context = {'contact':contact}
    return render(request,'dashboard/contact/detail.html',context)

def edit_contact(request,id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.is_show = bool(int(request.POST.get('is_show')))
        print(request.POST)
        contact.save()
        return redirect('contact-list')
    context = {'contact':contact}
    return render(request,'dashboard/contact/edit.html',context)