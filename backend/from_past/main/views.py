from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from main.models import Stack

# Create your views here.
class MainPageView(ListView):
    template_name = 'main/index.html'
    model = Stack
    context_object_name = 'stacks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная - FromPast'
        return context