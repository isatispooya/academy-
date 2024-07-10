from django.shortcuts import render
from rest_framework.views import APIView
from authentication import fun
from rest_framework.response import Response
from rest_framework import status
from . import models
from .serializers import DiscountSerializer
import datetime

class DiscountViewset(APIView):
    def get(self,request):
         token = request.headers['Authorization']
         user = fun.decryptionUser(token)
         if not user:
             result = {'message':'کاربر وجود ندارد'}
             return Response(result,status=status.HTTP_400_BAD_REQUEST)
         discount_code = request.data.get('code')
         if not discount_code:
             return Response({'message':'کد تخفیف وارد نشده است'},status=status.HTTP_406_NOT_ACCEPTABLE)
         check_code = models.Discount.objects.get(code = discount_code)
         if not check_code:
             return Response({'message':'کد تخفیف نامعتبر است'},status=status.HTTP_404_NOT_FOUND)
         codeserializer = DiscountSerializer(check_code).data
         expserializer = datetime.datetime.strptime(codeserializer['exp_date'],"%Y-%m-%dT%H:%M:%SZ").date()
         now = datetime.datetime.now().date()
         if now > expserializer:
             return Response({'message':'کد تخفیف منقضی شده است'},status=status.HTTP_400_BAD_REQUEST)
        #   type = type(expserializer)
        #  print(expserializer)
         return Response({'message':'ok'},status=status.HTTP_200_OK)