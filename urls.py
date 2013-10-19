from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
	url (r'^admin/', include(admin.site.urls)),
	url (r'^$', 'challenge.levels.views.index'),
	url (r'^done/$', 'challenge.levels.views.done'),
	
	url (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	url (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
	url (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
	url (r'^register/$', 'challenge.core.views.register'),
	url (r'^score/$', 'challenge.stats.views.score'),
	url (r'^attempts/$', 'challenge.stats.views.attempts'),
)
