from datetime import datetime

from django.db import models
import django


class Car(models.Model):
    plate = models.CharField(max_length=16, null=False, blank=False, unique=True)
    model = models.CharField(max_length=128, null=False, blank=False)
    motor = models.CharField(max_length=128, null=False, blank=False)
    chassis = models.CharField(max_length=128, null=False, blank=False, unique=True)
    color = models.CharField(max_length=32, null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
