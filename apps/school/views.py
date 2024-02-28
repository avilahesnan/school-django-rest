from rest_framework import viewsets, generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']

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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['name']
    search_fields = ['name', 'code']
    filterset_fields = ['level']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)  # noqa: E501
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
        return response


class RegistrationViewSet(viewsets.ModelViewSet):
    '''
    View all registrations

    Returns:
        List of all registrations
    '''

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['student']
    search_fields = ['student', 'course']
    filterset_fields = ['period']

    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(RegistrationViewSet, self).dispatch(*args, **kwargs)


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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['course']


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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['student']
