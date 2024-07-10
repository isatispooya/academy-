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

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class SubMenuSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = models.SubMenu
        fields = ['icon', 'title', 'url', 'menu']
