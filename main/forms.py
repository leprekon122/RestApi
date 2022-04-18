from django.forms import ModelForm, Textarea, TextInput, EmailInput, PasswordInput, Select
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CreateNewsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'link', 'author_name']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),

            'link': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'link'
            }),

            'author_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'author_name'
            }),

        }


class RegistrForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'username',
                'class': 'form-control'

            }),

            'password': PasswordInput(attrs={
                'placeholder': 'password',
                'class': 'form-control'

            }),
            'email': EmailInput(attrs={
                'placeholder': 'email',
                'class': 'form-control'

            })

        }


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['username', 'comments', 'name']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),

            'comments': Textarea(attrs={
                'class': 'form-control',
            }),

            'name': Select(attrs={
                'class': 'form-select',

            }),

        }
