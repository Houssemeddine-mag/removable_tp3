from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'address', 'university']


class StudentUniversitySerializer(serializers.Serializer):
    student_name = serializers.CharField()
    university_name = serializers.CharField()
