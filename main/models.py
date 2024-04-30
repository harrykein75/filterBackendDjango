from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Point(models.Model):
    location  = models.CharField(max_length=280)
    address = models.CharField(max_length=280, blank=True, null=True)
    user      = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    latitude  = models.FloatField()
    longitude = models.FloatField()
    visible   = models.BooleanField(default=True)
    date = models.DateField()
