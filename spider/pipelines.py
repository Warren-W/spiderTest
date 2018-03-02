# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class SpiderPipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(host='192.168.99.100', port=3306, user='warren', password='123456', db='eleme',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        insert_sql="insert into t_eleme_shop_info(f_name,f_address,f_latitude,f_longitude,f_phone,f_expressFee) VALUES (%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(insert_sql, (item["name"], item["address"], item["latitude"], item["longitude"], item["phone"], item["expressFee"]))
            self.connection.commit()
            print("插入数据")
        except:
            self.connection.rollback()

        return item

    def close_spider(self,spider):
        self.connection.close()
        print("插入数据库完成")