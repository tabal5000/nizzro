from django.db import models
from model_utils.managers import InheritanceManager
import datetime
# Create your models here.


class Lists(models.Model):
    code = models.CharField(max_length=20)
    value = models.CharField(max_length=128)

    def __str__(self):
        return self.value

class ListElements(models.Model):
    value = models.CharField(max_length=128)
    syslist_id = models.ForeignKey(Lists, on_delete = models.CASCADE)
    def __str__(self):
        return self.value

class Processor(models.Model):
    model = models.ForeignKey(ListElements, on_delete = models.CASCADE, related_name="model_le_id")
    quantity = models.PositiveIntegerField()
    socket = models.ForeignKey(ListElements, on_delete = models.CASCADE, related_name="socket_le_id")
    brand = models.ForeignKey(ListElements, on_delete = models.CASCADE, related_name="brand_le_id")
    frequency = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='images/components/processors')