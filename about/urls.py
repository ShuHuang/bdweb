from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='about-home'),
    path('about/', views.about, name='about-about'),
]