from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import SliderSerializer
from . import models

class AllSliderShow(APIView):
    def get(self,request):
        sliderShow = models.SliderShow.objects.all()

        if not sliderShow.exists():
           return Response({"messages":"اسلایدر وجود ندارد"},status=status.HTTP_404_NOT_FOUND)

        sliderShow =SliderSerializer(sliderShow,many=True).data
        return Response(sliderShow,status=status.HTTP_200_OK)



