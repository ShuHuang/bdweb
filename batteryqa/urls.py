from django.urls import path
from . import views

urlpatterns = [
    path('', views.batteryqa, name='batteryqa-qa'),
    path('search/', views.batterysearch, name='batteryqa-search'),
    path('search-results/', views.search_results, name='batteryqa-search-results'),
    path('answer/', views.answers, name='batteryqa-answer'),
    path('answer/<int:example>', views.answers_example, name='batteryqa-answer-example'),
    # path('test/', views.test, name='batteryqa-test'),
]