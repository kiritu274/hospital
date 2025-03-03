from django.shortcuts import render, redirect

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

