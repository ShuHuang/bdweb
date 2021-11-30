from django.urls import path
from . import views

urlpatterns = [
    path('', views.propertydata, name='data-propertydata'),
]