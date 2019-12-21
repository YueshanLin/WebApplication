from django.forms import ModelForm
from blog.models import *
from django.contrib.auth.models import User
from django import forms

"""
class RegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        
    excludes = ['user']
    fields = ['username', 'password']

    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    password_conf = forms.CharField(max_length=20)
"""


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    password_conf = forms.CharField(max_length=20)
    age = forms.CharField(max_length=3)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_conf = cleaned_data.get('password_conf')
        if password and password_conf and password != password_conf:
            raise forms.ValidationError('Passwords entered do not match!')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            raise forms.ValidationError('Username already exists')
        return username


class PostForm(forms.Form):
    comment = forms.CharField(max_length=42)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('Username does not exist!')
        return username


class EditForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    age = forms.CharField(max_length=3, required=False)
    biography = forms.CharField(max_length=420, required=False)
    profile = forms.ImageField(widget=forms.FileInput(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class PasswordResetForm(forms.Form):
    old_password = forms.CharField(max_length=20)
    new_password = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data











