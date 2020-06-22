# -*- coding: utf-8 -*-

import scrapy

from glidedsky.items import GlidedskyItem


class BasicTwoSpider(scrapy.Spider):
    name = "basictwo"

    start_urls = ["http://glidedsky.com/level/web/crawler-basic-2?page={0}".format(one) for one in range(1, 1001)]

    def parse(self, response):
        num = response.xpath("//div[@class='col-md-1']/text()").extract()
        item = GlidedskyItem(numbers=[int(str(one.strip())) for one in num])
        yield item
