from django.contrib.auth.forms import UserChangeForm
from django import forms
from users.models import User

class UpdateForm(UserChangeForm):
    image = forms.ImageField()
    username = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = ('image', 'username', 'email')