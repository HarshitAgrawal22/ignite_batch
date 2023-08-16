from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student
# Create your views here.
def login(request):
    print(request.method)
    if request.method=="POST":
        username=request.POST.get("stu_username")
        password=request.POST.get("stu_password")
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("stu_login")
        else:
            myuser=auth.authenticate(username=username,password=password)
            auth.login(request,myuser)
            messages.success(request,"Welcome back brother")
            
            return redirect("stu_dashboard")
        
        
    

    return render(request,"student/login.html")


def register(request):
    print(request.method)
    
    if request.method=="POST":
        username=request.POST.get("stu_username")
        
        bio=request.POST.get("stu_bio")
        
        phone_num=request.POST.get("stu_num")
        
        parent_phone_num=request.POST.get("stu_parent_num")
        
        profile_pic=request.FILES.get("stu_pic")
        
        address=request.POST.get("stu_address")
        
        gender=request.POST.get("stu_gender")
        
        password=request.POST.get("stu_password")
        
        print(username,bio)
        
        new_student=Student.objects.create(username=username,first_name=request.POST.get("stu_FN"),last_name=request.POST.get("stu_LN"),bio=bio,address=address,parent_phone_num=parent_phone_num,gender=gender,phone_num=phone_num)
        
        new_student.profile_pic=profile_pic
        
        new_student.set_password(password)
        
        new_student.save()
        
        messages.success(request,"Welcome to our little family")
        return redirect("stu_login")
    return render(request,"student/register.html")

def dashboard(request):
    
    return render(request,"student/dashboard.html")

def quiz(request):
    
    question_set={
        "questions":None
    }
    
    return render(request,"student/quiz.html",question_set)

def profile(request):
    
    return render(request,"student/profile.html",{"student":request.user})