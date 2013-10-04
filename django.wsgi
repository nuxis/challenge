import os
import sys

sys.path.append ('/var/www/pp22pc/')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/pp22pc/challenge/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'challenge.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler ()
