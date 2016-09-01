from celery_blog2 import fetch_url

from celery_add import add

def func(urls):
    for url in urls:
        fetch_url.delay(url)

if __name__ == "__main__":
    func(["https://www.baidu.com", "http://www.taobao.com", "http://www.163.com", "http://www.xyz.cn"])

    result = add.delay(4, 4)
    print(result.ready())
    print(result.get(timeout=2))