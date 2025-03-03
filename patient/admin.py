from django.contrib import admin

from patient.models import Patient, Diagnosis, Doctor

# Register your models here.
admin.site.register(Patient)
admin.site.register(Diagnosis)
admin.site.register(Doctor)
