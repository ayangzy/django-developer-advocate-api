from rest_framework.generics import ListAPIView
from advocate.serializer import AdvocateSerializer
from core.models import Advocate

class AdvocateListView(ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    

