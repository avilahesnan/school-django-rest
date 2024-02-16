from django.urls import path
from apps.school.views import students


app_name = 'school'

urlpatterns = [
    path('students/', students, name='students'),
]
