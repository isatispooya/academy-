from django.shortcuts import render
from rest_framework.views import APIView
from authentication import fun
from rest_framework.response import Response
from rest_framework import status
from . import models
from course.models import Course
from .serializers import DiscountSerializer,BasketBuySerializer
import datetime

class DiscountViewset(APIView):
    def get(self,request):
         token = request.headers.get('Authorization')
         if not token:
            return Response({'message': 'Authorization header is missing'}, status=status.HTTP_401_UNAUTHORIZED)
         user = fun.decryptionUser(token)
         if not user:
             result = {'message':'کاربر وجود ندارد'}
             return Response(result,status=status.HTTP_401_UNAUTHORIZED)
         discount_code = request.query_params.get('code')
         if not discount_code:
             return Response({'message':'کد تخفیف وارد نشده است'},status=status.HTTP_400_BAD_REQUEST)
         check_code = models.Discount.objects.filter(code = discount_code)
         if not check_code.exists():
             return Response({'message':'کد تخفیف نامعتبر است'},status=status.HTTP_406_NOT_ACCEPTABLE)
         check_code = check_code.first()
         codeserializer = DiscountSerializer(check_code).data
         expserializer = datetime.datetime.strptime(codeserializer['exp_date'],"%Y-%m-%dT%H:%M:%SZ").date()
         now = datetime.datetime.now().date()
         if now > expserializer:
             return Response({'message':'کد تخفیف منقضی شده است'},status=status.HTTP_406_NOT_ACCEPTABLE)
         if check_code.Number_of_consumption<=0:
             return Response({'message':'کد تخفیف به پایان رسیده است'},status=status.HTTP_404_NOT_FOUND)

         return Response({'message':'ok'},status=status.HTTP_200_OK) 
    
class BasketBuyViewSet(APIView):
    def post(self, request): 
        token = request.headers.get('Authorization')
        if not token:
            return Response({'message': 'Authorization header is missing'}, status=status.HTTP_401_UNAUTHORIZED)
        user = fun.decryptionUser(token)
        if not user:
            result = {'message':'کاربر وجود ندارد'}
            return Response(result,status=status.HTTP_401_UNAUTHORIZED)
        course = request.data.get('course')
        
        course = Course.objects.filter(id = course)

        if not course.exists():
            return Response({'message':'دوره وجود ندارد'},status=status.HTTP_404_NOT_FOUND)
        
        course = course.first()
        user = user.first()
        basket = models.BasketBuy.objects.filter(customer = user,course =course)

        if basket.exists():
            message = 'دوره از قبل در سبد خرید موجود است'
            return Response({'message':message},status=status.HTTP_406_NOT_ACCEPTABLE) 
            
        new_basket = models.BasketBuy(customer = user, course = course)
        new_basket.save()
        message = 'دوره اضافه شد'

        return Response({'message':message},status=status.HTTP_200_OK) 
        
    def get(self,request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({'message': 'Authorization header is missing'}, status=status.HTTP_401_UNAUTHORIZED)
        user = fun.decryptionUser(token)
        if not user:
            result = {'message':'کاربر وجود ندارد'}
            return Response(result,status=status.HTTP_401_UNAUTHORIZED)
        user = user.first()
        basket = models.BasketBuy.objects.filter(customer = user)
        
        serializer = BasketBuySerializer(basket,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

            
    def delete(self,request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({'message': 'Authorization header is missing'}, status=status.HTTP_401_UNAUTHORIZED)
        user = fun.decryptionUser(token)
        if not user:
            result = {'message':'کاربر وجود ندارد'}
            return Response(result,status=status.HTTP_401_UNAUTHORIZED)
        user = user.first()
        id = request.data.get('id')
        id = int(id)
        if not id:
            result = {'message':'آیدی انتخاب نشده'} 
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        basket = models.BasketBuy.objects.filter(customer = user, id = id ).first()
        print(basket)
        if not basket:
            return Response({'message': 'آیتم مورد نظر در سبد خرید پیدا نشد'}, status=status.HTTP_404_NOT_FOUND)
   
        basket.delete() 
        return Response({'message':'دوره از سبد خرید حذف شد'},status=status.HTTP_200_OK)