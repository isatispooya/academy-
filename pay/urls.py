from django.urls import path
from .views import DiscountViewset


urlpatterns = [
    path('discount/',DiscountViewset.as_view(), name = 'discount')
]