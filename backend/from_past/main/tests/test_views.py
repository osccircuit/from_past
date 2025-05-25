import pytest
from django.urls import reverse
from main.models import Stack

pytestmark = pytest.mark.django_db


def test_index_view_status_code(client):
    url = reverse("main:index")
    response = client.get(url)
    assert response.status_code == 200


def test_index_view_template(client):
    url = reverse("main:index")
    response = client.get(url)
    assert "main/index.html" in [t.name for t in response.templates]


def test_index_view_context(client):
    stacks = [
        Stack.objects.create(feature_name=f"feat-{i}", what_do="x", how_did="y")
        for i in range(3)
    ]
    url = reverse("main:index")
    response = client.get(url)
    assert stacks == list(response.context["stacks"])