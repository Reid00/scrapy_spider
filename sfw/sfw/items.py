# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SfwNewHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 小区名称
    name = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 几居室
    room = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 状态
    status = scrapy.Field()
    # 介绍
    desc = scrapy.Field()
    # 电话
    phone = scrapy.Field()


class SfwesfItem(scrapy.Item):
    # 小区名称
    name = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 几居室
    room = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 层数
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 建筑时间
    year = scrapy.Field()
    # 总价
    price = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 介绍
    desc = scrapy.Field()
