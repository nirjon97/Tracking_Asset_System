from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'position', 'company']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'device_type', 'condition']

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['device', 'employee', 'checked_out', 'checked_in', 'condition_when_checked_out', 'condition_when_checked_in']


