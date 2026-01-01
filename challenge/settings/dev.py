from challenge.settings.base import *  # noqa: F403

# FIXME: Refactor settings structure, using -environ or -decouple or some other solution that is nicer than noqa

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = "t+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)"

MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INSTALLED_APPS += ("debug_toolbar",)  # noqa: F405
