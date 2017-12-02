from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    ctx = {
        'title':'Hello world!',
        'content':'Welcome to home page',
    }
    if request.user.is_authenticated():
        ctx['premium_content'] = 'Yeah!'
    return render(request,'home-page.html',ctx)

def about_page(request):
    ctx = {
        'title': 'About page',
        'content': 'Welcome to about page',
    }
    return render(request, 'home-page.html',ctx)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form': login_form,
    }
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/")
        else:
            print('Error')

    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    ctx = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        User.objects.create_user(username,email,password)
    return render(request, 'auth/login.html', ctx)

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

