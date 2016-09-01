from __future__ import absolute_import

from celery import Celery

app = Celery('proj',
             broker='redis://guest@192.168.51.17:6379/8',
             backend='redis://guest@192.168.51.17:6379/9',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()