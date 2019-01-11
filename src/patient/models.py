# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
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

INSURANCE_CHOICES = (
			('Null', 'NULL'),
			('Y', 'YES'),
			('N', 'NO'),
		)

class Patient(models.Model):
	user = models.OneToOneField(User)
	slug = models.SlugField(unique=True)
	full_name = models.CharField(max_length=500, blank=False)
	thumb = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	nationality = models.CharField(max_length=155, blank=False)
	id_number = models.IntegerField(null=False, blank=False)
	home = models.CharField(max_length=155)
	mobile_number = models.IntegerField(blank=False)
	insurance = models.CharField(max_length=5, choices=INSURANCE_CHOICES, default="Null")
	allergies = models.CharField(max_length=500)

	def __str__(self):
		return "{}".format(self.full_name)

# 	def get_absolute_url(self):
# 		return reverse('patient:patient_detail', kwargs={'slug': self.id})

# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.full_name)
# 	if new_slug is not None:
# 		slug = new_slug
# 	qs = Appointment.objects.filter(slug=slug).order_by("-id")
# 	exists = qs.exists()
# 	if exists:
# 		new_slug = "%s-%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug

# def pre_save_appointment_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)

# pre_save.connect(pre_save_appointment_receiver, sender=Patient)

SERVICE_CHOICES = (
		('Medicine Appointment', 'Medicine Appointment'),
		('Paediatric Appointment', 'Paediatric Appointment'),
		('Dental Appointment', 'Dental Appointment'),
	)

HOSPITAL_CHOICES = (
		('Kijabe Hospital', 'Kijabe Hospital'),
		('Kenyatta National Hospital', 'Kenyatta National Hospital'),
		('Kikuyu PCEA Hospital', 'Kikuyu PCEA Hospital'),
		('Agakhan Hospital', 'Agakhan Hospital'),
		('Lionsight Hospital', 'Lionsight Hospital'),
	)

class Appointment(models.Model):
	patient = models.ForeignKey(User, on_delete=models.CASCADE)
	appointment_service = models.CharField(max_length=250, choices=SERVICE_CHOICES, default=None)
	appointment_description = models.CharField(max_length=250)
	appointment_date = models.DateField()
	appointment_time = models.TimeField()
	hospital = models.CharField(max_length=600, choices=HOSPITAL_CHOICES, default=None)

	def __str__(self):
		return "{}".format(self.appointment_service)