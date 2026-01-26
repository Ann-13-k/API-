from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UniversityViewSet, CourseViewSet, UniversityCourseViewSet

router = DefaultRouter()
router.register("universities", UniversityViewSet)
router.register("courses", CourseViewSet)
router.register("university-courses", UniversityCourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]