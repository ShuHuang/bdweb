from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def propertydata(request):
    return render(request, 'data/home.html')