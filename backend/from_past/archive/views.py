from django.shortcuts import render
from django.views.generic import TemplateView


class UserArchiveView(TemplateView):
    template_name = "archive/user_archive.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Архив - FromPast"
        return context
