# portfolio/portfolio/settings_production.py
from .settings import *
import os

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ['weedu34.github.io', 'web-portfolio-f189.onrender.com']

# Add CORS to installed apps if not already there
if 'corsheaders' not in INSTALLED_APPS:
    INSTALLED_APPS = ['corsheaders'] + list(INSTALLED_APPS)

# Modify existing MIDDLEWARE instead of redefining it
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
if 'corsheaders.middleware.CorsMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://weedu34.github.io",
]

# Use environment variable for secret key (important for security)
#SECRET_KEY = os.environ.get('SECRET_KEY', 'your-fallback-secret-key')