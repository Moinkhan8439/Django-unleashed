from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import loginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics,status,permissions

# Create your views here.

@api_view(['POST'])
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request=request,username=username,password=password)
    token , created =Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=status.HTTP_200_OK)
    