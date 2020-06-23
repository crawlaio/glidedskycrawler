# -*- coding: utf-8 -*-
import scrapy

from glidedsky.items import GlidedskyItem


class IPBlockTwoSpider(scrapy.Spider):
    name = "ipblocktwo"

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "CONCURRENT_REQUESTS": 10,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 10,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "glidedsky.downloadermiddlewares.useragent.RandomUserAgentMiddleware": 300,
            "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None,
            "glidedsky.downloadermiddlewares.httpproxy.RandomProxyMiddleware": 400,
            "glidedsky.downloadermiddlewares.cookies.LoginCookiesMiddleware": 300,
        },
    }

    start_urls = ["http://glidedsky.com/level/web/crawler-ip-block-2?page={0}".format(one) for one in range(1, 1001)]

    def parse(self, response):
        num = response.xpath("//div[@class='col-md-1']/text()").extract()
        item = GlidedskyItem(numbers=[int(str(one.strip())) for one in num])
        yield item
