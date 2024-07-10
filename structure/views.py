from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import SliderSerializer, MenuSerializer, SubMenuSerializer, InformationSerializer
from . import models

class AllSliderShow(APIView):
    def get(self,request):
        sliderShow = models.SliderShow.objects.all()

        if not sliderShow.exists():
           return Response({"messages":"اسلایدر وجود ندارد"},status=status.HTTP_404_NOT_FOUND)

        sliderShow =SliderSerializer(sliderShow,many=True).data
        return Response(sliderShow,status=status.HTTP_200_OK)


class AllMenu(APIView):
    def get(self,request):
        menu = models.SubMenu.objects.all()

        if not menu.exists():
            return Response({"messages":"منو وجود ندارد"},status=status.HTTP_404_NOT_FOUND)
        
        menu = SubMenuSerializer(menu, many=True).data
        print(menu)
        return Response(menu,status=status.HTTP_200_OK)
    
class AllInformation(APIView):
     def get(self,request):
        information = models.Information.objects.all()

        if not information.exists():
            return Response({"messages":"اطلاعات وجود ندارد"},status=status.HTTP_404_NOT_FOUND)

        information =InformationSerializer(information,many=True).data
        return Response(information,status=status.HTTP_200_OK)