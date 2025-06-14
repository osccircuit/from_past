from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from users.forms import RegistrationUserForm, LoginForm
from users.models import User


class RegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = RegistrationUserForm

    def get_success_url(self):
        return reverse_lazy("users:sign_in")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация - FromPast"
        return context

    def form_valid(self, form):
        form.save()
        form.instance
        return super().form_valid(form)


class SignInView(LoginView):
    template_name = "users/sign_in.html"
    form_class = LoginForm

    def get_success_url(self):
        if self.request.POST.get('next'):
            return self.request.POST.get('next')
        return reverse_lazy("main:index")

    def form_valid(self, form):
        user = form.get_user()

        if user:
            auth.login(self.request, user)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Вход - FromPast"
        return context
