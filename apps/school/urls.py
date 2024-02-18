from django.urls import path, include
from rest_framework import routers
from apps.school.views import (
    StudentsViewSet,
    CoursesViewSet,
    RegistrationViewSet,
    ListRegistrationsStudent,
    ListRegistrationsCourse
)


app_name = 'school'

router = routers.DefaultRouter()

router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:pk>/registrations/', ListRegistrationsStudent.as_view(), name='ListRegistrationsStudent'),  # noqa: E501
    path('course/<int:pk>/registrations/', ListRegistrationsCourse.as_view(), name='ListRegistrationsCourse'),  # noqa: E501
]
