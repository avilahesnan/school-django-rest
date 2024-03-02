from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.school.models import Registration, Student, Course


class RegistrationsTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('school:Registrations-list')
        self.course = Course.objects.create(
            name='Django',
            code='CD1',
            description='Django Course',
            level='B'
        )
        self.student = Student.objects.create(
            name='Jessica Lane',
            rg='332758455',
            cpf='22061588255',
            date_birth='2013-02-26',
            photo=''
        )
        self.registration_1 = Registration.objects.create(
            student=self.student,
            course=self.course,
            period='M'
        )
        self.registration_2 = Registration.objects.create(
            student=self.student,
            course=self.course,
            period='N'
        )

    def test_request_get_registration(self):
        '''Test to verify the GET request to list registrations.'''

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Registration.objects.count(), 2)

    def test_request_post_registration(self):
        '''Test to check the POST request to create a registration.'''

        data = {
            'period': 'A',
            'student': 1,
            'course': 1
        }
        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Registration.objects.count(), 3)

    def test_request_put_registration(self):
        '''Test to verify PUT request to update a registration.'''

        data = {
            'period': 'M',
            'student': 1,
            'course': 1
        }
        response = self.client.put('/registrations/1/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Registration.objects.count(), 2)

    def test_request_delete_registration(self):
        '''Test to verify that DELETE is not allowed to delete a registration.'''  # noqa: E501

        response = self.client.delete('/registrations/1/')

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # noqa: E501
