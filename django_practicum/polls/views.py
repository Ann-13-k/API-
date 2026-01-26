from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Avg
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer, UniversityCourseInfoSerializer

class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    # Поиск по названию и стране
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']

    @action(detail=True, methods=["get"])
    def courses(self, request, pk=None):
        courses = UniversityCourse.objects.filter(university_id=pk)

        # Фильтрация по title курса
        title = request.query_params.get('title')
        if title:
            courses = courses.filter(course__title__icontains=title)

        # Фильтрация по семестру
        semester = request.query_params.get('semester')
        if semester:
            courses = courses.filter(semester__icontains=semester)

        # Сортировка по длительности курса
        ordering = request.query_params.get('ordering')
        if ordering:
            courses = courses.order_by(ordering)

        serializer = UniversityCourseInfoSerializer(courses, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def course_stats(self, request, pk=None):
        qs = UniversityCourse.objects.filter(university_id=pk)

        total_courses = qs.count()
        average_duration = qs.aggregate(Avg('duration_weeks'))["duration_weeks__avg"] or 0
        return Response({
            "total_courses": total_courses,
            "average_duration": average_duration
        })

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title']
    ordering = ['title']

class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer

