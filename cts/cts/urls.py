from django.contrib import admin
from django.urls import include, path

handler500 = 'core.views.internal_server_error'
handler404 = 'core.views.page_not_found'
handler403 = 'core.views.custom_403'


urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('group/<slug>/', include('posts.urls', namespace='group')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls', namespace='post_detail')),
]
