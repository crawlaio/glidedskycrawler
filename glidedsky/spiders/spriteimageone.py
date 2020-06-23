# -*- coding: utf-8 -*-
import base64
import re
from io import BytesIO

import scrapy
from PIL import Image

from glidedsky.items import GlidedskyItem


class SpriteImageOneSpider(scrapy.Spider):
    name = "spriteimageone"

    start_urls = [
        "http://glidedsky.com/level/web/crawler-sprite-image-1?page={0}".format(one) for one in range(1, 1001)
    ]

    def parse(self, response):
        numbers = []
        images_base64 = re.findall(r'background-image:url\("data:image/png;base64,(.*?)"\)', str(response.text))[0]
        css_content_label = re.findall(r"\.(.*?) { background-position-x:(.*?)px }", str(response.text))
        num_map = dict()
        for cont in css_content_label:
            num_map[cont[0] + " sprite"] = cont[1]

        img_fp = BytesIO(base64.b64decode(str(images_base64).encode("utf-8")))
        img = Image.open(img_fp)
        right_border_list = self.split_img_number(img)

        col_list = response.xpath("//div[@class='col-md-1']")
        for col in col_list:
            class_names = col.xpath("./div/@class").extract()
            tags_nums = []
            for tag in class_names:
                tag_position_x = num_map[tag]
                for index, border_x in enumerate(right_border_list):
                    cur_pos_x = abs(int(tag_position_x))
                    if index + 1 >= len(right_border_list):
                        break
                    if border_x <= cur_pos_x < right_border_list[index + 1]:
                        tags_nums.append(str(index))
                        break
            numbers.append(int("".join(tags_nums)))
        item = GlidedskyItem(numbers=numbers)
        yield item

    @staticmethod
    def split_img_number(img):
        limg = img.convert("L")
        pixels = limg.load()

        for y in range(limg.height):
            for x in range(limg.width):
                pixels[x, y] = 0 if pixels[x, y] < 250 else 255

        def find_next_white_column(start_x):
            for x in range(start_x, limg.width):
                for y in range(limg.height):
                    if pixels[x, y] < 1:
                        break
                else:
                    return x
            raise ValueError("split_img_number")

        def find_next_black_column(start_x):
            for x in range(start_x, limg.width):
                for y in range(limg.height):
                    if pixels[x, y] < 1:
                        return x

        right_border_list = [0]
        black_start_x = find_next_black_column(0)

        white_start_x = find_next_white_column(black_start_x)
        right_border_list.append(white_start_x)
        for i in range(1, 10):
            black_start_x = find_next_black_column(white_start_x)
            white_start_x = find_next_white_column(black_start_x)
            right_border_list.append(white_start_x)

        return right_border_list
