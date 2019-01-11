from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from patient.patient_info import PatientForm, AppointmentForm
from patient.models import Patient, Appointment

def index(request):
	return render(request, 'patient/index.html')

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_patient = True
			user = form.save()
			login(request, user)
			messages.success(request, 'Your account has been succesfully created. Please proceed to logging in')
			return redirect('patient:login_view')
	else:
		form = UserCreationForm()
	return render(request, 'patient/signup.html', {'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('patient:index')
	else:
		form = AuthenticationForm()
	return render(request, 'patient/login.html', {'form':form})

def create_profile(request):
	if request.method == 'POST':
		form = PatientForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance = form.save()
			return redirect('patient:book_appointment')
	else:
		form = PatientForm()
	return render(request, 'patient/create_profile.html', {'form':form})

def book_appointment(request):
	if request.method == 'POST':
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance = form.save()
			return redirect('patient:view_appointments')
	else:
		form = AppointmentForm()
	return render(request, 'patient/book_appointment.html', {'form':form})

def view_appointments(request):
	queryset = Appointment.objects.all()
	return render(request, 'patient/view_appointment.html', {'query': queryset})

def appointment_detail(request, id=None):
	instance = get_object_or_404(Appointment, id=id)
	return render(request, 'patient/detail.html', {'title': 'Appointment Detail', 'instance':instance})

# def patient_detail(request, id=None):
# 	instance = get_object_or_404(Patient, id=id)
# 	return render(request, 'patient/patient_detail.html', {'title':'Patient Information', 'instance':instance})
	
def appointment_update(request, id=None):
	instance = get_object_or_404(Appointment, id=id)
	form = AppointmentForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance = form.save()
		return redirect('patient:view_appointments')
	return render(request, 'patient/appointment_update.html',{'title': instance.appointment_service, 'instance':instance, 'form':form})

def appointment_delete(request, id=None):
	instance = get_object_or_404(Appointment, id=id)
	instance.delete()
	messages.warning(request, "Successfully deleted the appointment")
	return redirect('patient:view_appointments')

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('patient:login_view')
	else:
		logout(request)
		messages.success(request, "You have been logged out. Please log back in")
		return redirect('patient:login_view')
