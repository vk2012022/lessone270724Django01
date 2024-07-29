from django.shortcuts import render

def home(request):
    return render(request, 'test290724/home.html')

def about(request):
    return render(request, 'test290724/about.html')

def services(request):
    return render(request, 'test290724/services.html')

def contact(request):
    return render(request, 'test290724/contact.html')
