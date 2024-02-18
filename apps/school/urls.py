from django.urls import path, include
from apps.school.views import (
    StudentsViewSet, CoursesViewSet, RegistrationViewSet
)
from rest_framework import routers


app_name = 'school'

router = routers.DefaultRouter()

router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('', include(router.urls)),
]
