from django import forms
from django.contrib.auth.models import User
from .models import File


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


"""class UploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_name', 'file', 'comment_by_secretary']"""
