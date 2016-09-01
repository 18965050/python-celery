import requests
import time

def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
    print("It took", time.time() - start, "seconds")

if __name__ == "__main__":
    func(["https://www.baidu.com", "http://www.taobao.com", "http://www.163.com", "http://www.xyz.cn"])