from pack.celery_fetch import func

if __name__ == "__main__":
    func(["https://www.baidu.com", "http://www.taobao.com", "http://www.163.com", "http://www.xyz.cn"])