from cgitb import html
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
from django import template
from django.template import loader
import json
from .models import User

# Create your views here.
def home(request):
    return render(request, "home.html", {}) 

def test(request):
    names=['apple', 'ball']
    #return HttpResponse("<p>ok</p>")
    return render(request, "test.html", {'names':names})

def profile(request, name):
    return render(request, "index.html", {'name':"binayak"})

def login(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        resp= User.objects.filter(email=username, password=password).first()
        if resp:
            #return render(request, "home.html", {})
            return redirect('socialApp:home')
        else:
            return render(request, "login.html", {"error_message":"Invalid Credentials"})
    return render(request, "login.html", {}) 

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        resp= User.objects.filter(email=email).first()
        
        if resp:
            return render(request, "register.html", {"error_message":"Email already exists"})
        else:
            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            return redirect('socialApp:home')
        
    return render(request, "register.html", {})

def admin(request):
    return render(request, "admin.html", {}) 
