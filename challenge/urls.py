from django.conf.urls import url, include

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

import django.views
import levels.views
import django.contrib.auth.views
import core.views
import stats.views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', levels.views.index, name='index'),
    url(r'^done/$', levels.views.done, name='done'),

    url(r'^media/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^login/$', django.contrib.auth.views.login,
        {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/$', django.contrib.auth.views.logout_then_login,
        name="logout_then_login"),
    url(r'^register/$', core.views.register, name="register"),
    url(r'^score/$', stats.views.score, name='score'),
    url(r'^attempts/$', stats.views.attempts, name='attempts'),
    url(r'^attempts/(?P<getnum>\d*)/$', stats.views.attempts),
]
