from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Enrollment


class UserAdmin(UserAdmin):
    list_display = ("username", "fio", "role", "phone")
    fieldsets = (
        (None, {"fields": ("username", "password", "fio", "phone", "role", "groups")}),
    )


admin.site.register(User, UserAdmin)
# admin.site.register(Enrollment)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
    )