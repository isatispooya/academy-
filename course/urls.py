from django.urls import path
from .views import AllCourseViewest,AllGroupViewset,AllCourseGroupView


urlpatterns = [
    path('course/',AllCourseViewest.as_view(), name = 'course'),
    path('group/',AllGroupViewset.as_view(), name = 'group'),
    path('coursegroup/<int:group>/',AllCourseGroupView.as_view(), name = 'coursegroup')

]