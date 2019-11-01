import os

from celery import Celery

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')

if __name__ == '__main__':
    app.start()
