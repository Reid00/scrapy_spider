# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE
import copy


class DownloadpicPipeline(object):
    def process_item(self, item, spider):
        return item


class BMWImagesPipeline(ImagesPipeline):
    # 方法一如下：重新构造请求，把catergory 在meta 里面传入
    def get_media_requests(self, item, info):
        # 这个方法用来发送下载请求,获取图片下载链接，生成request 对象
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取图片存储的路径， 下载请求之后调用
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        item = request.meta['item']
        category = item['category']
        images_store = IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        # 获取原先的图片名称
        # image_name = path.replace('full/', '')
        image_name = request.url.split('/')[-1]
        image_path = os.path.join(category_path, image_name)
        # image_path = u'{0}/{1}'.format(category_path, image_name)
        return image_path
    # 方法二如下：在父类中拿到请求的相关参数，如item category
    # def get_media_requests(self, item, info):
    #     request_objects = super().get_media_requests(item, info)  # super()直接调用父类对象
    #     for request_object in request_objects:
    #         request_object.item = item
    #     return request_objects
    #
    # def file_path(self, request, response=None, info=None):
    # # 该方法是在图片将要被存储时调用，用于获取图片存储的路径
    # # 下面方法用来拿到父类默认存储图片的path
    #     path = super().file_path(request, response, info)
    #
    #     category = request.item.get('category')
    #     images_stores = IMAGES_STORE  # 拿到IMAGES_STORE
    #     category_path = os.path.join(images_stores, category)
    #     if not os.path.exists(category_path):  # 判断文件名是否存在,如果不存在创建文件
    #         os.mkdir(category_path)
    # # 修改原先path 的存储路径，不再放在full 文件夹里面
    #     image_name = path.replace('full/', '')
    #     image_path = os.path.join(category_path, image_name)
    #     return image_path
