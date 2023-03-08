from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserRegistrationView, ActivateAccountView, ReactivationSentView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),  # ../users/login
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

    path('activate/<str:token>/<int:user_id>', ActivateAccountView.as_view(), name='activate'),
    path('reactivation_sent/', ReactivationSentView.as_view(), name='reactivation_sent')

]
