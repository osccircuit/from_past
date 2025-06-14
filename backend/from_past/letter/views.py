from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from letter.forms import LetterForm
from letter.models import Letter 

class NewLetterView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('users:sign_in')
    template_name = "letter/letter_form.html"
    form_class = LetterForm

    def get_success_url(self):
        return reverse_lazy('main:index')

    def form_valid(self, form):
        user = self.request.user
        for_who = form.cleaned_data['for_who']
        from_who = form.cleaned_data['from_who']
        date_arrival = form.cleaned_data['date_arrival']
        letter_text = form.cleaned_data['letter_text']
        letter = Letter(
            user=user,
            for_who=for_who,
            from_who=from_who,
            date_arrival=date_arrival,
            letter_text=letter_text
        )
        try:
            letter.full_clean()
            letter.save()
        except ValidationError as error:
            form.add_error(None, error)
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Письмо - FromPast"
        return context
