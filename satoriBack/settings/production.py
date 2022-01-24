from .settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['apisatori.herokuapp.com',
'http://localhost:8080/', 'http://localhost:3000/','roninsatori.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT':5432
    }
}
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587

GRAPHQL_AUTH = {
    "EMAIL_TEMPLATE_VARIABLES": {
        "current_domain": "apisatori.herokuapp.com"
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