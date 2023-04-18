from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Enrollment
from django import forms



User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class AddCourseUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_group',)

class SearchForm(forms.Form):
    query = forms.CharField()
