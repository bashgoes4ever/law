DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'law',
        'PASSWORD': 'getlow',
        'HOST': 'localhost',
        'PORT': '',
    }
}