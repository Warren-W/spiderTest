#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: warren

import scrapy
from scrapy_splash import SplashRequest

# 抓取使用splash js引擎解析页面后的request
class splashSpiders(scrapy.Spider):
    name = "test"
    start_urls = [
        "http://www.baidu.com"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        # titles = response.xpath("//div[@class='desc']//p[@class='title']").extract()
        # for title in titles:
        #     print(title)
        print(response.text)
