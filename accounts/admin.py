from django.contrib import admin
from .models import Student

admin.site.site_header="Ignite Team"
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("id","username","first_name","phone_number")
    
    exclude = ("password", "last_login", "is_superuser", "is_staff", "is_active", "groups", "user_permissions", "date_joined")

