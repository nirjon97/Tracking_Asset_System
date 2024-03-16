from .views import home_page,device_log_list,select_device_for_return,select_employee,assign_device,select_device,return_device,device_log, checkout_device, company_dashboard ,register_company, add_device,add_employee,checkout_device,login_company
from django.urls import path

urlpatterns = [
    path("",home_page,name='home_page'),
    path('login/', login_company, name='login_company'),
    path('register/', register_company, name='register_company'),
    path('dashboard/', company_dashboard, name='company_dashboard'),
    path('add-employee/', add_employee, name='add_employee'),
    path('add-device/', add_device, name='add_device'),
    path('checkout-device/<int:device_id>/', checkout_device, name='checkout_device'),
    path('assign/<int:device_id>/', assign_device, name='assign_device'),
    path('return/<int:device_id>/', return_device, name='return_device'),
    path('log/', device_log, name='device_log'),
    path('select-device/', select_device, name='select_device'),
    path('select-device_for_return/', select_device_for_return, name='select_device_for_return'),
    path('select-employee/', select_employee, name='select_employee'),

    #for api view
    path('device-logs/', device_log_list, name='device_logs')
   
]