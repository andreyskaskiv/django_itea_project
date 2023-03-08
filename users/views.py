from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from users.forms import UserLoginForm, UserRegistrationForm, ReactivationForm
from users.models import RegistrationToken
from users.utils import send_activation_email


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        username = form.cleaned_data['username']

        user = User.objects.filter(username=username)
        if user.exists():
            user = user.first()
            if not user.is_active:
                messages.error(self.request, 'Activate your account')
                return redirect('users:login')

        context['errors'] = form.errors
        return self.render_to_response(context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        user_token = RegistrationToken.objects.create(user=user)

        send_activation_email(user, user_token, self.request)
        messages.success(self.request, 'You have to activate your account')
        return super(UserRegistrationView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        return context


class ActivateAccountView(View):
    def get(self, request, user_id, token):
        user = get_object_or_404(User, id=user_id)
        token = get_object_or_404(RegistrationToken, token=token, user=user)

        if not user.is_active and token.verify_token():
            user.is_active = True
            token.clear_token()
            user.save()

            messages.success(request, 'Activation complete')
            return redirect('users:login')

        messages.error(request, 'Token expired')
        return redirect('users:login')


class ReactivationSentView(FormView):
    template_name = 'users/reactivation_sent.html'
    form_class = ReactivationForm
    success_url = reverse_lazy('users:reactivation_sent')

    def form_valid(self, form):
        user = User.objects.get(email=form.cleaned_data['email'])

        if user.is_active:
            messages.warning(self.request, 'This account is already activate')
            return redirect('users:login')

        token = user.token
        token.delete()
        new_token = RegistrationToken.objects.create(user=user)
        send_activation_email(user, new_token, self.request)
        messages.success(self.request, 'New activation email has been sent. Please check your inbox')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['form_errors'] = form.errors
        return self.render_to_response(context)
