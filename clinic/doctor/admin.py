from django.contrib import admin
from .models import doctordetails
from .models import patientdetails
from .models import newpatient
#from .models import clinicdb

# Register your models here.
admin.site.register(doctordetails)
admin.site.register(patientdetails)
admin.site.register(newpatient)
