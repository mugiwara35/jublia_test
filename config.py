import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/jublia_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "test-8c100af1-a6d6-4ae4-b752-ffefdd04411e-jublia"
