# -*- coding: utf-8 -*-
import scrapy

from .github1 import logger


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    # 如果form 有action url 可以考虑使用scrapy.FormRequest.from_response()
    # 如果有多个form 表单可以通过xpath 定位 formname, formid,传入from_response
    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,  # 从response 里面寻找form 表单

            formdata={

                'login': 'Reid00',  # login 字段取决于输入表单的name
                'password': 'User@123.'
            },
            callback=self.after_login

        )

    def after_login(self, response):
        print(response.url)
