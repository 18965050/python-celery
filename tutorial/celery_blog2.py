import requests
from celery_config import app

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print (resp.status_code)

