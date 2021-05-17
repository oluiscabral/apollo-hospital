'''
@author: oluiscabral
'''


class Config():
    SECRET_KEY = b'_\x99`\x84\xe8\xad\xa71\x8e\xa6\xe3\xdd\xd1:\xd2G'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
