from django.contrib import admin
from .models import Post, Group
from embed_video.admin import AdminVideoMixin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, AdminVideoMixin):
    list_display = (
        'pk',
        'text',
        'created',
        'author',
        'group',
        'video',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Group)
