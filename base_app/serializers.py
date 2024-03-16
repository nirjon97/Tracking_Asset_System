from rest_framework import serializers
from .models import DeviceLog

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checked_out', 'checked_in', 'condition_when_checked_out', 'condition_when_checked_in']