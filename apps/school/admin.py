from django.contrib import admin
from apps.school.models import Student, Course, Registration


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('level',)
    list_per_page = 10


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course',)
    list_display_links = ('id',)
    list_filter = ('period',)
    list_per_page = 10
