# -*- coding: utf-8 -*-
import hashlib
import json
import time

import scrapy

from glidedsky.items import GlidedskyItem


class JavaScriptObfuscationOneSpider(scrapy.Spider):
    name = "javascriptobfuscationone"

    def start_requests(self):
        for page in range(1, 1001):
            t = str(int(time.time()))
            sha = hashlib.sha1(f"Xr0Z-javascript-obfuscation-1{t}".encode("utf-8"))
            sign = sha.hexdigest()
            url = "http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page={0}&t={1}&sign={2}".format(
                page, t, sign
            )

            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        numbers = json.loads(response.text).get("items", [])
        item = GlidedskyItem(numbers=numbers)
        yield item
