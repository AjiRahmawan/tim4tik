from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('forget/', views.forget, name='forget'),
    path('beranda/', views.beranda, name='beranda'),
    path('home/', views.home, name='home'),
]