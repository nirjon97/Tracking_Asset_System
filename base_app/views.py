from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CompanyRegistrationForm,DeviceAssignmentForm, DeviceReturnForm, DeviceLogForm, EmployeeForm, DeviceForm, CheckoutForm,CompanyLoginForm
from .models import Company, Employee, Device, DeviceLog
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DeviceLogSerializer



#for api view
@api_view(['GET'])
def device_log_list(request):
    if request.method == 'GET':
        device_logs = DeviceLog.objects.all()
        serializer = DeviceLogSerializer(device_logs, many=True)
        return Response(serializer.data)

def home_page(request):


    context ={

    }

    return render(request, "home.html",context)

def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            company = form.save(commit=False)
            company.user = user
            company.save()
            return redirect('login_company')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company_register.html', {'form': form})

def company_dashboard(request):
    # Assuming you have a logged-in user
    company = request.user.company
    company_name = request.user.username
    employees = Employee.objects.filter(company=company)
    devices = Device.objects.all()  # Or you can filter by company if needed

    return render(request, 'company_dashboard.html', {'company': company,'company_name': company_name, 'employees': employees, 'devices': devices})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = request.user.company
            employee.save()
            return redirect('company_dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard')
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})

def checkout_device(request, device_id):
    device = Device.objects.get(pk=device_id)
    if request.method == 'POST':
        # Assuming you have a form for checking out devices
        # Handle form submission, update DeviceLog, etc.
        return redirect('company_dashboard')
    else:
        form = CheckoutForm()
    return render(request, 'checkout_device.html', {'device': device, 'form': form})


def login_company(request):
    if request.method == 'POST':
        form = CompanyLoginForm(request.POST)
        print("outside of valid ")
        if form.is_valid():
            print("inside of valid")
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to appropriate page after login
                return redirect('company_dashboard')  # Change 'dashboard' to your desired URL name
            else:
                # Invalid login
                form.add_error(None, "Invalid username or password")
    else:
        form = CompanyLoginForm()
    return render(request, 'login.html', {'form': form})


def assign_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)

    if request.method == 'POST':
        form = DeviceAssignmentForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee']
            assigned_date = form.cleaned_data['assigned_date']
            condition = form.cleaned_data['condition']
            employee = get_object_or_404(Employee, pk=employee_id)
            # Exclude 'checked_out' field from the form
            DeviceLog.objects.create(device=device, employee=employee, condition_when_checked_out=condition)
            return redirect('company_dashboard')
    else:
        form = DeviceAssignmentForm()
    return render(request, 'assign_device.html', {'form': form, 'device': device})

def return_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
       # device_id = request.POST.get('device')
        new_employee_id = request.POST.get('new_employee')
        
        # Get the device and employee objects
        #device = get_object_or_404(Device, pk=device_id)
        new_employee = get_object_or_404(Employee, pk=new_employee_id)
        
        # Create a new entry in DeviceLog
        DeviceLog.objects.create(
            device=device,
            employee=new_employee,
            checked_in=datetime.datetime.now(),  # Assuming you're importing datetime
            condition_when_checked_in='Good'  # Assuming you have a default value
        )
        return redirect('company_dashboard')
    else:
        form = DeviceReturnForm()
    return render(request, 'return_device.html', {'form': form})

def device_log(request):
    logs = DeviceLog.objects.all()
    return render(request, 'device_log.html', {'logs': logs})


def select_device(request):
    devices = Device.objects.all()
    return render(request, 'select_device.html', {'devices': devices})




def select_device_for_return(request):
    devices = Device.objects.all()
    
    context={
        'devices':devices,

    }

    return render(request, 'select_device_for_return.html',context)




def select_employee(request):
    device_id = request.POST.get('device')
    device = get_object_or_404(Device, pk=device_id)
    latest_log = device.devicelog_set.order_by('-checked_out').first()
    current_employee = latest_log.employee if latest_log else None
    employees = Employee.objects.all()
    return render(request, 'select_employee_for_return.html', {'device': device, 'current_employee': current_employee, 'employees': employees})


