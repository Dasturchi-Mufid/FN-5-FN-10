from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='dashboard'),
    path('banner-list/', views.list_banner),
    path('banner-create/', views.create_banner),
    path('service-create/', views.create_service),
    path('service-list/', views.list_service),
    path('aboutus-create/', views.create_aboutus),
    path('aboutus-list/', views.list_aboutus),
    path('price-create/', views.create_price),
    path('price-list/', views.list_price),
]
