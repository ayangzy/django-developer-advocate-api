from company.serializer import CompanySerializer
from core.models import Company
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters


class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    pagination_class = LimitOffsetPagination
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    
    
