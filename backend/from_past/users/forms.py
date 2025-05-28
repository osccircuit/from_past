from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"}),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Пароль"}),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Повторите пароль"}),
    )
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')
