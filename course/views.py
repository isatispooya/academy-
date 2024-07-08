from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from . import models
import pandas as pd


class AllCourseViewest(APIView):
    def get(self,request):
        course = models.Course.objects.all()
        course =CourseSerializer(course,many=True).data
        # result = {'message':'OK'}
        return Response(course,status=status.HTTP_200_OK)
