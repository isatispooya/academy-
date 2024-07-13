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
       course =CourseSerializer(course,many=True).data
       return Response(course,status=status.HTTP_200_OK)



class AllGroupViewset(APIView):
    def get(self,request):
       group = models.Grouping.objects.all()
       
       if not group.exists():
           return Response(request,status=status.HTTP_404_NOT_FOUND)
       
       serialize = groupingserializer(group,many=True)
       return Response(serialize.data, status=status.HTTP_200_OK)
    
class AllCourseGroupView(APIView):
    def get(self,request,group):
        group = models.Grouping.objects.filter(id=group)
        if not group.exists():
            result ={'message':"گروه وجود ندارد"}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        group = group.first()
        


        course = models.Course.objects.filter(grouping=group)
        if not course.exists():
            result ={'message':"وجود ندارد"}

            return Response(result,status=status.HTTP_404_NOT_FOUND)
        
        serialize = CourseSerializer(course,many=True)
        return Response(serialize.data,status=status.HTTP_200_OK)


