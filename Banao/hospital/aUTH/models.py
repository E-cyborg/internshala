from django.contrib.auth.models import AbstractUser
from django.db import models

class cuser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', blank=False, null=False)
    address_line1 = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    pincode = models.CharField(max_length=20, blank=False)
    USER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='patient',
    )

    def __str__(self):
        return self.username
