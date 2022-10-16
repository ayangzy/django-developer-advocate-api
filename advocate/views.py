from rest_framework.generics import ListAPIView, RetrieveAPIView
from advocate.serializer import AdvocateSerializer, AdvocateDetailSerializer
from core.models import Advocate

class AdvocateListView(ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    
class AdvocateDetailView(RetrieveAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateDetailSerializer
    

