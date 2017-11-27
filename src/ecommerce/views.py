from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    ctx = {
        'title':'Hello world!'
    }
    return render(request,'home-page.html',ctx)

def about_page(request):
    return render(request,'home-page.html',{})

def contact_page(request):
    return render(request,'home-page.html',{})