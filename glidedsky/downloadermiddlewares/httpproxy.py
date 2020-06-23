# -*- coding: utf-8 -*-
class RandomProxyMiddleware(object):
    def __init__(self, squid_url):
        self.squid_url = squid_url

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(squid_url=settings.get("SQUID_URL"))

    def process_request(self, request, spider):
        request.meta["proxy"] = self.squid_url
        return
