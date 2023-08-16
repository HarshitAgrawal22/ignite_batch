from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def dashboard(request):
    
    return render(request,"student/dashboard.html")

def quiz(request):
    
    question_set={
        "questions":None
    }
    
    return render(request,"student/quiz.html",question_set)

def profile(request):
    
    return render(request,"student/profile.html",{"student":request.user})