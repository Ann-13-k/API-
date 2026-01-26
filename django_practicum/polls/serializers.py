from rest_framework import serializers
from .models import University, Course, UniversityCourse

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        read_only_fields = ["id"]
        fields = [
            "id",
            "name",
            "country"
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        read_only_fields = ["id"]
        fields = [
            "id",
            "title",
            "description"
        ]

class UniversityCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityCourse
        read_only_fields = ["id"]
        fields = [
            "id",
            "university",
            "course",
            "semester",
            "duration_weeks"
        ]

class UniversityCourseInfoSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title')

    class Meta:
        model = UniversityCourse
        fields = [
            "course_title",
            "semester",
            "duration_weeks"
        ]