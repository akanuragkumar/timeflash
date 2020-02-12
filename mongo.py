from pymongo import MongoClient

env = 'production'

if env == 'production':
    mongo_db_host = '10.141.2.154'
    MONGO_USERNAME = 'cgadmin'
    MONGO_PASSWORD = '603W1%A1346MXaS'
    database_name = 'contentgrail'

else:
    mongo_db_host = '10.141.2.139'
    MONGO_USERNAME = 'cgadmin'
    MONGO_PASSWORD = '603W1%A1346MXaS'
    database_name = 'contentgrail'


def mongo_db_connect():
    conn = MongoClient(host=mongo_db_host, username=MONGO_USERNAME, password=MONGO_PASSWORD, authSource=database_name)
    db = conn['contentgrail']
    return db
