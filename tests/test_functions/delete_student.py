def test_delete_student(client):
    first_name = 'Nick'
    last_name = 'Cage'
    response = client.delete(f'http://127.0.0.1:5000/api/student/{first_name}/{last_name}')

    assert response.status_code == 200
    assert response.json == {'message': f'Student {first_name} {last_name} has been deleted.'}


def test_delete_does_not_exist(client):
    response = client.delete('/api/student/N/J')

    assert response.status_code == 200
    assert response.json == {'message': f'Student N J does not exist.'}
