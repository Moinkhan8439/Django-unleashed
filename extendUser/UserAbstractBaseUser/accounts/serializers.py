from rest_framework import serializers
from .models import NewUser
from rest_framework.exceptions import ValidationError 


class TeacherSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model =  NewUser
        fields = ['password','password1','email','mob_no']
    
    def validate(self,data):
        password1=data.pop('password1')
        if(data['password'] != password1):
            raise ValidationError(" your Password Doesn't Match")
        return data

    def save(self, validated_data):
        user = NewUser.objects.create_teacher(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class NormalUserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model =  NewUser
        fields = ['password','password1','email','mob_no']
    
    def validate(self,data):
        password1=data.pop('password1')
        if(data['password'] != password1):
            raise ValidationError(" your Password Doesn't Match")
        return data

    def save(self, validated_data):
        user = NewUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user