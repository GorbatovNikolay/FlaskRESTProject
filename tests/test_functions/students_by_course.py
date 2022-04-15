def test_get_students(client):
    response = client.get('/api/students/Art')

    assert response.status_code == 200
    assert 'data' in response.json.keys()


def test_get_students_with_invalid_course(client):
    response = client.get('/api/students/Arts')

    assert response.status_code == 200
    assert response.json == {'message': 'There is no Arts course.'}
