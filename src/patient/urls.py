app_name = 'patient'

from django.conf.urls import url
from patient.views import index, signup_view, login_view, logout_view, book_appointment, view_appointments, appointment_detail, create_profile, appointment_update, appointment_delete

urlpatterns = [
	url(r'^login/$', login_view, name='login_view'),
	url(r'^signup/$', signup_view, name='signup_view'),
    url(r'^$', index, name='index'),
    url(r'^create_profile/$', create_profile, name='create_profile'),
    url(r'^book_appointment/', book_appointment, name='book_appointment'),
    url(r'^view_appointments/$', view_appointments, name='view_appointments'),
    url(r'^view_appointments/(?P<id>\d+)/$', appointment_detail, name='appointment_detail'),
    # url(r'^view_appointments/(?P<id>\d+)/patient_detail/$', patient_detail, name='patient_detail'),
    url(r'^view_appointments/update/(?P<id>\d+)/$', appointment_update, name='appointment_update'),
    url(r'^view_appointments/delete/(?P<id>\d+)/$', appointment_delete, name='delete'),
    url(r'^logout/$', logout_view, name='logout_view'),
]
