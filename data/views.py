from django.shortcuts import render

def propertydata(request):
    return render(request, 'data/home.html')