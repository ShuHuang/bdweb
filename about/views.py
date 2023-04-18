from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


# @login_required()
def home(request):
    return render(request, 'about/home.html')


# @login_required()
def about(request):
    return render(request, 'about/about.html', {'title': 'About'})


def aboutme(request):
    return render(request, 'about/aboutme.html', {'title': 'About Me'})


# @login_required()
def citing(request):
    return render(request, 'about/citing.html', {'title': 'Citing'})

def acknowledgement(request):
    return render(request, 'about/acknowledgement.html', {'title': 'Acknowledgement'})


# @login_required()
def contact(request):
    return render(request, 'about/contact.html', {'title': 'Contact'})
