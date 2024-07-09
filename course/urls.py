from django.urls import path
from .views import AllCourseViewest,AllGroupViewset


urlpatterns = [
    path('course/',AllCourseViewest.as_view(), name = 'course'),
    path('group/',AllGroupViewset.as_view(), name = 'group')

]