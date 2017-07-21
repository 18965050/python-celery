from celery import Celery,platforms

app = Celery('tasks', broker='redis://guest@192.168.51.17:6379/8', backend='redis://guest@192.168.51.17:6379/9')

platforms.C_FORCE_ROOT=True

# app.conf.CELERY_TASK_SERIALIZER = 'json'

# app.conf.update(
#     CELERY_TASK_SERIALIZER='json',
#     CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
#     CELERY_RESULT_SERIALIZER='json',
#     CELERY_TIMEZONE='Asia/Shanghai',
#     CELERY_ENABLE_UTC=True
# )
# app = Celery('firststep.tasks', broker='redis://guest@192.168.51.17:6379/8')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    """add test"""
    return x + y

# celery -A first_step