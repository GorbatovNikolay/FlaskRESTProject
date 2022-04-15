def test_get_groups(client):
    response = client.get('/api/groups/30')

    assert response.status_code == 200
    assert 'data' in response.json.keys()


def test_get_groups_with_invalid_student_number(client):
    response = client.get('/api/groups/0')

    assert response.status_code == 200
    assert response.json == {'message': 'There are no matching groups.'}
