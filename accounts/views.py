from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Student


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not Student.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect("login")
        else:
            myuser = auth.authenticate(username=username, password=password)
            auth.login(request, myuser)
            messages.success(request, "Welcome back brother")
            return redirect("stu_dashboard")

    return render(request, "accounts/login.html")


def signup(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Student.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")
        
        elif Student.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")
        
        else:
            user = Student.objects.create_user(
                username=username, 
                email=email
            )
            
            user.set_password(password)
            
            user.save()
            messages.success(request, "Welcome to Ignite")

        return redirect("login")

    return render(request, "accounts/signup.html")
