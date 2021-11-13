from .local import *
import dj_database_url

#implementing whitenoise middleware to facilitate serving static files
MIDDLEWARE.insert(1,"whitenoise.middleware.WhiteNoiseMiddleware")

DATABASES['default'] = dj_database_url.config(conn_max_age = 500)



# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

#reduce the size of the static files when they are served (this is more efficient)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'