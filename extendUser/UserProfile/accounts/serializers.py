
from rest_framework import serializers

class loginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(style={'input_type':'password'})