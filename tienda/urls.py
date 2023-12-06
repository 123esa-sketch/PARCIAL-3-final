from django.urls import path
from.views_api import API1,API2,API3, InicioView

urlpatterns = [
    path('ap/', API1.as_view(), name='api_1'),
    path('ap2/',API2.as_view(), name='api_2'),
    path('ap3/',API3.as_view(), name='api_3'),
    path('',InicioView.as_view(), name='inicio_view'),
]