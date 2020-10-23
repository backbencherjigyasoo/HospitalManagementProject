from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment

def dashboard(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1

    return render(request, 'hospital/dashboard.html')


def about(request):
    return render(request, 'hospital/about.html')


def contact(request):
    return render(request, 'hospital/contact.html')

def view_doctor(request):
    doctor = Doctor.objects.all().order_by('name')
    return render(request, 'hospital/view_doctor.html', {'doctor':doctor})

def add_doctor(request):
    error=""
    if request.method == 'POST':
        n = request.POST.get('dname')
        c = request.POST.get('contact')
        sp = request.POST.get('special')
        try:
            Doctor.objects.create(name=n, mobile=c, special=sp)
            error='no'
        except:
            error='yes'

    return render(request, 'hospital/add_doctor.html', {'error':error})

def delete_doctor(request, pid):
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    return redirect('view_doctor')

def view_patient(request):
    patient = Patient.objects.all().order_by('name')
    return render(request, 'hospital/view_patient.html', {'patient': patient})

def add_patient(request):
    error=""
    if request.method == 'POST':
        n = request.POST.get('pname')
        c = request.POST.get('contact')
        addr = request.POST.get('address')
        g = request.POST.get('gender')
        try:
            Patient.objects.create(name=n, mobile=c, address=addr, gender=g,)
            error='no'
        except:
            error='yes'

    return render(request, 'hospital/add_patient.html', {'error':error})


def delete_patient(request, pid):
    patient = Patient.objects.get(id = pid)
    patient.delete()
    return redirect('view_patient')

def view_appointment(request):
    appointment = Appointment.objects.all()
    return render(request, 'hospital/view_appointment.html', {'appointment': appointment})

def add_appointment(request):
    error=""
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST.get('dname')
        p = request.POST.get('pname')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, cr_date=date, cr_time=time,)
            error='no'
        except:
            error='yes'

    return render(request, 'hospital/add_appointment.html', {'doctor':doctor1, 'patient':patient1, 'error':error})


def delete_appointment(request, pid):
    appointment = Appointment.objects.get(id = pid)
    appointment.delete()
    return redirect('view_appointment')