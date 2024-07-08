from django.urls import path
from .views import AllCourseViewest


urlpatterns = [
    path('course/',AllCourseViewest.as_view(), name = 'course')
]