from django.urls import path, include
from apps.school.views import StudentsViewSet, CoursesViewSet
from rest_framework import routers


app_name = 'school'

router = routers.DefaultRouter()

router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')

urlpatterns = [
    path('', include(router.urls)),
]
