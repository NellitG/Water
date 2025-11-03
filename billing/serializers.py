from rest_framework import serializers
from .models import Client, MeterReading
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone', 'meter_number']

class MeterReadingSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.name')
    class Meta:
        model = MeterReading
        fields = ['id', 'client', 'client_name', 'current_reading', 'previous_reading', 'units_consumed', 'amount', 'date']

        read_only_fields = ['previous_reading', 'units_consumed', 'amount']

        def create(self, validated_data):
            client = validated_data['client']
            current_reading = validated_data['current_reading']

            last = MeterReading.objects.filter(client=client).order_by('-date').first()
            prev = last.current_reading if last else 0

            if current_reading < prev:
                raise serializers.ValidationError("Current reading cannot be less than previous reading.")
            
            validated_data['previous_reading'] = prev
            validated_data['units_consumed'] = current_reading - prev
            validated_data['amount'] = validated_data['units_consumed'] * MeterReading.RATE_PER_UNIT

            return super().create(validated_data)

        def update(self, instance, validated_data):
            client = validated_data['client']
            current_reading = validated_data['current_reading']

            last = MeterReading.objects.filter(client=client).order_by('-date').first()
            prev = last.current_reading if last else 0

            if current_reading < prev:
                raise serializers.ValidationError("Current reading cannot be less than previous reading.")
            
            validated_data['previous_reading'] = prev
            validated_data['units_consumed'] = current_reading - prev
            validated_data['amount'] = validated_data['units_consumed'] * MeterReading.RATE_PER_UNIT

            return super().update(instance, validated_data)