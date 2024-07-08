from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=200)
    national_code = models.CharField(max_length=200,unique=True)
    mobile = models.CharField(max_length=200,unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    gender_choice= [('m','مرد'),('f','زن'),('u','نامشخص'),('c','حقوقی')]
    gender=models.CharField(max_length=1,choices=gender_choice,default='u')
    date_creation=models.DateTimeField(default=timezone.now)
    date_birth=models.DateTimeField(blank=True, null=True)
    date_last_act=models.DateTimeField(default=timezone.now)
    def __str__(self) :
        return f'{self.name}'

class OTP(models.Model):
    mobile = models.CharField(max_length=200)
    code = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return f'{self.code}'
    

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200,unique=True)
    national_code = models.CharField(max_length=200,unique=True)
    gender_choice= [('m','مرد'),('f','زن'),('u','نامشخص')]
    gender=models.CharField(max_length=1,choices=gender_choice,default='u')
    profile_photo = models.ImageField(upload_to='academy/static/image/',null=True, blank=True)
    def __str__(self) :
        return f'{self.name}'