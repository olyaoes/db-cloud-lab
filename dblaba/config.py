import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'
sys.dont_write_bytecode = True

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', '21server-db.mysql.database.azure.com')
    MYSQL_USER = os.getenv('MYSQL_USER', 'labolya21@21server-db')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '21Olya0822')
    MYSQL_DB = os.getenv('MYSQL_DB', 'solar_station')
    MYSQL_CURSORCLASS = 'DictCursor'
    MYSQL_PORT = 3306
