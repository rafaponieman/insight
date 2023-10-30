from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dev-unsafe-943a9ae36ba3aac56e9e8fb5fc999d4a226f0416ef009b65076e8f00a0547866'

ALLOWED_HOSTS = ['*']

# WARNING: do not enable in production
CORS_ALLOW_ALL_ORIGINS = True

try:
    from .local import *  # pylint: disable=wildcard-import
except ImportError:
    print('Please create a local.py settings file in your insight/settings/ folder, '
          + 'based on relevant/settings/local.example.py')
    raise

