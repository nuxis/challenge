import sys
from challenge.settings.base import *  # noqa: F403

# FIXME: Refactor settings structure, using -environ or -decouple or some other solution that is nicer than noqa

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = "t+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)"

INSTALLED_APPS += (  # noqa: F405
    "django_extensions",
)

WHITENOISE_AUTOREFRESH = True


def show_debug_toolbar(request):
    """Show debug toolbar for all requests in development"""
    return DEBUG


if "test" not in sys.argv:
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": "challenge.settings.dev.show_debug_toolbar",
    }
    INSTALLED_APPS += (  # noqa: F405
        "debug_toolbar",
    )
    MIDDLEWARE += [  # noqa: F405
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
