import pytest
import uuid

from rest_framework.test import APIClient

from django_rest.api_app.models import Events

test_password = 'strong-test-pass'


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = 'test_username_' + str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def create_event(db, create_user):
    def make_event(**kwargs):
        if 'title' not in kwargs:
            kwargs['title'] = 'test_title_' + str(uuid.uuid4())
        if 'owner' not in kwargs:
            kwargs['owner'] = create_user()
        return Events.objects.create(**kwargs)

    return make_event
