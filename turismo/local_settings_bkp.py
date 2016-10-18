DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'plataforma',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET storage_engine=MYISAM",
        }, 
    }
}
# smtp 
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_USE_TLS = False

SOCIAL_AUTH_FACEBOOK_KEY = '1529648703998052'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b7609e3cb5d8af0df1da85c61b263cf1'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '134061854666-op17m2c08s30q3des75on95hib3a4a43.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'uOgkGnpUXsvadfxq0g3DmEtk'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', ]
# social auth settings
# valid redirect domain for all apps: http://restsocialexample.c
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', # needed starting from protocol v2.4
}
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile']  # optional
MEDIA_URL='/Fotos/Fotos/'
URL_FRONTEND_RESET_PASSWORD='http://ecosistema.desarrollo.com/FrontEnd/public/#/forgotpassword'


LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
       'file': {
           'level': 'ERROR',
           'class': 'logging.FileHandler',
           'filename': 'debug6.log',
       },
   },
   'loggers': {
       'django': {
           'handlers': ['file'],
           'level': 'ERROR',
           'propagate': True,
       },
       'django.db.backends': {
           'handlers': ['file'],
           'level': 'DEBUG',
           'propagate': True,
       },

   },
}
