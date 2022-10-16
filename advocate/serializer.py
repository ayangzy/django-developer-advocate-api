from dataclasses import fields
from rest_framework import serializers
from core.models import Advocate

class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'
        depth = 1