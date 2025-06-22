from django.urls import path
from archive.views import UserArchiveView

app_name = 'archive'

urlpatterns = [
    path('user_archive/', UserArchiveView.as_view(), name='user-archive')
]
