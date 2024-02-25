from rest_framework import serializers
from apps.school.models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'date_birth', 'photo']


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'rg', 'cpf', 'date_birth', 'photo']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'description', 'level']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = ['created_at', 'updated_at']


class ListRegistrationsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class ListRegistrationsCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student']
