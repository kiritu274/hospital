from logging import exception

from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view

import patient
from patient.forms import PatientForm, DiagnosisForm, DoctorForm
from patient.models import Patient, Diagnosis, Doctor
from patient.serializers import PatientSerializer, DiagnosisSerializer, DoctorSerializer


# Create your views here.
def index(request):
    if request.method == "POST":
        form = PatientForm(request.POST,request.FILES)
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
        form = PatientForm(request.POST,request.FILES,instance= patient)
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



@api_view(['GET','POST'])
def patientapi(request):
    if request.method == "GET":
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def diagnosisapi(request):
    if request.method == "GET":
        diagnosis = Diagnosis.objects.all()
        serializer = DiagnosisSerializer(diagnosis, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def doctorapi(request):
    if request.method == "GET":
        doctor = Doctor.objects.all()
        serializer = DoctorSerializer(doctor, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0115640806'
    amount = 1
    account_reference = 'emobilis'
    transaction_desc = 'School fees payments'
    callback_url = 'https://darajambili.heroku.com/express-payment';
    response = client.stk_push(phone_number,amount,
                               account_reference,
                               transaction_desc,callback_url)
    return HttpResponse(response)
