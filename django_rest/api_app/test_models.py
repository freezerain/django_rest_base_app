import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from django_rest.api_app.models import Events
from django_rest.api_app.serializers import UserSerializer, EventSerializer


# EVENTS TESTS
@pytest.mark.django_db
def test_event_list(client, create_event, rf) -> None:
    """
    Test reading all events
    :param client:
    :return:
    """
    create_event()
    url = reverse('events-list')
    response = client.get(url)
    expected_data = EventSerializer(Events.objects.all(), many=True, context={
        'request': rf.get(url)
    }).data
    assert response.status_code == 200
    assert response.data['results'] == expected_data


@pytest.mark.django_db
def test_event_detail(client, create_event):
    """
    Test event detailed view by id
    :param client:
    :param create_event:
    :return:
    """
    event = create_event(title='myevent')
    url = reverse('events-detail', kwargs={'pk': event.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'myevent' in response.content.decode()


# USERS TESTS
@pytest.mark.django_db
def test_user_list(client, create_user, rf):
    """
    Test reading all users
    :param client:
    :param create_user:
    :return:
    """
    create_user(username='someone')
    url = reverse('user-list')
    response = client.get(url)
    expected_data = UserSerializer(User.objects.all(), many=True, context={
        'request': rf.get(url)
    }).data
    assert response.status_code == 200
    assert response.data['results'] == expected_data


@pytest.mark.django_db
def test_user_detail(client, create_user):
    """
    Test user detailed view by id
    :param client:
    :param create_user:
    :return:
    """
    user = create_user(username='someone')
    url = reverse('user-detail', kwargs={'pk': user.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'someone' in response.content.decode()
