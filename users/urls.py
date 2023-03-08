from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),  # ../users/login
    path('logout/', LogoutView.as_view(), name='logout'),

]
