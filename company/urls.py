from django.urls import path
from company.views import CompanyListView, ComapnyDetailView

urlpatterns = [
    path('', CompanyListView.as_view(), name='company_list'),
    path('<int:pk>/', ComapnyDetailView.as_view(), name='company_detail')
]
