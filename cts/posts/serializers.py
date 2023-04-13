# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('text', 'author', 'pub_date', 'video')
