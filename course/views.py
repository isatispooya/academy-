from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import CourseSerializer, groupingserializer
from . import models
import pandas as pd
from authentication import fun


class AllCourseViewest(APIView):
    def get(self,request):
       course = models.Course.objects.all()
       course =CourseSerializer(course,many=True, null = True , blank = True ).data
       return Response(course,status=status.HTTP_200_OK)

class AllGroupViewset(APIView):
    def get(self,request):
       token = request.headers['Authorization']
       user = fun.decryptionUser(token)
       if not user:
           result = {'message':'کاربر یافت نشد'}
           return Response(result,status=status.HTTP_400_BAD_REQUEST)
       group = models.Grouping.objects.all()
       
       if not group.exists():
           return Response(request,status=status.HTTP_404_NOT_FOUND)
       
       serialize = groupingserializer(group,many=True)
       return Response(serialize.data, status=status.HTTP_200_OK)
    
