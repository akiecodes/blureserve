from django.db import models
from django.conf import settings

class Seat(models.Model):
    seat_number = models.IntegerField(unique=True)
    is_reserved = models.BooleanField(default=False)

class Reservation(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

