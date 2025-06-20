from django.contrib import admin
from .models import Student
from django.contrib.auth.admin import UserAdmin

class StudentAdmin(UserAdmin):
    model = Student
    list_display = ["name","email","is_staff","is_superuser", "is_active"]
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email","password"),}),
        ("Personal  Info", {"fields": ("name",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Groups", {"fields": ( "groups", "user_permissions")}),
        ("Important dates", {"fields": ("date_joined","last_login",)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )
    
    readonly_fields =('date_joined', 'last_login')
    search_fields = ("email", "name")
    ordering = ("email",)
    
    
admin.site.register(Student, StudentAdmin)