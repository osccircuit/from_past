from django.contrib.auth.forms import UserChangeForm
from django import forms
from users.models import User

class UpdateForm(UserChangeForm):
    image = forms.ImageField(label='Изменить аватар')
    username = forms.CharField(label='Пользователь')
    email = forms.CharField(label='Email')

    class Meta:
        model = User
        fields = ('image', 'username', 'email')