# -*- coding: utf-8 -*-
import scrapy
import sys, io, os
from scrapy.selector import HtmlXPathSelector
from ..items import Sp1Item
from scrapy.http import Request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    """
    爬虫爬到数据后放入调度器或者持久化取决于yield的对象:
            如果yield的Sp1Item则持久化(Sp1Item名字可以自定义)
            如果是Request对象则放入调度器
    """
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item_list = hxs.select('//div[@id="content-list"]/div[@class="item"]')
        # 数据持久化放入pipeline
        for item in item_list:
            data = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-title').extract_first()
            url = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-pic').extract_first()
            obj = Sp1Item(title=data, url=url)
            yield obj

        #数据放入调度器
        # page_url_list = hxs.select('//div[@id="dig_lcpage"]//a/@href').extract()
        page_url_list = hxs.select('//div[@id="dig_lcpage"]//a[re:test(@href,"/all/hot/recent/\d+")]/@href').extract()
        for url in page_url_list:
            url = "http://dig.chouti.com" + url
            obj = Request(url=url, callback=self.parse)
            yield obj
