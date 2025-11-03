from django.shortcuts import render
from rest_framework import generics
from .models import Client, MeterReading
from .serializers import ClientSerializer, MeterReadingSerializer

# Create your views here.
class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MeterReadingListCreate(generics.ListCreateAPIView):
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer

class ClientReading(generics.ListAPIView):
    serializer_class = MeterReadingSerializer

    def get_queryset(self):
        client_id = self.kwargs['pk']
        return MeterReading.objects.filter(client__id=client_id)