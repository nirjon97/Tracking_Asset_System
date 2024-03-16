from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import datetime
from .models import Company, Employee, Device,DeviceLog




class CompanyRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ['name', 'email', 'password']


class CompanyLoginForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'password']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'position']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['serial_number', 'device_type', 'condition']

class CheckoutForm(forms.Form):
    condition_when_checked_out = forms.CharField(max_length=100)


class DeviceAssignmentForm(forms.Form):
    employees = Employee.objects.all().values_list('id', 'name')  # Get list of tuples containing employee ID and name
    employee = forms.ChoiceField(choices=employees)
    assigned_date = forms.DateTimeField(initial= datetime.datetime.now)
    condition = forms.CharField(max_length=100)
    




class DeviceReturnForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['checked_in', 'condition_when_checked_in']

class DeviceLogForm(forms.ModelForm):
    
    class Meta:
        model = DeviceLog
        exclude = ['checked_out']
        fields = ['device', 'employee', 'checked_out', 'checked_in', 'condition_when_checked_out', 'condition_when_checked_in']