from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"home/home.html")

def contact_us(request):
    return render(request,"home/panels.html")