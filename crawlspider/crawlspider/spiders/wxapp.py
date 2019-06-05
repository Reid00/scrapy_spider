# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/forum-47-1.html']

    rules = (
        # Rule(LinkExtractor(allow=r'forum-47-(\d+)'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[text()="下一页"]'), callback='parse_item', follow=True),
             # callback 是否对当前满足条件的url 回调函数
             # follow = true 对满足条件的页面，继续进行当前条件的查找
             )

    def parse_item(self, response):
        # 分组
        tbodys = response.xpath('//table[@id="threadlisttableid"]/tbody')[2:-1]
        for tbody in tbodys:
            item = {}
            category = tbody.xpath('.//th/em/a/text()').extract_first()
            title = tbody.xpath('.//tr/th/a[1]/text()').extract_first()
            href = tbody.xpath('.//tr/th/a[1]/@href').extract_first()
            item['catergory'] = category
            item['title'] = title
            item['href'] = response.urljoin(href)
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//div[@class="t_fsz"]//td//text()').extract()
        content = [i.strip() for i in content if len(content) > 0]
        content = ''.join(content)
        item['content'] = content
        print(item)
