# -*- coding: utf-8 -*-
import base64
import re
from io import BytesIO

import scrapy
from fontTools.ttLib import TTFont

from glidedsky.items import GlidedskyItem


class FontPuzzleOneSpider(scrapy.Spider):
    name = "fontpuzzleone"

    start_urls = ["http://glidedsky.com/level/web/crawler-font-puzzle-1?page={0}".format(one) for one in range(1, 1001)]

    def parse(self, response):
        base_font = TTFont(r"glidedsky/data/font.ttf")
        base_uni_list = base_font.getGlyphOrder()[1:]
        origin_dict = {
            "five": "0",
            "four": "1",
            "two": "2",
            "three": "3",
            "zero": "4",
            "one": "5",
            "nine": "6",
            "six": "7",
            "eight": "8",
            "seven": "9",
        }
        str2num_dict = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        num_map = dict()
        ttf_base64 = re.findall(r"data:font;charset=utf-8;base64,(.*?)\)", response.text)[0]
        base64_data = base64.decodebytes(ttf_base64.encode())
        online_font = TTFont(BytesIO(base64_data))
        online_uni_list = online_font.getGlyphOrder()[1:]
        for uni2 in online_uni_list:
            obj2 = online_font["glyf"][uni2]
            for uni1 in base_uni_list:
                obj1 = base_font["glyf"][uni1]
                if obj1 == obj2:
                    num_map[str2num_dict[uni2]] = origin_dict[uni1]
        num = response.xpath("//div[@class='col-md-1']/text()").extract()
        numbers = []
        for one in num:
            new_num = ""
            for i in one.strip():
                new_num += num_map[i]
            numbers.append(int(new_num))
        item = GlidedskyItem(numbers=numbers)
        yield item
