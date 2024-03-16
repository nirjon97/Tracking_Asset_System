from django.db import models
from django.contrib.auth.models import AbstractUser,User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)

class Device(models.Model):
    DEVICE_TYPES = [
        ('Phone', 'Phone'),
        ('Tablet', 'Tablet'),
        ('Laptop', 'Laptop'),
        ('Other', 'Other'),
    ]
    serial_number = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    condition = models.CharField(max_length=100)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out = models.DateTimeField(auto_now_add=True)
    checked_in = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=100)
    condition_when_checked_in = models.CharField(max_length=100, null=True, blank=True)
