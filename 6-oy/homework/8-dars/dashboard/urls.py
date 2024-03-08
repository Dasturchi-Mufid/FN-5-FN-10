from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='dashboard'),
    
    path('banner-create/', views.create_banner,name='banner-create'),
    path('banner-list/', views.list_banner,name='banner-list'),
    path('banner-detail/<int:id>/',views.detail_banner,name='banner-detail'),
    path('banner-edit/<int:id>/',views.edit_banner,name='banner-edit'),
    path('banner-delete/<int:id>/',views.delete_banner,name='banner-delete'),

    path('service-create/', views.create_service,name='service-create'),
    path('service-list/', views.list_service,name='service-list'),
    path('service-detail/<int:id>/',views.detail_service,name='service-detail'),
    path('service-edit/<int:id>/',views.edit_service,name='service-edit'),
    path('service-delete/<int:id>/',views.delete_service,name='service-delete'),
    
    path('aboutus-create/', views.create_aboutus,name='aboutus-create'),
    path('aboutus-list/', views.list_aboutus,name='aboutus-list'),
    path('aboutus-detail/<int:id>/',views.detail_aboutus,name='aboutus-detail'),
    path('aboutus-edit/<int:id>/',views.edit_aboutus,name='aboutus-edit'),
    path('aboutus-delete/<int:id>/',views.delete_aboutus,name='aboutus-delete'),
    
    path('price-create/', views.create_price,name='price-create'),
    path('price-list/', views.list_price,name='price-list'),
    path('price-delete/<int:id>/',views.delete_price,name='price-delete'),
    path('price-detail/<int:id>/',views.detail_price,name='price-detail'),
    path('price-edit/<int:id>/',views.edit_price,name='price-edit'),

    
    path('contact-list/', views.list_contact,name='contact-list'),
    path('contact-detail/<int:id>/',views.detail_contact,name='contact-detail'),
    path('contact-edit/<int:id>/',views.edit_contact,name='contact-edit'),
]
