from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.school.models import Student


class StudentsTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('school:Students-list')
        self.student_1 = Student.objects.create(
            name='Jessica Lane',
            rg='332758455',
            cpf='22061588255',
            date_birth='2013-02-26',
            photo=''
        )
        self.student_2 = Student.objects.create(
            name='Jessica Lane 2',
            rg='332758445',
            cpf='22061598255',
            date_birth='2013-02-26',
            photo=''
        )

    def test_request_get_students(self):
        '''Test to check the GET request to list the students.'''

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 2)

    def test_request_post_student(self):
        '''Test to check the POST request to create a student.'''

        data = {
            'name': 'Jessica Lane',
            'rg': '332758455',
            'cpf': '22061588255',
            'date_birth': '2013-02-26',
            'photo': ''
        }
        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 3)
        self.assertEqual(Student.objects.get(id=3).name, 'Jessica Lane')

    def test_request_put_student(self):
        '''Test to verify PUT request to update a student.'''

        data = {
            'name': 'Jessica Lane',
            'rg': '332758455',
            'cpf': '22061588255',
            'date_birth': '2013-02-26',
            'photo': ''
        }
        response = self.client.put('/students/1/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 2)

    def test_request_delete_student(self):
        '''Test to check for DELETE request to delete a student.'''

        response = self.client.delete('/students/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 1)
