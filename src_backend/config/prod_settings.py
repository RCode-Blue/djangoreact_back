import os

# SECRET_KEY = '5j_!%*1@aqyhn%%zff#l6n%4lecm_5*)jrsfd4$fmvzf=-)25u'
SECRET_KEY = os.urandom(24)
ALLOWED_HOSTS = ["vast-sierra-07062.herokuapp.com", "0.0.0.0", "localhost"]
DEBUG=False
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_NAME = os.environ["DB_NAME"]

# Database
DATABASES = {
  "default":{
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": DB_NAME,
    "USER": DB_USERNAME,
    "PASSWORD": DB_PASSWORD,
    "HOST": "rosie.db.elephantsql.com",
    "PORT": "5432"
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'combineddjangoreact',
#         'USER': 'dev',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }