from django.db import models
from django.utils import timezone

def today_date():
    return timezone.now().date()

class Notes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateField(default=today_date) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
