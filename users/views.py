from django.contrib.auth.views import LoginView
from django.shortcuts import render

from users.forms import UserLoginForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm




