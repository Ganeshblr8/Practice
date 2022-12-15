from django import forms
from .models import doctordetails
from .models import patientdetails
from .models import newpatient
#from django.forms.widgets import RadioSelect

class Loginfrm(forms.Form):
    doctorname = forms.CharField(label='doctorname', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    #password = forms.CharField(label='password', max_length=100)
    class Meta():
        model = doctordetails
        fields = ('doctorname','password')
    

class Registerfrm(forms.Form):
    doctorname = forms.CharField(label='doctorname', max_length=100)
    doctormobile = forms.CharField(label='doctormobile', max_length=100)
    
    
    password = forms.CharField(label='password', max_length=100)

    class Meta():
        model = doctordetails
        fields = ('doctorname','doctormobile','password')

class Patientfrm(forms.Form):
    patientname = forms.CharField(label='patientname', max_length=100)
    #doctormobile = forms.IntegerField(label='doctormobile')
    patienttreatment = forms.CharField(label='patienttreatment', max_length=100)
    patientdate = forms.DateField()
    #patienttime = forms.DateField(label='patienttime')

    class Meta():
        model = patientdetails
        #fields = ('patientname','patienttreatment','patientdate','patienttime')
        fields = ('patientname','patienttreatment','patientdate')

class Newpatientfrm(forms.Form):
    newpatientname = forms.CharField(label='newpatientname', max_length=100)
    #doctormobile = forms.IntegerField(label='doctormobile')
    patientmobile = forms.CharField(label='patientmobile', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    #patientgender = forms.CharField(max_length=1, choices)

    class Meta():
        model = newpatient
        fields = ('newpatientname','patientmobile','password')