from django.urls import path
from .views import ClientListCreate, MeterReadingListCreate, ClientPreviousReading, CalculateBill, DashboardStats

urlpatterns = [
    path("clients/", ClientListCreate.as_view(), name="clients"),
    path("readings/", MeterReadingListCreate.as_view(), name="meter_readings"),
    path("clients/<int:client_id>/previous-reading/", ClientPreviousReading.as_view(), name="previous_reading"),
    path("clients/<int:client_id>/calculate-bill/", CalculateBill.as_view(), name="calculate_bill"),
    path("dashboard-stats/", DashboardStats.as_view(), name="dashboard_stats"),
]
