import os

# Define if the application is running in debug mode
# Expected value = Boolean
DEBUG = True

# Manual configuration for testing environment
# Expected value = Boolean
TEST_ENV = False

# Define port to run the application on
# Expected value = Integer
PORT = 8080

#======================================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#======================================================================

# Defining application credentials
DATABASE_CREDS = {
    'USER': 'root',
    'PASSWORD': '*****',
    'HOST': '127.0.0.1',
    'DATABASE': 'bestdb'
}

# Specify default encoding for the application
DEFAULT_ENCODING = 'utf-8'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "fuckthisshitronnyjeremy"

# Secret key for signing cookies
SECRET_KEY = "ohmygodsomanshissoawesomefuckthisdick"

# server settings
API_PROTOCOL = 'http'
API_SERVER_NAME = 'dl.prspl.ay'

# API status codes
API_STATUS_CODES = {
  1 : "successful",
  2 : "wrong credentials",
  3 : "missing required parameters",
  4 : "illegal software version",
  5 : "permission mismatch",
  6 : "unable to register new box",
  7 : "successfully updated",
}
