from django.contrib import admin
from doctor.models import Doctor, AddAppointment
# Register your models here.
class DoctorModelAdmin(admin.ModelAdmin):
	list_display = ['user', 'full_name', 'id_num', 'mobile_number', 'doctor_type', 'hospital', 'nationality']
	list_filter = ['full_name']
	search_fields = ['full_name', 'hospital', 'id_num']
	class Meta:
		model = Doctor
		

admin.site.register(Doctor)
admin.site.register(AddAppointment)
