from ckeditor.fields import RichTextFormField
from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'geeks_field', 'group', 'image', 'video')
        widgets = {
            "geeks_field": RichTextFormField(config_name="default"),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
