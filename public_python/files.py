
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = 'public/'

# Zmienna BASE_DIR powinna być utworzona przez Django w pliku settings.py
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'public/', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/')

STATICFILES_DIRS = (
    
    os.path.join(BASE_DIR, 'public/'),
