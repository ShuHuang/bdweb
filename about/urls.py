from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='about-home'),
    path('about/', views.about, name='about-about'),
    path('citing/', views.citing, name='about-citing'),
    path('contact/', views.contact, name='about-contact'),
]