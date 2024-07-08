from django.shortcuts import render
from rest_framework.views import APIView
from GuardPyCaptcha.Captch import GuardPyCaptcha
from rest_framework.response import Response
from rest_framework import status
import random
from . import models
import datetime
from . import serializers
from . import fun

class CaptchaViewest(APIView):
    def get (self,request):
        captcha = GuardPyCaptcha()
        captcha = captcha.Captcha_generation(num_char=4,only_num=True)
        return Response(captcha,status=status.HTTP_200_OK)

class OtpViewest(APIView):
    def post(self,request):
        captcha = GuardPyCaptcha()
        captcha = captcha.check_response(request.data['encrypted_response'],request.data['captcha'])
        if False:
            result = {'message':'کد کپچا صحیح نمی باشد'}
            return Response(result,status=status.HTTP_406_NOT_ACCEPTABLE)
        mobile = request.data['mobile']
        if not mobile:
            result = {'message':'شماره موبایل لازم است.'}
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        try:
            users = models.Customer.objects.get(mobile=mobile)
            result = {'registered':True, 'message':'کد تایید ارسال شد'}

        except models.Customer.DoesNotExist:
            result = {'registered':False,'message':'کد تایید ارسال شد'}
  
        otp = '11111'# random.randint(10000,99999)
        otp_obj = models.OTP(code=otp,mobile=mobile)
        otp_obj.save()
        return Response(result,status=status.HTTP_200_OK)
    
class LoginViewest(APIView):
    def post(self,request):
        mobile = request.data['mobile']
        code = request.data['code']

        if not mobile :
            result = {'message':'شماره موبایل لازم است.'}
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        
        user = models.Customer.objects.filter(mobile = mobile)
        if not user.exists():
            result = {'message':'شماره موبایل صحیح نمی باشد'}
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        
        if not code:
            result = {'message':'کد صحیح نمی باشد'}
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        
        otp_obj = models.OTP.objects.filter(code = code,mobile = mobile)
        if not otp_obj.exists():
            result = {'message':'کد صحیح نمی باشد'}
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        otp_obj = otp_obj.first()
        now = datetime.datetime.now()
        deley = now-datetime.timedelta(minutes=10)
        if otp_obj.date.timestamp()<=deley.timestamp():
            result = {'message':'کد منقضی شده است'}
            otp_obj.delete()
            return Response(result,status=status.HTTP_400_BAD_REQUEST)
        otp_obj.delete()
        user = user.first()
        token = fun.encryptionUser(user)
        result = {'token':token}
        
        return Response(result,status=status.HTTP_200_OK)
    
class UserViewest(APIView):
    def get(self,request):
       token = request.headers['Authorization']
       user = fun.decryptionUser(token)
       if not user:
           result = {'message':'ن'}
           return Response(result,status=status.HTTP_400_BAD_REQUEST)
       userserialize = serializers.CustomerSerializer(user.first()).data
    #    print(user)
       return Response(userserialize,status=status.HTTP_200_OK)


