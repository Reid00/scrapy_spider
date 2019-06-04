# -*- coding: utf-8 -*-
import scrapy
import re

import logging

logger = logging.getLogger(__name__)


class Github1Spider(scrapy.Spider):
    name = 'github1'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        # 向github login 页面发起请求，获取登录所需的表单信息
        commit = response.xpath('//input[@name="commit"]/@value').extract_first()
        utf8 = response.xpath('//input[@name="utf8"]/@value').extract_first()
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        # 登录所需的表单信息，构建成字典
        formdata = {
            'login': 'Reid00',
            'password': '*****',
            'utf8': utf8,
            'commit': commit,
            'authenticity_token': authenticity_token,
            'webauthn-support': 'supported',
        }
        logger.warning(formdata)
        url = 'https://github.com/session'
        # 发送post 表单登录请求
        yield scrapy.FormRequest(
            url,
            formdata=formdata,
            callback=self.after_login
        )

    def after_login(self, response):
        # 验证是否登录成功，登录成功后的跳转url 为“https://github.com/”， 或者在此页面中抓独特的信息
        # reid = re.findall(r'Reid', response.body.decode())
        reid = re.findall(r'Reid00/move_files', response.text)
        # with open('github.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # logger.warning(response.url)
