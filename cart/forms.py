from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile
from django import forms


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email']


class LoginForm(AuthenticationForm):
    fields = ['email', 'password']


class ProfileImgForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
