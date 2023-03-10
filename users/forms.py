from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm the password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class ReactivationForm(forms.Form):
    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise forms.ValidationError('User with this email does\'t exist')
        return email
