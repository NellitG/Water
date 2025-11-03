from django.urls import path
from .views import ClientListCreate, MeterReadingListCreate, ClientReading

urlpatterns = [
    path('clients/', ClientListCreate.as_view(), name='client-list-create'),
    path('readings/', MeterReadingListCreate.as_view(), name='reading-list-create'),
    path('clients/<int:pk>/readings/', ClientReading.as_view(), name='client-readings'),
]