from .settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zj1$87yai!pwf9!u5oehzsh)a$(5ws&8tji0tp8%79x=1h6xc6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
""""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT':5432
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'deliveryfoodpopayan@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'Delivery123'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


GRAPHQL_AUTH = {
    "EMAIL_TEMPLATE_VARIABLES": {
        "current_domain": "localhost:8000"
    },
    'LOGIN_ALLOWED_FIELDS': ['email'],
    #No permite loguear si no esta verificado
    'ALLOW_LOGIN_NOT_VERIFIED': False,
    #En true permite registro sin contraseña
    'ALLOW_PASSWORDLESS_REGISTRATION':False,
    'UPDATE_MUTATION_FIELDS': ['first_name', 'last_name','email','is_staff',"user_phone","user_address"],
    'REGISTER_MUTATION_FIELDS':['first_name','last_name','email'],
    'REGISTER_MUTATION_FIELDS_OPTIONAL': ['is_superuser',"user_phone","user_address"],
    'USER_NODE_FILTER_FIELDS': {
                "email": ["exact",],
                "is_active": ["exact"],
    }
    # ...
}