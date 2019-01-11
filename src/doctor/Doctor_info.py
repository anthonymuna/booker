from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from doctor.models import Doctor, AddAppointment
# from accounts.models import MyUser
# from django.contrib.auth import get_user_model

class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = [
			'full_name',
			'profile_pic',
			'id_num',
			'hospital',
			'mobile_number',
			'nationality',
			'doctor_type',
		]
	
class AddAppointmentForm(forms.ModelForm):
	class Meta:
		model = AddAppointment
		fields = [
			'appointment_service',
			'doctor',
			'date_of_appointment',
			'time_of_appointment',
		]
		widgets = {
			'date_of_appointment': DatePickerInput(),
			'time_of_appointment': TimePickerInput(),
		}