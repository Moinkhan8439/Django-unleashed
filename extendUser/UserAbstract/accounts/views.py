from django.shortcuts import render
from .serializers import NormalUserSerializer,TeacherSerializer
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import AcademicUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TeacherView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AcademicUser.objects.filter(isTeacher=True)

    def perform_create(self, serializer):
        return serializer.save(serializer.validated_data)
        

@api_view(['POST'])
def normal_user_register(request):
    serializer=NormalUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.create(serializer.validated_data)
    return Response("Registered",status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request=request,username=username,password=password)
    token , created =Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=status.HTTP_200_OK)
