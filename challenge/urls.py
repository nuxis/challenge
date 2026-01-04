from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.conf import settings
import levels.views
import django.contrib.auth.views
import core.views
import stats.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core.views.index, name="index"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path(
        "logout/",
        django.contrib.auth.views.LogoutView.as_view(next_page="login"),
        name="logout_then_login",
    ),
    path("register/", core.views.register, name="register"),
    path("score/", stats.views.ScoreList.as_view(), name="score"),
    path("attempts/", stats.views.attempts, name="attempts"),
    path("attempts/<int:getnum>/", stats.views.attempts, name="attempts_with_limit"),
    path("levels/", levels.views.LevelList.as_view(), name="levellist"),
    path("levels/<int:pk>/", levels.views.level, name="level"),
]


if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
