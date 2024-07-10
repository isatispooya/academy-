from django.urls import path
from .views import AllSliderShow

urlpatterns = [
    path('slider/',AllSliderShow.as_view(), name = 'slider'),

]