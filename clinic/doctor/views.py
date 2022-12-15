from http.client import HTTPResponse
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#import mysql.connector as sql
#from . models import doctordetails
from .models import doctordetails
from .models import patientdetails
from .models import newpatient
from django.contrib.auth.decorators import login_required
#from .models import UserLogin
from .forms import Loginfrm
from .forms import Registerfrm
from django.core.exceptions import BadRequest
from django import forms
from django.views.generic import dates
import datetime


# Create your views here.
def home(request):
    return render(request, 'static/login.html')
def doctor_validate(request):
    return render(request, 'static/doctor_validate.html')
def patient_validate(request):
    return render(request, 'static/patient_validate.html')
def register(request):     
    return render(request, 'static/register.html')
def validate_doctor(request):
    if request.method=='POST':
        doctorname = request.POST.get('doctorname')
        doctormobile = request.POST.get('doctormobile')
        password = request.POST.get('password')
        #print("****")
        #print(doctorname)
        #print(password)
        userdata=doctordetails.objects.filter(doctorname=doctorname,doctormobile=doctormobile,password=password).values()
        patient_names_drop_down = patientdetails.objects.all()
        #print("****")
        for a in patient_names_drop_down:
            print (a.patientname)
        if not userdata:
            return HttpResponse("Not valid")
        else:
            context={"doctorname":doctorname,"patientname":patient_names_drop_down,"patientdetails":a}
            return render(request, 'static/doctor_home_page.html', context)
        
def show_patient_details_to_doctor(request):
    #print ("Testting")
    #print (patientname)
    if request.method=='POST':
        selectedpatientname = request.POST.get("selectpn")
        patient_details = patientdetails.objects.all()
        #selectedpatientmobile = patient_details.get()
        patient_treatment = ""
        for a in patient_details:
            if (a.patientname == selectedpatientname):
                print (a.patienttreatment)
                patient_treatment = a.patienttreatment
                #return (a.patienttreatment)
        #patientmobile = request.POST["patientmobile"]
        #patientgender = request.POST["patientgender"]
        #print("HHHHH")
        #print(selectedpatientname)
        context={"doctorname":"doctorname","selectedpatientname":selectedpatientname,"selectedpatientmobile":patient_treatment}
        return render(request, 'static/show_patient_details_to_doctor.html', context)

    #patient_list = patientdetails.objects.all()
    #for a in patient_list:
    #    if (a.patientname == patientname):
    #        print ("Patient already exist")
    #    else:
    #        patient_details = newpatient(newpatientname=newpatientname,patientmobile=patientmobile)
    #        patient_details.save()
    #        return HttpResponse("New Patient addedd successfuly!!")
    #return render(request, 'static/patient_choosed_display.html', context)
def validate_patient(request):
    #print ("hhhhhhhhhhhhhhhhhh")
    if request.method=='POST':
        newpatientname = request.POST.get('newpatientname')
        patientmobile = request.POST.get('patientmobile')
        password = request.POST.get('password')

        #print(password)
        #userdata=doctordetails.objects.filter(doctorname=doctorname,doctormobile=doctormobile,password=password).values()
        userdata=patientdetails.objects.filter(newpatientname=newpatientname,patientmobile=patientmobile,password=password).values()
        print("****")
        print(userdata)
        if not userdata:
            return HttpResponse("Not valid")
        else:
            print("****")
            print(newpatientname)
            context={"newpatientname":newpatientname}
            return render(request, 'static/patient_home_page.html', context)
def company(request):
    return render(request, 'static/company.html')
def services(request):
    return render(request, 'static/services.html')
def contact(request):
    return render(request, 'static/contact.html')
def add_patient(request):
    return render(request, 'static/addpatient.html')
def book_appointment(request):
    return render(request, 'static/book_appointment.html')
def get_my_appointment(request):
    return render(request, 'static/appointment_date_range.html')
    patient_appointment = patientdetails.objects.all()
    #print (patient_appointment)
    for a in patient_appointment:
        if (a.patientname == "Ganesh"):
            print ("Matching")
    #XX=patientdetails.patienttreatment
    #for a in patient_appointment:
        #context={"patientname":a.patientname}
    #for a in patient_appointment:
        #context1={"patienttreatment":a.patienttreatment}
        #return render(request, 'static/get_my_appointment.html', context)
    #print ("NOT matched")
    return render(request, 'static/get_my_appointment.html', {'patient_appointment': patient_appointment}) 

def show_patient_booked(request):
    fromdate = request.POST["from"]
    todate = request.POST["to"]
    #print (fromdate)
    #print ("break")
    #print (todate)
    #patient_appointment = patientdetails.objects.all()
    #patient_appointment = patientdetails.objects.filter(patientdate=["'"+str(fromdate)+"'","'"+str(todate)+"'"])
    #if not fromdate and todate:
    #    print ("Inside")
    #    patient_appointment = patientdetails.objects.all()
    #else:
     #   print ("Inside else")
    patient_appointment = patientdetails.objects.filter(patientdate__gte=fromdate,patientdate__lte=todate)
    #print (patient_appointment)
    #for a in patient_appointment:
     #   print (fromdate, a.patientdate)
      #  if re.match(r"fromdate", 'a.patientdate'):
       #     print ("Appoint date matched")
        #else:
         #   print ("No appointment")
    #XX=patientdetails.patienttreatment
    #for a in patient_appointment:
        #context={"patientname":a.patientname}
    #for a in patient_appointment:
        #context1={"patienttreatment":a.patienttreatment}
        #return render(request, 'static/get_my_appointment.html', context)
    #print ("NOT matched")
    return render(request, 'static/get_my_appointment.html', {'patient_appointment': patient_appointment})        
    #return render(request, 'static/get_my_appointment.html', locals)        
  
def save_doctor_details(request):
    #if request.method=='POST':
        #newpatientname = request.POST.get('newpatientname')
    if request.method=="POST":
        doctorname = request.POST.get('doctorname')
        doctormobile = request.POST.get('doctormobile')
        password = request.POST.get('password')
        #print ("here")
        #print (password)
        doctor_details = doctordetails(doctorname=doctorname,doctormobile=doctormobile,password=password)
        if not doctor_details:
            return HttpResponse("Enter all fields")
        else:            
            doctor_details.save()
            return HttpResponse("New Dotor details are registered successfully")
    else:
        return HttpResponse("Enter proper Doctor details")
def reset_password_doctor(request):
    
    #if request.method=='POST':
    #    doctorname = request.POST.get('doctorname')
    #    doctormobile = request.POST.get('doctormobile')
    #    password = request.POST.get('password')
    if request.method=='POST':
        #print ("XXXX")
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        doctor_list = doctordetails.objects.all()
        for i in doctor_list:
            if i.doctorname == 'Sangeetha' and i.password == oldpassword:
                i.password = newpassword
                #doctor_list = doctordetails(doctorname=doctorname,doctormobile=doctormobile,password=password)
                
                doctor_list = doctordetails(doctorname='Sangeetha',password=newpassword)
                #doctordetails.save(self=doctordetails)
                doctor_list.save()

        
        #print (doctorname)
        return HttpResponse("New Dotor details are registered successfully")
    else:
        return HttpResponse("Enter proper Doctor details")

def doctor_master_page_get(request):
    #print (doctorname)
    return render(request, 'static/doctor_master_page_display.html')

def show_doctor_profile_page(request):
    return render(request, 'static/show_doctor_profile_page.html')

def save_patient_details(request):
    if request.method=="POST":
        newpatientname = request.POST["newpatientname"]
        patientmobile = request.POST["patientmobile"]
        password = request.POST["password"]
        print ("here")
        print (patientmobile)
        patient_details = newpatient(newpatientname=newpatientname,patientmobile=patientmobile,password=password)
        patient_details.save()
        return HttpResponse("New Patient details are registered successfully")
    else:
        return HttpResponse("Enter proper Patient details")


def doctor_register(request):
    return render(request, 'static/doctor_register_first_time.html')
    if request.method=="POST": 
        #rfrm = Registerfrm(request.POST)        
        #print (rfrm.doctorname)       
        #name = doctordetails.objects.filter(position = request.POST.get("name"))
        #id1 = request.POST["id"]
        doctorname = request.POST["doctorname"]
        doctormobile = request.POST["doctormobile"]
        #email = ordrequest.POST["email"]
        password = request.POST["password"]
        #print (name)
        #print (password)
        doctor_details = doctordetails(doctorname=doctorname,password=password)
        doctor_details.save()
        #print("I am inside POST")
        #print (doctor_details.name)
        #print (password)
        if not doctorname and doctormobile and password:
            return HttpResponse("Enter required details")
        else:
            return render(request, 'static/doctor_validate.html')
def patient_register(request):
    #return render(request, 'static/patient_register_first_time.html')
    if request.method=="POST": 
        patientname = request.POST["patientname"]
        patienttreatment = request.POST["patienttreatment"]
        patientdate = request.POST["patientdate"]
        patienttime = request.POST["patienttime"]
        #print ("ha")
        #print (patientdate)
        patient_details = patientdetails(patientname=patientname,patienttreatment=patienttreatment,patientdate=patientdate)
        #patient_details = patientdetails(patientname=patientname,patienttreatment=patienttreatment,patientdate=patientdate,patienttime=patienttime)
        patient_details.save()
        return render(request, 'static/patient_details.html')
        #return HttpResponseRedirect(reverse('app_name:view_name', kwargs={'pk': saving_variable.pk}))
    else:
        return render(request, 'static/patient_details.html')


def newpatient_reg(request):
    if request.method=='POST':
        newpatientname = request.POST["newpatientname"]
        patientmobile = request.POST["patientmobile"]
        #patientgender = request.POST["patientgender"]
        #print("HHHHH")
        #print(patientmobile)
        patient_list = patientdetails.objects.all()
        for a in patient_list:
            if (a.patientname == newpatientname):
                print ("Patient already exist")
            else:
                print("HHHHH")
                print(patientmobile)
                patient_details = newpatient(newpatientname=newpatientname,patientmobile=patientmobile)
                patient_details.save()
                return HttpResponse("New Patient addedd successfuly!!")


            #if not patientmobile:
            #raise forms.ValidationError("Missng mobile number")
            #return render(request, 'static/addpatient.html') 
        



#def register(request):
#    if request.method=='POST':
#        name=request.POST['name']
        
