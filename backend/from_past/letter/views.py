from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from letter.forms import LetterForm

class NewLetterView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('users:sign_in')
    template_name = "letter/letter_form.html"
    form_class = LetterForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Письмо - FromPast"
        return context
