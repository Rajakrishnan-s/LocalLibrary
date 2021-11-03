from local import *
import dj_database_url

#implementing whitenoise middleware to facilitate serving static files
MIDDLEWARE.insert(1,"whitenoise.middleware.WhiteNoiseMiddleware")

DATABASES['default'] = dj_database_url.config(conn_max_age = 500)

STATIC_URL = get_secret('STATIC_URL') or '/static/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'