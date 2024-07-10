from . import models
from rest_framework import serializers

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Information
        fields = '__all__'
        
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SliderShow
        fields = '__all__'
