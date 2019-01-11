app_name = 'doctor'

from django.conf.urls import url
from doctor.views import login_view, signup_view, index, create_profile, add_appointment, view_appointment, appointment_detail, logout_view

urlpatterns = [
	url(r'^login/$', login_view, name='login_view'),
	url(r'^signup/$', signup_view, name='signup_view'),
    url(r'^$', index, name='index'),
    url(r'^create_profile/$', create_profile, name='create_profile'),
    # url(r'^add_appoitnment/$', add_appointment, name='add_appointment'),
    url(r'^view_appointment/', view_appointment, name='view_appointment'),
    url(r'^view_appointment/(?P<pk>\d+)/$',appointment_detail, name='appointment_detail'),
    # url(r'^view_appointment/(?P<pk>\d+)/update/$', update_appointment, name='update_appointment'),
    # url(r'^view_appointment/(?P<pk>\d+)/delete/$', delete_appointment, name='delete_appointment'),
    url(r'^logout/$', logout_view, name='logout_view'),
]
