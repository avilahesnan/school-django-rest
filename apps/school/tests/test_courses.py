from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.school.models import Course


class CoursesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('school:Courses-list')
        self.course_1 = Course.objects.create(
            name='Django',
            code='CD1',
            description='Django Course',
            level='B'
        )
        self.course_2 = Course.objects.create(
            name='Django REST',
            code='CD2',
            description='Django REST Course',
            level='I'
        )

    def test_request_get_courses(self):
        '''Test to check the GET request to list the courses.'''

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 2)

    def test_request_post_course(self):
        '''Test to check the POST request to create a course.'''

        data = {
            'name': 'Flask',
            'code': 'CF1',
            'description': 'Flask Course',
            'level': 'B'
        }
        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 3)
        self.assertEqual(Course.objects.get(id=3).name, 'Flask')

    def test_request_put_course(self):
        '''Test to verify PUT request to update a course.'''

        data = {
            'name': 'Django REST',
            'code': 'CD2',
            'description': 'Django REST Course',
            'level': 'A'
        }
        response = self.client.put('/courses/1/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 2)

    def test_request_delete_course(self):
        '''Test to check for DELETE request to delete a course.'''

        response = self.client.delete('/courses/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 1)
