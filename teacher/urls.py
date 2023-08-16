from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("Login",views.login,name="teach_login"),
    path("Register",views.register,name="teach_register")
    
    
    
]
