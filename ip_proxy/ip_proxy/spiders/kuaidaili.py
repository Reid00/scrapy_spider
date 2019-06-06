# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import telnetlib


class KuaidailiSpider(CrawlSpider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    rules = (
        Rule(LinkExtractor(allow=r'/free/inha/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 分组
        trs = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        for tr in trs:
            item = {}
            item['ip'] = tr.xpath('./td[@data-title="IP"]/text()').extract_first()
            item['port'] = tr.xpath('./td[@data-title="PORT"]/text()').extract_first()
            item['anonymous'] = tr.xpath('./td[@data-title="匿名度"]/text()').extract_first()
            item['type'] = tr.xpath('./td[@data-title="类型"]/text()').extract_first()
            item['location'] = tr.xpath('./td[@data-title="位置"]/text()').extract_first()
            item['speed'] = tr.xpath('./td[@data-title="响应速度"]/text()').extract_first()
            item['last_confirm_date'] = tr.xpath('./td[@data-title="最后验证时间"]/text()').extract_first()
            print('test the ip: ', item['ip'])
            # 验证是否可用
            try:
                telnetlib.Telnet(item['ip'], port=item['port'], timeout=20)
            except:
                print('{}:    is invalid'.format(item['ip']))
                item['valid'] = False
            else:
                print('{}:  is valid'.format(item['ip']))
                item['valid'] = True
            if item['valid']:
                print(item)
