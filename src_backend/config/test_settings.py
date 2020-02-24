import os
import psycopg2
# import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_URL = "postgres://jiekaflnbuzhgm:d1b4f0332b280cb829df9d4efb2ccd762d2716ba142fcce482f06298a0b2e117@ec2-35-172-85-250.compute-1.amazonaws.com:5432/d4r30ptm96tc6c"
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

SECRET_KEY = os.urandom(24)
ALLOWED_HOSTS = ["https://vast-sierra-07062.herokuapp.com/", "127.0.0.1"]
DEBUG = True

# print("----------------")
# print(dj_database_url.config.name)

# Database

db_uri = "postgres://pyeqawka:7sGHP58sHy4MIdC3DO6gP_irgwa7JDUv@rosie.db.elephantsql.com:5432/pyeqawka"

DATABASES = {
  "default":{
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": "pyeqawka",
    "USER": "pyeqawka",
    "PASSWORD": "7sGHP58sHy4MIdC3DO6gP_irgwa7JDUv",
    "HOST": "rosie.db.elephantsql.com",
    "PORT": "5432"
    }
}
# DATABASES['default']= dj_database_url.config(conn_max_age=600)
# DATABASES["default"]["ENGINE"] = 'django.db.backends.postgresql_psycopg2'
# DATABASES['default']: dj_database_url.config(conn_max_age=600, ssl_require=True)

# DATABASES = {
#   'default': {
#     "ENGINE": 'django.db.'
#   }
# }
