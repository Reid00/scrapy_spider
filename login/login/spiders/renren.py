# -*- coding: utf-8 -*-
import scrapy


# reqeusts 库 登录的方式
# 1. ses=requests.Session 用session 登录
# 2. 直接将cookie 放到headers 里面
# 3. 使用selenium 直接点击


# scrapy 携带cookie 登录的方式
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/327550029/profile']

    def start_requests(self):
        cookies = '_ga=GA1.2.1999533006.1547704672; _octo=GH1.1.814999195.1547704672; _device_id=45a1f4a2fa9c5cde12d17632fa19ebe2; user_session=v3LMf-oETpFSvKpiMAYxcugUN02zAlWKjmNs-eovchsI533w; __Host-user_session_same_site=v3LMf-oETpFSvKpiMAYxcugUN02zAlWKjmNs-eovchsI533w; logged_in=yes; dotcom_user=Reid00; tz=Asia%2FShanghai; _gh_sess=cWx3Rk5OUk15WEswYlM3OWJJdzhBTmJKTzdLeUhUcmJMa0lmdWl0cVZVRG5IeXUwV2pnTUcwelE3U1VNcUpIMmlqZCs5SGlWUHVXc1dXdWlvRmRuSXBRakpCZEZCTmNrZ1J5Yy9Xc0h3Wno0YWtQdlQzYkhYVGQ1VmZXNTZwL3MrNzVFQllHMStUb1RqNU5jL1ltRjJQWVFvOHNBd0hUR3FwUDh6UWFjU29UdExtVGdEVGFPVmFiV244aVJncUhBYmhOSTZ4NWRKVXBPQkhGNWRiTnNLR09ZbFluNVdidDhZU0crei9lZ2lJOD0tLXRvNUZKRURHT0NCR1hLeEpWOWtBUEE9PQ%3D%3D--ecde8f8851787f6f4c198c3745e28d2d33cc4c45'
        # 使用字典推导式构建字典的cookies
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}
        print(cookies)
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies,
        )

    def parse(self, response):
        print(response.url)
        # 这里面可以直接Reqeust 其他信息了，因为Scrapy 下一次的请求会携带上一次请求的cookies
