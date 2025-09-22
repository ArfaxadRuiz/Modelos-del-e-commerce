from django.urls import path
from .views import SalesDataView, DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('sales-data/', SalesDataView.as_view(), name='sales-data'),
]