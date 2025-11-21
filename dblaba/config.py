
import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'

sys.dont_write_bytecode = True

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'flask_user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '210lya0822')
    MYSQL_DB = os.getenv('MYSQL_DB', 'solar_station')
    MYSQL_CURSORCLASS = 'DictCursor'

