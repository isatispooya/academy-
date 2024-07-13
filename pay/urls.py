from django.urls import path
from .views import DiscountViewset , BasketBuyViewSet


urlpatterns = [
    path('discount/',DiscountViewset.as_view(), name = 'discount'),
    path('basket/', BasketBuyViewSet.as_view(), name = 'basket')
]