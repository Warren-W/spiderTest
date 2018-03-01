#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: warren

import scrapy
import json
from spider.items import ElemeSpiderItem


class elemeSpiders(scrapy.Spider):
    name = "ele"
    start_urls = [
        "https://www.ele.me/restapi/shopping/restaurants?extras[]=activities"
    ]
    geoHash = "&geohash=wtsw3zdyqjgk"
    latitude = "&latitude=32.078436"
    longitude = "&longitude=118.909068"
    limit = "&limit=30"
    terminal = "&terminal=web"
    offset = "&offset="
    cookie = {
        'SID': 'OtRODRmXsaLxcj75z5IQoeOJEDaQ1i2ohDzA',
        'USERID': '97157245'
    }

    def get_urls(self,n):
        url = self.start_urls[0] + self.geoHash + self.latitude + self.longitude + self.limit + self.terminal + self.offset
        return [url + str(x * 30) for x in range(1, n)]

    def start_requests(self):
        for url in self.get_urls(2):
           print(url)
           yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookie)

    def parse(self, response):
        # titles = response.xpath("//div[@class='desc']//p[@class='title']").extract()
        # for title in titles:
        #     print(title)
        sites = json.loads(response.body_as_unicode())
        for site in sites:
           yield self.get_item(site)


    def get_item(self, item):
        eleItem = ElemeSpiderItem()
        eleItem['name'] = item['name']
        eleItem['address'] = item['address']
        eleItem['phone'] = item['phone']
        eleItem['latitude'] = item['latitude']
        eleItem['longitude'] = item['longitude']
        eleItem['expressFee'] = item['piecewise_agent_fee']['description']
        return eleItem

