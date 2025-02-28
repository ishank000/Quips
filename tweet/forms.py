from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the correct model

class TweetForm(forms.ModelForm):  
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):  
    email = forms.EmailField()  # Add parentheses to define as a form field

    class Meta:
        model = User  # Use User model instead of Tweet
        fields = ('username', 'email', 'password1', 'password2')
