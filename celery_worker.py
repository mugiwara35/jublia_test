# celery_worker.py
from apps import create_celery

celery = create_celery()

if __name__ == '__main__':
    celery.start()