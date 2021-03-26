from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics,status,permissions
from .serializers import RegisterSerializer
from .models import NewUser

@api_view(['POST'])
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request=request,username=username,password=password)
    token , created =Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer=RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.create(serializer.validated_data)
    return Response("Registered",status=status.HTTP_200_OK)
