from django.urls import path

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import views
from .views import registerListView

app_name = 'web'
urlpatterns = [
        path('', views.loginPage, name='loginPage'),
        path('registerPage/<int:pk>', views.registerPage, name='registerPage'),
        path('registerData', views.registerData, name='registerData'),
        path('registerList/<int:pk>', registerListView.as_view(), name='registerList'),
        path('loginUser', views.loginUser, name='loginUser'),

    ]