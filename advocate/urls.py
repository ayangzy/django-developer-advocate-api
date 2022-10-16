from django.urls import path
from advocate.views import AdvocateListView, AdvocateDetailView

urlpatterns = [
    path('', AdvocateListView.as_view(), name='advocate'),
    path('<int:pk>/', AdvocateDetailView.as_view(), name='advocate-detail')
]
