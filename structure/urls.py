from django.urls import path
from .views import AllSliderShow ,AllMenu,AllInformation

urlpatterns = [
    path('slider/',AllSliderShow.as_view(), name = 'slider'),
    path('menu/',AllMenu.as_view(), name = 'menu'),
    path('information/', AllInformation.as_view(), name='information')


]