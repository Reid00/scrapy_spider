# -*- coding: utf-8 -*-
import scrapy
from ..items import SfwesfItem
import re


class SuzhouesfSpider(scrapy.Spider):
    name = 'suzhouesf'
    allowed_domains = ['fang.com']
    start_urls = ['https://suzhou.esf.fang.com/']

    def parse(self, response):
        infos = response.xpath('//div[@class="shop_list shop_list_4"]/dl[@dataflag]')
        for info in infos:
            item = SfwesfItem()
            name = info.xpath('.//h4/a/@title').extract_first()
            item['name'] = name
            details = info.xpath('.//p[@class="tel_shop"]//text()').extract()
            for detail in details:
                if '厅' in detail:
                    item['room'] = detail.strip()
                elif '㎡' in detail:
                    item['area'] = detail.strip()
                elif '层' in detail:
                    item['floor'] = detail.strip()
                elif '向' in detail:
                    item['toward'] = detail.strip()
                elif '年' in detail:
                    item['year'] = detail.strip()
            address = info.xpath('.//p[@class="add_shop"]//text()').extract()
            address = [re.sub(r'\s', '', address) for address in address]
            address = ''.join(address)
            item['address'] = address
            desc = info.xpath('.//p[@class="clearfix label"]//text()').extract()
            desc = [re.sub(r'\s', '', desc) for desc in desc]
            desc = ','.join(desc)
            item['desc'] = desc
            price = info.xpath('.//dd[@class="price_right"]/span[1]//text()').extract()
            price = [re.sub(r'\s', '', price) for price in price]
            price = ''.join(price)
            item['price'] = price
            unit = info.xpath('.//dd[@class="price_right"]/span[2]/text()').extract_first().strip()
            item['unit'] = unit
            yield item
        next_url = response.xpath('//p[text()="下一页"]/@href').extract_first()
        next_url = response.urljoin(next_url)
        yield scrapy.Request(next_url, callback=self.parse)
