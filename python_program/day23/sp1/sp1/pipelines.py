# -*- coding: utf-8 -*-

# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sp1Pipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        val = crawler.settings.get("FILE_NAME")
        return cls(val)

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_obj = None

    def process_item(self, item, spider):
        self.file_obj.write("%s%s%s%s" %(item['title'], "\r\n", item['url'], "\r\n"))
        return item

    def open_spider(self, spider):
        self.file_obj = open(self.file_path, mode="w",encoding="utf-8")

    def close_spider(self, spider):
        self.file_obj.close()
