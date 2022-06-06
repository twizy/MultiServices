from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.connect, name='login'),
    path('register/', views.registration, name='register'),
    path('logout', views.disconnect, name='logout'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('profile/', views.profileview, name='profile'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('list/', views.productList, name='list'),
    path('addClient/', views.addClient, name='addClient'),
    path('orderList/', views.orderList, name='orderList'),
    path('orderDetail/<int:id>/<int:idd>', views.orderDetail, name='orderDetail'),

]
