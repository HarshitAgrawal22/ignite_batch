from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("Student/",include("student.urls"),name="stu_login"),
    path("Teacher/",include("teacher.urls"),name="teach_login"),
    
    
]
