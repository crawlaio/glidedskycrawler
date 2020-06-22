# -*- coding: utf-8 -*-
import re

import scrapy

from glidedsky.items import GlidedskyItem


class CssPuzzleOneSpider(scrapy.Spider):
    name = "csspuzzleone"

    start_urls = ["http://glidedsky.com/level/web/crawler-css-puzzle-1?page={0}".format(one) for one in range(1, 1001)]

    def parse(self, response):
        numbers = []
        css_label = "".join(response.xpath('//style/text()').extract())
        before_dict = dict()
        css_content_label = re.findall(r'\.(.*?):before { content:"(.*?)" }', str(css_label))
        for cont in css_content_label:
            before_dict[cont[0]] = cont[1]
        css_del_names = re.findall(r'\.(.*?) { margin-right:-1em }', str(css_label))
        css_left_label = re.findall(r'\.(.*?) { left:(.*?)em }', str(css_label))
        count_dict = dict()
        for count in css_left_label:
            count_dict[count[0]] = count[1]
        col_list = response.xpath("//div[@class='col-md-1']")
        for col in col_list:
            class_names = col.xpath("./div/@class").extract()
            values = col.xpath("./div/text()").extract()
            if len(class_names) >= 3:
                move_num = ['0', '0', '0']
                index = 0
                for class_name, value in zip(class_names, values):
                    if class_name not in css_del_names:
                        if class_name in count_dict and class_name not in css_del_names:
                            move_num[index + int(count_dict[class_name])] = value
                        else:
                            move_num[index] = value
                        index += 1
                new_number = "".join(move_num)
                numbers.append(int(new_number))
            elif len(class_names) == 1:
                new_number = before_dict[class_names[0]]
                numbers.append(int(new_number))
            else:
                for class_name in class_names:
                    if class_name in before_dict.keys():
                        new_number = before_dict[class_name]
                        numbers.append(int(new_number))
                        break
        item = GlidedskyItem(numbers=numbers)
        yield item
