import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from main.models import Stack

pytestmark = pytest.mark.django_db


def test_str_method():
    feature_name = "feature-new"
    s = Stack.objects.create(
        feature_name=feature_name, what_do="something", how_did="good realization"
    )
    assert str(s) == feature_name.capitalize()


def test_unique_feature_name():
    feature_name = "feature-new"
    Stack.objects.create(
        feature_name=feature_name, what_do="something", how_did="good_realization"
    )
    with pytest.raises(IntegrityError):
        stack2 = Stack.objects.create(
            feature_name=feature_name,
            what_do="something 2",
            how_did="good realization 2",
        )

def test_max_length_feature_name():
    feature_name = "t" * 51
    stack = Stack.objects.create(
        feature_name=feature_name, what_do="x", how_did="y"
    )
    with pytest.raises(ValidationError):
        stack.full_clean()
