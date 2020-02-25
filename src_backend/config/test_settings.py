import os
import psycopg2
# import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

SECRET_KEY = os.urandom(24)
ALLOWED_HOSTS = ["https://vast-sierra-07062.herokuapp.com/", "127.0.0.1"]
DEBUG = True

# print("----------------")
# print(dj_database_url.config.name)

# Database


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
