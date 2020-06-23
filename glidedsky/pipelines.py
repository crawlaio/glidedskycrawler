# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class GlidedskyPipeline:
    def __init__(self):
        self.result = 0
        self.count = 1

    def close_spider(self, spider):
        print("*" * 100)
        print("题目：{0}  计算结果: {1}".format(spider.name, self.result))
        print("*" * 100)

    def process_item(self, item, spider):
        if item["numbers"]:
            numbers = item["numbers"]
            self.result += sum(numbers)
            print("次数：{0} 题目：{1}  计算结果: {2}".format(self.count, spider.name, self.result))
            self.count += 1
        else:
            return DropItem("Missing Number.")
        return item
