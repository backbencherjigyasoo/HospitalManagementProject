from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    special = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.IntegerField()
        
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    cr_date = models.DateField()
    cr_time = models.TimeField()
        
    
    def __str__(self):
        return self.doctor.name+"--"+self.patient.name
    
    
