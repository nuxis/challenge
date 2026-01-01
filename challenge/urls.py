from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib import admin
import django.views
import levels.views
import django.contrib.auth.views
import core.views
import stats.views

admin.autodiscover()


urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^$", core.views.index, name="index"),
    url(r"^done/$", levels.views.done, name="done"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    url(
        r"^logout/$",
        django.contrib.auth.views.logout_then_login,
        name="logout_then_login",
    ),
    url(r"^register/$", core.views.register, name="register"),
    url(r"^score/$", stats.views.ScoreList.as_view(), name="score"),
    url(r"^attempts/$", stats.views.attempts, name="attempts"),
    url(r"^attempts/(?P<getnum>\d*)/$", stats.views.attempts),
    url(r"^levels/$", levels.views.LevelList.as_view(), name="levellist"),
    url(r"^levels/(?P<pk>\d*)/$", levels.views.level, name="level"),
]
