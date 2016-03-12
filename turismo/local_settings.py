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

SOCIAL_AUTH_FACEBOOK_KEY = '1038428972870177'
SOCIAL_AUTH_FACEBOOK_SECRET = '24d4b5924906052fab2a2b2a46d6df1a'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]  # optional

