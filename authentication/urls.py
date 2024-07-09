from django.urls import path
from .views import CaptchaViewest , OtpViewest ,LoginViewest , UserViewest

urlpatterns = [
    path('captcha/',CaptchaViewest.as_view(),name = 'captcha'),
    path('otp/',OtpViewest.as_view(),name = 'otp'),
    path('login/',LoginViewest.as_view(),name = 'login'),
    path('user/',UserViewest.as_view(), name = 'user'),
]
