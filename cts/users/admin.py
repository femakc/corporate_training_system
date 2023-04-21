from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Enrollment, User


class UserAdmin(UserAdmin):
    list_display = ("username", "fio", "role", "phone")
    fieldsets = (
        (None, {"fields": ("username", "password", "fio", "phone", "role", "groups")}),
    )


admin.site.register(User, UserAdmin)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
    )