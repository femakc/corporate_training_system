from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Enrollment


class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password", "role", "groups")}),
    )


admin.site.register(User, UserAdmin)
# admin.site.register(Enrollment)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
        'date',
        'mark'
    )