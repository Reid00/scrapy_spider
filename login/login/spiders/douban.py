# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']

    def parse(self, response):
        # formdata = dict(username='18896510223', password='User@123')

        formdata = {
            'username': '****',
            'password': '***',
        }

        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_login,
        )

    def after_login(self, response):
        # formdata = {
        #     'ck': 'a',
        #     'signature': ''
        #
        # }
        # yield scrapy.FormRequest(
        #     'https://www.douban.com/people/184092171/',
        # )
        signature = response.xpath('//a[@class="sign-text"]/text()').extract_first()
        print(signature)
