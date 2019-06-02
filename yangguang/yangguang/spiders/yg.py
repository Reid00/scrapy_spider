# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://sun0769.com/']

    def parse(self, response):
        # pass
        for i in range(10):
            item = {}
            item['come_from'] = 'yg'
            logger.warning(item)
            yield item
