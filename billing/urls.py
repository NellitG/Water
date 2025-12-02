from django.urls import path
from .views import (
    ClientListCreate,
    ClientRetrieveUpdateDelete,
    MeterReadingListCreate,
    MeterReadingRetrieveUpdateDelete,
    ClientPreviousReading,
    CalculateBill,
    DashboardStats,
    LoginView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # CLIENT CRUD
    path("clients/", ClientListCreate.as_view(), name="clients"),
    path("clients/<int:id>/", ClientRetrieveUpdateDelete.as_view(), name="client_detail"),

    # METER READING CRUD
    path("readings/", MeterReadingListCreate.as_view(), name="meter_readings"),
    path("readings/<int:id>/", MeterReadingRetrieveUpdateDelete.as_view(), name="reading_detail"),

    # EXTRA OPERATIONS
    path("clients/<int:client_id>/previous-reading/", ClientPreviousReading.as_view(), name="previous_reading"),
    path("clients/<int:client_id>/calculate-bill/", CalculateBill.as_view(), name="calculate_bill"),

    # STATS + AUTH
    path("dashboard-stats/", DashboardStats.as_view(), name="dashboard_stats"),
    path("login/", LoginView.as_view(), name="login"),

    # Receipts
    path("receipts/", views.ReceiptListCreate.as_view(), name="receipts"),
    path("receipts/<int:id>/", views.ReceiptRetrieveUpdateDelete.as_view(), name="receipt_detail"),
    path("receipts/<int:id>/save-pdf/", views.SaveReceiptPDF.as_view(), name="save_receipt_pdf"),
]
