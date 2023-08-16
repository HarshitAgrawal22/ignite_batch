from django.contrib import admin

# Register your models here.

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("id","username","first_name","last_name","address","phone_num","phone_num","parent_phone_num","gender","bio","profile_pic")

admin.site.site_header="Ignite Team"
