from django.db import models
from django.contrib.auth.models import User
# Create your models here.
            
class Teacher(User):
    phone_num=models.CharField(max_length=10)
    
   
    bio=models.CharField(max_length=100,blank=True,null=True)
    
    gender=models.CharField(max_length=19,choices=(("Male","Male"),("Female","Female"),("Prefer not say","Prefer not to say")))
    
    profile_pic=models.ImageField(upload_to="student_profile",blank=True,null=True,default="student_profile/default.jpg")
    
    def set_prof_pic(self):
        if self.gender=="Male":
            self.profile_pic.set_image("student_profile/default_male.jpg")
            
            
        else:
            self.profile_pic.set_image("student_profile/default_female.jpg")
            
            