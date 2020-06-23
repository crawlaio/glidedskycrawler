# -*- coding: utf-8 -*-
import base64
import re
from io import BytesIO

import scrapy
from fontTools.ttLib import TTFont

from glidedsky.items import GlidedskyItem


class FontPuzzleTwoSpider(scrapy.Spider):
    name = "fontpuzzletwo"

    start_urls = ["http://glidedsky.com/level/web/crawler-font-puzzle-2?page={0}".format(one) for one in range(1, 1001)]

    def parse(self, response):
        num_str_list = response.xpath("//div[@class='col-md-1']/text()").extract()
        ttf_base64 = re.findall(r"data:font;charset=utf-8;base64,(.*?)\)", response.text)[0]
        base64_data = base64.decodebytes(ttf_base64.encode())
        font = TTFont(BytesIO(base64_data))
        uni_list = font.getGlyphOrder()[1:11]
        camp_list = font.getBestCmap()

        def str2num(string):
            number = ""
            for s in string.strip():
                unicode_str = s.encode("unicode-escape").decode()
                sixteen_ary = unicode_str.replace("\\u", "0x")
                num = uni_list.index(camp_list[int(sixteen_ary, 16)])
                number += str(num)
            return int(number)

        numbers = [str2num(one.strip()) for one in num_str_list]
        item = GlidedskyItem(numbers=numbers)
        yield item
