# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from ..items import Sp2Item
from scrapy.http import Request


class NeihanSpider(scrapy.Spider):
    name = 'neihan'
    allowed_domains = ['neihanshequ.com']
    # start_urls = ['http://neihanshequ.com/']

    def start_requests(self):
        yield Request(url="http://neihanshequ.com/", callback=self.parse, headers={"Host":"neihanshequ.com","Upgrade-Insecure-Requests":1})

    def parse(self, response):
        data = HtmlXPathSelector(response)
        duanzi_list = data.select('//div[@class="options"]')
        for duanzi in duanzi_list:
            text = duanzi.select('.//li[@class="share-wrapper right"]/@data-text').extract_first()
            print(text)
            obj = Sp2Item(text=text)
            yield obj


