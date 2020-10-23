from django.urls import include, path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Doctor Records
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('delete_doctor/<int:pid>/', views.delete_doctor, name='delete_doctor'),

    # Patient Records
    path('view_patient/', views.view_patient, name='view_patient'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('delete_patient/<int:pid>/', views.delete_patient, name='delete_patient'),

    # Appointment
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('delete_appointment/<int:pid>/', views.delete_appointment, name='delete_appointment'),

    path('', RedirectView.as_view(url='dashboard/')),
]