from django.contrib import admin

from patient.models import Patient, Appointment

class PatientAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'id_number', 'mobile_number', 'home', 'nationality']
	list_filter = ['full_name']
	search_fields = ['full_name', 'home', 'id_number']
	class Meta:
		model = Patient


admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment)