from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^events/$', 'home.views.events', name='events'),
    url(r'^gallery/$', 'home.views.gallery', name='gallery'),
    url(r'^course/$', 'home.views.course', name='course'),
    url(r'^student/$', 'home.views.student', name='student'),
    url(r'^teacher/$', 'home.views.teacher', name='teacher'),
    url(r'^contact/$', 'home.views.contact', name='contact'),
    url(r'^/admin/', include(admin.site.urls)),
]
