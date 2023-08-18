from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100, widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= get_user_model()
        fields=('username','email','first_name','last_name','role')

class ProfilePhoto(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=('profile_photo',)

