from django.db import models

from django.contrib.auth.models import User

class Student(User):
    
    phone_number=models.CharField(max_length=10)
    
    address=models.TextField()
    
    parent_phone_number=models.CharField(max_length=10,blank=True,null=True)
    
    gender=models.CharField(max_length=19,choices=(("Male","Male"),("Female","Female"),("Prefer not say","Prefer not say")))
    
    bio=models.CharField(max_length=100,blank=True,null=True)
    
    
    profile_pic=models.ImageField(upload_to="student_profile",blank=True,null=True,default="student_profile/default.jpg")
    
    
    class Meta:
        verbose_name_plural="Students"