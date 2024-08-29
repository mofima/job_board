from .base import * 


DEBUG = True 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'local',
        "USER": "postgres",
        "PASSWORD": 'mypassword',
        "HOST": "db",
        "PORT": 5432
    }
}