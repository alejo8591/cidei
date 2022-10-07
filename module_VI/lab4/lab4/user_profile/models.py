from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    customer_id = models.CharField(max_length=20, blank=True, null=True)
    driver_id = models.CharField(max_length=60, blank=True, null=True)
    is_driver = models.BooleanField(default=False)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
