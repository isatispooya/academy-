from . import models
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = '__all__'


class groupingserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grouping
        fields = '__all__'