def test_add_student(client):
    response = client.post('/api/student/Nick/Cage')

    assert response.status_code == 200
    assert 'message' in response.json.keys()
