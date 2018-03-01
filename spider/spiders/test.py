#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: warren

start_urls = [
        "https://www.ele.me/restapi/shopping/restaurants?extras[]=activities"
    ]
hash = "&geohash=wtsw3zdyqjgk"
latitude = "&latitude=32.078436"
longitude = "&longitude=118.909068"
limit = "&limit=30"
terminal = "&terminal=web"
offset = "&offset="
test = "test"

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def get_urls(n):
    url = start_urls[0]+hash+latitude+longitude+limit+terminal+offset
    return [url+str(x * 30) for x in range(1, n)]


if __name__ == '__main__':
    print(get_urls(10))
