from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from users.forms import RegistrationUserForm
from users.models import User

class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm

    def get_success_url(self):
        return reverse_lazy('main:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация - FromPast'
        return context
    
    def form_valid(self, form):
        form.save()
        form.instance
        return super().form_valid(form)

class SignInView(TemplateView):
    template_name = 'users/sign_in.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход - FromPast'
        return context