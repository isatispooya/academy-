from django.db import models
from authentication.models import Customer
from django.utils import timezone

class Discount(models.Model):
    code = models.IntegerField()
    exp_date = models.DateTimeField()
    Number_of_consumption = models.IntegerField()
    kind_of_discount = [('r','رقم'),('d','درصد')]
    discount = models.CharField(max_length=1,choices=kind_of_discount)
    amount = models.CharField(max_length=200)
    

class Pay(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    pay_date = models.DateTimeField(default=timezone.now)
    task = models.CharField(max_length=200)
    discount_code = models.ForeignKey(Discount,on_delete=models.CASCADE)
    def __str__(self) :
        return f'{self.customer}'

