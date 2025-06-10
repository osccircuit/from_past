from django import forms
from letter.models import Letter


class LetterForm(forms.Form):
    for_who = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "Кому"})
    )
    from_who = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "От кого"})
    )
    date_arrival = forms.DateField(
        required=True, label='Дата получения'
    )
    letter_text = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"placeholder": "Ваше письмо"})
    )

    class Meta:
        model = Letter
        fields = ['for_who', 'from_who', 'date_arrival', 'lettet_text']