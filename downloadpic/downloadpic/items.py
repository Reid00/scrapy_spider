# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadpicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    category = scrapy.Field()
    # urls = scrapy.Field()

    # imagesPipleline 的属性必须满足以下格式
    image_urls = scrapy.Field()  # url 存放的地址
    images = scrapy.Field()
