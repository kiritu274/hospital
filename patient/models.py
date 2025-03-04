from django.db import models

# Create your models here.
class Patient(models.Model):
    image = models.ImageField(upload_to='patient_images/',blank='True')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

class Diagnosis(models.Model):
    patient = models.CharField(max_length=20)
    doctor = models.CharField(max_length=30)
    diagnosis = models.TextField(max_length=200)
    date_diagnosed = models.DateField()

    def __str__(self):
        return self.patient

class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)




