from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import RegistrationView, SignInView 

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]
