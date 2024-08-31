import environ 
import os 

from .base import * 


# initialize environ
env = environ.Env()

# read the .env_local file
environ.Env.read_env(os.path.join(BASE_DIR, 'settings', '.env_local'))

DEBUG = env.bool('DEBUG', default=True) # set true for local devpt
SECRET_KEY = env('SECRET_KEY', default='your-default-secret-key')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])
