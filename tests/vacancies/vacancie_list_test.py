from datetime import date

import pytest


@pytest.mark.django_db
def test_vacancy_list(client, vacancy):

    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [{
            'id': vacancy.pk,
            'text': 'text test1',
            'slug': 'test1',
            'status': 'draft',
            'created': date.today().strftime('%Y-%m-%d'),
            'username': 'test1',
            'skills': []
        }]
    }

    response = client.get('/vacancy/')

    assert response.status_code == 200
    assert response.data == expected_response
