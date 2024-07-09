from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from . import models
import pandas as pd
from authentication import fun


class AllCourseViewest(APIView):
    def get(self,request):
    #    token = request.headers['Authorization']
    #    user = fun.decryptionUser(token)
    #    if not user:
    #         result = {'message':'کاربر یافت نشد'}
    #         return Response(result,status=status.HTTP_400_BAD_REQUEST)
    #    course = models.Course.objects.all()
    #    course =CourseSerializer(course,many=True, null = True , blank = True ).data
    #     # result = {'message':'OK'}
    #    return Response(course,status=status.HTTP_200_OK)

        token = request.header['Authorization']
        user = fun.decryptionUser(token)

        if not user:
            result = {'gfh'}
            return res




