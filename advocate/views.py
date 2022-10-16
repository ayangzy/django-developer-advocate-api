from rest_framework.generics import ListAPIView, RetrieveAPIView
from advocate.serializer import AdvocateSerializer, AdvocateDetailSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from core.models import Advocate

class AdvocateListView(ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    
    pagination_class = LimitOffsetPagination
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class AdvocateDetailView(RetrieveAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateDetailSerializer
    

