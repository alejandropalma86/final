from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm




class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ), max_length=30)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ), max_length=80)
    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), max_length=30)
    password2 = forms.CharField(label='Contraseña2', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), max_length=30)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ), max_length=30)
    #password = forms.CharField(max_length=30)
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), max_length=30)
    class Meta:
        model = User
        fields = ('username', 'password')


