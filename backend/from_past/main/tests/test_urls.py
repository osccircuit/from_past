from django.urls import reverse, resolve
from main.views import MainPageView

def test_index_url_resolves():
    path = reverse('main:index')
    assert resolve(path).func.view_class == MainPageView