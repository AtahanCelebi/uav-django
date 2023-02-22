from rest_framework import serializers
from .models import IHA

class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = '__all__'