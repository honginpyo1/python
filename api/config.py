from sqlalchemy import create_engine, text

db = {
    'user' : 'admin',
    'password' : 'SOFNUJIUDEIDQFUA',
    'host' : 'sl-aus-syd-1-portal.4.dblayer.com',
    'port' : 21947,
    'database' : 'miniter'
}

config = {
    'DB_URL' : f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8",
    'JWT_SECRET_KEY' : 'HELLO_MY_SECRET',
    'JWT_EXP_DELTA_SECONDS' : 7 * 24 * 60 * 60,
    'UPLOAD_DIRECTORY' : './profile_pictures'
}

test_db = {
    'user' : 'admin',
    'password' : 'SOFNUJIUDEIDQFUA',
    'host' : 'sl-aus-syd-1-portal.4.dblayer.com',
    'port' : 21947,
    'database' : 'test_db'
}

test_config = {
    'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
    'JWT_SECRET_KEY' : 'HELLO_MY_SECRET',
    'JWT_EXP_DELTA_SECONDS' : 7 * 24 * 60 * 60
}

UPLOAD_direCTORY = './profile_pictures'
JWT_SECRET_KEY = 'HELLO_MY_SECRET',
JWT_EXP_DELTA_SECONDS = 7 * 24 * 60 * 60