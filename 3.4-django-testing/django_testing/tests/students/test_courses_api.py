import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory()


@pytest.mark.django_db
def test_first_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    url = '/api/v1/courses/' + f'{course[0].pk}/'
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert course[0].name == data['name']
    assert course[0].pk == data['id']


@pytest.mark.django_db
def test_list_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'test_course'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_filter_by_id(client, courses_factory):
    course = courses_factory(_quantity=1)
    url = '/api/v1/courses/?id=' + f'{course[0].pk}'
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert course[0].pk == data[0]['id']


@pytest.mark.django_db
def test_filter_by_name(client):
    course = client.post('/api/v1/courses/', data={'name': 'test_course'})
    data = course.json()
    response = client.get('/api/v1/courses/?name=test_course')
    assert response.status_code == 200
    assert data['name'] == 'test_course'


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    url = '/api/v1/courses/' + f'{course[0].pk}/'
    response = client.patch(url, data={'name': 'test_course'})
    data = client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert data.data[0]['name'] == 'test_course'


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    count = Course.objects.count()
    course = courses_factory(_quantity=1)
    assert Course.objects.count() == count + 1
    url = '/api/v1/courses/' + f'{course[0].pk}/'
    response = client.delete(url)
    assert response.status_code == 204
    assert Course.objects.count() == count
