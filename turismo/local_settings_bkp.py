
DATABASES = {
    'default': {
 	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'prueba',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
# smtp 
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_USE_TLS = False


