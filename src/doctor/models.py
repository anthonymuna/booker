# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import random
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910202452)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "images_uploaded/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class Doctor(models.Model):
    user  =models.OneToOneField(User)
    full_name = models.CharField(max_length=600)
    profile_pic = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    doctor_type = models.CharField(max_length=250)
    availability = models.CharField(max_length=255)
    id_num = models.IntegerField(blank=False, null=False)
    nationality = models.CharField(max_length=150)
    mobile_number = models.IntegerField()
    hospital = models.CharField(max_length=250)

    def __str__(self):
    	return "{} {}".format(self.first_name, self.middle_name, self.last_name)

APPOINTMENT_CHOICES = (
        ('Medicine Appointment', 'Medicine Appointment'),
        ('Paediatric Appointment', 'Paediatric Appointment'),
        ('Dental Appointment', 'Dental Appointment'),
    )


class AddAppointment(models.Model):
    appointment_service = models.CharField(max_length=250, choices=APPOINTMENT_CHOICES, default=None)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_appointment = models.DateField()
    time_of_appointment = models.TimeField()
