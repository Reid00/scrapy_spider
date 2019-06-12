# -*- coding: utf-8 -*-
import scrapy
from ..items import SfwNewHouseItem
import re


class SuzhoufangSpider(scrapy.Spider):
    name = 'suzhoufang'
    allowed_domains = ['fang.com']
    start_urls = ['https://suzhou.newhouse.fang.com/house/s/']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse_newhouse)
        # yield scrapy.Request(self.start_urls[1], callback=self.parse_newhouse)

    def parse_newhouse(self, response):
        infos = response.xpath('//div[@class="nhouse_list"]/div/ul/li')
        for info in infos:
            item = SfwNewHouseItem()
            item['name'] = info.xpath('.//div[@class="nlcd_name"]/a/text()')
            if not item['name']:
                continue
            item['name'] = info.xpath('.//div[@class="nlcd_name"]/a/text()').extract_first().strip()
            item['room'] = info.xpath('.//div[@class="house_type clearfix"]/a/text()').extract()
            item['room'] = '/'.join(item['room'])
            areas = info.xpath('.//div[@class="house_type clearfix"]/text()').extract()
            areas = [re.sub(r'\s|－', '', area) for area in areas][-1]
            item['area'] = areas
            item['address'] = info.xpath('.//div[@class="address"]/a/@title').extract_first().strip()
            unit = info.xpath('.//div[@class="nhouse_price"]//text()').extract()
            unit = [re.sub(r'\s', '', unit) for unit in unit]
            item['unit'] = ''.join(unit)
            item['phone'] = info.xpath('.//div[@class="tel"]/p//text()').extract()
            item['phone'] = ''.join(item['phone'])
            status = info.xpath('//div[@class="fangyuan"]/span/text()').extract_first()
            item['status'] = status
            desc = info.xpath('.//div[@class="fangyuan"]/a//text()').extract()
            item['desc'] = ','.join(desc)
            yield item
        next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        next_url = response.urljoin(next_url)
        yield scrapy.Request(next_url, callback=self.parse_newhouse)
