from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Service, AboutUs, AboutUsListItem


def index(request):
    services = Service.objects.all()
    aboutUs = AboutUs.objects.last()
    aboutUsListItems = AboutUsListItem.objects.all()
    
    context = {
        'services': services,
        'aboutUs': aboutUs,
        'aboutUsListItems': aboutUsListItems
    }
    
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']
    
        if password == password_confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail already taken')
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('login')
        messages.info(request, 'The passwords must match')
        return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        messages.info(request, 'Invalid credentials')
        return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')