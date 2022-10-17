from tkinter.tix import Tree
from rest_framework import serializers
from core.models import Company, Advocate


class GetAdvocate(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'links'] 
        
class CompanySerializer(serializers.ModelSerializer):
     class Meta:
        model = Company
        fields = '__all__'
        
     advocates = GetAdvocate(many=True, read_only=True)
     
     
class CompanyDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = Company
        fields = '__all__'
        
     advocates = GetAdvocate(many=True, read_only=True)