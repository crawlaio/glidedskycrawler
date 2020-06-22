# -*- coding: utf-8 -*-

import scrapy

from glidedsky.items import GlidedskyItem


class BasicOneSpider(scrapy.Spider):
    name = "basicone"

    start_urls = ["http://glidedsky.com/level/web/crawler-basic-1"]

    def parse(self, response):
        num = response.xpath("//div[@class='col-md-1']/text()").extract()
        item = GlidedskyItem(numbers=[int(str(one.strip())) for one in num])
        yield item
