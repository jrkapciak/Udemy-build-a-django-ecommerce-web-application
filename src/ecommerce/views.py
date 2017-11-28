from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,LoginForm

def home_page(request):
    ctx = {
        'title':'Hello world!',
        'content':'Welcome to home page',
    }
    return render(request,'home-page.html',ctx)

def about_page(request):
    ctx = {
        'title': 'About page',
        'content': 'Welcome to about page',
    }
    return render(request, 'home-page.html',ctx)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        print(login_form.cleaned_data)
    return render(request, 'auth/login.html', {})

def register_page(request):

    return render(requst, 'auth/register.html', {})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    ctx = {
        'title': 'Contact page',
        'content': 'Welcome to contact page',
        'form':contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)


    return render(request, 'contact/view.html',ctx)

