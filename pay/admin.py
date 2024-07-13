from django.contrib import admin
from .models import Discount,Pay,BasketBuy

admin.site.register(Discount)
admin.site.register(Pay)
admin.site.register(BasketBuy)