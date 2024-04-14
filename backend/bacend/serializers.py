from .models import *
from rest_framework import serializers

class filmeSerializer(serializers.ModelSerializer):
    class Meta:
        model=film 
        fields="__all__"
class rezervareSerializer(serializers.ModelSerializer):
    class Meta:
        model=rezervare 
        fields="__all__"
class recomandariSerializer(serializers.ModelSerializer):
    class Meta:
        model=recomandari 
        fields="__all__"