from challenge.settings.base import *  # noqa: F403

# FIXME: Refactor settings structure, using -environ or -decouple or some other solution that is nicer than noqa

DEBUG = False


# These persons will be emailed with exception information when running with DEBUG=False.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#admins
# ADMINS = (
# ('Mr. Your Name', 'email@example.com'),
# )
# MANAGERS = ADMINS

TIME_ZONE = "Europe/Oslo"
LANGUAGE_CODE = "en"

