from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class NewLetterView(TemplateView):
    template_name = "letter/letter_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Письмо - FromPast"
        return context
