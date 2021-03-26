from rest_framework import serializers
from .models import NewUser
from rest_framework.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(max_length=20,write_only=True)

    class Meta :
        model = NewUser
        fields = ['username','email','password','password1']
    
    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        print(password1)
        if(validated_data['password'] == password1 ):
            user = NewUser.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
        else:
            raise ValidationError("password doesnt match")
        return user

