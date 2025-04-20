from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,forms
from .models import *

class SignupForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','first_name','last_name','email',]


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['topic','image','blog','post_date',]
        exclude=['user']
