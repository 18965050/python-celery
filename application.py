from celery import Celery

app = Celery()

app.conf.CELERY_TIMEZONE='Asia/Shanghai'

@app.task
def add(x,y):
    return x+y

if __name__ == '__main__':
    # app.worker_main()
    #
    # add.delay(4,4)
    # print(add.ready())
    # print(add.get(timeout=1))

    print(app.conf.CELERY_TIMEZONE)