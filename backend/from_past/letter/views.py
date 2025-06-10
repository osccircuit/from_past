from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class NewLetterView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users:sign_in')
    template_name = "letter/letter_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Письмо - FromPast"
        return context
