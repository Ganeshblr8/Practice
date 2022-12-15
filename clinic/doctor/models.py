from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from phonenumber_field.modelfields import PhoneNumberField

#from .forms import Loginfrm
#from .forms import Registerfrm


class doctordetails(models.Model):
    id = models.IntegerField
    doctorname = models.CharField(max_length=100)
    doctormobile = models.CharField(max_length=100, null=True)
    #doctormobile = PhoneNumberField(null=True, blank=False)
    password = models.CharField(max_length=100)
    #mobile = models.IntegerField
    #email = models.CharField(max_length=100)
    
def __str__(self):
    return self.doctor_register

class patientdetails(models.Model):
    patientid = models.IntegerField
    patientname = models.CharField(max_length=100)    
    patienttreatment = models.CharField(max_length=100)
    patientdate = models.DateTimeField(default=timezone.now)
    #patienttime = models.DateTimeField
    #mobile = models.IntegerField
    #email = models.CharField(max_length=100)
    
def __str__(self):
    return self.patientdetails

class newpatient(models.Model):
    patientid = models.IntegerField
    newpatientname = models.CharField(max_length=100)
    patientmobile = models.CharField(max_length=100, null=True)
    #patientmobile = PhoneNumberField(null=True, blank=False)
    #patientmobile = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=100, default="NA")
    
    #patientgender = models.Choices(widget=forms.RadioSelect())
    
def __str__(self):
    return self.newpatient


# Create your models here.
