from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Teacher
# Create your views here.
def login(request):
    print(request.method)
    if request.method=="POST":
        username=request.POST.get("teah_username")
        password=request.POST.get("teah_password")
        if not Teacher.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("teach_login")
        else:
            myuser=auth.authenticate(username=username,password=password)
            auth.login(request,myuser)
            messages.success(request,"Welcome back brother")
            
            return redirect("dashboard")
        
        
    

    return render(request,"teacher/login.html")


def register(request):
    print(request.method)
    
    if request.method=="POST":
        username=request.POST.get("teach_username")
        
        
        
        bio=request.POST.get("teach_bio")
        
        phone_num=request.POST.get("teach_num")
        
        
        
        profile_pic=request.FILES.get("teach_pic")
        
        
        
        gender=request.POST.get("teach_gender")
        
        password=request.POST.get("teach_password")
        
        
        
        new_teacher=Teacher.objects.create(username=username,first_name=request.POST.get("teach_FN"),last_name=request.POST.get("teach_LN"),bio=bio,gender=gender,phone_num=phone_num)
        
        new_teacher.profile_pic=profile_pic
        
        new_teacher.set_password(password)
        
        new_teacher.save()
        
        messages.success(request,"Welcome to our little family")
        return redirect("teach_login")
    return render(request,"teacher/register.html")

def dashboard(request):
    
    return render(request,"teacher/dashboard.html")

def quiz(request):
    
    question_set={
        "questions":None
    }
    
    return render(request,"teacher/quiz.html",question_set)