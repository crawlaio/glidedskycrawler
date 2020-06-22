# -*- coding: utf-8 -*-

BOT_NAME = "glidedsky"

SPIDER_MODULES = ["glidedsky.spiders"]
NEWSPIDER_MODULE = "glidedsky.spiders"

ROBOTSTXT_OBEY = False

SQUID_URL = "http://localhost:3128"

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR "
    "2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
]

LOGIN_COOKIES = {
    "_ga": "GA1.2.1297474790.1592555590",
    "footprints": "eyJpdiI6Imp0SnlSV2s3Tlc1em0xV0NOK3lkUUE9PSIsInZhbHVlIjoidTlCWitmZTVNXC9nYWQ4cjFnajZtRkdwOHFkNjFqOHh0NVpRcGN3RThNVnNHbkZ6ZGI4ajFrbHp0MER0aW9LalQiLCJtYWMiOiJlY2I5ZmMwYTRlOWE0ZDU4MzljYTJjYTdmNTk0NmI3M2JhODIzNWMyMTk2NTQ2OWUwMWEwN2ZiODYwMTFjYWFhIn0%3D",
    "Hm_lvt_020fbaad6104bcddd1db12d6b78812f6": "1592556082,1592605807,1592639209,1592789182",
    "_gid": "GA1.2.1438536078.1592789182",
    "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "eyJpdiI6IjBQVlNvQ0RNR28xWkI3emEzSlA4bFE9PSIsInZhbHVlIjoiZ2VuWXp0WlV0TVlnSEhDQ0ZKRDcwaG9nTmYwOXpDSzJUTnRqXC95UXdHcTFCODVrMFQzVXdUa1dIeE5nbWFSUXpDRFFtdWpWOGhTR3UrVHNyVmFNUzNselpsTnR2azdhUllKRUU2Q3MwWEpzS3hCb2JtTjY4T0VuR25FNVBtR3lra1ZzaGVmRFROQmVGYlJVZFwvV3lrSlNYVUE5QTU1aFV1Q2orN01kV3cyZWM9IiwibWFjIjoiMmYyYmRlMTdmYWU2OGI5ZTg5MGMyNDdiN2Y1NjZhZDk3OTAzYmU2MWYxMmJkNDA3NmFmNjUxYzVjN2RiNjBlMiJ9",
    "XSRF-TOKEN": "eyJpdiI6IjkwcGZpNGllUnFPOXZ1bmpQT0FSemc9PSIsInZhbHVlIjoiallZSWxQWThTNzBnRXZVaXJcL0NyeEJOUWJEakN1STlFZVpybjFiXC9SN3UwcUpXaTVsdXFxc0hWQ3BxeE5sZlNaIiwibWFjIjoiZTA5YjFlNTI5YjQ3N2JmMDBhNjczNDUzMzYwNzNkZDcwZTI1NzRkN2Q0M2JlYmVkODc0NDg2MTlhY2M1NjY3NyJ9",
    "glidedsky_session": "eyJpdiI6Iml3WUN2dGtEaTdpXC9TS1RmU3FNU2pBPT0iLCJ2YWx1ZSI6ImErYkR0dUhyRFdTQ09IcTZzU0R5dGx3UjFrbzlicU9vMllNM3VJV2NFTmtqXC9JQWoyVlpUK3p0V3FybjdkNU9wIiwibWFjIjoiOWVkZGY3ZmExYmVlYjZhMzdkNDU1YWM4Y2U0ZWMxNWI1OTYzYzFhOGU5YTVjZjUyNTgxMjc1NzU5YjlhZTExMyJ9",
    "Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6": "1592790255",
}

DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7",
}

DOWNLOADER_MIDDLEWARES = {
    # "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    # "glidedsky.downloadermiddlewares.useragent.RandomUserAgentMiddleware": 300,
    # "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None,
    # "glidedsky.downloadermiddlewares.httpproxy.RandomProxyMiddleware": 400,
    "glidedsky.downloadermiddlewares.cookies.LoginCookiesMiddleware": 300,
}

RETRY_ENABLED = True
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408, 406, 403, 404, 429]
RETRY_TIMES = 25

ITEM_PIPELINES = {
    "glidedsky.pipelines.GlidedskyPipeline": 100
}

LOG_LEVEL = "INFO"
