# -*- coding: utf-8 -*-

from scrapy import signals


class RandomProxyMiddleware(object):

    def __init__(self, squid_url):
        self.squid_url = squid_url

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        s = cls(
            squid_url=settings.get("SQUID_URL"),
        )
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.meta["proxy"] = self.squid_url
        return

    def spider_opened(self, spider):
        spider.logger.info("Proxy opened: %s" % spider.name)
