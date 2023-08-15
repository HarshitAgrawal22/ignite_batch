from django.contrib import admin

# Register your models here.

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("id","phone_num","address","parent_phone_num","gender","bio","profile_pic")

admin.site.site_header="Igbite Team"
