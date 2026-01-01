from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from django.contrib import admin
import django.views
import levels.views
import django.contrib.auth.views
import core.views
import stats.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core.views.index, name="index"),
    path("done/", levels.views.done, name="done"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path(
        "logout/",
        django.contrib.auth.views.LogoutView.as_view(next_page="login"),
        name="logout_then_login",
    ),
    path("register/", core.views.register, name="register"),
    path("score/", stats.views.ScoreList.as_view(), name="score"),
    path("attempts/", stats.views.attempts, name="attempts"),
    re_path(r"^attempts/(?P<getnum>\d*)/$", stats.views.attempts),
    path("levels/", levels.views.LevelList.as_view(), name="levellist"),
    re_path(r"^levels/(?P<pk>\d*)/$", levels.views.level, name="level"),
]
