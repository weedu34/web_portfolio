from .settings import *

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ['weedu34.github.io', 'web-portfolio-f189.onrender.com']

# WhiteNoise for production
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://weedu34.github.io",
]