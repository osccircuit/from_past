from django.shortcuts import render
from django.views.generic import TemplateView

class RegistrationView(TemplateView):
    template_name = 'users/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация - FromPast'
        return context
    
class SignInView(TemplateView):
    template_name = 'users/sign_in.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход - FromPast'
        return context