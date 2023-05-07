from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Course, LessonSubmitUser, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, AdminVideoMixin):
    list_display = (
        'pk',
        'text',
        # 'geeks_field',
        'created',
        'author',
        'group',
        'video',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Course)
admin.site.register(LessonSubmitUser)
