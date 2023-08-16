
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("login/",views.login,name="stu_login"),
    path("register",views.register,name="stu_register"),
    path("dashboard",views.dashboard,name="stu_dashboard"),
    path("Student_profile",views.profile,name="stu_profile")
    
    
    
]
