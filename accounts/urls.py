
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("Login",views.login,name="login"),
    path("Sign-up",views.signup,name="register")
    
    
    
]
