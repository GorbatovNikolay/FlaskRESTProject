def test_add_student_to_course(client):
    data = '{"course_ids": [1, 2, 3]}'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    response = client.post('/api/courses/student/200', data=data, headers=headers)

    assert response.status_code == 200
    assert response.json == {'message': f'Student id=200 has been enrolled to chosen courses.'}


def test_add_does_not_exist(client):
    data = '{"course_ids": [4, 5, 6]}'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    response = client.post('/api/courses/student/999', data=data, headers=headers)

    assert response.status_code == 200
    assert response.json == {'message': f'Student id=999 does not exist.'}
