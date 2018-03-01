# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    titlePicUrl = scrapy.Field()
    newsContext = scrapy.Field()
    newsCreateTime = scrapy.Field()
    newsEditer = scrapy.Field()


class ElemeSpiderItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    #坐标
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    #物流费用
    expressFee = scrapy.Field()

