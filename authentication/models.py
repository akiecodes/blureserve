from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    w3_id = models.CharField(max_length=100, unique=True)  # Store W3 ID
    is_verified = models.BooleanField(default=False)  # For 2FA verification

    def __str__(self):
        return self.username
