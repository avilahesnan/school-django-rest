from rest_framework import viewsets, generics
from apps.school.models import Student, Course, Registration
from apps.school.serializer import (
    StudentSerializer,
    StudentSerializerV2,
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

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer


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
