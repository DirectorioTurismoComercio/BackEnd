DATABASES = {
    'default': {
 	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'plataforma',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
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
# social auth settings
# valid redirect domain for all apps: http://restsocialexample.c
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', # needed starting from protocol v2.4
}
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # optional

