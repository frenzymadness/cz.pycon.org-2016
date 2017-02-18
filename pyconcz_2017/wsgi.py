import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "pyconcz_2017.settings")

'''
if os.environ.get('NEW_RELIC_ENVIRONMENT') == 'production':
    import newrelic.agent
    newrelic.agent.initialize()
'''

application = get_wsgi_application()
