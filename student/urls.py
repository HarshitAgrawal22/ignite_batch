
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("dashboard",views.dashboard,name="stu_dashboard"),
    path("myprofile",views.profile,name="stu_profile")

]
