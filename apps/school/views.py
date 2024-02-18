from rest_framework import viewsets
from apps.school.models import Student, Course, Registration
from apps.school.serializer import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer
)


class StudentsViewSet(viewsets.ModelViewSet):
    '''
    View all students.

    Returns:
        List of all students.
    '''

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    '''
    View all courses.

    Returns:
        List of all courses.
    '''

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    '''
    View all registrations

    Returns:
        List of all registrations
    '''

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
