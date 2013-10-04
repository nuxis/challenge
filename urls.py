from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),

	(r'^$', 'challenge.levels.views.index'),
	(r'^done/$', 'challenge.levels.views.done'),
	
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
	(r'^register/$', 'challenge.core.views.register'),
	(r'^score/$', 'challenge.stats.views.score'),
)
