from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

@login_required(login_url='login')
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='login')
def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
        messages.success(request, 'Banner muvaffaqiyatli yaratildi')
        return redirect('banner-list')
    return render(request, 'dashboard/banner/create.html')

@login_required(login_url='login')
def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

@login_required(login_url='login')
def detail_banner(request,id):
    banner = models.Banner.objects.get(id=id)
    context = {'banner':banner}
    return render(request,'dashboard/banner/detail.html',context)

@login_required(login_url='login')
def edit_banner(request,id):
    banner = models.Banner.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST.get('title')
        banner.body = request.POST.get('body')
        banner.save()
        messages.success(request, 'Banner muvaffaqiyatli o`zgartirildi')
        return redirect('banner-detail',banner.id)
    context = {
            'banner':banner
        }
    return render(request,'dashboard/banner/edit.html',context)

@login_required(login_url='login')
def delete_banner(request, id):
    models.Banner.objects.get(id=id).delete()
    messages.success(request, 'Banner muvaffaqiyatli o`chirildi')
    return redirect('banner-list')

@login_required(login_url='login')
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
        messages.success(request, 'Service muvaffaqiyatli yaratildi')
        return redirect('service-list')
    return render(request,'dashboard/service/create.html')

@login_required(login_url='login')
def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request,'dashboard/service/list.html',context)

@login_required(login_url='login')
def detail_service(request,id):
    service = models.Service.objects.get(id=id)
    context = {'service':service}
    return render(request,'dashboard/service/detail.html',context)

@login_required(login_url='login')
def edit_service(request,id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.body = request.POST.get('body')
        if request.FILES:
            service.icon = request.FILES.get('icon')
        service.save()
        messages.success(request, 'Service muvaffaqiyatli o`zgartirildi')
        return redirect('service-detail',service.id)
    
    context = {'service':service}

    return render(request,'dashboard/service/edit.html',context)

@login_required(login_url='login')
def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    messages.success(request, 'Service muvaffaqiyatli o`chirildi')
    return redirect('service-list')

@login_required(login_url='login')
def create_aboutus(request):
    if request.method == 'POST':
        body = request.POST.get('body')
        models.AboutUs.objects.create(
            body=body
        )
        messages.success(request, 'AboutUs muvaffaqiyatli yaratildi')
        return redirect('aboutus-list')
    return render(request,'dashboard/aboutus/create.html')

@login_required(login_url='login')
def list_aboutus(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }
    return render(request,'dashboard/aboutus/list.html',context)

@login_required(login_url='login')
def detail_aboutus(request,id):
    aboutus = models.AboutUs.objects.get(id=id)
    context = {'aboutus':aboutus}
    return render(request,'dashboard/aboutus/detail.html',context)

@login_required(login_url='login')
def edit_aboutus(request,id):
    aboutus = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
        aboutus.body = request.POST.get('body')
        aboutus.save()
        messages.success(request, 'AboutUs muvaffaqiyatli o`zgartirildi')
        return redirect('aboutus-detail',aboutus.id)
    context = {'aboutus':aboutus}
    return render(request,'dashboard/aboutus/edit.html',context)

@login_required(login_url='login')
def delete_aboutus(request, id):
    models.AboutUs.objects.get(id=id).delete()
    messages.success(request, 'AboutUs muvaffaqiyatli o`chirildi')
    return redirect('aboutus-list')

@login_required(login_url='login')
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
        messages.success(request, 'Price muvaffaqiyatli yaratildi')
        return redirect('price-list')
    return render(request,'dashboard/price/create.html')

@login_required(login_url='login')
def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request,'dashboard/price/list.html',context)

@login_required(login_url='login')
def detail_price(request,id):
    price = models.Price.objects.get(id=id)
    context = {'price':price}
    return render(request,'dashboard/price/detail.html',context)

@login_required(login_url='login')
def edit_price(request,id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        price.title = request.POST.get('title')
        price.body = request.POST.get('body')
        price.price = request.POST.get('price')
        price.save()
        messages.success(request, 'Price muvaffaqiyatli o`zgartirildi')
        return redirect('price-detail',price.id)
    context = {'price':price}
    return render(request,'dashboard/price/edit.html',context)

@login_required(login_url='login')
def delete_price(request, id):
    messages.success(request, 'Price muvaffaqiyatli o`chirildi')
    models.Price.objects.get(id=id).delete()
    return redirect('price-list')

@login_required(login_url='login')
def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {'contacts':contacts}
    return render(request,'dashboard/contact/list.html',context)

@login_required(login_url='login')
def detail_contact(request,id):
    contact = models.Contact.objects.get(id=id)
    context = {'contact':contact}
    return render(request,'dashboard/contact/detail.html',context)

@login_required(login_url='login')
def edit_contact(request,id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.is_show = bool(int(request.POST.get('is_show')))
        contact.save()
        messages.success(request, 'Contact muvaffaqiyatli o`zgartirildi')
        return redirect('contact-detail',contact.id)
    context = {'contact':contact}
    return render(request,'dashboard/contact/edit.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    return render(request,'dashboard/auth/register.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request,'dashboard/auth/login.html')
    return render(request,'dashboard/auth/login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def search(request):
    query = request.GET.get('query')
    banners = models.Banner.objects.filter(Q(title__icontains=query)|Q(body__icontains=query))
    services = models.Service.objects.filter(Q(name__icontains=query)|Q(body__icontains=query))
    aboutus = models.AboutUs.objects.filter(Q(body__icontains=query))
    prices = models.Price.objects.filter(Q(title__icontains=query)|Q(price__icontains=query))
    contacts = models.Contact.objects.filter(Q(name__icontains=query)|Q(body__icontains=query)|Q(email__icontains=query)|Q(phone__icontains=query))
    context = {
        'banners': banners,
        'services': services,
        'aboutus': aboutus,
        'prices': prices,
        'contacts': contacts,
    }
    return render(request,'dashboard/search/search.html',context)