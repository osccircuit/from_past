from django.urls import path
from users.views import RegistrationView, SignInView 

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('sign-in/', SignInView.as_view(), name='sign_in')
]
