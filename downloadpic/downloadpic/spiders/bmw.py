# -*- coding: utf-8 -*-
import scrapy

# from downloadpic.downloadpic.items import DownloadpicItem
from ..items import DownloadpicItem


class BmwSpider(scrapy.Spider):
    name = 'bmw'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/153.html']

    # base_url = 'https://car.autohome.com.cn'

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            item = DownloadpicItem()  # 在此处定义item， 每种类型返回一次
            category = uibox.xpath('./div[@class="uibox-title"]/a/text()').extract_first()
            urls = uibox.xpath('.//ul/li/a/img/@src').extract()
            # urls = ['https://' + url for url in urls]     #列表推导式
            urls = [response.urljoin(url) for url in urls]  # response.urljoin()方法
            item['category'] = category
            item['image_urls'] = urls
            # print(item)
            yield item
