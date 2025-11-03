from django.contrib import admin
from .models import Client, MeterReading

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'meter_number')

@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('client', 'current_reading', 'previous_reading', 'units_consumed', 'amount', 'date')