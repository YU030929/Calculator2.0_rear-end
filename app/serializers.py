# serializers.py
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        fields = '__all__'

class Cun(serializers.ModelSerializer):
    class Meta:
        model = Cun
        fields = '__all__'

class Dai(serializers.ModelSerializer):
    class Meta:
        model = Dai
        fields = '__all__'