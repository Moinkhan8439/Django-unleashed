from rest_framework import serializers
from .models import AcademicUser
from rest_framework.exceptions import ValidationError 


class TeacherSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)
    isTeacher=serializers.BooleanField(default=True)
    class Meta:
        model =  AcademicUser
        fields = ['username','password','password1','email','isTeacher']
    
    def validate(self,data):
        password1=data.pop('password1')
        if(data['password'] != password1):
            raise ValidationError(" your Password Doesn't Match")
        return data

    def save(self, validated_data):
        user = AcademicUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class NormalUserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField()
    class Meta:
        model =  AcademicUser
        fields = ['username','password','password1','email']
    
    def validate(self,data):
        password1=data.pop('password1')
        if(data['password'] != password1):
            raise ValidationError(" your Password Doesn't Match")
        return data

    def create(self, validated_data):
        user = AcademicUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user