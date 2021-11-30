from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def batteryqa(request):
    return render(request, 'batteryqa/qa.html')