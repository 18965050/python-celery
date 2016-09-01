import requests
from celery import Celery

app = Celery('celery_blog', broker='redis://192.168.51.17:6379/8')

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)

def func(urls):
    for url in urls:
        fetch_url.delay(url)

if __name__ == "__main__":
    func(["https://www.baidu.com", "http://www.taobao.com", "http://www.163.com", "http://www.xyz.cn"])