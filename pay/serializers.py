from . import models
from rest_framework import serializers

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discount
        fields = '__all__'

class PaySerializer(serializers.ModelSerializer):
    discount_code = serializers.PrimaryKeyRelatedField(queryset=models.Discount.objects.all())
    class Meta:
        model = models.Pay
        fields = '__all__'

class BasketBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasketBuy
        fields = '__all__'
