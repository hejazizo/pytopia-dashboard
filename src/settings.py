import os

# This defines the base dir for all relative imports for our project, put the file in your root folder so the
# base_dir points to the root folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# According to your data file, you can change the engine, like mysql, postgresql, mongodb etc make sure your data is
# directly placed in the same folder as this file, if it is not, please direct the 'NAME' field to its actual path.
if os.environ['STAGE'] == 'TEST':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'connect_timeout': 6000,
            },
            'NAME': os.environ['MYSQL_DB_NAME'],
            'HOST': os.environ['MYSQL_DB_HOST'],
            'PORT': os.environ['MYSQL_DB_PORT'],
            'USER': os.environ['MYSQL_DB_USER'],
            'PASSWORD': os.environ['MYSQL_DB_PASSWORD'],
        }
    }

# Since we only have one app which we use
INSTALLED_APPS = (
    'db',
)

# Write a random secret key here
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
