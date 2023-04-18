from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='about-home'),
    path('about/', views.about, name='about-about'),
    path('aboutme/', views.aboutme, name='about-aboutme'),
    path('citing/', views.citing, name='about-citing'),
    path('acknowledgement/', views.acknowledgement, name='about-acknowledgement'),
    path('contact/', views.contact, name='about-contact'),
]