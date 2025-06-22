from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView
from archive.forms import UpdateForm
from users.models import User


class UserArchiveView(UpdateView):
    template_name = "archive/user_archive.html"
    form_class = UpdateForm

    def get_success_url(self):
        return reverse_lazy('archive:user-archive')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Архив - FromPast"
        return context
