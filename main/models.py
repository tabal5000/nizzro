from django.db import models
import datetime
# Create your models here.

class Computer(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    serial_number = models.CharField(max_length=128)
    date_created = models.DateField(default=datetime.date.today, blank=True)
    keywords = models.CharField(max_length=256)

    