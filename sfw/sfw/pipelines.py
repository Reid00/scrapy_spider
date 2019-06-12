# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import os
import pymongo

class SfwPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'suzhoufang':
            if not os.path.exists('newhours.csv'):
                df = pd.DataFrame([item])
                df.to_csv('newhours.csv', index=None, mode='a', encoding='utf-8-sig')
            else:
                df = pd.DataFrame([item])
                df.to_csv('newhours.csv', index=None, mode='a', header=None, encoding='utf-8-sig')
        if spider.name == 'suzhouesf':
            if not os.path.exists('esf.csv'):
                df = pd.DataFrame([item])
                df.to_csv('esf.csv', index=None, mode='a', encoding='utf-8-sig')
            else:
                df = pd.DataFrame([item])
                df.to_csv('esf.csv', index=None, mode='a', header=None, encoding='utf-8-sig')

class MongoPipeline(object):
    #  将数据存入MongoDB数据库中
    @classmethod
    def from_crawler(cls, crawler):
        # 类方法，读取settings.py中的配置，根据配置创建MongoPipeline对象
        cls.MONGO_CLIENT = crawler.settings.get('MONGO_CLIENT', 'mongodb://localhost:27017/')
        cls.MONGO_DB = crawler.settings.get('MONGO_DB', 'sfw')
        return cls()

    def open_spider(self, spider):
        # 创建MongoDB连接，指明连接的数据库和集合
        self.client = pymongo.MongoClient(self.MONGO_CLIENT)
        self.db = self.client[self.MONGO_DB]
        self.collection = self.db[spider.name]  # 集合名为spider.name

    def close_spider(self, spider):
        # 数据处理完后，关闭MongoDB连接
        self.client.close()

    def process_item(self, item, spider):
        # 将数据存入MongoDB集合中
        if isinstance(item, Item):  # 传入的item为Item类型，先转换为dict类型再存入MongoDB
            db_item = dict(item)
        else:
            db_item = item
        self.collection.insert_one(db_item)
        return item