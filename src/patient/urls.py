app_name = 'patient'

from django.conf.urls import url
from patient.views import index, signup_view, login_view, logout_view, booked, book_appointment, appointment_detail, create_profile, appointment_update, appointment_delete

urlpatterns = [
	url(r'^login/$', login_view, name='login_view'),
	url(r'^signup/$', signup_view, name='signup_view'),
    url(r'^$', index, name='index'),
    url(r'^create_profile/$', create_profile, name='create_profile'),
    url(r'^book_appointment/', book_appointment, name='book_appointment'),
	url(r'^booked/', booked, name='booked'),
	url(r'^(?P<id>\d+)/update/', appointment_update, name='update'),
	url(r'^booked_appointments/(?P<id>\d+)/delete/$', appointment_delete, name='delete'),
	url(r'^booked_appointments/(?P<id>\d+)/', appointment_detail, name='appointment_detail'),
    #url(r'^view_appointments/(?P<user>\w+)/patient_detail/$', patient_detail, name='patient_detail'),
    url(r'^logout/$', logout_view, name='logout_view'),
]
