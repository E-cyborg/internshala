from django.db import models

# Create your models here.
class UsernameTelegram(models.Model):
    name=models.CharField(max_length=50)
    data_time=models.DateTimeField(auto_now_add=True)