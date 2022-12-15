from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor_validate', views.doctor_validate, name='validate'),
    path('register', views.register, name='register'),
    path('doctor_register', views.doctor_register, name='doctor_register'),
    path('validate_doctor', views.validate_doctor, name='validate_doctor'),
    path('company', views.company, name='company'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('patient_register', views.patient_register, name='patient_register'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('newpatient_reg', views.newpatient_reg, name='newpatient_reg'),
    path('book_appointment', views.book_appointment, name='book_appointment'),
    path('get_my_appointment', views.get_my_appointment, name='get_my_appointment'),
    path('show_patient_booked', views.show_patient_booked, name='show_patient_booked'),
    path('patient_validate', views.patient_validate, name='validate'),
    path('validate_patient', views.validate_patient, name='validate_patient'),
    path('save_doctor_details', views.save_doctor_details, name='save_doctor_details'),
    path('save_patient_details', views.save_patient_details, name='save_patient_details'),
    path('show_patient_details_to_doctor', views.show_patient_details_to_doctor, name='show_patient_details_to_doctor'),
    path('doctor_master_page_get', views.doctor_master_page_get, name='doctor_master_page_get'),
    path('show_doctor_profile_page', views.show_doctor_profile_page, name='show_doctor_profile_page'),
    path('reset_password_doctor', views.reset_password_doctor, name='reset_password_doctor'),
    
    
]