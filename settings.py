import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

jwt_secret_key='s3cr3t'

MYSQL = {
    "host": os.environ['DBHOST'],
    "user": os.environ['DBUSER'],
    "database": os.environ['DBDATABASE'],
    "password": os.environ['DBPASSWORD'],
    "port": os.environ["DBPORT"],
    "pool_size": int(os.environ['DBPOOLSIZE']),
    "echo": False if os.environ["DBECHO"] != 'True' else True
}

connect_string = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(**MYSQL)
engine = create_engine(connect_string, pool_size=MYSQL['pool_size'], echo_pool=True, encoding='utf-8', echo=MYSQL['echo'], pool_recycle=120)
session_factory = sessionmaker(bind=engine, autoflush=False)
Session = scoped_session(session_factory)
session = Session()