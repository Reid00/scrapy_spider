# -*- coding: utf-8 -*-
import scrapy
import json


class RandomUseragentSpider(scrapy.Spider):
    name = 'random_useragent'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent']
        print('****' * 20)
        print(user_agent)
        print('****' * 20)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
