from rest_framework import serializers

from patient.models import Patient, Diagnosis, Doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name','email','age','gender']


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['patient','doctor','diagnosis','date_diagnosed']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name','email','age','gender']