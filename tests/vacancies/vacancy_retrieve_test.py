from datetime import date

import pytest


@pytest.mark.django_db
def test_retrieve_vacancy(client, vacancy, hr_token):
    expected_response = {
        'id': vacancy.pk,
        'skills': [],
        'created': date.today().strftime('%Y-%m-%d'),
        'text': 'text test1',
        'slug': 'test1',
        'status': 'draft',
        'min_experience': None,
        'likes': 0,
        'updated_at': None,
        'user': vacancy.user_id
    }

    response = client.get(
        f'/vacancy/{vacancy.pk}/',
        HTTP_AUTHORIZATION='Token ' + hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
