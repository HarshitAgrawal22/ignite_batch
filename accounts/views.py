from django.shortcuts import render,redirect

from . import views
from django.contrib.auth.models import User

from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method=="POST":
        username=request.POST.get("stu_username")
        password=request.POST.get("stu_password")
        if  not User.objects.filter(username=username).exists():
            messages.error("Invalid Username")
            return redirect("login")
        else:
            myuser=auth.authenticate(username=username,password=password)
            auth.login(request,myuser)
            messages.success("Welcome back brother")
            return redirect("dashboard")
    return render(request,"home/login.html")



def signup(request):
    if request.method=="POST":
        
        
        new_user=User.objects.create(username=request.POST.get("stu_username"),email=request.POST.get("email"))
        
        new_user.set_password(request.POST.get("password"))
        
        new_user.save()
        
        messages.success("Welcome to Ignite")
        
        return redirect("login")
    
    return render(request,"notes.html")

