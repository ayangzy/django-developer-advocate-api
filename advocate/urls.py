from django.urls import path
from advocate.views import AdvocateListView

urlpatterns = [
    path('', AdvocateListView.as_view(), name='advocate'),
]
