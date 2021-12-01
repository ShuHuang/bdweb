from django.urls import path
from . import views

urlpatterns = [
    path('', views.batteryqa, name='batteryqa-qa'),
    path('search/', views.batterysearch, name='batteryqa-search'),
    path('results/<str:result_id>', views.results, name='batteryqa-results'),
]