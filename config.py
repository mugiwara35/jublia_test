import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/jublia_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "test-8c100af1-a6d6-4ae4-b752-ffefdd04411e-jublia"
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='rekrut.hrd.ai@gmail.com'
    MAIL_DEFAULT_SENDER='rekrut.hrd.ai@gmail.com'
    MAIL_PASSWORD='xrkuqmtopsihzhvo'
    MAIL_USE_SSL=False