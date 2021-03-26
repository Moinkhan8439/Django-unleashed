from django.shortcuts import render
from .serializers import NormalUserSerializer,TeacherSerializer
from rest_framework import status,generics
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import NewUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

# Create your views here.
class TeacherView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        u= NewUser.objects.filter(is_teacher=True)
        return u

    def perform_create(self, serializer):
        return serializer.save(serializer.validated_data)
        

class NormalUserView(generics.ListCreateAPIView):
    serializer_class = NormalUserSerializer

    def get_queryset(self):
        u= NewUser.objects.filter(is_teacher=False)
        return u

    def perform_create(self, serializer):
        return serializer.save(serializer.validated_data)

@api_view(['POST'])
def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=authenticate(request=request,email=email,password=password)
    token , created =Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=status.HTTP_200_OK)

@renderer_classes([JSONRenderer])
@permission_classes(['IsAuthenticated'])
@api_view(['GET'])
def all_mb(request):
    mb=NewUser.objects.all().values('mob_no')
    return Response(mb)