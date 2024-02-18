from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.school.models import Student, Course, Registration
from apps.school.serializer import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer,
    ListRegistrationsStudentSerializer,
    ListRegistrationsCourseSerializer
)


class StudentsViewSet(viewsets.ModelViewSet):
    '''
    View all students.

    Returns:
        List of all students.
    '''

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    '''
    View all courses.

    Returns:
        List of all courses.
    '''

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    '''
    View all registrations

    Returns:
        List of all registrations
    '''

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListRegistrationsStudent(generics.ListAPIView):
    '''
    View all student registrations

    Returns:
        List of student registrations
    '''

    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationsStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListRegistrationsCourse(generics.ListAPIView):
    '''
    View all course registrations

    Returns:
        List of course registrations
    '''

    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationsCourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
