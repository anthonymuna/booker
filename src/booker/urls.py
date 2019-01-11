from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from booker.views import home, about, contact, clear

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^clear/$', clear, name='clear'),
    url(r'^patient/', include('patient.urls', namespace='patient')),
    url(r'^doctor/', include('doctor.urls', namespace='doctor')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
