from rest_framework import serializers
from apps.school.models import Student, Course, Registration
from apps.school.validators import (
    cpf_valid,
    rg_valid,
    phone_valid
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'date_birth', 'photo']

    def validate(self, data):
        if not rg_valid(data['rg']):
            raise serializers.ValidationError({'rg': 'The ID is invalid'})
        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'The CPF is invalid'})
        return data


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'rg', 'cpf', 'date_birth', 'photo']

    def validate(self, data):
        if not phone_valid(data['phone']):
            raise serializers.ValidationError({'phone': 'This mobile phone format is not supported'})  # noqa: E501
        if not rg_valid(data['rg']):
            raise serializers.ValidationError({'rg': 'The ID is invalid'})
        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'The CPF is invalid'})
        return data


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
