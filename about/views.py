from django.shortcuts import render

def home(request):
    return render(request, 'about/home.html')

def about(request):
    return render(request, 'about/about.html', {'title': 'About'})