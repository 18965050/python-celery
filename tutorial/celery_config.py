from celery import Celery

app = Celery('celery_config', broker='redis://192.168.51.17:6379/8', backend='redis://guest@192.168.51.17:6379/9', include=['celery_blog2','celery_add','pack.celery_fetch'])