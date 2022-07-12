# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l3s0j8ynya0-*fqd!$w2@y=b4%gs&rx6z@o%onrhytje6^f^g@'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'car_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}