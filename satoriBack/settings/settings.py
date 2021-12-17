"""
Django settings for satoriBack project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'users.apps.UsersConfig',
    'api_graphql',
    "graphql_auth",
    'corsheaders',
    'roles.apps.RolesConfig'
    # refresh tokens are optional
    #'graphql_jwt.refresh_token.apps.RefreshTokenConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOWED_ORIGINS = ["http://backend-authql.herokuapp.com",
"http://localhost:8080", "http://localhost:3000","https://prueba-react-app.herokuapp.com","http://localhost:8000"]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'satoriBack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'satoriBack.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'Etc/GMT-5'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.UserStori'

GRAPHENE = {
    'SCHEMA': 'satoriBack.schema.schema',
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ]
}
AUTHENTICATION_BACKENDS = [
    #"graphql_jwt.backends.JSONWebTokenBackend",
    "graphql_auth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
    
]
GRAPHQL_AUTH = {
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
GRAPHQL_JWT = {
    #...
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",

        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
    ],
    #"JWT_ALLOW_ARGUMENT": True,
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Activate Django-Heroku.
django_heroku.settings(locals())
"""
GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,

    # optional
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
}
"""