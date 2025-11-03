from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    meter_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MeterReading(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='readings')
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    previous_reading = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    units_consumed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateField(default=timezone.now)

    RATE_PER_UNIT = 120  

    def save(self, *args, **kwargs):
        is_new = self.pk is None  

        if is_new:
            
            last_record = MeterReading.objects.filter(client=self.client)\
                                              .exclude(pk=self.pk)\
                                              .order_by('-date')\
                                              .first()

            self.previous_reading = last_record.current_reading if last_record else 0

        if self.current_reading < (self.previous_reading or 0):
            raise ValueError("Current reading cannot be less than previous reading.")

        self.units_consumed = self.current_reading - (self.previous_reading or 0)
        self.amount = self.units_consumed * self.RATE_PER_UNIT

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client.name} - {self.date}"
