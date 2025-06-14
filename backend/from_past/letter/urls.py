from django.urls import path
from letter import views

app_name = 'letter'

urlpatterns = [
    path('letter/', views.NewLetterView.as_view(), name='letter'),
]
