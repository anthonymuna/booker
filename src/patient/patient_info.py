from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from patient.models import Patient, Appointment

class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
			'full_name',
			'thumb',
			'id_number',
            'home',
			'nationality',
			'mobile_number',
			'insurance',
			'allergies',
		]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [ 
        	'appointment_service',
        	'patient',
            'hospital',
        	'appointment_description', 
        	'appointment_date', 
        	'appointment_time',
        ]
        widgets = {
            'appointment_date': DatePickerInput(),
            'appointment_time': TimePickerInput(),
        }