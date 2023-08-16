from django.contrib import admin

# Register your models here.
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=("id","username","first_name","last_name","phone_num","bio","profile_pic","gender")

admin.site.site_header="Ignite Teachers"