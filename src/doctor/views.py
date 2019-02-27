from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from doctor.Doctor_info import DoctorForm, AddAppointmentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from patient.models import Appointment

def index(request):
    return render(request, 'doctor/index.html', {})

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_doctor = True
			user = form.save()
			login(request, user)
			messages.success(request, 'Please login with your registered credentials')
			return redirect('doctor:login_view')
	else:
		form = UserCreationForm()
	return render(request, 'doctor/signup.html', {'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			user.is_doctor = True
			login(request, user)
			return redirect('doctor:index')
	else:
		form = AuthenticationForm()
	return render(request, 'doctor/login.html', {'form':form})

def create_profile(request):
	form = DoctorForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('doctor:add_appointment')
	else:
		form = DoctorForm()
	return render(request, 'doctor/create_profile.html', {'form':form})

def add_appointment(request):
	form = AddAppointmentForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('doctor:view_appointment')
	else:
		form = AddAppointmentForm()
	return render(request, 'doctor/add_appointment.html', {'form':form})

# def list_appointments(request):
# 	queryset
# 	return render(request, 'doctor/list_appointments.html', {})

def view_appointment(request):
    queryset = Appointment.objects.all()
    return render(request, 'doctor/view_appointment.html', {'query': queryset})

def appointment_detail(request, id=None):
	instance = get_object_or_404(Appointment, id=id)
	return render(request, 'is_doctor/detail.html', {'title': 'Appointment Detail', 'instance':instance})

# def update_appointment(request):
# 	return render(request, 'doctor/update_appointment.html', {})

# def delete_appointment(request):
# 	return render(request, 'doctor/delete_appointment.html', {})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('doctor:login_view')
	else:
		logout(request)
		messages.success(request, "You have been logged out. Please log back in")
		return redirect('doctor:login_view')
