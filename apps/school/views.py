from rest_framework import viewsets
from apps.school.models import Student, Course
from apps.school.serializer import StudentSerializer, CourseSerializer


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
