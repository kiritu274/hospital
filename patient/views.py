from logging import exception

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

import patient
from patient.forms import PatientForm, DiagnosisForm, DoctorForm
from patient.models import Patient, Diagnosis


# Create your views here.
def index(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PatientForm()
    return render(request, 'index.html', {'form': form})

def diagnosis(request):
    if request.method == "POST":
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnosis')
    else:
        form = DiagnosisForm()
    return render(request, 'diagnosis.html', {'form': form})

def doctors(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctors.html', {'form': form})

def patientlist(request):
    patients = Patient.objects.all()
    return render(request, 'patientlist.html',{'patients':patients})

def diagnosislist(request):
    diagnosis = Diagnosis.objects.all()
    return render(request, 'diagnosislist.html',{'diagnosis':diagnosis})



def updatepatient(request,id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        form = PatientForm(request.POST,instance= patient)
        if form.is_valid():
            form.save()
            return redirect('patientlist')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'updatepatient.html',{'form':form,'patient':patient},)



def deletepatient(request,id):
    patient = get_object_or_404(Patient, id=id)

    try:
        patient.delete()
    except exception as e:
        messages.error(request, 'patient not deleted')
    return redirect('patientlist')

def updatediagnosis(request,id):
    diagnosis = get_object_or_404(Diagnosis, id=id)
    if request.method == "POST":
        form = DiagnosisForm(request.POST,instance=diagnosis)
        if form.is_valid():
            form.save()
            return redirect('diagnosislist')
    else:
            form = DiagnosisForm(instance=diagnosis)
    return render(request, 'updatediagnosis.html',{'form':form,'diagnosis':diagnosis},)

def deletediagnosis(request,id):
    diagnosis = get_object_or_404(Diagnosis, id=id)

    try:
        diagnosis.delete()
    except exception as e:
        messages.error(request, 'diagnosis not deleted')
    return redirect('diagnosislist')
