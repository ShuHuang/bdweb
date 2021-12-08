from django.urls import path
from . import views

urlpatterns = [
    path('', views.classifier, name='classifier-classifier'),
    path('classifier-results/', views.classifier_results, name='classifier-results'),
    path('classifier-results/<int:example>', views.classifier_results_example, name='classifier-results-example'),
]