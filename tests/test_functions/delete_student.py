def test_delete_student(client):
    response = client.delete('/api/student/99')

    assert response.status_code == 200
    assert response.json == {'message': f'Student id=99 has been deleted.'}


def test_delete_does_not_exist(client):
    response = client.delete('/api/student/999')

    assert response.status_code == 200
    assert response.json == {'message': f'Student id=999 does not exist.'}
